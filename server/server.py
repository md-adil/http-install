from shutil import which

class Location:
	pattern: str
	modifier: str
	root: str
	index: str

class Server:
	server: str
	filename: str
	name: str
	location: Location
	port: int
	is_ssl: bool


def is_apache2():
	return which('apache2') is not None or  which('httpd') is not None

def is_nginx():
	return True
    # return which('nginx') is not None