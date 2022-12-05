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
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("", server_port))
    server_socket.listen(1)
    logging.info("The server is ready to receive")

    # connection_socket, addr = server_socket.accept()
    # logging.info("[TCP Setup] New client attached")

    return server_socket

def brute_force(password):
    # start = string where we start the brute force search
    # stop = string where we stop the brute force search
    # password = the hashed password we want to crack

    # TODO: use md5-brute-force
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for chr in itertools.product(chars, 5):
        guess = ''.join(chr)
        found = guess
        md5 = hashlib.md5()
        md5.update(guess.encode('utf-8'))
        if md5.hexdigest() == password:
            print("\nFound string:", found)

    return found

def main():
    buffer_size = 64000 # max TCP msg size

    # TODO: double check what command line args we want to parse
    server_port = parse_args() # parse command line args
    server_socket = tcp_setup(server_port) # server socket setup
    logging.info("Worker setup done")

    connection_socket, addr = server_socket.accept()
    logging.info("New client (" + str(addr) + ") attached")

    # receive input from the management service
    msg = connection_socket.recv(buffer_size).decode()

    # parse message

    brute_force(msg)

    connection_socket.close()

if __name__ == "__main__":
    main()
