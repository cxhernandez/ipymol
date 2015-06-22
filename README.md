IPyMol
======

IPyMol allows you to control PyMol sessions via IPython. This tool is ideal for situations where you'd like to present your work neatly in a [Jupyter Notebook](https://jupyter.org/) or conveniently prototype PyMol scripts.

Before You Begin
----------------
Please ensure that PyMol is in your `$PATH` as `pymol` or you can start PyMol in server mode:

```shell
$ pymol -R #-Rqpc to run it without a GUI
```

Example Usage
--------------
In order to You can fire up an IPython or IPython Notebook session and start using IPyMol. For example:

```python
from ipymol import init, MolViewer
init()
pymol = MolViewer()
pymol.do('fetch 3odu; as cartoon; bg white')
pymol.show()
```
This series of commands will define a variable ```mol``` of class ```MolViewer```, which can pass commands to PyMol, and then create an image of ```PDBID:3odu``` in your IPython session.
Any additional commands can be invoked via `pymol.do("[ENTER YOUR COMMAND HERE]")`.

Here's an additional [example](http://nbviewer.ipython.org/urls/raw.github.com/cxhernandez/iPyMol/master/Example.ipynb).

Enjoy!
