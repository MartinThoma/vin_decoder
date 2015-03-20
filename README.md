# cardb
A database of cars, their VIN numbers and other information about them.

## Example

```python
>>> result = parse_vin("JN1FAAZE0U0000001")
>>> {'wmi': {'wmi': 'JN1',
             'geo_area': 'Asia',
             'geo_detailed_area': 'Japan',
             'manufacturer': 'Nissan'},
     'vds': 'FAAZE0',
     'vis': {'vis': 'U0000001',
             'assembly_plant': '0',
             'year': None}}
```