import zmq
import json


class Client:
    def __init__(self, host="localhost", port=5555):
        self.address = f"tcp://{host}:{port}"

    def send_request(self, request):
        context = zmq.Context() # create a container for all the sockets of a single process.
        socket = context.socket(zmq.REQ)  # REQ socket for request
        try:
            # Connect to the server
            socket.connect(self.address)

            # Send JSON request
            socket.send_json(request)

            # Receive JSON response
            response = socket.recv_json()
            return response
        except Exception as e:
            return {"error": str(e)}
        finally:
            socket.close()
            context.term()

