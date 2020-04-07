import os
from config import is_httpd
def restart():
	if is_httpd():
		os.system("systemctl restart httpd")
	os.system("systemctl restart apache2")
	