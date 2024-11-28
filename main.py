import threading
from ZeroMQ.server import Server
from ZeroMQ.client import Client

# Function to run the server in a separate thread
def run_server():
    server = Server()
    server.start()

if __name__ == "__main__":
    # Start the server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True  # Make the thread a daemon so it exits when the main program exits
    server_thread.start()

    # Create client and send requests
    client = Client()

    
    import time
    time.sleep(1)  # Wait for a moment to allow server to process

   
    # Sending multiple requests sequentially
    request_1 = {"command_type": "os", "command_name": "ls", "parameters": ["-l"]}
    request_2 = {"command_type": "compute","expression":"print(4)"}
    # request_3 = {"command_type": "os", "command_name": "ping", "parameters": ["127.0.0.1"]}
    
    
    print("Sending OS Command 1...")
    print(client.send_request(request_1))

    print("Sending OS Command 2...")
    print(client.send_request(request_2))

    # print("Sending OS Command 3...")
    # print(client.send_request(request_3))
