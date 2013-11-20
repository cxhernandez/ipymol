iPyMol
======

Control PyMol sessions via iPython

Before You Begin
----------------
Before using iPyMol, you should start a PyMol session in 'server mode'. You can do this by using the ```-R``` flag:

```bash
$PathToPyMol/pymol -R
```


Example Usage
--------------
Once PyMol is open in 'server mode', you can fire up an iPython or iPython Notebook session and start using iPyMol. For example:

```python
import ipymol
mol=ipymol.MolViewer()
mol.server.do('fetch 3odu; as cartoon; bg white')
mol.Show()
```
This series of commands will define a variable ```mol``` of class ```MolViewer```, which can pass commands to PyMol, and then create an image of ```PDBID:3odu``` in your iPython session.
Any additional commands can be invoked via ```mol.server.do(ENTER_YOUR_COMMAND_HERE)```

Here's an additional [example](http://nbviewer.ipython.org/urls/raw.github.com/cxhernandez/iPyMol/master/Example.ipynb).

Enjoy!
