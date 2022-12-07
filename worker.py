from socket import *
import argparse
import logging
import hashlib
import itertools, string
import math

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def parse_args():
    # create parser
    parser = argparse.ArgumentParser()

    # add arguments to the parser
    parser.add_argument("server_port", type=int)

    # parse the arguments
    args = parser.parse_args()
    logging.info(args)

    return args.server_port

def tcp_setup(server_port):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(('localhost', server_port))
    logging.info("The worker is ready to work")
    client_socket.send("ready".encode())
    return client_socket

def complete_task(server_port):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(('localhost', server_port))
    logging.info("The worker has completed the work")
    return client_socket

def brute_force(password):
    # password = the hashed password we want to crack

    for chr in itertools.product(CHARS, repeat=5):
        guess = ''.join(chr)
        found = guess
        md5 = hashlib.md5()
        md5.update(guess.encode('utf-8'))
        if md5.hexdigest() == password:
            print("Found string:", found)

            return found

    return 0

def divide_work(total, seq):
    # total = total number of nodes
    # seq = sequence number

    block = len(CHARS) // total
    # print("len(chars): ", len(CHARS))
    # print("total: ", total)
    # print("block: ", block)

    list = []
    for i in range(total):
        if i < (total-1):
            list.append(CHARS[i * block : (i+1) * block])
        else:
            list.append(CHARS[(i * block):])

    return list

def md5_hash(guess):
    # Given the guess string, compute and return its md5 hash
    md5 = hashlib.md5()
    md5.update(guess.encode('utf-8')) # compute hash
    return md5.hexdigest() # return the hash string

def brute_force_partial(total, seq, password):
    # total = total number of nodes
    # seq = sequence number
    # password = the hashed password we want to crack

    iter = 0

    # Worker i is in charge of iterating through all 5-character strings that starts with any letter in the string in entry i of list
    list = divide_work(total, seq)
    first_letters = list[seq]
    # print(list)
    # print(seq)
    # print(first_letters)

    # For each 1st letter in first_letters, append all possible 4-character strings to create the guess string. Then hash the guess string and compare this to the input password.
    for letter in first_letters:
        for chr in itertools.product(CHARS, repeat=4):
            guess = letter + ''.join(chr) # create the 5 character guessed password
            # print(guess)
            hash = md5_hash(guess)
            if hash == password:
                print("Found string:", guess)
                return guess

    print("Password Not Found")
    return 0

def main():
    buffer_size = 64000 # max TCP msg size

    server_port = parse_args() # parse command line args

    while(True) :
        client_socket = tcp_setup(server_port) # server socket setup
        # receive input from the management service
        msg = client_socket.recv(buffer_size).decode()

        # md5hash has 32 characters, if >32 then the user has input
        # TODO: When would len(msg) <= 32?
        if len(msg) > 32:
            client_socket.close() # Why do we close the socket, then re-connect in the complete_task function? Can't we keep the socket open throughout?
            total_node = int(msg[0])
            seq_num = int(msg[1])
            result = brute_force_partial(total_node, seq_num, msg[2:])
        else:
            client_socket.close()
            result = brute_force(msg)

        client_socket = complete_task(server_port)

        if result == 0:
            client_socket.send(str(result).encode())
        else:
            client_socket.send(result.encode())

        client_socket.close()

if __name__ == "__main__":
    main()
