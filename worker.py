from socket import *
import argparse
import logging
import hashlib
import itertools, string
import math

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
    # start = string where we start the brute force search
    # stop = string where we stop the brute force search
    # password = the hashed password we want to crack

    # TODO: use md5-brute-force
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for chr in itertools.product(chars, repeat=5):
        guess = ''.join(chr)
        found = guess
        md5 = hashlib.md5()
        md5.update(guess.encode('utf-8'))
        if md5.hexdigest() == password:
            print("Found string:", found)

            return found

    return 0

def brute_force_partial(total, seq, password):
    # start = string where we start the brute force search
    # stop = string where we stop the brute force search
    # password = the hashed password we want to crack

    # TODO: use md5-brute-force
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    perm_length = math.perm(len(chars), 5)
    iter = 0
    block = perm_length // total
    # the node is responsible for the first block
    if seq == 1:
        perm_start = 0
        perm_end = block - 1
    # responsible for the last block
    elif seq == total:
        perm_start = block * (seq - 1)
        perm_end = perm_length - 1
    #responsible for the block in the middle
    else:
        perm_start = block * (seq - 1)
        perm_end = perm_start + block - 1
    for chr in itertools.product(chars, repeat=5):
        if perm_start <= iter <= perm_end:
            iter += 1
            guess = ''.join(chr)
            found = guess
            md5 = hashlib.md5()
            md5.update(guess.encode('utf-8'))
            if md5.hexdigest() == password:
                print("Found string:", found)

                return found
        elif iter > perm_end:
            break
        else:
            iter += 1
            continue
    print("Password Not Found")
    return 0

def main():
    buffer_size = 64000 # max TCP msg size

    # TODO: double check what command line args we want to parse
    server_port = parse_args() # parse command line args

    while(True) :
        client_socket = tcp_setup(server_port) # server socket setup
        # receive input from the management service
        msg = client_socket.recv(buffer_size).decode()
        # md5hash has 32 characters, if >32 then the user has input 
        if len(msg) > 32:
            client_socket.close()
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
