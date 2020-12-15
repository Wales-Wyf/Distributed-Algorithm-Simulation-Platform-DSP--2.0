
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
