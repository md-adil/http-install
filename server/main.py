import os
from .apache2 import Apache2Server
from .nginx import NginxServer
from .server import *

def server():
    if is_nginx():
        return NginxServer()
    if is_apache2():
        return Apache2Server()
    raise Exception("Server is not installed")
    
