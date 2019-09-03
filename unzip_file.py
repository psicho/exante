import zipfile

stories_zip = zipfile.ZipFile('C:\\Stories\\Funny\\archive.zip')

for file in stories_zip.namelist():
    if stories_zip.getinfo(file).file_size < 1024 * 1024:
        stories_zip.extract(file, 'C:\\Stories\\Short\\Funny')

stories_zip.close()