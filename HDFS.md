# HDFS Notes

- Hadoop Distributed File System
- Files once written aren't changed
- Interfaces for moving computation closer to the data
- Master/Slave architecture

## Master/Slave architecture

- Single NameNode (master server) managing file system namespace and access by clients
- Number of DataNodes usually one per node managing storage attached to the node(s)
- Data never flows through NameNode

[<img src="HDFS.png">]()
