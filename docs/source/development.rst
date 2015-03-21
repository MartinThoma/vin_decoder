Development
===========

The ``vin_decoder`` is developed by Martin Thoma. The development began in
March 2015.

It is developed on GitHub: https://github.com/MartinThoma/vin_decoder

You can file issues and feature requests there. Alternatively, you can send
me an email: info@martin-thoma.de

Contributions
-------------

Everybody is welcome to contribute to ``vin_decoder``. You can do so by

* Testing it and giving me feedback / opening issues on GitHub.

  * Writing unittests.

  * Simply using the software.

* Writing new code and sending it to me as pull requests or as email
  (info@martin-thoma.de). However, before you add new functionality you should
  eventually ask if I really want that in the project.

* Improving existing code.

* Suggesting something else how you can contribute.


I suggest reading the issues page https://github.com/MartinThoma/vin_decoder/issues
for more ideas how you can contribute.


Tools
-----

* ``nosetests`` for unit testing
* ``pylint`` to find code smug
* GitHub for hosting the source code
* https://pythonhosted.org/vin_decoder for hosting the documentation


Code coverage can be tested with

.. code:: bash

    $ nosetests --with-coverage --cover-erase --cover-package vin_decoder --logging-level=INFO --cover-html

and uploaded to coveralls.io with

.. code:: bash

    $ coveralls


Documentation
-------------

The documentation is generated with `Sphinx <http://sphinx-doc.org/latest/index.html>`_.
On Debian derivates it can be installed with

.. code:: bash

    $ sudo apt-get install python-sphinx

Sphinx makes use of `reStructured Text <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_

The documentation can be built with ``make html``.



Current State
-------------

* lines of code without tests: LOC
* lines of test code: LOT
* test coverage: cov
* pylint score: lint

::

    date,        LOC,  LOT, cov, lint, cheesecake_index, users, changes
    2015-03-21,  986,    0,  0%, 9.47, 381/595, 1