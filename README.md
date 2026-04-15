# SDN-Port-Monitoring

SDN Port Status Monitoring using POX and Mininet

---

## Problem Statement
To monitor port status (UP/DOWN) dynamically in a Software Defined Network using a POX controller and Mininet topology.

---

## Objectives
- Monitor switch port status in real-time
- Detect link failures and recovery
- Implement OpenFlow-based control using POX
- Validate network connectivity using Mininet

---

## Setup & Execution

1. Start POX controller:
./pox.py forwarding.l2_learning port_monitor

2. Run Mininet topology:
sudo mn --controller remote,ip=127.0.0.1,port=6633 --topo single,3

3. Test connectivity:
pingall

4. Simulate link failure:
link s1 h1 down

5. Restore link:
link s1 h1 up

6. Exit Mininet:
exit

---

## Expected Output
- Ports show UP/DOWN status in POX logs
- All hosts successfully ping each other
- Link failure causes packet drop
- Network recovers after link restoration

---

## Screenshots

### Port Status Logs
![Port Status Logs](port_status_logs.png)

### Network Test (Ping + Link Failure/Recovery)
![Network Test](network_ping_and_link_test.png)

### Execution Flow
![Execution Flow](network_execution_flow.png)
