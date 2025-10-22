---
id: education.orange-business.data-engineering.nosql.architecture.deployment
title: NoSQL Database Deployment Options
desc: "Migrated from 11-Reading-NoSQL-Database-Deployment-Options.md"
updated: 1761134516000
created: 1761134516000
---

NoSQL Database Deployment Options

Database deployment options refer to the various methods and strategies for implementing and managing databases within an organization. Choosing the right deployment option is crucial for optimizing performance, scalability, and efficiency. Here, you'll explore some common database deployment options and their key characteristics
What you will learn

After completing this reading, you'll be able to

    Identify methods for deploying NoSQL databases
    List examples of NoSQL database deployments
    Describe some of the advantages and challenges associated with deploying NoSQL databases

On-premises deployment

On-premises deployment involves hosting the entire database infrastructure within the organization's physical location or a dedicated data center.
Example of two databases deployed on-premises connected to a single data center brain.
Example

An organization manages customer relationship data using an on-premises Oracle Database installed on dedicated servers within its corporate data center.
Advantages

Full control: Organizations have complete control over hardware specifications, software configurations, and security measures.

Compliance: On-premises solutions might be necessary for industries with stringent regulatory or compliance requirements.
Challenges

Upfront costs: High initial investments in hardware, infrastructure, and skilled personnel.

Scalability: Limited scalability compared to cloud alternatives, which might result in challenges during periods of rapid growth.
Cloud deployment

Cloud deployment involves utilizing cloud service providers to host and manage databases over the internet.
Illustration that communicates built-in data goverence exists with cloud, hybrid cloud, and on-premises deployments.
Example

A startup leverages Amazon Web Services (AWS) to deploy and host its e-commerce database, utilizing Amazon relational database service (RDS) for scalability and managed database services.
Advantages

Scalability: Resources can be scaled up or down based on demand, providing flexibility and cost savings.

Cost-effectiveness: Pay-as-you-go pricing allows organizations to pay only for the resources they consume.

Automation: Cloud providers handle routine maintenance tasks, updates, and backups.
Challenges

Connectivity dependencies: Relies on internet connectivity, which might pose issues in areas with limited or unreliable access.

Security concerns: Requires robust security measures to protect sensitive data from unauthorized access.
Hybrid deployment

Hybrid deployment combines on-premises and cloud solutions, allowing organizations to distribute data and workloads based on specific needs.
Unlocked cloud image connecting to computers, tablets, smartphones and cameras.
Example

A financial institution stores sensitive customer information, such as account balances, in an on-premises database while utilizing a cloud-based service, like AWS Lambda, for processing non-sensitive data analytics workloads.
Advantages

Flexibility: Companies can keep sensitive data on-premises while using the cloud for scalable and dynamic workloads.

Disaster recovery: Companies can use cloud storage for backups, enhancing disaster recovery capabilities.
Challenges

Integration complexity: Integration complexities require effective integration between on-premises and cloud environments for seamless operation.

Management overhead: Monitoring and managing two different environments might increase administrative complexity.
Database as a service (DBaaS)

DBaaS provides a fully managed database solution where the service provider handles administrative tasks, allowing organizations to focus on application development.
Illustration that shows an application communicating through a public network and database as a service (API) with the data.
Example

A software development company uses Microsoft Azure SQL Database as a DBaaS solution to host and manage its relational databases, allowing developers to focus on application development rather than database administration tasks.
Advantages

Reduced overhead: Organizations benefit from reduced administrative tasks, including maintenance, backups, and updates.

Rapid deployment: Quick deployment without the need for in-depth database expertise.
Challenges

Limited control: Organizations have less control over underlying infrastructure, which might be a concern for some organizations.

Data security: Trusting a third-party provider with sensitive data raises security and privacy considerations.
Containerized deployment

Containerization involves packaging the database and its dependencies into containers for consistent deployment across various environments.
Illustration displaying one Docker container running Mongo DB with one Docker volume and two workers, each with one Docker container and one Docker volume.
Example

A tech company adopts Docker containers to deploy its microservices-based application, with each microservice encapsulating a specific function and a separate container running a MongoDB database.
Advantages

Portability: Containers ensure consistent operation across development, testing, and production environments.

Resource efficiency: Lightweight containers consume fewer resources compared to traditional virtual machines.
Challenges

Orchestration complexity: Production-scale deployment requires knowledge of container orchestration tools like Kubernetes.

Learning curve: Teams might need to familiarize themselves with containerization concepts and tools.
Serverless deployment

Serverless architecture provisions and scales database resources automatically based on demand, with organizations paying for actual usage.
An illustration that compares traditional deployment to serverless deployment, with serverless deployment showing the front-end logic separated from the back-end logic, security, and database.
Example

A mobile app developer utilizes Google Cloud Firestore as a serverless NoSQL database for storing user data, where the database scales automatically based on demand, and the developer only pays for the data storage and operations used by the app.
Advantages

No manual provisioning: No need for manual provisioning or maintenance of server resources.

Cost savings: Efficient resource utilization leads to cost savings as organizations only pay for the resources consumed.
Challenges

Limited control: Organizations have less control over underlying infrastructure, which might concern some organizations.

Applicability: Serverless might not be suitable for all types of databases or workloads due to architectural constraints.
Recap

In this reading, you learned that:

    The choice of a database deployment option depends on organizational priorities, budget constraints, scalability needs, and how the company manages the nature of the data. It's essential to carefully evaluate these options in alignment with specific use cases to ensure optimal performance and efficiency.

    On-premises deployment involves hosting the entire database infrastructure within the organization's physical location or a dedicated data center, providing full control and compliance with regulatory requirements but with high upfront costs and limited scalability.

    Cloud deployment uses cloud service providers to host and manage databases. Cloud deployment offers scalability, cost-effectiveness, and automation. However, cloud deployments have connectivity dependencies and can be prone to security concerns.

    Hybrid deployment combines on-premises and cloud solutions, allowing organizations to distribute data and workloads based on specific needs, providing flexibility and enhanced disaster recovery capabilities; however, effective integration between on-premises and cloud environments requires increased administrative complexity and costs.

    Database as a Service (DBaaS) provides a fully managed database solution where the company's choice service provider handles administrative tasks. When using DBaaS, organizations focus on application development but usually have limited control over underlying infrastructure and data security.

    Containerized deployment involves packaging the database and its dependencies into containers for consistent deployment across various environments, which can ensure consistent operations and resource efficiency—however, if containerization practices are not already in place, the company will need time for employees to gain knowledge of container orchestration tools and implement them.

    Serverless deployment provisions and scales database resources automatically based on demand, with organizations paying for actual usage, eliminating manual provisioning and maintenance of server resources, and leading to cost savings. However, companies usually have limited control over the underlying infrastructure, and serverless deployments might not be technically suitable for all databases or workloads.


Congratulations! You have completed this reading and are ready for the next topic. 