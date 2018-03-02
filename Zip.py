import zipfile
import tarfile
import rarfile
import os
import shutil
from glob import glob
import sys

Pos_zip=sys.argv[1]
Pos_unzip=sys.argv[2]
Type=sys.argv[3]

files = glob(Pos_zip)

def un_zip(filename):
	zip_file = zipfile.ZipFile(filename)
	a_name=zip_file.namelist()
	if (filename.find(".zip")) > -1:
		zip_file = zipfile.ZipFile(filename)
		a_name=zip_file.namelist()
	if (filename.find(".tar")) > -1:
		zip_file = tarfile.open(filename)
		a_name=zip_file.getnames()
		#zip_file=zipfile.getnames()
	if (filename.find(".rar")) > -1:
		zip_file = rarfile.RarFile(filename)
		a_name=zip_file.namelist()
	for names in a_name:
		if (names.find(Type)) > -1:
			try:
				zip_file.extract(names,Pos_unzip)
			except:
				print(filename+"解压失败！")
				pass
	print (filename+"解压完成！")
for file_name in files:
	un_zip(file_name)