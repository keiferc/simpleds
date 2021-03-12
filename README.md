# simpleds 

`simpleds` is a Python 3 package that provides a collection of higher-order 
data science functions with simple and consistent function contracts. 
`simpleds` is built with a functional programming paradigm and operates as a simplifying wrapper for major Python data science modules (e.g. `numpy`, `scipy`, `pandas`, etc).

The underlying idea of `simpleds` is that one doesn't need an airplane to get
to the bodega across the street; it can get time-consuming digging through
the various docs to just to do something simple. `simpleds` attempts to avoid 
the need to switch between different packages and package-specific data 
structures for the everyday-type of data analysis. Because sometimes all one
wants is to find central tendencies, test hypotheses, and calculate
significances in one simple way on Python's built-in data types/containers. 


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

