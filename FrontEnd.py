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
        client_socket.send(hash.encode())
    #with open('tests.csv', newline='') as csvfile:
    #    csv_reader = csv.reader(csvfile, delimiter=',')
    #    for row in csv_reader:
    #        if line_count == 0:
    #            line_count += 1
    #            pass
    #        else:
    #            time.sleep(random.random())
    #            client_socket.send(row[1].encode())
    #            line_count += 1
    client_socket.close()
        
        


if __name__ == "__main__":
    main()