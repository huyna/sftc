'''
	Part of the authentification class of NightlyAuth Server.

	Leaked by Nightlydev.
'''

def handle(socket,address):
    # A new client is connected.
    print("%s:%s connected. Awaiting data." % address)
    auth_class = Authentification()
    auth_class.set_socket(socket)
    # The client have to send data within 1 second.
    socket.settimeout(1)
    while True:
        line = ""
        max_data = 100
        cur_data = 0
        try:
            # Read until "EOS"
            while line[-3:] != "\x45\x4f\x53":
                data = socket.recv(1024)
                if not data:
                    break
                line += data
                cur_data += 1
                # If the client have sent too much packets, kick it.
                if cur_data >= max_data:
                    kick_notice(socket,"Too much data.")
                    line = ""
                    break
            if line:
                print("[~] Checking token.")
                auth_class.check_token(line)
            line = ""
            break
        except timeout:
            print("[!] Timed out.")
            kick_notice(socket,"Please access this service with the NightlyAUTH Client.")
            break
    print("[~] Connection closed.")
    socket.close()

class Authentification:
    def __init__(self):
        print("[~] Auth class loaded...")
        # Load the token lib.
        self.token_verifier = Token()

    def set_socket(self,socket):
        self.sock = socket

    def check_token(self,token):
        print("[~] Processing token...")
        # Split the data and check the opcode.
        data = re.split(regexsplitter, token)
        if data[0] == "1":
            print("[+] TOKEN_REQUEST !")
            # Check if the user is valid...
            if check_username(data[1]):
                print("[+] Valid UserID :)")
                # Generate a token for the client.
                self.process(data)
            else:
                print("[!] Bad UserID...")
                self.fail()
        elif data[0] == "2":
            print("[+] AUTH_REQUEST !")
            self.process(data)

    def send_token(self,uid,pwd):
        self.sock.sendall(self.token_verifier.generate_token(uid,pwd))

    def process(self,data):
        if data[3] != "EOS": #If it's not an TOKEN Request, decompress the current token token.
            print("[~] Decompressing the token...")
            token = decompress(data[3])
        if data[0] == "1": # If it's a token request, create and sent a new token.
            print("[TOKEN_REQUEST] Generating a valid token...")
            self.send_token(data[1],data[2])
            return True
        # We don't have to check if data[0] == "2" because we are professional coders and check_token already check this.
        if token:
            print("[AUTH_REQUEST] Verifying the token...")
            time.sleep(3) # Sleep for blocking bruteforce attacks.
            if self.token_verifier.verify(token,data[1],data[2]):
                AuthSuccess()
                return True
            else:
		AuthFail()
		return False
