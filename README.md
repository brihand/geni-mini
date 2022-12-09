# geni-mini
Project: Password Cracker

Authors: Chun To Pun, Brian Sohn, Zongxi Cheng, Megan Chen

Writeup [document](https://docs.google.com/document/d/1vAtTclWTXI9HiJjKROnm9SA3CvpJgDWSA3B-15j78KE/edit?usp=sharing)

Introduction:

In this project, we want to understand whether it’s possible to speed up the brute force search via creating a network of worker nodes. Given an md5 hash of a 5-character password (a-z, A-Z), we consider the average time it takes a hacker to recover a password. The hacker may run a distributed system in which worker nodes are dynamically activated depending on worker availability.

We design and implement a distributed system that allows dynamic participation of workers. We also collect experimental data on the average runtime for when the adversary’s distributed system runs in GENI. We describe these in detail in the coming sections.

# Usage instructions:
Our code runs with the following steps:
1. Pick a `<management_port_number>` for the manager. This will be the same for all the commands below. For example, Megan picked `<management_port_number> = 30001`.

## Set up the management node.
2. ssh into the node with the command `ssh -i <local ssh key file> <username>@<hostname> -p <port_number>`. For example: `ssh -i ~/.ssh/id_geni_ssh_rsa megchen@pc2.instageni.wisc.edu -p 25010`.
3. Run management.py code: `python3 ../alcheng/management.py <management_port_number>`.
4. Set up the worker nodes. For all worker nodes (worker1 - worker 4), do the following:
ssh into each worker node with the command `ssh -i <local ssh key file> <username>@<hostname> -p <port_number>`.
5. Run worker.py code: `python ../alcheng/worker.py <worker_port_number>`.

## Input hash into the front end (i.e. worker5).
6. ssh into the worker5 node with the command `ssh -i <local ssh key file> <username>@<hostname> -p <port_number>`.
7. Run FrontEnd.py code: `python ../alcheng/FrontEnd.py <managment_port_number>`.
8. When the command line prompt says ‘Please input number of nodes to split work’, put in the number of workers you want to crack the password (between 1-4).
9. When the command line prompt says ‘Please input a md5 hash of 5 character password:’, put in the md5 hash string that you want to crack. We provided test cases in tests.csv.

10. After the workers finish cracking the password, the manager node will print out how long it took to crack the password.

11. To change the number of worker nodes, kill the manager first because it is the server. Next, kill the workers and front end. Finally, restart at Step 1 above.
