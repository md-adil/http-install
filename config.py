import os
def isHttpd():
	return True
	
def sites_dir():
	return "/var/www"
	
def conf_dir():
	return "."
	if isHttpd():
		return "/etc/httpd/conf.d"
	return "/etc/apache2/sites-available"

def log_dir():
	if isHttpd():
		return "/var/log/httpd"
	return "/var/log/httpd"
	
def create_site_dir(site):
	os.mkdir(f'{sites_dir()}/{site}')

def generate_host_config(site_name):
	site = sites_dir()
	log = log_dir()
	return f"""<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	ServerName {site_name}
	DocumentRoot {site}/{site_name}
	ErrorLog {log}/{site_name}-error.log
	CustomLog {log}/{site_name}-access.log combined
</VirtualHost>
"""
	
def write_config(name, config):
	fname = f"{conf_dir()}/{name}.conf"
	with open(fname, "w") as file:
		file.write(config);
	return fname