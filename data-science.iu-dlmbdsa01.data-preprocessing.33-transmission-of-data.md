# 3.3 Transmission of Data

In organizations, data often originates from various departments and needs to be transmitted to create a comprehensive business-related dataset. For instance, in an industrial organization, machines operate based on predefined schedules and employee workloads, with sensors attached to these machines to measure critical parameters like idle and processing times. To leverage data science in this organization, all data variables from the machines must be consolidated into a single dataset. These variables come from various sources, including sensors attached to the machines (for measuring parameters), documents from the HR department (for workload information), and input from the production manager (for operational details).

Transmission of the required data can be done in two main ways:

1. **Manual Transmission**: This is the simplest method, involving the manual insertion of variables into the dataset. While straightforward, it can be time-consuming.
2. **Electronic Transmission**: For digital data represented in bits (computer memory units), electronic transmission is preferred. This is typically accomplished using local and/or wireless area networks. Electronic transmission can be further categorized into two methods:
   * **Serial Transmission**: In this method, digital data is sent bit by bit over a single channel. It is suitable for various transmission distances and is cost-effective.
   * **Parallel Transmission**: Parallel transmission employs multiple channels to simultaneously deliver multiple data bits. This approach offers faster transmission but can be more expensive and is typically used for shorter distances.

Both manual and electronic transmission methods serve the purpose of consolidating data from various sources, allowing organizations to harness the power of data science for informed decision-making and analysis.

![](<../../.gitbook/assets/image (1) (1) (1) (1).png>)

When it comes to data transmission, there are two main methods: asynchronous and synchronous. Each has its own characteristics and use cases:

**Asynchronous Transmission:**

* In asynchronous transmission, the bit stream is divided into segments with start and stop bits.
* There is a variable period between these transmissions.
* The start bit signals the receiver to expect the transmitted stream, while the stop bit marks the end of the transmission.
* Asynchronous transmission is cost-effective but relatively slow. It incurs additional overhead due to the start and stop bits.

**Synchronous Transmission:**

* Synchronous transmission, on the other hand, combines the bit stream into longer frames.
* There is a constant period between these transmissions.
* Any gaps among the streams are filled with idle bits (either 0 or 1).
* Synchronous transmission is faster and doesn't have the additional overhead of start and stop bits.

The data transmission rate is typically expressed in terms of the number of bits transmitted per second (bps). The choice between asynchronous and synchronous transmission depends on factors like transmission speed, reliability, and cost, and it's made based on the specific requirements of the data transmission task.
\n\n---\n\n## Navigation\n\n- **Parent**: [[data-science.iu-dlmbdsa01.data-preprocessing]]\n- **Course**: [[data-science.iu-dlmbdsa01]]\n