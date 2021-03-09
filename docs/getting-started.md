# Getting Started

## Importing `simpleds`

To use `simpleds` in your project, simple add the following line to your 
Python file or shell:

```python
import simpleds
```

Functions can then be called using dot notation (e.g. 
`simpleds.stats.calc_mean(...)`).


You can also import specific modules. For example:

```python
import simpleds.stats as stats
```

So that functions can be called using the module name (e.g. 
`stats.calc_mean(...)`).

## Using `simpleds`

`simpleds` functions are named in verb-object form (e.g. 
`calc_standard_error(...)`) and follow the functional programming
paradigm. In other words, `simpleds` functions will always take an input,
return a value, and will never change a state. Available `simpleds` functions
can be found in the [Docs section](stats.md).
