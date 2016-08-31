.. image:: https://badge.fury.io/py/ipymol.svg
    :target: https://pypi.python.org/pypi/mdtraj/ipymol/
    :alt: Latest PyPI version

IPyMOL
======

IPyMOL allows you to control `PyMOL <https://www.pymol.org>`_ sessions via IPython. This tool is ideal for situations where you'd like to present your work neatly in a `Jupyter Notebook <https://jupyter.org/>`_ or conveniently prototype PyMOL scripts.

Before You Begin
----------------
Please ensure that PyMOL is in your ``$PATH`` as ``pymol`` or you can start PyMOL in server mode:

.. code:: shell

    $ pymol -R #-cKRQ to run it without a GUI

Installation
------------


.. code:: shell

    pip install ipymol



Example Usage
--------------
You can fire up an IPython or IPython Notebook session and start using IPyMOL. For example:

.. code:: python

    from ipymol import viewer as pymol
    pymol.start()   # Start PyMOL RPC server
    pymol.fetch('3odu') # Fetch PDB
    pymol.show_as('cartoon') # Show as cartoon
    pymol.bg_color('white') # Set background color to white
    pymol.display() # Show current display

This series of commands will define a variable ``pymol`` of class ``MolViewer``, which can pass commands to PyMOL, and then create an image of ``PDBID:3odu`` in your IPython session.
Additional commands can be invoked via ``pymol.do("[ENTER YOUR COMMAND HERE]")``.

Here's an `example notebook <http://nbviewer.ipython.org/urls/raw.github.com/cxhernandez/iPyMol/master/examples/Example1.ipynb>`_ with more information.

Enjoy!
