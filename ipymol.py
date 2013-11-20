# $Id$
# This Python file uses the following encoding: utf-8
"""
#   Author: Carlos Xavier Hernández [cxh@stanford.edu]
#
#
#   This module was adapted from RDKit.
#
#
"""
import xmlrpclib,os,tempfile,numpy

_server=None
class MolViewer(object):
  def __init__(self,host=None,port=9123,force=0,**kwargs):
    global _server
    if not force and _server is not None:
      self.server=_server
    else:
      if not host:
        host=os.environ.get('PYMOL_RPCHOST','localhost')
      _server=None
      serv = xmlrpclib.Server('http://%s:%d'%(host,port))
      serv.ping()
      _server = serv
      self.server=serv
    self.InitializePyMol()
  
  def InitializePyMol(self):
    """ does some initializations to set up PyMol according to our
    tastes
    
    """
    self.server.do('set valence,1')
    self.server.do('set stick_rad,0.15')
    self.server.do('set mouse_selection_mode,0')
    self.server.do('set line_width,2')
    self.server.do('set selection_width,10')
    self.server.do('set auto_zoom,0')

  
  def GetPNG(self,h=None,w=None,preDelay=0):
    try:
      import Image
    except ImportError:
      from PIL import Image
    import time
    if preDelay>0:
      time.sleep(preDelay)
    fd = tempfile.NamedTemporaryFile(suffix='.png',delete=False)
    fd.close()
    self.server.do('png %s'%fd.name)
    time.sleep(0.2)  # <- wait a short period so that PyMol can finish
    for i in range(10):
      try:
        img = Image.open(fd.name)
        break
      except IOError:
        time.sleep(0.1)
    os.unlink(fd.name)
    fd=None
    if h is not None or w is not None:
      sz = img.size
      if h is None:
        h=sz[1]
      if w is None:
        w=sz[0]
      if h<sz[1]:
        frac = float(h)/sz[1]
        w *= frac
        w = int(w)
        img=img.resize((w,h),True)
      elif w<sz[0]:
        frac = float(w)/sz[0]
        h *= frac
        h = int(h)
        img=img.resize((w,h),True)
    return img
  
  def Show(self):
      import matplotlib.pyplot as plt
      plt.figure(figsize=(20,20))
      plt.axis('off')
      plt.imshow(numpy.asarray(self.GetPNG()))