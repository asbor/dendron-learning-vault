---
id: data-engineering.nosql.architecture.cap-theorem
title: CAP Theorem
desc: "Migrated from 15-CAP-Theorem.md"
updated: 1761134516000
created: 1761134516000
---


## 🎯 Learning Objectives

After completing this lesson, you will be able to:

- 📏 Define the CAP theorem and its three components
- 🔍 Describe the characteristics and trade-offs of CAP theorem
- 📚 Understand the history and relevance of CAP theorem in distributed systems
- 🗂️ Classify NoSQL databases using CAP theorem principles

---

## 📖 Historical Context: The Birth of Distributed Computing

### The Early 2000s: A Paradigm Shift

In the early 2000s, the technology landscape was transforming rapidly:

```mermaid
timeline
    title Evolution of Distributed Systems
    
    2000 : Professor Eric Brewer introduces CAP Theorem
         : Need for globally distributed services emerges
    
    2002 : MIT professors formalize CAP Theorem proof
         : Hadoop architecture development begins
    
    2004-2006 : Big Data challenges become mainstream
              : NoSQL databases start emerging
    
    2007-2010 : Cloud computing adoption accelerates
              : Web-scale applications demand new solutions
```

### The Challenge

**Traditional Relational Databases** faced a critical limitation:
- ✅ **Strong consistency** was their strength
- ❌ **Global distribution** while maintaining consistency seemed impossible
- ❌ **High availability** conflicted with consistency requirements

**The Question**: How can we build systems that are globally distributed, always available, AND consistent?

**The Answer**: CAP Theorem proved this was fundamentally impossible.

---

## 🧮 What is CAP Theorem?

### Definition

**CAP Theorem** (also known as **Brewer's Theorem**) states:

> 💡 **"A distributed system can guarantee delivery of only TWO of these three desired characteristics: Consistency, Availability, and Partition Tolerance."**

### The CAP Triangle

```mermaid
graph TB
    subgraph "CAP Theorem"
        C[Consistency<br/>📊 All nodes see same data]
        A[Availability<br/>🌐 System remains operational]
        P[Partition Tolerance<br/>🔗 Works despite network failures]
    end
    
    subgraph "Possible Combinations"
        CA[CA Systems<br/>🏦 Traditional RDBMS<br/>Single Location]
        CP[CP Systems<br/>🔒 Strong Consistency<br/>MongoDB, HBase]
        AP[AP Systems<br/>📱 High Availability<br/>Cassandra, DynamoDB]
    end
    
    C -.-> CA
    A -.-> CA
    C -.-> CP
    P -.-> CP
    A -.-> AP
    P -.-> AP
    
    style C fill:#e53e3e,color:#ffffff
    style A fill:#51cf66,color:#ffffff
    style P fill:#339af0,color:#ffffff
    style CA fill:#ffd43b
    style CP fill:#ff922b
    style AP fill:#845ef7,color:#ffffff
```

### Key Insight

🚨 **You must sacrifice one of the three properties**. There's no system that can guarantee all three simultaneously in a distributed environment.

---

## 🔍 Understanding the Three Properties

### 1. 📊 **Consistency**

**Definition**: All nodes in a distributed system see the same data at the same time.

```mermaid
sequenceDiagram
    participant Client1 as Client 1
    participant Client2 as Client 2
    participant Node1 as Node 1
    participant Node2 as Node 2
    participant Node3 as Node 3
    
    Client1->>Node1: Write: Balance = $500
    Node1->>Node2: Replicate: Balance = $500
    Node1->>Node3: Replicate: Balance = $500
    
    Note over Node1,Node3: All nodes synchronized
    
    Client2->>Node2: Read: Balance = ?
    Node2-->>Client2: Balance = $500
    
    Client2->>Node3: Read: Balance = ?
    Node3-->>Client2: Balance = $500
    
    Note over Client1,Node3: Strong Consistency:<br/>All reads return same value
```

**Key Questions**:
- Do all nodes see the data they're supposed to see?
- Is the system operating with complete, synchronized information?
- Are all replicas identical at any given moment?

**Real-World Example**: Bank account balance must be identical across all ATMs worldwide.

### 2. 🌐 **Availability**

**Definition**: Every request receives a response (success or failure) without system downtime.

```mermaid
graph TB
    subgraph "High Availability System"
        LB[Load Balancer]
        N1[Node 1<br/>✅ Operational]
        N2[Node 2<br/>❌ Failed]
        N3[Node 3<br/>✅ Operational]
        N4[Node 4<br/>✅ Operational]
    end
    
    subgraph "Client Requests"
        C1[Client 1]
        C2[Client 2]
        C3[Client 3]
    end
    
    C1 --> LB
    C2 --> LB
    C3 --> LB
    
    LB --> N1
    LB --> N3
    LB --> N4
    
    style N1 fill:#51cf66
    style N2 fill:#e03131
    style N3 fill:#51cf66
    style N4 fill:#51cf66
    style LB fill:#339af0,color:#ffffff
```

**Key Questions**:
- Does each request get a response?
- Is the system accessible even during partial failures?
- Can users always interact with the system?

**Real-World Example**: Social media platform stays accessible even if some servers fail.

### 3. 🔗 **Partition Tolerance**

**Definition**: System continues operating despite network failures or communication breakdowns between nodes.

```mermaid
graph TB
    subgraph "Before Network Partition"
        A1[Node A]
        B1[Node B]
        C1[Node C]
        D1[Node D]
        E1[Node E]
        F1[Node F]
        G1[Node G]
        H1[Node H]
    end
    
    A1 --- B1
    B1 --- C1
    C1 --- D1
    D1 --- E1
    E1 --- F1
    F1 --- G1
    G1 --- H1
    H1 --- A1
    
    subgraph "After Network Partition"
        subgraph "Cluster 1"
            A2[Node A]
            B2[Node B]
            C2[Node C]
            D2[Node D]
        end
        
        subgraph "Cluster 2"
            E2[Node E]
            F2[Node F]
            G2[Node G]
            H2[Node H]
        end
    end
    
    A2 --- B2
    B2 --- C2
    C2 --- D2
    D2 --- A2
    
    E2 --- F2
    F2 --- G2
    G2 --- H2
    H2 --- E2
    
    style A1 fill:#51cf66
    style B1 fill:#51cf66
    style C1 fill:#51cf66
    style D1 fill:#51cf66
    style E1 fill:#51cf66
    style F1 fill:#51cf66
    style G1 fill:#51cf66
    style H1 fill:#51cf66
```

**What is a Network Partition?**
- A communication break within a distributed system
- Lost or temporarily delayed connection between nodes
- Can split one cluster into multiple smaller clusters

**Key Point**: 🚨 **In distributed systems, partitions CAN'T be avoided** - they will happen due to:
- Network hardware failures
- Software bugs
- High network latency
- Maintenance operations

---

## ⚖️ CAP Trade-offs in Practice

### Why Partition Tolerance is Mandatory

In real distributed systems, **Partition Tolerance** becomes a requirement, not an option:

```mermaid
graph LR
    subgraph "Distributed System Reality"
        A[Network Failures<br/>WILL Happen]
        B[Geographic Distribution<br/>Required for Global Services]
        C[Hardware Failures<br/>Inevitable at Scale]
    end
    
    subgraph "Consequence"
        D[Partition Tolerance<br/>MANDATORY]
    end
    
    A --> D
    B --> D
    C --> D
    
    subgraph "Choice Remains"
        E[Consistency<br/>vs<br/>Availability]
    end
    
    D --> E
    
    style D fill:#339af0,color:#ffffff
    style E fill:#ffd43b
```

### The Real Choice: CP vs AP

Since **Partition Tolerance** is mandatory in distributed systems, the choice becomes:

| **CP Systems** | **AP Systems** |
|----------------|----------------|
| **Choose**: Consistency + Partition Tolerance | **Choose**: Availability + Partition Tolerance |
| **Sacrifice**: Availability during partitions | **Sacrifice**: Immediate consistency |
| **Behavior**: System may become unavailable to maintain consistency | **Behavior**: System stays available but data may be temporarily inconsistent |
| **Examples**: MongoDB, HBase, Redis Cluster | **Examples**: Cassandra, DynamoDB, Riak |

---

## 🗂️ NoSQL Database Classification

### CP (Consistency + Partition Tolerance) Systems

```mermaid
graph TB
    subgraph "CP Systems: MongoDB Example"
        M[MongoDB Primary]
        S1[Secondary 1]
        S2[Secondary 2]
        
        Client[Client Application]
    end
    
    Client -->|Write Request| M
    M -->|Replicate| S1
    M -->|Replicate| S2
    M -->|Confirm Write| Client
    
    Note1[If network partition occurs:<br/>Only primary accepts writes<br/>Ensures consistency]
    
    style M fill:#e03131,color:#ffffff
    style S1 fill:#fd7e14
    style S2 fill:#fd7e14
    style Note1 fill:#fff3cd
```

**MongoDB Characteristics**:
- ✅ **Strong consistency**: All reads return the most recent write
- ✅ **Partition tolerant**: Continues operating during network issues
- ❌ **Limited availability**: May become read-only during partitions

**Use Cases**: Financial systems, inventory management, any application requiring immediate consistency

### AP (Availability + Partition Tolerance) Systems

```mermaid
graph TB
    subgraph "AP Systems: Cassandra Example"
        C1[Cassandra Node 1]
        C2[Cassandra Node 2]
        C3[Cassandra Node 3]
        C4[Cassandra Node 4]
        
        Client[Client Application]
    end
    
    Client -->|Write Request| C1
    Client -->|Read Request| C2
    
    C1 -.->|Async Replication| C2
    C1 -.->|Async Replication| C3
    C1 -.->|Async Replication| C4
    
    Note2[If network partition occurs:<br/>All nodes accept writes<br/>Ensures availability]
    
    style C1 fill:#51cf66
    style C2 fill:#51cf66
    style C3 fill:#51cf66
    style C4 fill:#51cf66
    style Note2 fill:#e7f5ff
```

**Cassandra Characteristics**:
- ✅ **High availability**: Always accepts reads and writes
- ✅ **Partition tolerant**: Each node operates independently
- ❌ **Eventual consistency**: Data may be temporarily inconsistent

**Use Cases**: Social media, content delivery, IoT data collection, analytics

---

## 🎯 Real-World Examples

### Financial Institution: CP Choice

```mermaid
sequenceDiagram
    participant ATM1 as ATM New York
    participant Bank as Banking System
    participant ATM2 as ATM London
    
    ATM1->>Bank: Withdraw $100
    Bank->>Bank: Check Balance: $500
    Bank->>Bank: Update Balance: $400
    Bank->>ATM2: Sync Balance: $400
    ATM2-->>Bank: Confirm Sync
    Bank-->>ATM1: Approve Withdrawal
    
    Note over ATM1,ATM2: Strong Consistency Maintained<br/>Even if slower or less available
```

**Why CP for Banking**:
- Account balance must be accurate everywhere
- Better to have ATM temporarily unavailable than show wrong balance
- Regulatory compliance requires consistency

### Social Media Platform: AP Choice

```mermaid
sequenceDiagram
    participant User1 as User (US)
    participant Server1 as US Server
    participant Server2 as EU Server
    participant User2 as User (EU)
    
    User1->>Server1: Post "Hello World!"
    Server1-->>User1: Post Confirmed
    
    Note over Server1: Post visible to US users immediately
    
    Server1->>Server2: Replicate Post (async)
    
    User2->>Server2: View Feed
    Server2-->>User2: Feed (without new post yet)
    
    Note over Server2: EU user sees post after brief delay
    
    Server2->>Server2: Post arrives
    User2->>Server2: Refresh Feed
    Server2-->>User2: Feed (with new post)
```

**Why AP for Social Media**:
- Users expect platform to always work
- Brief delays in seeing posts are acceptable
- Global scale requires high availability

---

## 📊 CAP in Modern Database Landscape

### Database Comparison

| **Database** | **CAP Type** | **Primary Choice** | **Secondary Feature** | **Use Cases** |
|--------------|--------------|-------------------|---------------------|---------------|
| **PostgreSQL** | CA | Consistency + Availability | Limited partition tolerance | Single-region OLTP |
| **MongoDB** | CP | Consistency + Partition Tolerance | Configurable availability | Financial, inventory |
| **Cassandra** | AP | Availability + Partition Tolerance | Tunable consistency | IoT, social media |
| **Redis** | CP/CA | Depends on configuration | Flexible deployment | Caching, sessions |
| **DynamoDB** | AP | Availability + Partition Tolerance | Eventually consistent | Web applications |
| **HBase** | CP | Consistency + Partition Tolerance | Strong consistency | Big data analytics |

### Tunable Consistency

Many modern databases offer **tunable consistency**:

```mermaid
graph TB
    subgraph "Cassandra Consistency Levels"
        ONE[ONE<br/>Fastest, Least Consistent]
        QUORUM[QUORUM<br/>Balanced Performance/Consistency]
        ALL[ALL<br/>Slowest, Most Consistent]
    end
    
    subgraph "MongoDB Read Preferences"
        PRIMARY[PRIMARY<br/>Strongest Consistency]
        SECONDARY[SECONDARY<br/>Higher Performance]
        NEAREST[NEAREST<br/>Lowest Latency]
    end
    
    style ONE fill:#e03131,color:#ffffff
    style QUORUM fill:#fd7e14,color:#ffffff
    style ALL fill:#51cf66,color:#ffffff
    style PRIMARY fill:#51cf66,color:#ffffff
    style SECONDARY fill:#fd7e14,color:#ffffff
    style NEAREST fill:#339af0,color:#ffffff
```

**Key Insight**: You can adjust the consistency/availability trade-off based on specific operations!

---

## 🎓 Advanced Concepts

### PACELC Theorem

An extension of CAP that considers latency:

> **"In case of network Partitioning (P), one has to choose between Availability (A) and Consistency (C), but Else (E), even when the system is running normally in the absence of partitions, one has to choose between Latency (L) and Consistency (C)."**

```mermaid
graph TB
    subgraph "PACELC Extension"
        P1[During Partition<br/>PA or PC?]
        E1[Normal Operation<br/>EL or EC?]
    end
    
    subgraph "Examples"
        PAEC[PA/EC: Cassandra<br/>Available during partition<br/>Consistent when stable]
        PCEC[PC/EC: MongoDB<br/>Consistent during partition<br/>Consistent when stable]
        PAELC[PA/EL: DynamoDB<br/>Available + Low Latency<br/>Eventual consistency]
    end
    
    P1 --> PAEC
    P1 --> PCEC
    E1 --> PAELC
    
    style P1 fill:#e03131,color:#ffffff
    style E1 fill:#51cf66,color:#ffffff
```

### Evolution Beyond CAP

Modern distributed systems use sophisticated techniques:

1. **Consensus Algorithms** (Raft, PBFT)
2. **Multi-Model Databases** (ArangoDB, CosmosDB)
3. **NewSQL** (CockroachDB, TiDB) - trying to achieve all three
4. **Microservices** - different services with different CAP choices

---

## 🚀 Practical Implications

### When to Choose Each Type

#### Choose CP (Consistency + Partition Tolerance)
```
✅ Financial transactions
✅ Inventory management  
✅ Healthcare records
✅ Legal documents
✅ Audit logs

❌ Global social platforms
❌ Real-time gaming
❌ IoT sensor data
❌ Content delivery
```

#### Choose AP (Availability + Partition Tolerance)
```
✅ Social media feeds
✅ Product catalogs
✅ User preferences
✅ Analytics data
✅ Content delivery

❌ Payment processing
❌ Account balances
❌ Critical system state
❌ Compliance data
```

### Migration Considerations

When moving from traditional RDBMS to NoSQL:

```mermaid
flowchart TD
    A[Current RDBMS System] --> B{Analyze Requirements}
    B --> C{Need Global Scale?}
    B --> D{Consistency Critical?}
    
    C -->|Yes| E{Can Accept Eventual Consistency?}
    D -->|Yes| F[Consider CP System<br/>MongoDB, HBase]
    
    E -->|Yes| G[Consider AP System<br/>Cassandra, DynamoDB]
    E -->|No| F
    
    C -->|No| H[May Stay with RDBMS<br/>or Consider Hybrid]
    D -->|No| I[More Flexibility<br/>Consider AP Systems]
    
    style F fill:#fd7e14,color:#ffffff
    style G fill:#845ef7,color:#ffffff
    style H fill:#51cf66,color:#ffffff
    style I fill:#339af0,color:#ffffff
```

---

## 📋 Key Takeaways

### ✅ **What You Should Remember**

1. **CAP Theorem** = You can only guarantee 2 out of 3: Consistency, Availability, Partition Tolerance
2. **Partition Tolerance** is mandatory in distributed systems
3. **Real choice** is between Consistency (CP) and Availability (AP)
4. **MongoDB** = CP (consistency first, availability tunable)
5. **Cassandra** = AP (availability first, consistency tunable)
6. **Choice depends on use case**, not technical preference

### 🎯 **The Decision Framework**

```mermaid
graph LR
    A[Business Requirements] --> B{What Matters Most?}
    B -->|Data Accuracy| C[Choose CP<br/>MongoDB, HBase]
    B -->|System Uptime| D[Choose AP<br/>Cassandra, DynamoDB]
    B -->|Both Critical| E[Consider Hybrid<br/>or NewSQL]
    
    style B fill:#ffd43b
    style C fill:#fd7e14,color:#ffffff
    style D fill:#845ef7,color:#ffffff
    style E fill:#51cf66,color:#ffffff
```

### 🚨 **Common Misconceptions**

❌ **Wrong**: "NoSQL is always better than RDBMS"  
✅ **Right**: "Choose the right tool for the job"

❌ **Wrong**: "You can have all three CAP properties"  
✅ **Right**: "You must make trade-offs"

❌ **Wrong**: "CP systems are never available"  
✅ **Right**: "CP systems prioritize consistency, availability is tunable"

---

## 🔗 Related Topics

- **[[12-ACID versus BASE Operations]]** - How consistency models relate to CAP
- **[[13-Distributed-Databases]]** - Implementation of CAP principles
- **[[05-characteristics-of-NoSQL-databases]]** - NoSQL design principles
- **[[09-column-based-NoSQL-Databases]]** - Cassandra as AP example
- **[[16-Challenges in Migrating from RDBMS to NoSQL Databases]]** - Migration considerations

---

## 📝 Study Questions

1. Explain why you cannot have all three CAP properties simultaneously.
2. Why is Partition Tolerance considered mandatory in distributed systems?
3. Compare MongoDB and Cassandra in terms of CAP choices.
4. When would you choose a CP system over an AP system?
5. How does the PACELC theorem extend CAP theory?
6. What factors should drive your CAP decision in system design?

---

*Next: Learn about the practical challenges of migrating from RDBMS to NoSQL systems.*