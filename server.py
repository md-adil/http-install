from config import isHttpd
def restart():
	if isHttpd():
		system("systemctl restart httpd")
	system("systemctl restart apache2")
	