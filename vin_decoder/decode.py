#!/usr/bin/env python

"""Utility functions for the vehicle identification number (vin) as defined in
   ISO 3779.
"""

try:
    from future.builtins import open
except:
    pass

import csv
import re

import logging
import sys
import pprint
import pkg_resources
import os
from collections import OrderedDict

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)


def get_parser():
    """Return the parser object for this script."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--vin",
                        dest="vin",
                        required=True,
                        help="Get VIN")
    return parser


def parse_vin(vin):
    """
    Parse the VIN into a dictionary. Return `None` if the VIN is not valid.

    >>> result = parse_vin("JN1FAAZE0U0000001")
    >>> e = {'vds': 'FAAZE0', 'wmi': {'geo_area': 'Asia', 'manufacturer': 'Nissan', 'wmi': 'JN1', 'geo_detailed_area': 'Japan'}, 'vis': {'assembly_plant': '0', 'vis': 'U0000001', 'year': None}}
    >>> e == result
    True

    >>> parse_vin("O")
    """
    if len(vin) != 17:
        logging.error(("The VIN '%s' is too short. It has to have "
                       "17 characters. Yours had %i"), vin, len(vin))
        return None

    match = re.match("^[ABCDEFGHJKLMNPRSTUVWXYZ0-9]*$", vin)
    if match is None:
        logging.error("The VIN '%s' contains an invalid character.", vin)
        return None

    parsed = {}

    wmi = parse_wmi(vin[0:3])
    if wmi is None:
        logging.error("The WMI '%s'is invalid", vin[0:3])
        return None
    parsed['wmi'] = wmi

    from . import vdsnissan
    if 'nissan' in wmi['manufacturer']:
        vds = vdsnissan.parse(vin[3:9], wmi['manufacturer'])
    else:
        vds = parse_vds(vin[3:9], wmi['manufacturer'])
    if vds is None:
        logging.error("The VDS '%s'is invalid", vin[3:9])
        return None
    parsed['vds'] = vds

    vis = parse_vis(vin[9:17], wmi['manufacturer'])
    if vis is None:
        logging.error("The vis '%s'is invalid", vin[9:17])
        return None
    parsed['vis'] = vis
    return parsed


def check_digit_vin(vin):
    """The following function returns `True` if the VIN is valid according to
       https://en.wikibooks.org/wiki/Vehicle_Identification_Numbers_(VIN_codes)/Check_digit
    >>> check_digit_vin("JN1FAAZE5U0000001")
    True
    """
    translate = {}
    for digit, char in enumerate("0123456789"):
        translate[char] = digit
    for digit, char in enumerate("ABCDEFGH", start=1):
        translate[char] = digit
    for digit, char in enumerate("JKLMNOPQR", start=1):
        translate[char] = digit
    del(translate['O'])
    del(translate['Q'])
    for digit, char in enumerate("STUVWXYZ", start=2):
        translate[char] = digit
    weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    check = sum(translate[char]*weight for char, weight in zip(vin, weights)) % 11
    if check == 10 and vin[8] == 'X':
        return True
    elif vin[8] == str(check):
        return True
    else:
        logging.debug("Actual check digit was '%s', but '%s' expected.",
                      vin[8],
                      check)
        return False


def parse_wmi(wmi):
    """Parse the World Manufacturer Identifier (WMI).
       The WMI is defined in ISO 3780.

       Return `None` if it is invalid.

       See https://en.wikibooks.org/wiki/Vehicle_Identification_Numbers_(VIN_codes)/World_Manufacturer_Identifier_(WMI)
    """
    if len(wmi) != 3:
        logging.error("A WMI has exactly 3 characters. You gave '%s'.", wmi)
        return None

    match = re.match("^[ABCDEFGHJKLMNPRSTUVWXYZ0-9]*$", wmi)
    if match is None:
        logging.error("The WMI '%s' contains an invalid character.", wmi)
        return None

    geo_area_table = {}
    for char in "12345":
        geo_area_table[char] = "North America"
    for char in "STUVWXYZ":
        geo_area_table[char] = "Europe"
    for char in "ABCDEFGH":
        geo_area_table[char] = "Africa"
    for char in "JKLMNPR":
        geo_area_table[char] = "Asia"
    for char in "67":
        geo_area_table[char] = "Oceania"
    for char in "890":
        geo_area_table[char] = "South America"

    geo_area_table_detailed = {}
    misc_path = pkg_resources.resource_filename('vin_decoder', 'misc/')
    geo_area_table_csv = os.path.join(misc_path, 'geo_area_table_detailed.csv')

    with open(geo_area_table_csv, 'rt', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        # next(csvreader, None)  # skip the headers
        for key, value in csvreader:
            geo_area_table_detailed[key] = value

    parsed = {'wmi': wmi,
              'geo_area': geo_area_table[wmi[0]],
              'geo_detailed_area': geo_area_table_detailed["".join(wmi[:2])]}

    manufacturer_table = {}
    manufacturer_table_csv = os.path.join(misc_path, 'manufacturer_table.csv')
    with open(manufacturer_table_csv, 'rt', encoding='utf-8', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        # next(csvreader, None)  # skip the headers
        for key, value in csvreader:
            manufacturer_table[key] = value

    if wmi in manufacturer_table:
        parsed['manufacturer'] = manufacturer_table[wmi]

    return parsed


def parse_vds(vds, manufacturer):
    """Parse the Vehicle Descriptor Section (VDS).
       Return `None if it is invalid.

       The VDS is used to specify general attributes of the vehicle.
       The coding and the sequence of this section are determined by the
       manufacturer.
    """
    if len(vds) != 6:
        logging.error("A VDS has exactly 6 characters. You gave '%s'.", vds)
        return None

    from . import vdsnissan
    parsed = {'vds': vds, 'parsed': vdsnissan.parse(vds)}
    return parsed


def parse_vis(vis, manufacturer):
    """Parse the Vehicle Indicator Section (VIS).
       Return `None` if it is invalid.

       The year and/or plant is encoded in this section.
       It is recommended that the year encodes the first character of the VIS,
       and the plant of manufacture by the second character.
    """
    if len(vis) != 8:
        logging.error("A VIS has exactly 8 characters. You gave '%s'.", vis)
        return None
    if len([char for char in vis if char.isdigit()]) < 4:
        logging.error("A VIS has at least 4 digits. You gave '%s'.", vis)
        return None
    year_table = {}
    for i, digitchar in enumerate("123456789ABCDEFGHJKLMNPRSTVWXY", start=1971):
        year_table[digitchar] = [i]
    for i, digitchar in enumerate("123456789A", start=2001):
        year_table[digitchar].append(i)

    if vis[0] in year_table:
        year = year_table[vis[0]]
    else:
        year = None
    assembly_plant = vis[1]

    return {'vis': vis, 'year': year, 'assembly_plant': assembly_plant}


def main(vin):
    pp = pprint.PrettyPrinter(indent=4)
    parsed = parse_vin(vin)
    pp.pprint(parsed)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
