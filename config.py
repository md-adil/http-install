import os
from shutil import which

def is_httpd():
	return which('httpd') is not None
	
def get_sites_dir():
	return "/var/www"
	
def get_conf_dir():
	if is_httpd():
		return "/etc/httpd/conf.d"
	return "/etc/apache2/sites-available"

def get_log_dir():
	if is_httpd():
		return "/var/log/httpd"
	return "/var/log/httpd"
	
def create_site_dir(site):
	os.mkdir(f'{sites_dir()}/{site}')

def generate_host_config(site_name):
	log_dir = get_log_dir()
	return f"""<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	ServerName {site_name}
	DocumentRoot {get_sites_dir()}/{site_name}
	ErrorLog {log_dir}/{site_name}-error.log
	CustomLog {log_dir}/{site_name}-access.log combined
</VirtualHost>
"""
	
def write_config(name, config):
	name = f"{get_conf_dir()}/{name}.conf"
	with open(name, "w") as file:
		file.write(config);
	return name