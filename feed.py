import socket
import os
from dotenv import find_dotenv, load_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Twitch IRC server and port
HOST = "irc.chat.twitch.tv"
PORT = 6667

# Twitch IRC credentials
NICK = os.getenv("BOT_NAME")
PASS = os.getenv("TWITCH_OAUTH_TOKEN")
CHANNEL = os.getenv("TWITCH_CHANNEL")

# Connect to Twitch IRC
sock = socket.socket()
sock.connect((HOST, PORT))
sock.send(f"PASS {PASS}\n".encode())
sock.send(f"NICK {NICK}\n".encode())
sock.send(f"JOIN #{CHANNEL}\n".encode())

# Read chat messages
while True:
    resp = sock.recv(2048).decode()
    if resp.startswith("PING"):
        sock.send("PONG\n".encode())
    elif len(resp) > 0:
        parts = resp.split(":", 2)
        if len(parts) > 2:
            message = parts[2].strip()
            print(f"{parts[1].split('!')[0]}: {message}")
