Traitlets is a small library for traits-like behavior. It was extracted from
ipython traitlets implementation, itself inspired by Enthought's traits library

It supports both python 2.x and python 3.x (>= python 3.2).

Example
-------

Simple model for an employee::

        class Employee(HasTraits):
            name = Unicode()
            age = Long()

        dilbert = Employee(name="dilbert", age=35)
        # This will raise an error as age is not a string
        dilbert.age = "35"

Installation
------------

traitlets is pure python and only depends on six for 2/3 compatibility::

        pip install six
        python setup.py install
