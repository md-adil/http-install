import os
import nginx
from .server import Location, Server

class NginxServer():
    def __init__(self):
        self.sites_dir = 'stubs/nginx'
        self.command = 'nginx'

    def getServers(self):
        servers = []
        for file in os.scandir(self.sites_dir):
            servers.append(createServer(nginx.loadf(file.path).servers, file.path))
        return servers

    def list(self):
        names = []
        for server in self.getServers():
            names.append(server.name)
        return names

    def restart(self):
        os.system(f'{self.command} -s reload')

    def stop(self):
        os.system(f'{self.command} -s stop')
    
    def start(self):
        os.system(f'{self.command} -s start')
    
    def remove(self, filename: str, server_name: str):
        print('removing server', filename, server_name)
    
    def add(self, name: str):
        print('Adding server')
    
    def add_proxy(self, name: str, port: int, host: str = 'http://127.0.0.1'):
        pass

def createServer(rows, filename):
    srv = Server()
    srv.filename = filename
    for row in rows:
        for line in row.as_dict.get('server'):
            for key, val in line.items():
                if key[0] == '#':
                    continue
                if key == 'server_name': srv.name = val; continue
                if key == 'listen': srv.port = val; continue
            
    return srv

def createLocation(key: str, val: str) -> Location:
    loc = Location()
    loc.pattern = ''
    return loc