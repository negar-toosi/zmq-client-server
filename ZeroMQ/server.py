from command.command_factory import CommandFactory
from command.command import Commands
from command.compute_commands import ComputeCommands
from command.os_commands import OSCommands
import zmq


class Server:
    def __init__(self, host="127.0.0.1", port=5555):
        self.address = f"tcp://{host}:{port}" 

    def start(self):
        context = zmq.Context() # create a container for all the sockets of a single process.
        socket = context.socket(zmq.REP)  # REP socket for reply
        socket.bind(self.address) # bind allows a resource to be sent or received.
        print(f"Server running at {self.address}...")

        while True:
            try:
                # Receive and decode JSON request
                message = socket.recv_json() # deserializes the JSON string into a Python dictionary.
                print(f"Received: {message}")

                # Process the request
                factory = CommandFactory()
                command = factory.get_command(message.get("command_type"))
                response = command.execute(message)

                # Send response
                socket.send_json(response)
            except Exception as e:
                socket.send_json({"error": str(e)})



# import zmq
# import threading
# import subprocess
# import time

# class Server:
#     def __init__(self, host="127.0.0.1", port=5555):
#         self.address = f"tcp://{host}:{port}"

#     def handle_request(self, socket):
#         while True:
#             try:
#                 # Receive JSON request
#                 message = socket.recv_json() # deserializes the JSON string into a Python dictionary.
#                 print(f"Received request: {message}")

#                 # Simulate processing time
#                 time.sleep(2)  # Simulate long task like executing OS commands

#                 # Process the request and create response
#                 factory = CommandFactory()
#                 command = factory.get_command(message.get("command_type"))
#                 response = command.execute(message)

#                 # Send response back to the client
#                 socket.send_json(response)

#             except Exception as e:
#                 socket.send_json({"error": str(e)})

#     def start(self):
#         context = zmq.Context() # create a container for all the sockets of a single process.
#         socket = context.socket(zmq.REP) # REP socket for reply
#         socket.bind(self.address)  # bind allows a resource to be sent or received.
#         print(f"Server running at {self.address}...")

#         while True:
#             # Create a new thread for each incoming client request
#             thread = threading.Thread(target=self.handle_request, args=(socket,))
#             thread.daemon = True  # Daemonize the thread so it exits when the program exits
#             thread.start()

# if __name__ == "__main__":
#     server = Server()
#     server.start()

