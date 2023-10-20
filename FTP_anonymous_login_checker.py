import ftplib

def anonLogin(hostname):
	try:
		ftp= ftplib.FTP(hostname)
		ftp.login('anonymous')
		print('\n [+] ' + str(hostname) + ' FTP Anonymous Login Allowed.')
		ftp.quit()
		return True
	except Exception:
		print('\n [-]' + str(hostname) + ' FTP Anonymous Login Fails.')
		return False

if __name__ == '__main__':
	anonLogin('{IP}')
