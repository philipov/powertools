# powertools

---
##### export
- `export` decorator - uses stack frame inspection to add an object to a module's __all__, creating it if it doesn't exist


---
##### logging
- `AutoLogger` class provides a recipe that automatically initialises a logger with color support, stack depth indentation, and a context manager to enable debug output


---
##### meta
- `classproperty` decorator - descriptors for classmethods


---
##### 
utilities to support setuptools


---
##### print
pretty printers
- custom hook into `pprint` and `pformat`
- `add_pprint` registers a class's \_\_pprint\_\_ method as a pretty printer
- `dictprint` - print a dict when pprint isn't working
- `listprint` - print a list when pprint isn't working
- `rprint` - recursively print nested containers without relying on pprint


---
##### term
ansi color for terminal output
- `white`, `red`, `green`, `blue`, `pink`, `yellow`, `cyan`
- `dwhite`, `dred`, `dgreen`, `dblue`, `dpink`, `dyellow`, `dcyan`

all of these take *args, stringify it, join with '', add ansi codes, and return the string for printing


---
##### test
test execution utilities - fixtures, pytest plugins
- `path_testdata` - a fixture for instrumenting stateful tests


--------------------------------------------------------------------------
