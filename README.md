iPyMol
======

Control PyMol sessions via iPython

Example Usage
--------------

```python
import ipymol
mol=ipymol.MolViewer()
mol.server.do('fetch 3odu; bg white')
mol.Show()
```
