# simpleds 

`simpleds` is a Python 3 package that provides a collection of higher-order 
data science functions with simple and consistent function contracts. 
`simpleds` is built with a functional programming paradigm and operates as a simplifying wrapper for major Python data science modules (e.g. `numpy`, `scipy`, `pandas`, etc).

As it can get time-consuming digging through various docs for different
packages and different exception handling systems to just to do something
simple, `simpleds` seeks to simplify and add consistency to basic data science
operations by avoiding the need to switch between different packages and
package-specific data structures for the everyday-type of data analysis.
Because sometimes all one wants is to find central tendencies, test hypotheses,
and calculate significances in one simple way on Python's built-in data 
types/containers and exception handling system. 


## Requirements

- Python 3
- pip3


## Installation

```bash
$ pip3 install git+https://github.com/keiferc/simpleds.git
```

Run `pip3 uninstall simpleds` to uninstall `simpleds`.


## Development

To install manually:

```bash
$ git clone https://github.com/keiferc/simpleds.git
$ cd simpleds
$ python3 -m venv venv # we recommend using a virtual environment
$ source venv/bin/activate
$ pip3 install -e .[dev] # note: may need to escape brackets if using zsh
```

Run `python3 -m pytest` to run automated testing.

Run `pip3 uninstall simpleds` to uninstall `simpleds`.


## Documentation

Documentation is built using [MkDocs](https://www.mkdocs.org/).

