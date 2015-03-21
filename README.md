# cardb
A database of cars, their VIN numbers and other information about them.

## Example

```python
>>> result = parse_vin("JN1FAAZE0U0000001")
>>> {   'vds': {   'parsed': {   'body_type': 'Z',
                                 'engine': ['KA24E'],
                                 'misc': 'Driver and front passenger SRS air '
                                         'bags, SRS side air bags, SRS curtain '
                                         'air bag & 3 point manual seat belt',
                                 'model_change': 'A',
                                 'model_line': ['Armada, Titan, Maxima']},
                   'vds': 'FAAZE0'},
        'vis': {'assembly_plant': '0', 'vis': 'U0000001', 'year': None},
        'wmi': {   'geo_area': 'Asia',
                   'geo_detailed_area': 'Japan',
                   'manufacturer': 'Nissan',
                   'wmi': 'JN1'}}
```

## On-Line versions

Currently, vin decoder is not online. Alternatives are

* [www.vindecoderz.com](http://www.vindecoderz.com/)

## VIN documentation

Information about VIN can be found at

* [en.wikibooks.org/wiki/Category:Vehicle_Identification_Numbers_(VIN_codes)](https://en.wikibooks.org/wiki/Category:Vehicle_Identification_Numbers_(VIN_codes))