import os
import time
import tempfile
import xmlrpclib
import threading
import numpy as np
import matplotlib.pyplot as plt
from ipymol.compat import Image

HOST = os.environ.get('PYMOL_RPCHOST', 'localhost')
PORT = 9123


class MolViewer(object):
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = int(port)
        self._thread = threading.Thread(
            target=os.system,
            args=(('pymol -cKRQ',)),
        )
        self._thread.daemon = True

    def start(self):
        if self._thread.is_alive():
            print "A PyMOL RPC server is already running."
            return
        self._thread.start()
        self._server = xmlrpclib.Server(
            'http://%s:%d' % (self.host, self.port)
        )
        self._server.ping()

    def do(self, cmd):
        """Perform any PyMOL command(s)

        Parameters
        ----------
        cmd : str
            PyMOL command String.

        Examples:
        --------
        >>> MolViewer.do('as cartoon;')

        """

        if isinstance(cmd, str):
            self._server.do(cmd)
        else:
            TypeError('Command must be a String.')

    def reinit(self):
        """A convenience function to reinitialize a PyMOL session"""
        self._server.do('reinit;')

    def to_png(self, height=0, width=0, dpi=300, delay=0.0):
        """Render a PNG from a PyMol session

        Parameters
        ----------
        height : int
            Height of rendered image.
        width : int
            Width of rendered image.
        dpi : int
            Resolution of rendered image in dots-per-inch.
        delay : float
            Time delay (seconds) before image is rendered.

        Returns
        -------
        img : PIL.Image
        """

        if delay > 0.0:
            time.sleep(delay)
        elif delay < 0.0:
            ValueError('Time should be non-negative.')
        fname = tempfile.mkstemp(suffix='.png')[1]
        self.do('png %s, %d, %d, %d' % (fname, height, width, dpi))
        # retry 10 times and wait a short period everytime so that PyMOL can
        # finish
        img = None
        for i in xrange(10):
            time.sleep(0.1)
            try:
                img = Image.open(fname)
                break
            except IOError:
                pass
        if img is not None:
            os.unlink(fname)
            return img
        else:
            IOError('Could not load image from PyMOL.')

    def show(self):
        """Display PyMol session using matplotlib

        Returns
        -------
        fig : matplotlib.pyplot.figure

        """
        fig = plt.figure(figsize=(20, 20))
        ax = fig.add_subplot(111)
        ax.axis('off')
        ax.imshow(np.asarray(self.to_png()))
        return fig

# Create a default instance for convenience
viewer = MolViewer()
