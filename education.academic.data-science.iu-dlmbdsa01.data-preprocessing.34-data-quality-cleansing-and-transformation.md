# 3.4 Data Quality, Cleansing, and Transformation

Collected datasets often suffer from various quality issues, including noisy, inaccurate, incomplete, inconsistent, missing, duplicate, or outlier values. It's important to differentiate between "true" outliers, which represent legitimate but unusual data events, and "fake" outliers, which result from data quality problems.

Data scientists spend a significant amount of their time addressing these data quality issues, as the quality of the dataset forms the foundational "prior" on which predictive models are built. Resolving missing values and outliers can fundamentally change this prior, affecting how machine learning models operate.

## Missing Values and Outliers

To handle missing values and outliers, several common methods are employed:

1. **Removal of Records**: In cases where the dataset is large and the removal of certain records won't significantly impact the analysis, data records containing missing values and/or outliers can be removed. This step must be taken cautiously to ensure it doesn't affect the results.
2. **Interpolation**: Missing values or outliers can be replaced with interpolated values derived from neighboring records. For example, linear interpolation can be used to estimate missing temperature values based on surrounding data points.
3. **Replacement with Averages**: Missing values or outliers can be replaced with the average value of their respective variables across all data records.
4. **Replacement with Mode**: Alternatively, missing values or outliers can be replaced with the most frequently observed value for their respective variables across all data records.

To retain information about how missing values and outliers were handled, a new binary variable can be introduced in the dataset. It would have a value of "0" for normal data records and "1" for records that had missing and/or outlier values and were processed using one of the above methods.

## Duplicate Records in Datasets

When working with datasets, it's common to encounter duplicate records, which are essentially identical data entries. The decision regarding whether to remove these duplicates or retain them depends on various factors:

### **Removing Duplicate Records:**

* **Computational Efficiency**: Removing duplicate records can significantly reduce computing time, especially when dealing with large datasets. Fewer records mean faster analysis and processing.

### **Retaining Duplicate Records:**

* **Analysis Objectives**: In some cases, retaining duplicate records may not negatively impact the outcomes of the analysis. It depends on the specific goals of the analysis. Duplicate records might not provide new insights but generally won't degrade the results.

The choice between removing or keeping duplicate records should align with the objectives of the data analysis and the available computational resources. While removing duplicates can improve efficiency, it's essential to consider the potential loss of information. Ultimately, the decision should be made with a clear understanding of how duplicates affect the specific analysis at hand.

## Redundancy

Datasets often contain redundant and irrelevant variables, which can hinder the effectiveness of data analysis. To address these issues, correlation analysis is a valuable technique. It allows us to identify and eliminate variables that exhibit high correlation with other variables while retaining important information about the dataset.

![](<../../.gitbook/assets/image (9).png>)

Key points regarding correlation analysis:

**1. Correlation Shapes:**

* Circular shape: Indicates no correlation between variables.
* Cigar shape: Suggests partial correlation.
* Line shape: Represents strong correlation.

**2. Correlation Coefficient (ρ):**

* The correlation coefficient ρ quantifies the relationship between two variables, x and y, within a dataset of n records.
*   The formula for calculating ρ is as follows:

    $$\rho = \frac{\displaystyle\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\displaystyle\sum_{i=1}^{n}(x_i - \bar{x})^2}\sqrt{\displaystyle\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

Where $$\bar{x}$$ and $$\bar{y}$$ are the average values of variables $$\bar{x}$$ and $$\bar{y}$$, respectively.

**3. Interpretation of ρ:**

* ρ ranges from -1 to 1.
* ρ = 1: Variables are fully correlated.
* ρ = 0: No correlation or independence between variables.
* Negative ρ: Indicates anti-correlation; as one variable goes up, the other goes down.

**4. Threshold Setting:**

* A threshold can be set on ρ to determine when to remove one of two correlated variables. If ρ exceeds this threshold, the removal has negligible influence on performance.

**5. Dimensionality Reduction:**

* Another approach to handle redundant variables is dimensionality reduction techniques like Principal Component Analysis (PCA).
* PCA sorts variables by importance and removes those with minor influence on data variability.
* This technique results in a dataset with fewer variables, simplifying subsequent analysis.

In summary, correlation analysis and dimensionality reduction techniques play a critical role in identifying and addressing redundant variables in a dataset, enhancing the efficiency and effectiveness of data analysis.

## Variable Transformation Methods

In the realm of data science, transforming data is often necessary to prepare the dataset for analysis. Several key data transformation methods include variable scaling, decomposition, and aggregation:

### **Variable Scaling**

This method is applied when the dataset contains variables with varying scales. For instance, a dataset might have income values in dollars, the number of monthly purchases, and the amount of car fuel consumed per month. To ensure that all variables carry equal weight during analysis, modeling techniques often require scaling.

#### Motivation for Variable Scaling

* **Equal Weighting**: Many data analysis and modeling techniques assume that all variables contribute equally to the analysis. However, when variables have different scales, those with larger scales can dominate the results, leading to biased or misleading outcomes.

* **Normalization**: Scaling is often used to normalize variables, transforming them into a consistent range, typically between 0 and 1. This makes it easier to compare and interpret variable importance.

#### Methods of Scaling

* **Min-Max Normalization**: This method scales variables to a specific range, typically between 0 and 1, by transforming the data linearly. It is calculated as:

$$x_{Scaled} = \frac{x-x_{min}}{x_{max} - x_{min}}$$​

* **Standardization (Z-score Scaling)**: This method transforms variables to have a mean of 0 and a standard deviation of 1. It is calculated as:

$$x_{Scaled} = \frac{x-x_{mean}}{x_{std}}$$

* **Robust Scaling**: This method is similar to standardization but uses the median and interquartile range, making it more robust to outliers.

* **Log Transformation**: When dealing with highly skewed data, applying the logarithmic transformation can help scale and normalize the distribution.

#### Benefits of Variable Scaling

* **Fair Comparison**: Scaling ensures that variables with different scales can be compared on an equal footing, preventing one variable from dominating the analysis.

* **Improved Model Performance**: Many machine learning algorithms, such as gradient-based optimization methods, perform better on scaled data, converging faster and producing more accurate results.

* **Enhanced Interpretability**: Scaling can make the coefficients or feature importance scores in models more interpretable since variables are on the same scale.

{% embed url="https://www.youtube.com/watch?v=sxEqtjLC0aM" %}
Standardization Vs Normalization Clearly Explained
{% endembed %}

{% embed url="https://www.youtube.com/watch?v=n9KeJLGwW0U" %}
Should you always scale your data?
{% endembed %}

### **Variable Decomposition**

Some variables may benefit from further decomposition into multiple variables, enhancing data representation. For instance, a time variable can be decomposed into hour and minute variables. Additionally, it's possible that only one of the decomposed variables (e.g., hour or minute) is relevant, leading to the removal of irrelevant variables from the dataset.

#### Motivation for Variable Decomposition

* **Data Representation**: In many real-world datasets, a single variable may not capture all the relevant information. Decomposing variables allows us to represent the data in a more detailed and informative manner.

* **Feature Engineering**: In machine learning, creating meaningful features is crucial for model performance. Decomposition can lead to the creation of new features that can improve model accuracy and interpretability.

#### Benefits of Variable Decomposition

* **Improved Interpretability**: Decomposed variables often have a more intuitive and interpretable meaning, making it easier to understand patterns in the data.

* **Enhanced Modeling**: Machine learning models can benefit from decomposed variables as they capture more detailed information, potentially leading to better predictive performance.

* **Feature Selection**: Decomposition can help in identifying and selecting the most relevant features, reducing the risk of overfitting and improving model generalization.

### **Variable Aggregation**

This method involves merging or aggregating two or more variables into a single variable when it makes more sense or simplifies the analysis. For example, "gross income" and "paid tax" variables could be aggregated into a single "net income" variable.

These data transformation techniques are essential for ensuring that the dataset is in a suitable form for data analysis, improving the accuracy and effectiveness of subsequent data science tasks.

#### Motivation for Variable Aggregation

* **Simplification**: In some cases, combining related variables into a single variable simplifies the dataset and makes it more manageable for analysis. This simplification can lead to a clearer and more concise representation of the data.

* **Enhancing Relevance**: Aggregating variables can help create new variables that are more relevant to the analysis or problem at hand. These new variables can often capture essential information that might be obscured when dealing with multiple separate variables.

#### Benefits of Variable Aggregation

* **Improved Clarity**: Aggregating variables reduces the complexity of the dataset, making it easier to understand and work with, especially in cases with many variables.

* **Relevance Enhancement**: Aggregated variables can provide a more relevant and direct perspective on the data, simplifying subsequent analyses and interpretations.

* **Dimension Reduction**: Aggregation can help reduce the number of variables, which is particularly valuable in cases where dimensionality needs to be managed.
\n\n---\n\n## Navigation\n\n- **Parent**: [[education.academic.data-science.iu-dlmbdsa01.data-preprocessing]]\n- **Course**: [[education.academic.data-science.iu-dlmbdsa01]]\n