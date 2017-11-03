from __future__ import print_function

import os
import time
import tempfile
import threading
import numpy as np
import warnings
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from .compat import Image, Server


HOST = os.environ.get('PYMOL_RPCHOST', 'localhost')
PORT = 9123


class MolViewer(object):
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = int(port)
        self._thread = threading.Thread(
            target=os.system,
            args=(('pymol -RQ',)),
        )
        self._thread.daemon = True

    def _add_methods(self):
        for method in self._server.system.listMethods():
            if method[0].islower():
                setattr(self, method, getattr(self._server, method))

    def start(self):
        if self._thread.is_alive():
            print("A PyMOL RPC server is already running.")
            return
        self._thread.start()
        self._server = Server(
            uri="http://%s:%d/RPC2" % (self.host, self.port)
        )

        # check if the server is online yet, then add methods
        server_online = False
        while not server_online:
            try:
                if hasattr(self, '_server'):
                    self._add_methods()
                server_online = True
            except:
                pass

    def display(self):
        """Display PyMol session using matplotlib

        Returns
        -------
        fig : matplotlib.pyplot.figure

        """
        fig = plt.figure(figsize=(20, 20))
        ax = fig.add_subplot(111)
        ax.axis('off')
        fh = tempfile.NamedTemporaryFile()
        self._server.do("cmd.png('%s')" % fh.name)
        ax.imshow(mpimg.imread(fh.name))
        os.close(fh)
        return fig

# Create a default instance for convenience
viewer = MolViewer()
