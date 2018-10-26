from __future__ import print_function

import os
import time
import tempfile
import subprocess

from .compat import Server

HOST = os.environ.get('PYMOL_RPCHOST', 'localhost')
PORT = 9123


class MolViewer(object):
    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = int(port)
        self._process = None

    def __del__(self):
        self.stop()

    def __getattr__(self, key):
        if not self._process_is_running():
            self.start(["-cKQ"])

        return getattr(self._server, key)

    def _process_is_running(self):
        return self._process is not None and self._process.poll() is None

    def start(self, args=("-Q",), exe="pymol"):
        """Start the PyMOL RPC server and connect to it

        Start simple GUI (-xi), suppress all output (-Q):

            >>> viewer.start(["-xiQ"])

        Start headless (-cK), with some output (-q):

            >>> viewer.start(["-cKq"])

        """
        if self._process_is_running():
            print("A PyMOL RPC server is already running.")
            return

        assert isinstance(args, (list, tuple))

        self._process = subprocess.Popen([exe, "-R"] + list(args))

        self._server = Server(uri="http://%s:%d/RPC2" % (self.host, self.port))

        # wait for the server
        while True:
            try:
                self._server.bg_color('white')
                break
            except IOError:
                time.sleep(0.1)

    def stop(self):
        if self._process_is_running():
            self._process.terminate()

    def display(self, ray=0):
        """Display PyMol session

        Returns
        -------
        fig : IPython.display.Image

        """
        from IPython.display import Image
        from IPython.display import display
        from ipywidgets import IntProgress

        progress = None
        filename = tempfile.mktemp('.png')

        try:
            self._server.png(filename, 0, 0, -1, int(ray))

            # ~2min timeout
            for i in range(1, 50):
                if os.path.exists(filename):
                    break

                if progress is None:
                    progress = IntProgress(min=0, max=50)
                    display(progress)

                progress.value += 1
                time.sleep(i / 10.0)

            return Image(filename)
        finally:
            if progress is not None:
                progress.close()

            try:
                os.unlink(filename)
            except:
                pass


# Create a default instance for convenience
viewer = MolViewer()
