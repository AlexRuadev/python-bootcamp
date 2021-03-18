f = open('fileone.text', 'w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.text', 'w+')
f.write('TWO FILE')
f.close()

import zipfile

comp_file = zipfile.ZipFile('comp_file.zip', 'w')

comp_file.write('fileone.text', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.text', compress_type=zipfile.ZIP_DEFLATED)

comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip','r')

zip_obj.extractall('extracted_content')


import shutil
# Point out a directory which we want to turn into a zip file
dir_to_zip = "C:/xampp/htdocs/python-bootcamp"
output_filename = 'example'

shutil.make_archive(output_filename, 'zip', dir_to_zip)