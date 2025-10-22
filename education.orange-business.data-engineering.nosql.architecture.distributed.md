---
id: education.orange-business.data-engineering.nosql.architecture.distributed
title: Distributed Databases
desc: "Migrated from 13-Distributed-Databases.md"
updated: 1761134516000
created: 1761134516000
---


## 🎯 Learning Objectives

After completing this lesson, you will be able to:

- 📊 Describe the concepts of distributed databases
- 🔄 Define fragmentation and replication of data
- ⚖️ Describe the advantages and challenges of distributed systems
- 🏗️ Understand distributed database architecture patterns

---

## 📖 What are Distributed Databases?

A **distributed database** is a collection of multiple interconnected databases that are spread physically across various locations and communicate via a computer network.

### Key Characteristics

```mermaid
graph TB
    subgraph "Distributed Database System"
        A[Central Coordinator]
        B[Site 1<br/>Database Fragment]
        C[Site 2<br/>Database Fragment]
        D[Site 3<br/>Database Fragment]
        E[Site 4<br/>Database Fragment]
    end
    
    F[Client Applications]
    
    F --> A
    A --> B
    A --> C
    A --> D
    A --> E
    
    B -.->|Replication| C
    C -.->|Replication| D
    D -.->|Replication| E
    
    style A fill:#e1f5fe
    style B fill:#e8f5e8
    style C fill:#e8f5e8
    style D fill:#e8f5e8
    style E fill:#e8f5e8
    style F fill:#fff3e0
```

> 💡 **Key Point**: A distributed database is physically distributed across data sites by **fragmenting** and **replicating** the data, following the BASE consistency model.

---

## 🔧 Data Fragmentation (Partitioning/Sharding)

To store large amounts of data across all servers in a distributed system, you need to break your data into smaller pieces. This process has several names:

- **Fragmentation** (distributed databases)
- **Partitioning** (general distributed systems)
- **Sharding** (NoSQL databases)

### Fragmentation Strategies

#### 1. **Lexical Grouping (Range-Based)**
```
Keys A-C → Server 1
Keys D-F → Server 2
Keys G-I → Server 3
```

#### 2. **Key-Based Grouping (Hash-Based)**
```
Store ID 1-100 → Server 1
Store ID 101-200 → Server 2
Store ID 201-300 → Server 3
```

### Practical Example

```mermaid
graph LR
    subgraph "Original Large Dataset"
        A[All Customer Data<br/>Millions of Records]
    end
    
    subgraph "Fragmented Data"
        B[Customers A-H<br/>Server 1]
        C[Customers I-P<br/>Server 2]
        D[Customers Q-Z<br/>Server 3]
    end
    
    A --> B
    A --> C
    A --> D
    
    style A fill:#ffcdd2
    style B fill:#c8e6c9
    style C fill:#c8e6c9
    style D fill:#c8e6c9
```

**Benefits:**
- ✅ Query: "Give me all sales from Store ID 15" → All records on single server
- ✅ Faster query processing
- ✅ Reduced network traffic

---

## 🔄 Data Replication

After data is distributed across cluster nodes, **replication** ensures data availability when nodes fail.

### What is Replication?

**Replication** means all fragments/partitions/shards of your data are stored redundantly in two or more sites.

```mermaid
graph TB
    subgraph "Primary Sites"
        P1[Primary Node 1<br/>Fragment A]
        P2[Primary Node 2<br/>Fragment B]
        P3[Primary Node 3<br/>Fragment C]
    end
    
    subgraph "Replica Sites"
        R1[Replica Node 1<br/>Fragment A Copy]
        R2[Replica Node 2<br/>Fragment B Copy]
        R3[Replica Node 3<br/>Fragment C Copy]
    end
    
    P1 -.->|Replicate| R1
    P2 -.->|Replicate| R2
    P3 -.->|Replicate| R3
    
    style P1 fill:#4caf50,color:#ffffff
    style P2 fill:#4caf50,color:#ffffff
    style P3 fill:#4caf50,color:#ffffff
    style R1 fill:#81c784
    style R2 fill:#81c784
    style R3 fill:#81c784
```

### Replication Benefits & Challenges

| ✅ **Advantages** | ❌ **Disadvantages** |
|------------------|---------------------|
| Increased data availability | Data synchronization complexity |
| Fault tolerance | Storage overhead |
| Load distribution | Consistency challenges |
| Reduced latency | Network overhead |

> ⚠️ **Challenge**: Any change at one site must be replicated to every site storing related data, or inconsistency occurs.

---

## 🚀 Advantages of Distributed Systems

### 1. **Reliability and Availability**
- Data replicated at multiple sites
- If local server unavailable, data retrieved from another server
- No single point of failure

### 2. **Improved Performance**
- Reduced query processing time for high data volumes
- Parallel processing capabilities
- Local data access reduces latency

### 3. **Scalability**
- Easy horizontal scaling by adding new servers
- Elastic capacity adjustment
- Cost-effective growth

### 4. **Continuous Operation**
- No reliance on central site
- Independent node operation
- High availability architecture

```mermaid
graph TB
    subgraph "Distributed Database Benefits"
        A[Reliability<br/>& Availability]
        B[Improved<br/>Performance]
        C[Scalability]
        D[Continuous<br/>Operation]
    end
    
    subgraph "Real-World Applications"
        E[Global Banking Systems]
        F[Social Media Platforms]
        G[E-commerce Websites]
        H[Streaming Services]
    end
    
    A --> E
    B --> F
    C --> G
    D --> H
    
    style A fill:#e8f5e8
    style B fill:#fff3e0
    style C fill:#e1f5fe
    style D fill:#fce4ec
```

---

## ⚖️ Challenges of Distributed Systems

### 1. **Concurrency Control**

**The Problem**: Same data stored in multiple locations - how to handle concurrent modifications?

**Solutions**:

#### Approach A: Single-Node Operations
```mermaid
sequenceDiagram
    participant Client
    participant Master Node
    participant Replica 1
    participant Replica 2
    
    Client->>Master Node: Write Request
    Master Node->>Master Node: Process Write
    Master Node->>Replica 1: Sync Data
    Master Node->>Replica 2: Sync Data
    Master Node-->>Client: Confirm Write
```

#### Approach B: Multi-Node Operations
```mermaid
sequenceDiagram
    participant Client
    participant Node 1
    participant Node 2
    participant Node 3
    
    Client->>Node 1: Write Request
    Client->>Node 2: Write Request
    Client->>Node 3: Write Request
    Node 1-->>Client: ACK
    Node 2-->>Client: ACK
    Node 3-->>Client: ACK
    Note over Client: Success when N nodes confirm
```

### 2. **Limited Transaction Support**

- Distributed databases provide limited ACID transaction support
- Focus on BASE model (Basically Available, Soft state, Eventually consistent)
- Trade-off: Consistency vs. Availability

### 3. **Data Synchronization**

| **Challenge** | **Impact** | **Solution** |
|---------------|------------|--------------|
| Network latency | Delayed updates | Optimized protocols |
| Partial failures | Inconsistent state | Consensus algorithms |
| Concurrent updates | Data conflicts | Conflict resolution strategies |

---

## 🏗️ BASE Consistency Model

Distributed databases follow the **BASE** model:

```mermaid
graph LR
    subgraph "BASE Model"
        A[Basically<br/>Available]
        B[Soft<br/>State]
        C[Eventually<br/>Consistent]
    end
    
    subgraph "Characteristics"
        D[Always accessible<br/>even during failures]
        E[Data may change<br/>over time]
        F[Consistency achieved<br/>eventually, not immediately]
    end
    
    A --> D
    B --> E
    C --> F
    
    style A fill:#4caf50,color:#ffffff
    style B fill:#ff9800,color:#ffffff
    style C fill:#2196f3,color:#ffffff
```

---

## 🎯 Real-World Applications

### Modern Services Using Distributed Databases

| **Service** | **Use Case** | **Database Type** |
|-------------|--------------|------------------|
| **Netflix** | Content delivery, user preferences | Cassandra, DynamoDB |
| **Facebook** | Social graph, messaging | Cassandra, MySQL clusters |
| **Amazon** | Product catalog, shopping cart | DynamoDB, Aurora |
| **Google** | Search index, user data | Bigtable, Spanner |
| **Uber** | Real-time location, trip data | Cassandra, MySQL |

---

## 📋 Key Takeaways

### ✅ **What You Should Remember**

1. **Distributed databases** = Multiple interconnected databases across locations
2. **Fragmentation** = Breaking large data into smaller, manageable pieces
3. **Replication** = Storing data copies redundantly for availability
4. **BASE model** = Eventually consistent, always available
5. **Trade-offs** = Availability vs. immediate consistency

### 🔄 **The Distribution Process**
```
Large Dataset → Fragmentation → Distribution → Replication → BASE Consistency
```

### 🚀 **Why Use Distributed Databases?**
- Handle massive data volumes
- Serve global user bases
- Provide high availability
- Scale horizontally
- Reduce latency

---

## 🔗 Related Topics

- **[[12-ACID versus BASE Operations]]** - Understanding consistency models
- **[[05-characteristics-of-NoSQL-databases]]** - NoSQL principles
- **[[09-column-based-NoSQL-Databases]]** - Cassandra as distributed example
- **[[11-Reading-NoSQL-Database-Deployment-Options]]** - Deployment strategies

---

## 📝 Study Questions

1. What are the two main fragmentation strategies?
2. How does replication improve system reliability?
3. What are the main challenges of distributed systems?
4. Why do distributed databases follow BASE instead of ACID?
5. Give examples of when you'd choose distributed over centralized databases.

---

*Next: Continue with advanced NoSQL topics and hands-on implementation examples.*