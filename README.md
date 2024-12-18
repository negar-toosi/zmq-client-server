# Client-Server Application Using ZeroMQ

## Project Overview
This is a client-server application using ZeroMQ (ZMQ) for communication between the client and server. The server will accept two types of commands: OS commands and Math commands. The client will send these commands in JSON format, and the server will process and return the result.

## Architecture & Design

### Command Execution

The **Factory Pattern** is used for processing the commands that the client sends to the server for the following reasons:

1. **Common Attributes**:
   - All commands share common attributes, such as the need to be executed, the requirement to clear data, and the validation of that data. 
   - By using the Factory Pattern, I ensure that every command adheres to a common interface or structure, which makes the code easier to manage and extend.

2. **Extensibility**:
   - This design pattern provides the flexibility to add new command types easily without modifying the existing codebase.
   - With the Factory Pattern in place, new command classes can be created and integrated by simply defining a new command type. The Factory Pattern will automatically handle the creation of the correct command class based on the provided command type.

3. **Ease of Access**:
   - The Factory Pattern simplifies retrieving the appropriate command class based on the command type. This makes the code cleaner and more organized. By passing the command type, I can easily access the relevant class without manually managing all possible command types.

### Messaging Pattern

I used the **Request-Reply Pattern** for communication between the client and server for the following reason:

- The **Request-Reply Pattern** connects a set of clients to a set of services, enabling **remote procedure calls (RPC)** and **task distribution**. It allows clients to send requests to the server and receive responses. This pattern is ideal for situations where the server processes commands or tasks and responds with the results.

## Installation and Setup

### Install Dependencies

1. **Clone the Repository**:
```bash
git clone https://github.com/username/repository-name.git
cd zmq-server-client
```
2. **Start servers**:
- Start ZeroMQ Server:
```bash
python zmq_server/server.py
```
- Start Django Server in another terminal:
```bash
python manage.py runserver
```
## Usage
you can send a POST request to http://127.0.0.1:8000/api/ endpoint in Postman or Curl
### Example 1: Compute Command
```bash
{
    "command_type": "compute",
    "expression": "2 + 3 * (4 - 1)"
}
```
### Example 2: OS command
```bash
{
    "command_type": "os",
    "command_name": "ls",
    "parameters": ["-l"]
}
```