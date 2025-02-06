# HDFS Notes

## General

- Hadoop Distributed File System
- Files once written aren't changed
- Interfaces for moving computation closer to the data
- Master/Slave architecture

## Master/Slave architecture

- Single NameNode (master server) managing file system namespace and access by clients
- Number of DataNodes usually one per node managing storage attached to the node(s)
- Data never flows through NameNode

[<img src="HDFS.png">]()

## File system namespace

- Similar structure to typical file systems (dirs, files)
- No hard or soft links
- Files can be replicated (replication factor)
- NameNode maintains information on replication of particular files

## Data Replication

- Each file is stored as sequence of blocks of the same size except of the last block
- HDFS has a rack awarness feature and puts 1/3 of data in single node on one rack and 2/3 of data in two nodes in different (one) rack

[<img src="HDFSreplication.png">]()

## File system metadata

- NameNode stores logs of operations in EditLog
- Mapping of blocks to files and file system properties is stored in FsImage file
-

