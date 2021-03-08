# Installation Guide

## Quick Installation

### Requirements

- Python 3
- pip3

### Installation

To install `simpleds`, run the following in your terminal:

```bash
pip3 install git+https://github.com/keiferc/simpleds.git
```

### Uninstallation

To uninstall `simpleds`, run the following in your terminal: 

```bash
pip3 uninstall simpleds
```


## Development Installation

### Requirements

- Python 3
- pip3
- Make

### Installation

To manually install `simpleds`, run the following commands in your terminal:

```bash
git clone https://github.com/keiferc/simpleds.git
cd simpleds
python3 -m venv venv # we recommend using a virtual environment
source venv/bin/activate
make install
make clean
```

### Uninstallation

To uninstall `simpleds`, run the following in your terminal:

```bash
pip3 uninstall simpleds
```

### Testing

To run automated tests, run the following in your terminal while in the root
directory:

```bash
pytest
```
