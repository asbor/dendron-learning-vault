# 5.4 Cluster Analysis

Cluster analysis is an <mark style="color:orange;">**unsupervised learning method**</mark> used to group input data into meaningful clusters without predefined labels. Each cluster consists of data records that exhibit a certain degree of similarity within the cluster, while being dissimilar to records in other clusters, as defined by the dataset. The number of clusters formed depends on context and perspective. Various clustering techniques exist, including K-means, expectation maximization, agglomerative, density-based spatial, and affinity propagation. For our discussion, we will focus on K-means clustering and agglomerative clustering.

## 5.4.1 K-Means Clustering

K-means clustering is an algorithm that categorizes N data records into K clusters. The algorithm follows these steps (Runkler, 2012):

1. Determine the desired number of clusters, K.
2. Randomly select data records to represent the centroids of these clusters.
3.  Compute the distances between each data record and the designated centroids. Assign each data record to the cluster whose centroid is closest (i.e., the centroid with the minimum distance). The Euclidean distance, denoted as d(i,C), is used for distance measurement in K-means clustering, as expressed by the equation:

    $$d_{i,c} = \sqrt{(x_{i1} - x_{c1})^2 + (x_{i2} - x_{c2})^2 + \cdots + (x_{iM} - x_{cM})^2}$$

    where (x1, x2, …, xM) represent the M data variables, i denotes the ith data record, and c denotes the centroid of the cluster.
4. Recalculate the new centroids for each cluster by averaging the data records within each cluster.
5. Repeat steps (3) and (4) until no further changes occur in the computed centroids.
6. The final clusters contain the data records grouped within them.

![K-Means Clustering Example](assets/images/data-science/iu-dlmbdsa01/k-means-clustering-example.png)

1. It is assumed that there are three clusters (i.e., K = 3): C1,C2 and C3.
2. The centroids for these clusters are selected to be the first (1, 1), third (3, 4), and fourth (5, 7) data records.

![K-Means Clustering Assignment](assets/images/data-science/iu-dlmbdsa01/K-Means-Clustering-Assignment.png)

The distances between each data record and the defined centroids are:

$$d_{2,C_1} = \sqrt{(1.5-1)^2 + (2-1)^2}$$

$$d_{2,C_2} = \sqrt{(1.5-3)^2 + (2-4)^2}$$

$$d_{2,C_3} = \sqrt{(1.5-5)^2 + (2-7)^2}$$

* **Record #2:** is assigned to $$C_1$$ because it has the minimum distance to the centroid of $$C_1$$. In the same manner, the other data records are assigned to their closest clusters as follows: record #4, #5 and #6 are assigned is assigned to $$C_2$$.

![K-Means Second Cluster Assignment](assets/images/data-science/iu-dlmbdsa01/K-Means-Second-Cluster-Assignment.png)

3.  Recalculate the new centroid for each cluster by averaging its included data records.

    * For **C1**, the centroid is:

    $$(\frac{1}{2} \cdot (1+1.5, 1+2)) = \frac{1}{2} \cdot (2.5, 3) = (1.25, 1.5)$$

    * For **C2**, the centroid is:

    $$(\frac{1}{4} \cdot (3+3.5+3.5+4.5, 4+4.5+5+5)) = (3.625, 4.625)$$

    * For **C3**, the centroid remains as it is at (5, 7)

![K-Means Newly Calculated Centroids](assets/images/data-science/iu-dlmbdsa01/K-Means-Newly-Calculated-Centroids.png)

4. Calculate the new distances between each data record and cluster centroids and assign data records to clusters according to their minimum distances.

**New Distances Between Data Records and Cluster Centroids:**

| # | Distance to $$C_1$$ | Distance to $$C_2$$ | Distance to $$C_3$$ |
| - | ------------------- | ------------------- | ------------------- |
| 1 | 0.559017            | 4.475628            | 7.211103            |
| 2 | 0.559017            | 3.377314            | 6.103278            |
| 3 | 3.051639            | 0.883883            | 3.605551            |
| 4 | 6.656763            | 2.744312            | 0                   |
| 5 | 4.160829            | 0.395285            | 2.5                 |
| 6 | 4.776243            | 0.951972            | 2.061553            |
| 7 | 3.75                | 0.176777            | 2.915476            |

Since there are no changes in the assignments of the data records to the clusters, the centroids remain at their previous values, and there is no need to proceed with more iterations. Therefore, the final cluster contents are:&#x20;

* **C1**: {#1, and #2},&#x20;
* **C2**: {#3, #5, #6, and #7}, and&#x20;
* **C3**: {#4}.

## 5.4.2 Hierarchical Clustering

Hierarchical clustering is applied to data that has an underlying hierarchy. For example, consider the following items in a supermarket: apples and pears are fruit; tomatoes and cucumbers are vegetables; and both are fresh produce.

There are two approaches to hierarchical clustering: divisive (top-down) and agglomerative (bottom-up).

## 5.4.3 Agglomerative Clustering

Agglomerative clustering creates a bottom-up tree (dendrogram) of clusters that repeatedly merge two nearest points or clusters into a bigger super cluster. The “leaves” of the tree are the individual data records, and the “root” is the universe of these records. The agglomerative clustering algorithm is formulated as follows: Assign each record of the given N data records to a unique cluster, forming N clusters.

Merge the data records (i.e., clusters) with minimum Euclidean distance between them into a single cluster.

Repeat this process until there is only one cluster remaining, forming a hierarchy of clusters.

### 5.4.3.1 Example: Agglomerative Clustering

Apply agglomerative clustering to the following dataset containing two variables and six data records.

![Agglomerative Clustering Example](assets/images/data-science/iu-dlmbdsa01/Agglomerative-Clustering-Example.png)

Each data record is assigned to a cluster, resulting in six clusters (leaves of the tree). The Euclidean distances between these data records form a symmetric matrix (also known as a proximity matrix).

**Proximity Matrix:**

| # | 1    | 2    | 3    | 4    | 5    | 6    |
| - | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | 0.00 |      |      |      |      |      |
| 2 | 0.23 | 0.00 |      |      |      |      |
| 3 | 0.22 | 0.15 | 0.00 |      |      |      |
| 4 | 0.37 | 0.19 | 0.16 | 0.00 |      |      |
| 5 | 0.34 | 0.14 | 0.28 | 0.28 | 0.00 |      |
| 6 | 0.24 | 0.24 | 0.10 | 0.22 | 0.39 | 0.00 |

Here, the minimum distance is between data records #3 and #6, so they are merged into a single cluster C1. The next minimum distance is between data records #2 and #5, so they are merged into another single cluster, C2.

![Agglomerative First Cluster Assignment](assets/images/data-science/iu-dlmbdsa01/Agglomerative-First-Cluster-Assignment-1.png)

The third minimum distance is found between data records #2 (an element of C2) and #3 (an element of C1); therefore, these two clusters are merged into a single cluster, C3.

![Agglomerative First Cluster Assignment](assets/images/data-science/iu-dlmbdsa01/Agglomerative-First-Cluster-Assignment-2.png)

The fourth minimum distance is found between data records #4 and #3 (an element of C3); therefore, single cluster C4 is formed to include data record #4 and cluster C3.

![Agglomerative First Cluster Assignment](assets/images/data-science/iu-dlmbdsa01/Agglomerative-First-Cluster-Assignment-3.png)

Finally, the super cluster C5 is formed to include data record #1.

![Agglomerative First Cluster Assignment](assets/images/data-science/iu-dlmbdsa01/Agglomerative-First-Cluster-Assignment-4.png)

The dendrogram is shaped as:

![Dendrogram](assets/images/data-science/iu-dlmbdsa01/Dendrogram.png)

A well-designed, standalone tool for clustering analysis can be accessed through the sklearn website.



{% content-ref url="codes/03-cluster-analysis/3.2-k-means-clustering.md" %}
[3.2-k-means-clustering.md](codes/03-cluster-analysis/3.2-k-means-clustering.md)
{% endcontent-ref %}

{% content-ref url="codes/03-cluster-analysis/3.1-k-means-clustering-elbow-method.md" %}
[3.1-k-means-clustering-elbow-method.md](codes/03-cluster-analysis/3.1-k-means-clustering-elbow-method.md)
{% endcontent-ref %}

{% content-ref url="codes/03-cluster-analysis/interactive-cluster-analysis.md" %}
[interactive-cluster-analysis.md](codes/03-cluster-analysis/interactive-cluster-analysis.md)
{% endcontent-ref %}
\n\n---\n\n## Navigation\n\n- **Parent**: [[data-science.iu-dlmbdsa01.mathematical-techniques]]\n- **Course**: [[data-science.iu-dlmbdsa01]]\n