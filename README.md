# basic-python-shell
First in server.py and client.py we are creating a basic shell using subprocess module

Then we use threads to allow more connections.

1. Create Worker thread
- Use for loop
- Creating threads using t= threading.Thread()
- Assign t.daemon = True
- Start the thread with t.start()

2. Store the jobs in a queue because threades looking for jobs in queues and not in lists

3. Create a work function and get the Queue
- if the job id  is 1 then handle the connections
- if the job id  is 2 then send commands to the client
