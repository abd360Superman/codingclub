import zipfile

# Create zip file
zip_atr = zipfile.ZipFile('mytest.zip', 'a')
zip_atr.close()

# Adding files to zip
zip_atr = zipfile.ZipFile('mytest.zip', 'a')
zip_atr.write('send2trash_funcs.py', compress_type=zipfile.ZIP_DEFLATED)
zip_atr.close()

# Adding folders to zip
zip_atr = zipfile.ZipFile('mytest.zip', 'a')
zip_atr.write('test', compress_type=zipfile.ZIP_DEFLATED)
zip_atr.close()

# Looking at files in zip
zip_atr = zipfile.ZipFile('mytest.zip')
print(zip_atr.namelist())
zip_atr.close()

# Extract files and folders from zip
zip_atr = zipfile.ZipFile('mytest.zip')
zip_atr.extractall(path='test')
zip_atr.close()