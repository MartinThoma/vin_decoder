#!/usr/bin/env python

"""Parse the VDS number given that it is a nissan car."""


import logging
import sys

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)


def parse(vds):
    """
    Nissan structures its VDS number like this:
    char 1: Engine type
    char 2: Model Line
    char 3: Model Change
    char 4: Body Type
    char 5: Miscellaneous
    char 6: Check Digit
    char 7: Model Year
    char 8: Plant Code

    Source: http://nissanhelp.com/diy/common/nissan_vin.php
    """
    parsed = {}
    logging.error("#"*80)
    logging.error(vds)
    parsed['engine'] = get_engine(vds[0])
    parsed['model_line'] = get_model_line(vds[1])
    parsed['model_change'] = get_model_change(vds[2])
    parsed['body_type'] = get_body_type(vds[3])
    parsed['misc'] = get_misc(vds[4])
    #parsed['check_digit'] = get_check_digit(vds[5])
    # parsed['model_year'] = get_model_year(vds[6])
    # parsed['plant_code'] = get_plant_code(vds[7])
    return parsed


def get_engine(char):
    translate = {}
    translate['A'] = ['VG30D, VK45DE, VQ35DE, VK56DE, VQ40DE, QR25DE']
    translate['B'] = ['KA24DE, SR20DE, VQ35HR, MR18DE, QR25DE']
    translate['C'] = ['SR20DE, VG30DETT, QG18DE']
    translate['D'] = ['KA24DE, QG18DE, VQ35DE']
    translate['E'] = ['VE30DE, GA16DE, VG33E']
    translate['F'] = ['KA24E']
    translate['H'] = ['VG30E']
    translate['M'] = ['KA24DE, VG33ER']
    translate['N'] = ['VH45DE']
    translate['R'] = ['VG30DE']
    translate['S'] = ['KA24E']
    translate['T'] = ['VG33E']
    return translate[char]


def get_model_line(char):
    translate = {}
    translate['A'] = ['Armada, Titan, Maxima']
    translate['B'] = ['Sentra']
    translate['C'] = ['Versa (07-11)']
    translate['D'] = ['Truck, Xterra (00-04), Frontier']
    translate['J'] = ['Maxima']
    translate['N'] = ['Xterra (05-11)']
    translate['R'] = ['Pathfinder']
    translate['S'] = ['240SX, Rogue (08-11)']
    translate['U'] = ['Altima']
    translate['Z'] = ['300Z, 350Z, Murano']
    return translate[char]


def get_model_change(char):
    translate = {}
    translate['0'] = 'No Change'
    if char not in translate:
        return char
    return translate[char]


def get_body_type(char):
    translate = {}
    translate['1'] = '4-Door Sedan, Standard Body Truck'
    translate['4'] = '2-Door Coupe'
    translate['5'] = '4-Door Wagon'
    translate['6'] = '2-Door Convertible, Fastback, King Cab Truck'
    translate['7'] = 'Crew Cab Truck'
    translate['8'] = '8- Door Wagon'
    if char not in translate:
        return char
    return translate[char]


def get_misc(char):
    translate = {}
    translate['A'] = 'Air Bag System'
    translate['C'] = 'Air Bag System'
    translate['D'] = 'Driver & Front Passenger Air Bag  + 3 Point Seat Belt'
    translate['E'] = 'Driver and front passenger SRS air bags, SRS side air bags, SRS curtain air bag & 3 point manual seat belt'
    translate['P'] = 'Passive Restraint System'
    translate['S'] = '2 Wheel Drive (2WD) - Rear ABS'
    translate['T'] = '2 Wheel Drive (2WD) - 4-Wheel ABS'
    translate['Y'] = '2 Wheel Drive (2WD) - 4-Wheel ABS'
    translate['U'] = '2WD'
    translate['W'] = 'AWD (4WD)'

    if char not in translate:
        return char
    return translate[char]


def get_check_digit(char):
    return char


def get_model_year(char):
    translate = {}
    translate['L'] = '1990'
    translate['M'] = '1991'
    translate['N'] = '1992'
    translate['P'] = '1993'
    translate['R'] = '1994'
    translate['S'] = '1995'
    translate['T'] = '1996'
    translate['V'] = '1997'
    translate['W'] = '1998'
    translate['X'] = '1999'
    translate['Y'] = '2000'
    translate['1'] = '2001'
    translate['2'] = '2002'
    translate['3'] = '2003'
    translate['4'] = '2004'
    translate['5'] = '2005'
    translate['6'] = '2006'
    translate['7'] = '2007'
    translate['8'] = '2008'
    translate['9'] = '2009'
    translate['A'] = '2010'
    translate['B'] = '2011'
    translate['C'] = '2012'

    if char not in translate:
        return char
    return translate[char]


def get_plant_code(char):
    translate = {}
    translate['C'] = 'Smyrna, Tennessee, USA'
    translate['L'] = 'Aguas Calientes, Mexico'
    translate['M'] = 'Tochigi, Japan'
    translate['N'] = 'Canton, Mississippi, USA'
    translate['T'] = 'Tochigi, Japan OR Oppama, Japan'
    translate['W'] = 'Kyushyu, Japan'

    if char not in translate:
        return char
    return translate[char]
