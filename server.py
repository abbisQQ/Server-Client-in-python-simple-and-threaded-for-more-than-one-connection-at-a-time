import socket
import sys


# Create a Socket()
def create_socket():
    try:
        global host
        global port
        global s
        host = "127.0.0.1"
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation Error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding Error: " + str(msg) +"\n" +"Retrying...")
        bind_socket()


# Establish connection
def socket_accept():
    conn,addreess = s.accept()
    print("Connection has been established with : " +addreess[0] + ":"+str(addreess[1]))
    send_commands(conn)
    conn.close()


# Send Commands to Client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_responce = str(conn.recv(1024), "utf-8")
            print(client_responce, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
