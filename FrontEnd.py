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
    logging.info("The front end is connected.")
    client_socket.send("FrontEnd".encode())
    return client_socket

def complete_task(server_port):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(('localhost', server_port))
    logging.info("The worker has completed the work")
    return client_socket



def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO) # logging configuration

    server_port = parse_args()

    client_socket = tcp_setup(server_port)
    while(True):
        
        
        


if __name__ == "__main__":
    main()