docs:
	python setup.py upload_docs --upload-dir docs/_build/html

upload:
	make clean
	python3 setup.py sdist bdist_wheel && twine upload dist/*

test:
	nosetests --with-coverage --cover-erase --cover-package vin_decoder --logging-level=INFO --cover-html

testall:
	make test
	cheesecake_index -n vin_decoder -v

count:
	cloc . --exclude-dir=docs,cover,dist,vin_decoder.egg-info

countc:
	cloc . --exclude-dir=docs,cover,dist,vin_decoder.egg-info,tests

countt:
	cloc tests

clean:
	rm -f *.hdf5 *.yml *.csv
