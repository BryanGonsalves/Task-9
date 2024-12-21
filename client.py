import socket

from playsound import playsound

EMERGENCY_CODES = {
    "Code1": "breaking_doors.wav",
    "Code2": "damaging_cameras.wav",
    "Code3": "burning_car.wav"
}

def send_code(code, server_ip, server_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((server_ip, server_port))
            client_socket.sendall(code.encode('utf-8'))
            print(f"Sent code: {code}")
    except Exception as e:
        print(f"Error sending code: {e}")

def play_mp3(code):
    if code in EMERGENCY_CODES:
        print(f"Playing sound for {code}")
        playsound(EMERGENCY_CODES[code])
    else:
        print(f"No MP3 file associated with {code}")

# Client usage
SERVER_IP = "192.168.0.185"  # please place ur server ip, ie computer 1 ip
SERVER_PORT = 12345

while True:
    print("\nAvailable Codes: Code1, Code2, Code3")
    action = input("Type 'send' to send a code or 'play' to play a local file: ").strip().lower()
    if action == "send":
        code = input("Enter the code to send: ").strip()
        send_code(code, SERVER_IP, SERVER_PORT)
    elif action == "play":
        code = input("Enter the code to play locally: ").strip()
        play_mp3(code)
    else:
        print("Invalid action. Type 'send' or 'play'.")
