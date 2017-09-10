
---
##### `powertools.export`
- `export` decorator - uses stack frame inspection to add an object to a module's \_\_all\_\_ attribute, creating it if it doesn't exist


---
##### `powertools.logging`
- `AutoLogger` class provides a recipe that automatically initialises a logger with color support, stack depth indentation, and a context manager to enable debug output


---
##### `powertools.meta`
- `classproperty` decorator - descriptors for classmethods


---
##### `powertools.strap`
utilities to support setuptools


---
##### `powertools.print`
- custom hook into `pprint` and `pformat`
- `add_pprint` registers a class's \_\_pprint\_\_ method as a pretty printer
- `dictprint` - print a dict when pprint isn't working
- `listprint` - print a list when pprint isn't working
- `rprint` - recursively print nested containers without relying on pprint


---
##### `powertools.term`
- ansi color for terminal output
  - `white`, `red`, `green`, `blue`, `pink`, `yellow`, `cyan`
  - `dwhite`, `dred`, `dgreen`, `dblue`, `dpink`, `dyellow`, `dcyan`

all of these take *args, stringify them, join over '', add ansi codes, and return a single string for printing


---
##### `powertools.test`
test execution utilities - fixtures, pytest plugins
- `path_testdata` - a fixture for instrumenting stateful tests


--------------------------------------------------------------------------
