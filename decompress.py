#!/usr/bin/env python3
import sys, os

def descompress(file):
    file_separation = file.split('.')
    file_size = len(file_separation)
    name_file = file_separation[0]
    file_extension = file_separation[1:]
    size_extension = len(file_extension)
    convert_extension =''
    for c in range(0,size_extension):
        convert_extension = convert_extension + '.' + file_extension[c] 

    compress = os.system('find {}'.format(sys.argv[1]))
    if convert_extension == '.zip' and (compress == 0):
        folder = os.system('find {}'.format(name_file))
        if folder == 0:
            print('The folder exist')
            sys.exit(1)
        else:
            os.system('mkdir {}'.format(name_file))
            os.system('unzip {} -d {}'.format(file, name_file))
    else:
        sys.exit(2)

if __name__ == "__main__":
    descompress(sys.argv[1])
