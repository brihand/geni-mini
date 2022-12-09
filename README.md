# geni-mini
Project: Password Cracker

Authors: Chun To Pun, Brian Sohn, Zongxi Cheng, Megan Chen

Writeup [document](https://docs.google.com/document/d/1vAtTclWTXI9HiJjKROnm9SA3CvpJgDWSA3B-15j78KE/edit?usp=sharing)

Introduction: 

In this project, we want to understand whether it’s possible to speed up the brute force search via creating a network of worker nodes. Given an md5 hash of a 5-character password (a-z, A-Z), we consider the average time it takes a hacker to recover a password. The hacker may run a distributed system in which worker nodes are dynamically activated depending on worker availability.

We design and implement a distributed system that allows dynamic participation of workers. We also collect experimental data on the average runtime for when the adversary’s distributed system runs in GENI. We describe these in detail in the coming sections.

Procedure:

