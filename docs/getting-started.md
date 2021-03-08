# Getting Started

## Importing `simpleds`

To use `simpleds` in your project, simple add the following line to your 
Python file or shell:

```python
import simpleds
```

Functions can then be called using dot notation (e.g. 
`simpleds.calc_mean(...)`).


You can also use name aliases in your import statement. For example:

```python
import simpleds as sds
```

So that functions can be called using `sds` (e.g. `sds.calc_mean(...)`).

We do not recommend importing `simpleds` functions using the `from`
syntax as such means of importing can muddy the namespaces of your
project.

## Using `simpleds`

`simpleds` functions are named in verb-object form (e.g. 
`calc_standard_error(...)`) and follow the functional programming
paradigm. In other words, `simpleds` functions will always take an input,
return a value, and will never change a state. Available `simpleds` functions
can be found in the [Docs page](docs.md).
