import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

install_dependencies = [
    'wheel      == 0.*',
    'numpy      == 1.*',
    'pandas     == 1.*',
    'scipy      == 1.*'
]

dev_dependencies = [
    'mkdocs             == 1.*',
    'mkdocs-material    == 7.*',
    'pytest             == 6.*'
]

setuptools.setup(
    name                = 'simpleds',
    version             = '0.0.0a1',
    description         = 'A package of simple, first-order data science functions.',
    long_description    = long_description,
    license             = 'MIT',
    url                 = 'https://github.com/keiferc/simpleds',
    author              = '@keiferc',
    packages            = ['simpleds'],
    install_requires    = install_dependencies,
    extras_require      = {
        'dev': dev_dependencies
    }
)
