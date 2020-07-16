import subprocess, os, sys

def descompress(file):
    file_separation = file.split('.')
    file_size = len(file_separation)
    file_extension = file_separation[1:]
    size_extension = len(file_extension)
    name_one_extension = file_separation[:file_size-1]
    size_array1 = len(name_one_extension)
    name_two_extension = file_separation[:file_size-2]
    size_array2 = len(name_two_extension)

    def convert_name(value, max):
        name_folder = ''
        count = 1
        for i in value: 
            if count == max:
                name_folder = name_folder + i
            else:
                name_folder = name_folder + i + '.'
            count = count + 1
        return name_folder

    gz = False
    xz = False
    
    if file_extension[size_extension-2] == 'tar':
        name_folder = convert_name(name_two_extension, size_array2)
        if file_extension[size_extension-1] == 'gz':
            gz = True
        elif file_extension[size_extension-1] == 'xz':
            xz = True
        if gz or xz:
            convert_extension = '.' + file_extension[size_extension-2] + '.' + file_extension[size_extension-1] 
        else:
            convert_extension = '.' + file_extension[size_extension-1]
    else:
        convert_extension = '.' + file_extension[size_extension-1] 
        name_folder = convert_name(name_one_extension, size_array1)
               
    try:
        compress = subprocess.run(
            ('find {} 1>&2'.format(sys.argv[1])),
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as er:
        errr = er
    else:
        if compress.returncode != 0:
            print('Compressed file is missing')
        else:
            try:
                completed = subprocess.run(
                    ('find {} 1>&2'.format(name_folder)),
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            except subprocess.CalledProcessError as err:
                e = err
            else:
                if completed.returncode == 0:
                    print('The folder exists')
                    sys.exit(1)
                else:
                    os.system('mkdir {}'.format(name_folder))
                    if convert_extension == '.zip':
                        os.system('unzip {} -d {}'.format(file, name_folder))
                    elif convert_extension == '.tar.gz' and gz:
                        os.system('tar -xzvf {} -C {}'.format(file, name_folder))
                    elif convert_extension == '.tar':
                        os.system('tar -xvf {} -C {}'.format(file, name_folder))
                    elif convert_extension == '.rar':
                        os.system('unrar x {} -d {}'.format(file, name_folder))
                    elif convert_extension == '.tar.xz' and xz:
                        os.system('tar -Jxvf {}'.format(file))
                    elif convert_extension == 'gz':
                        os.system('gzip -d {}'.format(file))
                    else:
                        os.system('rmdir {}'.format(name_folder))
                        os.system('gunzip -r {}'.format(file))          

if __name__ == "__main__":
    descompress(sys.argv[1])
