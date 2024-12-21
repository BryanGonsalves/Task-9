import socket

from playsound import playsound

EMERGENCY_CODES = {
    "Code1": "breaking_doors.wav",
    "Code2": "damaging_cameras.wav",
    "Code3": "burning_car.wav"
}

def play_mp3(code):
    if code in EMERGENCY_CODES:
        print(f"Playing sound for {code}")
        playsound(EMERGENCY_CODES[code])
    else:
        print(f"No MP3 file associated with {code}")


HOST = '0.0.0.0' 
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Server is listening for incoming connections...")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024).decode('utf-8')
            if data:
                print(f"Received code: {data}")
                play_mp3(data)
