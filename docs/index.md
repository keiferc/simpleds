# Documentation: `simpleds` v0.1.0-alpha

`simpleds` is a lightweight Python 3 package that provides a collection of 
first-order data science functions with simple and consistent function 
contracts. `simpleds` is built with a functional programming paradigm and operates as a simplifying wrapper for major Python data science modules (e.g. `numpy`, `scipy`, etc).

## Documentation Overview

Please see the [Installation page](installation.md) for more information on
installing `simpleds`. The [Getting Started page](getting-started.md) has 
some information on how to import `simpleds` in your projects. The 
[Docs page](docs.md) has all the public function contracts for `simpleds`.
Finally, the [Examples page](examples.md) provides examples on how to use
`simpleds`'s functions in your projects.

## Contribution

`simpleds` is an open-source project that welcomes contributions to its 
development and maintenance. If you wish to contribute to `simpleds`, 
please follow the contribution guidelines below:

- Code must follow styling consistent with the rest of the package. The styling
  used is consistent with the [Linux kernel coding style](https://www.kernel.org/doc/html/v4.10/process/coding-style.html) with the following exceptions:
    - Use four-character indents.
    - Follow pythonic casing for function, variable, and file names.
    - Create descriptive names that follow their natural language equivalent.
      For example, name functions/methods as verbs, name classes/attributes/modules as nouns, and name conditional functions/booleans as questions 
      (e.g. `is_empty`).
- Readability is a priority and cannot be at the expense of optimization. 
  Therefore, any user should be able to easily infer what a function does with the function name, function parameters, and function return value alone.
- Run regression tests on changes using `pytest`. For information on how to use 
  pytest, please see the [pytest docs](https://docs.pytest.org/en/stable/contents.html).
- Update [Docs](docs.md) and the semantic version (top of this page) with 
  changes. For information on how to update the documentation, please see the
  [Mkdocs docs](https://www.mkdocs.org/).
- When ready to submit your contribution, please submit a pull request on the
  [`simpleds` GitHub repository](https://github.com/keiferc/simpleds).
- Add your name/handle/identifier to the list of contributors below.

### Contributors

- [@keiferc](https://github.com/keiferc)