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

    # Test OS Command
    os_request = {
                "command_type": "os", 
                "command_name": "ping", 
                "parameters": [
                        "127.0.0.1", 
                        "-n",
                        "6"]
 }
    request = {
                "command_type": "os", 
                "command_name": "ls", 
                "parameters": [
                        "-lt"]
 }
    print("Sending OS Command...")
    response = client.send_request(os_request)
    print(response)
    
    # Optionally, you can add a sleep to allow the server to process
    import time
    time.sleep(1)  # Wait for a moment to allow server to process
