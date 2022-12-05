# This file generates the tests.csv file, which compares pairs of the form (plaintext, md5 hash of plaintext).

import hashlib
import csv

PLAINTXTS = ['aaaaa','bbbbb','AAAAA','aAaAa','zzzZZ','abcde']
FIELDS = ['plaintext', 'hashed_val']

def gen_hash_pairs():

    #init md5 hash function
    md5 = hashlib.md5()

    hashes = []
    for p in PLAINTXTS:
        md5.update(p.encode('utf-8'))
        pair = [p, md5.hexdigest()]
        hashes.append(pair)

    return hashes

def main():
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
