import os
import hashlib

# read() function called without arguments will read all the contents of file and load them in memory.
# We don't want to allocate 2 gigs of ram for a 2 gigabyte file so, we gotta deal with those bigger files in chunks!
# buf_size is totally arbitrary, change for your app. For this example, lets read stuff in 64kb chunks!


def get_file_hash(file_path, buf_size=65536):
    sha1 = hashlib.sha1()
    f = open(file_path, 'rb')   # Read file in binary mode. md5 function needs to read file as sequence of binary bytes.
    data = f.read(buf_size)
    while len(data) > 0:
        sha1.update(data)
        data = f.read(buf_size)
    f.close()
    return sha1.hexdigest()


# os.walk takes care of the details, and on every pass of the loop, it gives us three things:
# dirName: The next directory it found.
# subdirList: A list of sub-directories in the current directory.
# fileList: A list of files in the current directory.
def find_dups(dir_path):
    dup_hashs = {}
    for dir_name, sub_dirlist, file_list in os.walk(dir_path):
        for file_name in file_list:
            path = os.path.join(dir_name, file_name)
            file_hash = get_file_hash(path)
            print ("path=%s, file_hash=%s" %(path, file_hash))
            if file_hash in dup_hashs:
                dup_hashs[file_hash].append(path)
            else:
                dup_hashs[file_hash] = [path]
    return dup_hashs


if __name__ == "__main__":
    dir_path = "/Users/tahir/dup/"
    dup_hashs = find_dups(dir_path)
    print (dup_hashs)

