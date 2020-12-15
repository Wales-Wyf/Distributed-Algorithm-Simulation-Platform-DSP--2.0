
# Distributed Algorithm Simulation Platform (DSP) 2.0
Distributed Algorithm Simulation Platform (DSP) 2.0 is a virtual software system to simulate the distributed system. It can provide users an environment to design distributed algorithms and verify their feasibility. By the way, users can explore and solve the potential problems in the distributed system.
## Significance

### Verifying algorithms and tasks
DSP is basically consistent with the real distributed system in the aspect of structure, communication and task execution. It provides an environment for users to write distributed algorithms and tasks. The feasibility and efficiency of them can be examined without a real hardware system.

### High fault-tolerance
 As a software system, DSP can provide relatively high fault tolerance. Before the implementation of programs in a hardware system, DSP can better discover the errors and avoid irreparable hardware damage and economic losses.
 
### High Scalability and Reliability
Cloud servers can be utilized to greatly increase the number of nodes simulated by software system to avoid problems caused by scale expansion.

## System Architecture

### Node (Process)
Processes are used to simulate distributed nodes. The topology of the distributed system is defined through a JSON file, which stores nodes ID, nodes' information, neighbors' information, routing table and other information. Each process is mainly divided into three modules: communication, external interaction and task calculation.

### Communication Module (TCP servers)
Each process has 6 sub threads of TCP server which is used to communicate with their neighbors. Each server has its own port and only accept messages from one neighbor. The one-to-one communication mode simulates the actual hardware connection. The thread number limit is according to the fact of the Computing Process Node (CPN) has at most 6 neighbors.

### External Interaction Module (TCP server)
Each process has a sub thread interacting with users. It has functions such as receiving task requests, executing corresponding tasks and returning data.

### Task Calculation Module (Thread)
Users can upload their specific distributed algorithm to DSP through a python file. When one node receives the request to execute the algorithm from the External Interaction Module, it broadcast the task information to nodes in the network and all of them start new threads to run the algorithm.

## Running Environment

### Hardware Environment
Windows / Linux / Mac OS X

### Software Environment
- Python3
- Mysql database
- pysnooperDB (Python Library)
- requests (Python Library)
- PyQt5 (Python Library)

Mysql database and pysnooperDB are needed for the debug mode while requests and PyQt are necessary for Linux / Mac OS X operating system.

## Usage Process

1. **Configure Environment**
Configure the software environment. Open DSP.exe (Windows) or run DSP.py (All operation systems)

2. **Create Topology**
Fill in the number of nodes and import the topology in correct JSON format according to the given topology template. Each node object should have ID, IP, port (port), adjid (the ID of neighbor nodes), adjdirection (the direction of neighbor nodes), datalist (data list for task)

3. **Upload Algorithm**
Upload the correct algorithm (Python file) according to the algorithm template. The available functions are *self.transmitdata (data)*, *self.sendDataToDirection (direction,data)*, *self.syncNode ()*, *self.sendUDP (str)*
- ***self.transmitdata (data)***
*self.transmitData (data)* is the synchronous communication function. *data* can be any data type that can be parsed in JSON format. The data received is a binary array. The first component is the neighbor directions and the second component represents the corresponding datas which one-to-one correspond with the neighbor directions.
- ***self.sendDataToDirection (direction,data)***
*self.sendDataToDirection (direction,data)* is the asynchronous communication function. *direction* is the neighbor direction to send *data*.  Users can use *self.adjData* to get the data information passed by neighbors. The asynchronism and delay of program execution shall be considered while using asynchronous communication function.
- ***self.syncNode()***
*self.syncNode()* can temporarily synchronize the problem while running asynchronous algorithm.
- ***self.sendUDP (str)***
*self.sendUDP (str)* is a debug function which can print out the algorithm operation information in the running state area. The data needs to be string format.

4. **Run Algorithm**
Click the "run" button to start the program, and the operation information will be shown in the running state area.

## Debug Mode
The debug mode is to debug the algorithm from the functional level, not syntax.
1. Complete steps 1-3 in the Usage Process and turn on "debug mode switch"

2. Establish a database for debugging and input database relative information. Click the "display all data tables" button to check whether the input information is correct.

3. Input the variable names needs to be monitored in the algorithm (seperated by English commas, like m, data, adjData). If the variable name is empty, all variable changes will be recorded by default. The program records all changes of the monitored variables.

4. Click the "run" button to start the program. After the running process, input the data table name generated by the program into "data table name" and click "query" button to obtain data table information. The table name can be acquired by clicking "show all data tables" button.
