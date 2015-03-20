docs:
	python setup.py upload_docs --upload-dir docs/_build/html

update:
	python setup.py sdist upload --sign
	sudo pip install vin_decoder --upgrade

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
	rm *.hdf5 *.yml *.csv