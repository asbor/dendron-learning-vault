# 6.3 Support Vector Machines

Support Vector Machines (SVM) is a versatile technique used for both classification and regression tasks. In this discussion, we'll focus on SVM's application in classification problems. SVM is a binary linear classification method, meaning it separates data into two classes based on a linear equation formed from the input dataset variables {$$x_{1k}, x_{2k}, …, x_{Mk}$$}, where $$k = 1, 2, …, N$$. Here, $$N$$ represents the number of data records, and M represents the number of data variables (Polson & Scott, 2011).

{% embed url="https://www.youtube.com/watch?v=efR1C6CvhmE" %}
Support Vector Machines Part 1 (of 3): Main Ideas!!!
{% endembed %}

## 6.3.1 Linear Classification Rule

In scenarios where a dataset consists of two distinct classes, such as distinguishing between rich and poor individuals or tall and short students, a crucial concept is the **classification line**. This line acts as the boundary, effectively separating the two classes on opposite sides.

This classification line is alternatively referred to as the **decision boundary** and is mathematically defined as:

$$w \cdot x_i + b = 0$$

Here, $$w$$ represents the weight vector, $$x_i$$ represents the data vector, and $$b$$ represents the bias term. The weight vector $$w$$ is perpendicular to the classification line, determining its orientation, while the bias term $$b$$ influences the position of the line along the weight vector.

The classification rule can be succinctly expressed as:

$$f(x) = \begin{cases} +1 & \text{if } w \cdot x_i + b \geq 0 \\ -1 & \text{if } w \cdot x_i + b < 0 \end{cases}$$

Additionally, the data records (represented by $$x_i$$) that reside on either side of this separation are called **support vectors**. The distance between these support vectors on opposite sides, known as the **margin (l)**, plays a significant role in understanding the quality of the classification.

![Support Vector Machines](assets/images/data-science/iu-dlmbdsa01/Support-Vector-Machines.png)

When the threshold is positioned precisely midway between the two classes, the classification line becomes equidistant from both sides. In this scenario, the classification line can be expressed as:

$$w \cdot x_i + b = \pm 1$$

This implies that if we choose to shift the classification boundary, whether towards the left or right, one side's classification area will expand while the other side's classification area will contract.

When we utilize the threshold that maximizes the margin, we are essentially implementing the **Maximal Margin Classifier**.

However, it's crucial to emphasize that the Maximal Margin Classifier is exclusively applicable to datasets that exhibit linear separability. In simpler terms, it can only be effectively employed when it's possible to draw a straight classification line that distinctly separates the two classes. In cases where the dataset doesn't exhibit linear separability, the Maximal Margin Classifier isn't a suitable choice. Additionally, it's important to note that the Maximal Margin Classifier is highly susceptible to the influence of outliers within the data.

**Allow misclassification**: In scenarios where the dataset isn't linearly separable, the Maximal Margin Classifier can be modified to allow for a certain number of misclassifications. This is achieved by introducing a **slack variable (ξ)**, which is a non-negative value that represents the degree of misclassification. The Maximal Margin Classifier is then modified to:

## 6.3.2 Separating Channel

The region lying between the classification line (often referred to as the **decision boundary**) and parallel lines, equidistant from both sides, constitutes what is known as the **separating channel**. This channel is effectively enclosed by support vectors, which are the data records (again, $$x_i$$) residing on either side of the **separating channel**. The **margin (l)**, as previously mentioned, represents the width or distance between the two sides of this channel and can be computed as the separation distance between the right and left support vectors.

## 6.3.3 Margin Calculation

$$1 = x_i^{+1}-x_i^{-1}$$

$$1 = \frac{+1-b}{w}-\frac{-1-b}{w} = \frac{2}{||w||}$$

The primary goal of SVM is to maximize the margin (l) to achieve the best possible separation between the two classes. Therefore, the problem is transformed into an optimization task, aiming to find the classification equation that yields the maximum margin.

## 6.3.4 Kernel Trick

When dealing with nonlinearly separable datasets, SVM employs a strategy called the Kernel trick (Wenzel et al., 2017). The idea is to project all data points into a higher-dimensional space where the dataset becomes linearly separable. Instead of physically projecting data into higher dimensions, SVM only considers the relative distances between data points in this "virtual" projection space, facilitated by an appropriate Kernel function. Common Kernel functions include polynomial, sigmoid, and radial kernels.

![Nonlinear Classification by SVM](assets/images/data-science/iu-dlmbdsa01/Nonliniar-Classification-By-SVM.png)

{% content-ref url="codes/01-LinearSVC/1.1-SupportVectorMachine.md" %}
[1.1-SupportVectorMachine.md](codes/01-LinearSVC/1.1-SupportVectorMachine.md)
{% endcontent-ref %}

{% content-ref url="codes/01-LinearSVC/1.2-LinearSVM-Example-1.md" %}
[1.2-LinearSVM-Example-1.md](codes/01-LinearSVC/1.2-LinearSVM-Example-1.md)
{% endcontent-ref %}

{% content-ref url="codes/01-LinearSVC/1.3-LinearSVM-Example-2.md" %}
[1.3-LinearSVM-Example-2.md](codes/01-LinearSVC/1.3-LinearSVM-Example-2.md)
{% endcontent-ref %}

{% content-ref url="codes/01-LinearSVC/1.4-SVM-Complete-Example.md" %}
[1.4-SVM-Complete-Example.md](codes/01-LinearSVC/1.4-SVM-Complete-Example.md)
{% endcontent-ref %}

## 6.3.5 Online Resources

Numerous online software packages are available for SVM classification on any dataset. The library for support vector machines, LIBSVM, is an excellent online resource and includes helpful software downloads (Chang & Lin, 2011). Additionally, the "Scikit-Learn" tool in Python provides a valuable online resource suitable for clustering and regression tasks.

{% content-ref url="https://www.csie.ntu.edu.tw/~cjlin/libsvm/" %}
[https://www.csie.ntu.edu.tw/\~cjlin/libsvm/](https://www.csie.ntu.edu.tw/\~cjlin/libsvm/)
{% endcontent-ref %}

{% content-ref url="https://scikit-learn.org/stable/" %}
[https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)
{% endcontent-ref %}
\n\n---\n\n## Navigation\n\n- **Parent**: [[data-science.iu-dlmbdsa01.ai-techniques]]\n- **Course**: [[data-science.iu-dlmbdsa01]]\n