try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'vin_decoder',
    'version': '0.1.0',
    'author': 'Martin Thoma',
    'author_email': 'info@martin-thoma.de',
    'maintainer': 'Martin Thoma',
    'maintainer_email': 'info@martin-thoma.de',
    'packages': ['vin_decoder'],
    'scripts': ['bin/vin_decoder'],
    'package_data': {'vin_decoder': ['templates/*', 'misc/*']},
    'platforms': ['Linux', 'MacOS X', 'Windows'],
    'url': 'https://github.com/MartinThoma/vin_decoder',
    'license': 'MIT',
    'description': 'VIN decoder (Vehicle identification number)',
    'long_description': ("A tookit to get data about your car"),
    'install_requires': [
        "argparse",
        "nose"
    ],
    'keywords': ['VIN', 'WMI', 'OBD'],
    'download_url': 'https://github.com/MartinThoma/vin_c',
    'classifiers': ['Development Status :: 3 - Alpha',
                    'Environment :: Console',
                    'Intended Audience :: Developers',
                    'Intended Audience :: Science/Research',
                    'License :: OSI Approved :: MIT License',
                    'Natural Language :: English',
                    'Programming Language :: Python :: 2.7',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.3',
                    'Programming Language :: Python :: 3.4',
                    'Topic :: Software Development',
                    'Topic :: Utilities'],
    'zip_safe': False,
    'test_suite': 'nose.collector'
}

setup(**config)
