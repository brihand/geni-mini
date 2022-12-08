from socket import *
import argparse
import logging
import csv
import time
import random

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
    client_socket.connect(('172.17.2.1', server_port))
    logging.info("The front end is connected.")
    client_socket.send("FrontEnd".encode())
    return client_socket



def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO) # logging configuration

    server_port = parse_args()

    client_socket = tcp_setup(server_port)

    print(client_socket.recv(1024).decode())
    num_of_nodes = input()
    client_socket.send(str(num_of_nodes).encode())
    while(True):
        print('Please input a md5 hash of 5 character password:')
        hash = input()

        if hash == 'exit':
            client_socket.close()

        client_socket.send(hash.encode())


if __name__ == "__main__":
    main()
