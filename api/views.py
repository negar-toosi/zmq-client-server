from rest_framework.views import APIView
from rest_framework.response import Response
import zmq

class CommandAPIView(APIView):
    def post(self, request, *args, **kwargs):
        payload = request.data

       #connect to ZMQ server
        try:
            context = zmq.Context()
            socket = context.socket(zmq.REQ)  # REQ socket for Request
            socket.connect("tcp://127.0.0.1:5555")  # آدرس سرور ZMQ

            # send request to ZMQ server
            socket.send_json(payload)

            # receive response from ZMQ server
            response = socket.recv_json()
            return Response(response)
        except Exception as e:
            return Response({"success": False, "error": str(e)})
        finally:
            socket.close()
            context.term()
