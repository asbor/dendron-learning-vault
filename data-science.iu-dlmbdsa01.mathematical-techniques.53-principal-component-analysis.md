# 5.3 Principal Component Analysis (PCA)

{% embed url="https://www.youtube.com/watch?v=HMOI_lkzW08" %}
PCA main ideas in only 5 minuts !!!
{% endembed %}

* [0:00](https://www.youtube.com/watch?v=HMOI\_lkzW08\&t=0s) Awesome song and introduction
* [0:27](https://www.youtube.com/watch?v=HMOI\_lkzW08\&t=27s) Motivation for using PCA&#x20;
* [1:23](https://www.youtube.com/watch?v=HMOI\_lkzW08\&t=83s) Correlations among samples&#x20;
* [3:36](https://www.youtube.com/watch?v=HMOI\_lkzW08\&t=216s) PCA converts correlations into a 2-D graph&#x20;
* [4:26](https://www.youtube.com/watch?v=HMOI\_lkzW08\&t=266s) Interpreting PCA plots&#x20;
* [5:08](https://www.youtube.com/watch?v=HMOI\_lkzW08\&t=308s) Other options for dimension reduction

{% embed url="https://www.youtube.com/watch?t=882s&v=_UVHneBUBW0" %}
Principial Component Analasys (PCA) Clearly Explained
{% endembed %}

* [0:00](https://www.youtube.com/watch?v=\_UVHneBUBW0\&t=0s) Awesome song and introduction&#x20;
* [1:45](https://www.youtube.com/watch?v=\_UVHneBUBW0\&t=105s) An introduction to dimensions&#x20;
* [6:29](https://www.youtube.com/watch?v=\_UVHneBUBW0\&t=389s) Why we can omit dimensions&#x20;
* [8:53](https://www.youtube.com/watch?v=\_UVHneBUBW0\&t=533s) Principal components in terms of variance and covariance!!!&#x20;
* [12:47](https://www.youtube.com/watch?v=\_UVHneBUBW0\&t=767s) Transforming samples with loading scores&#x20;
* [17:49](https://www.youtube.com/watch?v=\_UVHneBUBW0\&t=1069s) Review of main ideas&#x20;
* [19:11](https://www.youtube.com/watch?v=\_UVHneBUBW0\&t=1151s) Scree plots for diagnostics&#x20;
* [19:39](https://www.youtube.com/watch?v=\_UVHneBUBW0\&t=1179s) Loadings and Eignvectors

Input data often come with numerous correlated variables, some of which may be redundant or irrelevant, complicating prediction models. When variables are not perfectly correlated (which is usually the case), each still carries some independent information. However, analyzing data with many variables can be highly complex. To manage this, a threshold for acceptable correlation (e.g., 80 percent) may be set. When two variables exceed this threshold, they are considered correlated, and one can be safely removed from the dataset as redundant.

PCA steps in to transform linearly correlated variables into uncorrelated ones known as **principal components (PCs)**. It also arranges these uncorrelated variables by their variance across data records. Variables with low changeability, usually found at the bottom of the PC list, can then be excluded, reducing the dataset's dimensionality as desired.

The goal is to create a new set of variables from the original, retaining most of the information in the first few variables. This simplifies defining a cutoff point and enables the use of only a subset of the new variables in subsequent steps, like a machine learning model or regression.

The first PC captures a significant portion of the data's variability. PCA begins by seeking linear combinations of the original variables weighted by their contributions to extract maximum variance. After removing this variance, it identifies the second linear combination of variables that explains the second most variance, forming the second PC. This process continues for succeeding PCs, each accounting for the remaining data variability.

In the figure provided, there's a dataset with two variables, $$x_1$$and $$x_2$$. $$PC_1$$represents the axis along which data records exhibit the most significant variation, while $$PC_2$$ represents the axis with the second-highest variation, perpendicular to $$PC_1$$.

![PCA Example](<../../.gitbook/assets/image (12).png>)

## 5.3.1 PCA Algorithm

**Step (1): Get and subtract the mean** For an input dataset with $$N$$ records $$(1,2,...,N)$$and $$M$$ variables $$(x_1, x_2, ..., x_M)$$, the mean of each variable is calculated using the following equation:

$$\bar{x_i}=\frac{1}{N}\displaystyle\sum_{k=1}^{N}x_{i_k}$$

$$i=1,2,...,M$$

The calculated **mean** is then subtracted from its associated variable for all data records by the equation given below. This step produces a dataset with a mean of zero and simplifies the remaining steps of the PCA algorithm.

$$x_i=x_i-\bar{x_i}$$

$$i=1,2,...,M$$

**Step (2): Calculate the covariance matrix** The covariance $$C(x_i , x_j)$$ is a measure of the changes in variable $$x_i$$ with respect to changes in variable $$x_j$$ , according to the following equation:

$$C(x_i, x_j)=\displaystyle\frac{1}{N-1}\displaystyle\sum_{k_1}^{N}(x_i\cdot x_j)_k$$

Since the covariance is calculated for all data variables with respect to each other, this will form a symmetric matrix with dimensions $$[M \cdot M]$$, as shown below.

$$\begin{bmatrix} C(x_1, x_1) & C(x_1, x_2) & C(x_1, x_3) & \cdots & C(x_1, x_M) \\ C(x_2, x_1) & C(x_2, x_2) & C(x_2, x_3) & \cdots & C(x_2, x_M) \\ C(x_3, x_1) & C(x_3, x_2) & C(x_3, x_3) & \cdots & C(x_3, x_M) \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ C(x_M, x_1) & C(x_M, x_2) & C(x_M, x_3) & \cdots & C(x_M, x_M) \\ \end{bmatrix}$$

The exact value of $$C(x_i, x_j)$$ is an indication of how strongly the two variables depend on each other; however, the value is not as important as the sign. A positive covariance indicates that both variables increase (or decrease) together, while a negative value indicates that if one variable increases, the other variable decreases (or vice versa). If the covariance is zero, the variables are uncorrelated.

**Step (3): Calculate the eigenvalues and eigenvectors** The objective of PCA is to transform the calculated covariance matrix into an optimum form where all the variables are uncorrelated linearly to first order (i.e., $$C(x_i, x_j) = 0,i ≠ j)$$. This results in a diagonal matrix where all elements equal zero except those in the diagonal, as presented by the following equation:

$$\begin{bmatrix} C(x_1, x_1) & C(x_1, x_2) & C(x_1, x_3) & \cdots & C(x_1, x_M) \\ C(x_2, x_1) & C(x_2, x_2) & C(x_2, x_3) & \cdots & C(x_2, x_M) \\ C(x_3, x_1) & C(x_3, x_2) & C(x_3, x_3) & \cdots & C(x_3, x_M) \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ C(x_M, x_1) & C(x_M, x_2) & C(x_M, x_3) & \cdots & C(x_M, x_M) \\ \end{bmatrix}= \begin{bmatrix} \lambda_1 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & \lambda_M \\ \end{bmatrix}$$

The diagonal elements of the matrix are known as the **eigenvalues (λ)** of the covariance matrix, and the corresponding columns are known as the **eigenvectors**. The eigenvectors are orthogonal to each other, and the eigenvalues are sorted in descending order. The eigenvector with the highest eigenvalue is the first principal component, and the second-highest eigenvalue is the second principal component, and so on.

$$∴C-\begin{bmatrix} \lambda_1 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & \lambda_M \\ \end{bmatrix}=0$$

$$C-\begin{bmatrix} \lambda_1 & \cdots & \lambda_M \\ \end{bmatrix}=\begin{bmatrix} 1 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & 1 \\ \end{bmatrix}=0$$

$$C-\begin{bmatrix} \lambda_1 & \cdots & \lambda_M \\ \end{bmatrix}\cdot I=0$$

where the diagonal elements of the transformed matrix are called eigenvalues (λ), and I denotes the identity matrix (i.e., a matrix with “1” in its diagonal and “0” otherwise). The eigenvalues are found by solving the following equation:

$$det(C-\lambda\cdot I)=|C-\lambda\cdot I|=0$$

where det is the determinant of the matrix. The principal components (PCs) are the Eigenvectors of the calculated eigenvalues. An eigenvector is a vector which, when transformed by the covariance matrix, results in a scaled version of the vector, and this scale is the associated eigenvalue, as explained in the following equation:

$$C\cdot PC_i=(\lambda_i\cdot I)PC_i$$ $$i=1,2,...,M$$ Therefore, the solution to $$[(C – \lambda_i \cdot I) · PC_i = 0]$$ will result in the ith principal component $$(PCi)$$. Since there are no correlations between the obtained PCs, the eigenvectors are orthogonal vectors.

**Step (4): Formulate the PCs** The PC (i.e., eigenvector) that corresponds to the highest eigenvalue is the first principal component of the dataset. Consequently, the next step is to order all other PCs according to their eigenvalues, from highest to lowest. The percentage of how much variance (V) each PC represents is calculated by the following equation: $$H_{PC_i}=\frac{\lambda_i}{[\lambda_1+\cdots +\lambda_M]}\cdot 100\%$$

**Step (5): Dimensionality reduction** We may decide to ignore the PCs with less significance (i.e., those that appear at the bottom of the PC list) due to their low eigenvalues. This will reduce the original dataset of $$(x_1, x2, …, xM)$$ variables to a smaller version with $$(PC_1, PC_2, …, PC_M)$$, where $$M* < M$$.

**Step (6): Reconstruct the dataset** The dataset is now reconstructed by the produced PCs, using the following equation: $$[y]^T=[PC_1, PC_2, ..., PC_M]\cdot [x]^T$$ where $$[y]^T$$ is the reconstructed dataset, and $$[x]^T$$ is the original dataset. \


## PCA Example:&#x20;

For the dataset given in the figure, follow the PCA algorithm to develop a new version of the dataset in which its variables are uncorrelated and ordered according to their significance to the input data.

![PCA Example](assets/images/data-science/iu-dlmbdsa01/PCA-Example.png)

The dataset is shown using the “normal” $$x_1$$ and $$x_2$$ axes, but looking at the distribution, this does not seem to be optimal. The data records are scattered around the diagonal $$(x_1 = x_2)$$, so we would expect that the diagonal itself would be a better primary axis as it captures the most important variance of the data records. Since the data records are not all on the diagonal, we expect that a second axis perpendicular to the diagonal will capture the second-highest variability of these data records. Hence, the information in the graph is better described using the diagonal and a new axis perpendicular to it. If we need to reduce the number of variables, we could use only the new (diagonal) axis, as it captures most of the information, and neglect the second new axis which contains less significant information about the variance of the data points. The algorithm is performed as follows:

**The mean values are:**

$$\bar{x_1}=\frac{1}{10}\cdot 18.1=1.81$$ and $$\bar{x_2}=\frac{1}{10}\cdot 19.1=1.91$$

**Subtract the mean from the dataset:**

$$x_1 = x_1 – 1.81$$ and $$x_2 = x_2 – 1.91$$

**Adjusted Dataset (Zero Mean):**

| #  | $$x_1$$ | $$x_2$$ |
| -- | ------- | ------- |
| 1  | 0.69    | 0.49    |
| 2  | -1.31   | -1.21   |
| 3  | 0.39    | 0.99    |
| 4  | 0.09    | 0.29    |
| 5  | 1.29    | 1.09    |
| 6  | 0.49    | 0.79    |
| 7  | 0.19    | -0.31   |
| 8  | -0.81   | -0.81   |
| 9  | -0.31   | -0.31   |
| 10 | -0.71   | -1.01   |

**Calculate the covariance matrix:**

$$C=\begin{bmatrix} C(x_1, x_1) & C(x_1, x_2) \\ C(x_2, x_1) & C(x_2, x_2) \\ \end{bmatrix}=\frac{1}{9}\begin{bmatrix} 5.549 & 5.539 \\ 5.539 & 6.449 \\ \end{bmatrix}= \begin{bmatrix} 0.616 & 0.615 \\ 0.615 & 0.716 \\ \end{bmatrix}$$

**Calculate the eigenvalues and eigenvectors:**

$$det(C-\lambda\cdot I)=|C-\lambda\cdot I|=0$$

$$\begin{bmatrix} 0.616-\lambda & 0.615 \\ 0.615 & 0.716-\lambda \\ \end{bmatrix}=0$$

$$(0.616-\lambda)(0.716-\lambda)-0.615\cdot 0.615=0$$

$$(0.442-1.333\lambda+\lambda^2)-0.378=0$$ $$\lambda^2-1.333\lambda+0.063=0$$

$$\lambda_1=1.28$$ and $$\lambda_2=0.049$$

**Calculate the eigenvectors:** $$PC_1$$

$$(C-\lambda_1\cdot I) PC_1=0$$

$$\begin{bmatrix} 0.616-1.28 & 0.615 \\ 0.615 & 0.716-1.28 \\ \end{bmatrix}\cdot \begin{bmatrix} PC_{11} \\ PC_{21} \\ \end{bmatrix}=0$$

$$\begin{bmatrix} -0.664 & 0.615 \\ 0.615 & -0.564 \\ \end{bmatrix}\cdot \begin{bmatrix} PC_{11} \\ PC_{21} \\ \end{bmatrix}=0$$

$$-0.664\cdot PC_{11}+0.615\cdot PC_{21}=0$$

$$0.615\cdot PC_{11}-0.564\cdot PC_{21}=0$$

$$PC_1=\begin{bmatrix} PC_{11} \\ PC_{21} \\ \end{bmatrix}=\begin{bmatrix} 0.779 \\ 0.627 \\ \end{bmatrix}$$

![Eigenvectors for PC\_1](assets/images/data-science/iu-dlmbdsa01/EigenvectorsForPC1.png)

**Calculate the eigenvectors:** $$PC_2$$

$$(C-\lambda_2\cdot I) PC_2=0$$

$$\begin{bmatrix} 0.616-0.049 & 0.615 \\ 0.615 & 0.716-0.049 \\ \end{bmatrix}\cdot \begin{bmatrix} PC_{12} \\ PC_{22} \\ \end{bmatrix}=0$$

$$\begin{bmatrix} 0.567 & 0.615 \\ 0.615 & 0.667 \\ \end{bmatrix}\cdot \begin{bmatrix} PC_{12} \\ PC_{22} \\ \end{bmatrix}=0$$

$$0.567\cdot PC_{12}+0.615\cdot PC_{22}=0$$

$$0.615\cdot PC_{12}+0.667\cdot PC_{22}=0$$

$$PC_2=\begin{bmatrix} PC_{12} \\ PC_{22} \\ \end{bmatrix}=\begin{bmatrix} -0.735 \\ 0.678 \\ \end{bmatrix}$$

![Alt text](assets/images/data-science/iu-dlmbdsa01/EigenVectorsForPC1andPC2.png)

**Reconstruct the dataset:**

$$[y]^T=[PC_1, PC_2]\cdot [x]^T$$

Reconstructed Data

| #  | $$y_1$$ | $$y_2$$ |
| -- | ------- | ------- |
| 1  | 1.22    | -0.25   |
| 2  | -2.62   | 0.21    |
| 3  | 1.46    | 0.56    |
| 4  | 0.40    | 0.19    |
| 5  | 2.47    | -0.30   |
| 6  | 1.34    | 0.25    |
| 7  | -0.14   | -0.51   |
| 8  | -1.68   | 0.06    |
| 9  | -0.64   | 0.02    |
| 10 | -1.80   | -0.24   |

![Reconstruction Graph](<../../.gitbook/assets/image (13).png>)



{% content-ref url="codes/02-dimensionality-reduction-using-PCA/2.2-PCA-Complete-Example.md" %}
[2.2-PCA-Complete-Example.md](codes/02-dimensionality-reduction-using-PCA/2.2-PCA-Complete-Example.md)
{% endcontent-ref %}
\n\n---\n\n## Navigation\n\n- **Parent**: [[data-science.iu-dlmbdsa01.mathematical-techniques]]\n- **Course**: [[data-science.iu-dlmbdsa01]]\n