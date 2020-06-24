#!/usr/bin/env python3
import sys, os

def descompress(file):
    file_separation = file.split('.')
    file_size = len(file_separation)
    name_folder = file_separation[0]
    file_extension = file_separation[1:]
    size_extension = len(file_extension)
    convert_extension =''

    for c in range(0,size_extension):
        convert_extension = convert_extension + '.' + file_extension[c] 

    compress = os.popen('find {}'.format(sys.argv[1])).read()
    if compress != '':
        folder = os.popen('find {}'.format(name_folder)).read()
        if folder != '':
            print('The folder exists')
            sys.exit(1)
        else:
            os.system('mkdir {}'.format(name_folder))
            if convert_extension == '.zip':
                os.system('unzip {} -d {}'.format(file, name_folder))
            elif convert_extension == '.tar.gz':
                os.system('tar -xzvf {}'.format(file))
            elif convert_extension == '.tar':
                os.system('tar -xvf {} -C {}'.format(file, name_folder))
            elif convert_extension == '.rar':
                os.system('unrar x {} -d {}'.format(file, name_folder))
            else:
                os.system('rmdir {}'.format(name_folder))
                os.system('gunzip -r {}'.format(file))          
    else:
        sys.exit(2)

if __name__ == "__main__":
    descompress(sys.argv[1])
