"""
Python PIP

PIP is a package manager for Python packages, or modules if you like.
Note: If you have Python version 3.4 or later, PIP is included by default.

What is a Package?
A package contains all the files you need for a module.
Modules are Python code libraries you can include in your project.

Check if PIP is Installed
Navigate your command line to the location of Python's script directory, and type the following:
Example: Check PIP version:
"""
"""
Download a Package

Downloading a package is very easy.
Open the command line interface and tell PIP to download the package you want.
Navigate your command line to the location of Python's script directory, and type the following:
Example: Download a package named "camelcase":
"""
"""
Using a Package

Once the package is installed, it is ready to use.
Import the "camelcase" package into your project.
"""
import camelcase

c = camelcase.CamelCase()

txt = "Hello Camel"

print (c.hump(txt))
"""
Find Packages

Find more packages at https://pypi.org/ (Links to an external site.).

Remove a Package

Use the uninstall command to remove a package:
Example: Uninstall the package named "camelcase":

The PIP Package Manager will ask you to confirm that you want to remove the camelcase package:
"""
"""
List Packages

Use the list command to list all the packages installed on your system:
Example: List installed packages:
"""

