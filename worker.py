from socket import *
import argparse
import logging
import hashlib
import itertools, string

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
    client_socket.connect(("172.17.2.1", server_port))
    logging.info("The worker is ready to work")

    # connection_socket, addr = server_socket.accept()
    # logging.info("[TCP Setup] New client attached")

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

def main():
    buffer_size = 64000 # max TCP msg size

    # TODO: double check what command line args we want to parse
    server_port = parse_args() # parse command line args
    client_socket = tcp_setup(server_port) # server socket setup
    logging.info("Worker setup done")



    # receive input from the management service
    msg = client_socket.recv(buffer_size).decode()

    # parse message

    client_socket.send(brute_force(msg))


    client_socket.close()

if __name__ == "__main__":
    main()
