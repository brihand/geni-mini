from socket import *
import argparse # for command line parsing
import logging
##import time
#import statistics # for computing mean
import csv

def milliseconds(seconds):
    # convert seconds to milliseconds
    return seconds * 1000

def parse_args():
    # command for parsing command line arguments

    # create parser
    parser = argparse.ArgumentParser()

    # add arguments to the parser
    parser.add_argument("server_port")
    parser.add_argument("hashed_pw") # hashed pw
    parser.add_argument("num_nodes") # number of worker nodes used to crack

    # parse the arguments
    args = parser.parse_args()
    logging.info(args)

    return int(args.server_port), args.hashed_pw, int(args.num_nodes)

def tcp_setup(server_port):
    # Set up connection with the server
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('localhost', server_port))
    #logging.info("[TCP Setup] Client connection attempted")
    server_socket.listen(10)
    return server_socket

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

    server_port, hashed_pw, num_nodes = parse_args()

    server_socket = tcp_setup(server_port)
    count = 1
    while(True):
        connection_socket, addr = server_socket.accept()
        logging.info("New client (" + str(addr) + ") attached")
        response = connection_socket.recv(1024).decode()
        # if user wants multiple workers to crack the same password(evenly distributed)
        if num_nodes > 1:
            if count <= num_nodes:
                if response == "ready":
                    connection_socket.send((str(num_nodes) + str(count) + "594f803b380a41396ed63dca39503542").encode())
                    count += 1
                else:
                    print("Found string:", response)
        # if user wants only one worker to crack the whole password
        elif num_nodes <= 1:
            if response == "ready":
                connection_socket.send("594f803b380a41396ed63dca39503542".encode())
            else:
                print("Found string:", response)
    server_socket.close()
    logging.info("Connection closed")

    # TODO: manager logic

if __name__ == "__main__":
    main()
