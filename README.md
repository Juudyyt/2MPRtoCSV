2MPR interlace TO CSV
===============

- [`The purpose of the project`](#The-purpose-of-the-project).
- [`How to use`](#How-to-use).

The purpose of the project
---------------
The purpose of this project is to reads the ".mpeg" files and interleaves them according to the
time column. The resulting file will be a ".CSV"

How to use
---------------
#### Execute
You just need to run the program as another Python file. You must pass 2 arguments per parameter. And if you want, you can tell the destination.
##### Example:
> python main.py file.mpr file2.mpr

> python main file.mpr file2.mpr --dst="result.csv"