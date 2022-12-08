# This file generates the tests.csv file, which compares pairs of the form (plaintext, md5 hash of plaintext).

import hashlib
import csv
import random
import string 


#PLAINTXTS = ['aaaaa','bbbbb','AAAAA','aAaAa','zzzZZ','abcde']
PLAINTXTS = []
FIELDS = ['plaintext', 'hashed_val']

def gen_single_random_plaintext():

    rand = string.ascii_letters
    random_plain = ''.join(random.choice(rand) for i in range(5))
    
    return random_plain

def gen_multi_random_plaintext(size):

    for i in range(size):
        PLAINTXTS.append(gen_single_random_plaintext())
    
    #print(PLAINTXTS)

def gen_hash_pairs():

    #init md5 hash function
    md5 = hashlib.md5()

    hashes = []
    for p in PLAINTXTS:
        md5 = hashlib.md5()
        md5.update(p.encode('utf-8'))
        pair = [p, md5.hexdigest()]
        hashes.append(pair)

    return hashes

def main():

    gen_multi_random_plaintext(20)

    hash_pairs = gen_hash_pairs()
    print('Hash pairs:', hash_pairs)

    filename = 'tests.csv'

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # write the header row
        csvwriter.writerow(FIELDS)

        # write the data rows
        csvwriter.writerows(hash_pairs)

    print('Wrote hash pairs to ', filename)

if __name__ == "__main__":
    main()
    
