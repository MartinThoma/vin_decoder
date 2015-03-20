#!/usr/bin/env python

try:
    from future.builtins import open
except:
    pass

import csv

## Data start
geo_area_table_detailed = {}
for char in "ABCDEFGH":
    geo_area_table_detailed["A" + char] = "South Africa"
for char in "ABCDEFGHJKLMNPRSTUVWXYZ1234567890":
    geo_area_table_detailed["J" + char] = "Japan"
for char in "LMNPR":
    geo_area_table_detailed["K" + char] = "South Korea"
for char in "ABCDEFGHJKLMNPRSTUVWXYZ1234567890":
    geo_area_table_detailed["L" + char] = "China"
for char in "ABCDE":
    geo_area_table_detailed["M" + char] = "India"
for char in "FGHJK":
    geo_area_table_detailed["M" + char] = "Indonesia"
for char in "LMNPR":
    geo_area_table_detailed["M" + char] = "Thailand"
for char in "ABCDE":
    geo_area_table_detailed["P" + char] = "Philippines"
for char in "LMNPR":
    geo_area_table_detailed["P" + char] = "Malaysia"
for char in "FG":
    geo_area_table_detailed["R" + char] = "Taiwan"
for char in "ABCDEFGHJKLM":
    geo_area_table_detailed["A" + char] = "United Kingdom"
for char in "NPRST":
    geo_area_table_detailed["S" + char] = "Germany"
for char in "ABCDEFGHJKLMNPRSTUVWXYZ1234567890":
    geo_area_table_detailed["W" + char] = "Germany"
for char in "UVWXYZ":
    geo_area_table_detailed["S" + char] = "Poland"
for char in "ABCDEFGH":
    geo_area_table_detailed["T" + char] = "Switzerland"
for char in "JKLMNP":
    geo_area_table_detailed["T" + char] = "Czech Republic"
for char in "RSTUV":
    geo_area_table_detailed["T" + char] = "Hungary"
geo_area_table_detailed["TW"] = "Portugal"
for char in "ABCDE":
    geo_area_table_detailed["V" + char] = "Austria"
for char in "FGHJKLMNPR":
    geo_area_table_detailed["V" + char] = "France"
for char in "STUVW":
    geo_area_table_detailed["V" + char] = "Spain"
for char in "XYZ12":
    geo_area_table_detailed["V" + char] = "Yugoslavia"
for char in "LMN":
    geo_area_table_detailed["X" + char] = "The Netherlands"
for char in "STUVW":
    geo_area_table_detailed["X" + char] = "USSR"
for char in "34567890":
    geo_area_table_detailed["X" + char] = "Russia"
for char in "ABCDE":
    geo_area_table_detailed["Y" + char] = "Belgium"
for char in "FGHJK":
    geo_area_table_detailed["Y" + char] = "Finland"
for char in "STUVW":
    geo_area_table_detailed["Y" + char] = "Sweden"
for char in "ABCDEFGHJKLMNPR":
    geo_area_table_detailed["Z" + char] = "Italy"
for char in "ABCDEFGHJKLMNPRSTUVWXYZ1234567890":
    geo_area_table_detailed["1" + char] = "United States"
for char in "ABCDEFGHJKLMNPRSTUVWXYZ1234567890":
    geo_area_table_detailed["4" + char] = "United States"
for char in "ABCDEFGHJKLMNPRSTUVWXYZ1234567890":
    geo_area_table_detailed["5" + char] = "United States"
for char in "ABCDEFGHJKLMNPRSTUVWXYZ1234567890":
    geo_area_table_detailed["2" + char] = "Canada"
for char in "ABCDEFGHJKLMNPRSTUVWXYZ1234567890":
    geo_area_table_detailed["3" + char] = "Mexico"
for char in "ABCDEFGHJKLMNPRSTUVW":
    geo_area_table_detailed["6" + char] = "Australia"
for char in "ABCDE":
    geo_area_table_detailed["7" + char] = "New Zealand"
for char in "ABCDE":
    geo_area_table_detailed["8" + char] = "Argentina"
for char in "FGHJ":
    geo_area_table_detailed["8" + char] = "Chile"
for char in "XYZ12":
    geo_area_table_detailed["8" + char] = "Venezuela"
for char in "ABCDE":
    geo_area_table_detailed["9" + char] = "Brazil"
for char in "3456789":
    geo_area_table_detailed["9" + char] = "Brazil"
for char in "FGHJ":
    geo_area_table_detailed["9" + char] = "Colombia"
## Data End

with open('geo_area_table_detailed.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile,
                           delimiter=';',
                           quotechar='"',
                           quoting=csv.QUOTE_MINIMAL)
    for key, value in geo_area_table_detailed.items():
        csvwriter.writerow([key, value])
