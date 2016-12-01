try:
    from PIL import Image
except ImportError:
    import Image

try:
    from xmlrpc.client import ServerProxy as Server
except:
    from xmlrpclib import Server
