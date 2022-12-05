from socket import *
import argparse # for command line parsing
import logging
import time
import statistics # for computing mean
import csv

def milliseconds(seconds):
    # convert seconds to milliseconds
    return seconds * 1000

def parse_args():
    # command for parsing command line arguments

    # create parser
    parser = argparse.ArgumentParser()

    # add arguments to the parser
    parser.add_argument("hostname_ip") # can be string or integer
    parser.add_argument("server_port")
    parser.add_argument("hashed_pw") # hashed pw

    # parse the arguments
    args = parser.parse_args()
    logging.info(args)

    return args.hostname_ip, int(args.server_port)

def tcp_setup(server_name, server_port):
    # Set up connection with the server
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    logging.info("[TCP Setup] Client connection attempted")
    return client_socket

# mt is measurement type
# rows is the data rows generated by measurement phase
def write_data_to_csv(mt, rows):
    # write tput or rtt data to csv
    with open(mt + '.csv', 'w') as f:
        headers = [["size", "mean"]]
        write = csv.writer(f)
        write.writerows(headers)
        write.writerows(rows)

def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO) # logging configuration
    TPUT_MSG_SIZE = 1
    buffer_size = TPUT_MSG_SIZE + 10000

    # Command: python3 client.py csa1.bu.edu 58002
    # Command: python3 client.py localhost 58002
    server_name, server_port, hashed_pw = parse_args()


    client_socket = tcp_setup(server_name, server_port)

    client_socket.close()
    logging.info("Connection closed")

    # TODO: manager logic

if __name__ == "__main__":
    main()
