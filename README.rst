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
    pymol.do('fetch 3odu; as cartoon; bg white')
    pymol.show()

This series of commands will define a variable ``pymol`` of class ``MolViewer``, which can pass commands to PyMOL, and then create an image of ``PDBID:3odu`` in your IPython session.
Any additional commands can be invoked via ``pymol.do("[ENTER YOUR COMMAND HERE]")``.

Here's an additional `example <http://nbviewer.ipython.org/urls/raw.github.com/cxhernandez/iPyMol/master/examples/Example.ipynb>`_.

Enjoy!
