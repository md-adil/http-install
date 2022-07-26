#!/usr/local/bin/python3
from config import generate_host_config, write_config, create_site_dir, is_httpd
from user_input import site_name
from server.main import server


def run():
	site = site_name()
	print("Generating configuration file")
	conf = generate_host_config(site)
	print("Writing configuration file")
	written = write_config(site, conf)
	print(f"Configuration written to {written} successfully")
	print("Creating directory")
	create_site_dir(site)
	print("Restarting server:")
	print("Server is restarted.")


def main():
	serv = server()
	print("Running main task", serv.list())
if __name__ == "__main__":
	main()
	