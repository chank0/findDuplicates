#!/usr/bin/python3

import hashlib
import os
import sys

#Get the hash (md5) of a file
def get_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


try:
    dir_a = sys.argv[1]
    dir_b = sys.argv[2]
except:
    print("Please provide two arguments")
    sys.exit(1)

list_dirs = [dir_a, dir_b]

#Check that the two directories are really directories
for c in list_dirs:
    if not os.path.isdir(c):
        print("Argument " + c + " is not a directory")
        sys.exit(1)

#Get a dictionary with all the files in the two directories, using the hash as key
dict_all_files = dict()

for cdir in list_dirs:
    for root, subfolders, files in os.walk(cdir):
        for item in files:
            cpath = os.path.join(root,item)
            hash = get_hash(cpath)
            newdict = {"dir" : cdir, "name" : item, "relpath" : cpath, "hash" : hash}
            if hash in dict_all_files:
                print("File " + cpath + " is a duplicate of " + dict_all_files[hash]["relpath"])
            dict_all_files[hash] = newdict

sys.exit(0)