import os
import time
import tempfile
import xmlrpclib
import numpy as np
try:
    import Image
except ImportError:
    from PIL import Image


def init():
    """ Initialize a local instance of PyMol.

    """

    from multiprocessing import Process

    def f(cmd):
        import os
        os.system(cmd)

    p = Process(target=f, args=('pymol -Rq',))
    p.start()


class MolViewer(object):
    def __init__(self, host=None, port=9123):

        if not host:
            host = os.environ.get('PYMOL_RPCHOST', 'localhost')

        self._server = xmlrpclib.Server('http://%s:%d' % (host, port))
        self._server.ping()

    def do(self, cmd):
        """Perform any PyMol command(s).

        Parameters
        ----------
        cmd : str
            PyMol command String. Example usage: MolViewer.do('as cartoon;')

        """

        if isinstance(cmd, str):
            self._server.do(cmd)
        else:
            TypeError('Command must be a String.')

    def reinit(self):
        """ A convenience function to reinitialize a PyMol session.

        """
        self._server.do('reinit;')

    def to_png(self, height=0, width=0, dpi=300, delay=0.0):
        """Render a PNG from a PyMol session.

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
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as fd:
            fname = fd.name
        self.do('png %s, %d, %d, %d' % (fname, height, width, dpi))
        time.sleep(0.2)  # <- wait a short period so that PyMol can finish
        img = None
        for i in range(10):
            try:
                img = Image.open(fname)
                break
            except IOError:
                time.sleep(0.1)
        if img is not None:
            os.unlink(fname)
            return img
        else:
            IOError('Could not load image from PyMol.')

    def show(self):
        """Display PyMol session using matplotlib.

        Returns
        -------
        fig : matplotlib.pyplot.figure

        """

        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(20, 20))
        ax = fig.add_subplot(111)
        ax.axis('off')
        ax.imshow(np.asarray(self.to_png()))
        return fig
