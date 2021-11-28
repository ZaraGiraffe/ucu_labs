import argparse, os, zipfile


par = argparse.ArgumentParser(description='zip the files')
par.add_argument('path', help='path to directory')
par.add_argument('dst', help='destination of the archive')


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


if __name__ == '__main__':
    obj = par.parse_args()
    if not os.path.exists(obj.path) or not os.path.exists(obj.dst):
        print('there is no such directory')
        exit()
    zip = zipfile.ZipFile(os.path.join(obj.dst, 'new.zip'), 'w')
    zipdir(obj.path, zip)
    zip.close()
