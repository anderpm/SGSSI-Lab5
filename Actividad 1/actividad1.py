import hashlib as hl
import sys
import shutil
import string,random
NEW_FILE_SUFIX = "hash50"
TARGET_HASH_PREFIX = '00'
STRING_LEN = 8

def find_file_hash(file_name):
    # Create the new file without the modification
    new_file_name = file_name[:-3]+NEW_FILE_SUFIX+".txt"
    shutil.copyfile(file_name, new_file_name)
    f = open(file_name,'r')
    f2 = open(new_file_name, "w")
    # file_content = (''.join(str(e)) for e in f.readlines())
    file_con = f.readlines()

con = ''
for i in range(0,len(file_con)):
    con += file_con[i]
random.seed(30)
rand_string = ''.join(random.choices(string.hexdigits,k=STRING_LEN))+'\n'
con+=rand_string+'\n'
h = hl.sha256(con.encode('ascii')).hexdigest()
ite = 1

while h[:len(TARGET_HASH_PREFIX)] != TARGET_HASH_PREFIX:
    #Remove last 8 caracters
    con = con[:-9]
    # Find 8 character chain to obtain target hash of the new file
    rand_string = ''.join(random.choices(string.hexdigits,k=STRING_LEN))+'\n'
    # Add to the file and check the hash
    con += str(rand_string)
    # Calculate the new hash
    h = hl.sha256(con.encode('ascii')).hexdigest()
    ite += 1
    print(h)
print("VALID hash: "+h+"\n")
f2.write(con + " G3738")
f.close()
f2.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("ERROR")
        exit(1)
    else:
    file_name = sys.argv [1]
    find_file_hash(file_name)