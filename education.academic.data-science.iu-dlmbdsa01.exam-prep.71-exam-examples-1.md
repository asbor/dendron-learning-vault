# 7.1 Exam Examples 1

## Question 1

Which of the following is **not** a variable transformation method?

1. variable aggregation
2. variable extraction
3. variable decomposition
4. variable scaling

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">2. variable extraction</mark>

_Among the options provided, "variable extraction" is not a variable transformation method. Variable extraction involves creating new variables from existing ones, typically by applying dimensionality reduction techniques like Principal Component Analysis (PCA) or feature selection methods. The other methods listed, such as variable aggregation, variable decomposition, and variable scaling, all involve altering or modifying existing variables rather than extracting new ones._

See chapter:

[#variable-transformation-methods](../3.-data-pre-processing/3.4-data-quality-cleansing-and-transformation.md#variable-transformation-methods "mention")

</details>

***

## Question 2

Iterations represent the total number of ...

1. Passes of the training data through the network
2. Input layer neurons.
3. Passes of the test data through the network
4. Network neurons.

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">1. passes of the training data through the network</mark>

_Iterations represent the total number of passes of the training data through the network. The training data is passed through the network in batches, and each batch is passed through the network once per iteration. The number of iterations is a hyperparameter that can be tuned to improve model performance._

</details>

***

## Question 3

Which of these approaches is an unsupervised learning approach?

1. Regression
2. Classification
3. Forecasting
4. Clustering

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">4. Clustering</mark>

_Clustering is an unsupervised learning approach that involves grouping data points into clusters based on their similarities. The goal of clustering is to identify patterns in the data and group similar data points together. The other options listed, such as regression, classification, and forecasting, are all supervised learning approaches._

See chapter:

[5.4-cluster-analysis.md](../5.-selected-mathematical-techniques/5.4-cluster-analysis.md "mention")

</details>

***

## Question 4

During back propagation training, the purpose of the delta rule is to make weight adjustments so as to minimize the ...

1. number of times the test data must pass thought the network
2. sum of absolute differences between computed and actual outputs
3. error between computed and actual output
4. number of times the training data must pass thought the network

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">3. error between computed and actual output</mark>

_During backpropagation training, the **delta rule** plays a crucial role in adjusting the weights of a neural network to minimize the error between the computed (predicted) and actual output. It guides the network in learning to produce more accurate predictions by iteratively updating the weights based on the difference between what the network predicts and what it should predict. This process continues until the error is minimized, leading to better model performance._

</details>

***

## Question 5

which of the following models predict a future observation as a function of the errors in previous forecasts?

1. ARIMA(0,1,0) model
2. Any auto-regressive model
3. ARIMA(1,1,0) model
4. Any moving average model

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">4. Any moving average model</mark>

_Moving average models predict a future observation as a function of the errors in previous forecasts. The ARIMA(0,1,0) model is a special case of a moving average model, and the ARIMA(1,1,0) model is a special case of an auto-regressive model._

See chapter:

[5.5-AutoregressiveIntegratedMovingAverageModel.md](../5.-selected-mathematical-techniques/codes/05-time-series-forcasting/5.5-AutoregressiveIntegratedMovingAverageModel.md "mention")

</details>

***

## Question 6

The activation function which generates outputs that are **not** confined to a specific range, is called ...

1. Linear function
2. Step function
3. log sigmoid function
4. tan sigmoid function

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">1. Linear function</mark>

_The **activation function** which generates outputs that are not confined to a specific range is called a **linear function**. The other options listed, such as step function, log sigmoid function, and tan sigmoid function, all generate outputs that are confined to a specific range._

See chapter:

[#typical-activation-functions](../6.-selected-artificial-intelligence-techniques/6.4-artificial-neural-networks.md#typical-activation-functions "mention")

</details>

***

## Question 7

which of the following type of information is operational in motor car manufacturing?

1. Decision on introducing a new model
2. Computing sales tax collected
3. Scheduling production
4. Assessing competitor car

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">3. Scheduling production</mark>

_In the context of motor car manufacturing, the operational type of information refers to the scheduling of production. This involves the day-to-day planning and coordination of manufacturing activities, ensuring that tasks are performed efficiently, resources are allocated effectively, and the production process runs smoothly to meet demand. This operational information is crucial for the timely and organized production of motor vehicles._

</details>

***

## Question 8

Stratigic information is required by ...

1. middle management
2. line management
3. all workers
4. top management

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">4. top management</mark>

_Strategic information is required by top management. This type of information is used to make long-term decisions that affect the organization as a whole. It is used to set the organization's goals and objectives, and to develop plans for achieving them. Strategic information is also used to monitor the organization's performance and to evaluate its progress towards achieving its goals._

</details>

***

## Question 9

Which of the following are **not** required to claculate the classification model precision?

1. TN and FN
2. FP and FN
3. TP and TN
4. TP and FP

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">1. TN and FN</mark>

_The precision of a classification model is calculated using the number of true positives (TP) and false positives (FP). The number of true negatives (TN) and false negatives (FN) are used to calculate the model's recall._

See chapter:

</details>

***

## Question 10

Which statement is true about neural network and linear regression models?

1. Both models require numeric attributes to range between 0 and 1
2. The output of both models is a categorical attribute value
3. both models require input attributes to be numeric
4. both techniques build models whose output is determined by a linear sum of weighted input attributes values

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">3. both models require input attributes to be numeric</mark>

_This means that in both neural networks and linear regression, the input variables must be numerical in nature, and they can take any numeric values. This requirement ensures that mathematical operations can be performed on the input attributes, allowing these models to make predictions or classifications based on numerical patterns in the data._

</details>

***

## Question 11

if there is a spike at low order lag in the residual PACF plot, then we ...

1. decrease p by 1 and re-fit the ARIMA(p,d,q) model
2. decrease q by 1 and re-fit the ARIMA(p,d,q) model
3. increase p by 1 and re-fit the ARIMA(p,d,q) model
4. increase q by 1 and re-fit the ARIMA(p,d,q) model

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">3. increase p by 1 and re-fit the ARIMA(p,d,q) model</mark>

_If there is a spike at low order lag in the residual PACF plot, then we increase p by 1 and re-fit the ARIMA(p,d,q) model. This is because the residual PACF plot is used to determine the value of p, which is the number of auto-regressive terms in the model. If there is a spike at low order lag in the residual PACF plot, then this indicates that there is a significant correlation between the residuals at low order lags. This means that the model is not capturing all the information in the data, and so we need to increase p by 1 and re-fit the model to improve its performance._

See chapter:

[#5.6.6-auto-regressive-integrated-moving-average-arima-model](../5.-selected-mathematical-techniques/5.6-time-series-forecasting.md#5.6.6-auto-regressive-integrated-moving-average-arima-model "mention")

</details>

***

## Question 12

Organizations have hierarchial structures because ...

1. it is done by every organization
2. specific responsibilities are assigned to each level
3. it is convenient to do so
4. it provides opportunities for promotion

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">2. specific responsibilities are assigned to each level</mark>

> **Hierarchical structure** is a way to organize a company in which different levels are ranked one above the other, with each level having certain responsibilities and duties. It is a very common organizational structure, and it is used by many companies around the world. The main reason for this is that it is a very effective way to organize a company, as it allows for the efficient allocation of resources and the effective management of employees.

</details>

***

## Question 13

The back propagation algorithm is applied in ANN to ...

1. Define the neuron's activation function
2. estimate the weights which minimize the network's error
3. predict the network's inputs from its outputs
4. reduce the number of the network's hidden layers

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">2. estimate the weights which minimize the network's error</mark>

> The backpropagation algorithm is applied in ANN to estimate the weights which minimize the network's error. This is done by iteratively updating the weights based on the difference between what the network predicts and what it should predict. This process continues until the error is minimized, leading to better model performance.

</details>

***

## Question 14

which of the following is characteristic of a processed data?

1. Hard to use for data analysis
2. Raw data are successfully extracted
3. Data is not ready for analysis
4. The information and insights of the dataset are noted

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">4. The information and insights of the dataset are noted</mark>

> *Processed data typically undergo various transformations, cleaning, and analysis steps to extract meaningful information and insights from the raw data. Therefore, processed data are ready for analysis, and the results of this analysis are often noted or documented for further use.*

</details>

***

## Question 15

Why is data collection considered an expensive process in some applications?

_**(6 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">Because it sometimes requires humans to look into the data (3 points) and manually insert related important tags, labels and/or valuable comments (3 points)</mark>

</details>

***

## Question 16

What are the six stages of data processing?

_**(6 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">

These stages are:

1. Data collection
2. Data preparation
3. Data input
4. Data analysis - Better to say "Data processing"
5. Data Interpretation
6. Data storage

</mark>

> The six stages of data processing are as follows:
>
> 1. **Data Collection**: In this initial stage, data is gathered or collected from various sources. This could include manual data entry, sensor readings, surveys, or data extraction from databases, among other methods.
>
> 2. **Data Preparation**: Once collected, data often requires cleaning and preprocessing. This stage involves handling missing data, removing duplicates, transforming data into a suitable format, and standardizing variables. Data preparation ensures that the data is ready for analysis.
>
> 3. **Data Input**: After data preparation, the processed data is input into the chosen data analysis or processing tools. This could be a database, spreadsheet software, statistical software, or specialized data analysis platforms.
>
> 4. **Data Processing**: Data processing involves applying various techniques and algorithms to analyze, transform, or manipulate the data. This stage may include calculations, statistical analysis, machine learning, or other data processing methods to extract insights or generate results.
>
> 5. **Data Output**: The processed data is presented in a meaningful and understandable format in this stage. This could involve creating reports, visualizations, dashboards, or any other form of output that communicates the results of the data analysis.
>
> 6. **Data Storage and Archiving**: Once the data has been processed and the results have been obtained, it is important to store and archive the data for future reference, compliance, or historical analysis. Proper data storage practices ensure that the data remains accessible and secure.
>
> These stages are typically part of a cyclical process, as data analysis often leads to further questions or refinements, requiring repeated iterations through these stages. Additionally, data processing can vary in complexity and may involve advanced techniques depending on the specific goals of the analysis.

</details>

***

## Question 17

1. Why do we need data visualization tools in data science?
2. Mention four visualization types

_**(18 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">

1. Data visualization tools:
   * Data visualization is adopted to increase understanding of the underlying dataset by providing graphical representation (3 points).
   * Visualized data is easier to analyze, and it is easier to diagnose the data's categorical and numerical content (3 points).

2. Visualization types
   * Scatter plot
   * Bar chart
   * Histogram
   * Pie chart
   * Line chart
   * Area chart
   * Box plot
   * Heat map
   * Bubble chart
   * Tree map
   * etc.

(3 points for each type, maximum 12 points).

</mark>

</details>

***

## Question 18

Determine which is the best approach for each problem: (1) supervised learning, (2) unsupervised learning.

1. Develop a profile for credit card customers likely to carry an average monthly balance of more than $1000.00
2. Determine the characteristics of a successful used car salesperson
3. Find attribute similarities of a group of customers holding one or several insurance policies.
4. Do meaningful attribute relationships exist in a database containing information about credit card customers?
5. Determine wether a credit card transaction is valid or fraudulent.
6. Discriminate some animals according to their weights and heights.

_**(18 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">

1. (2) - unsupervised learning
2. (1) - supervised learning
3. (2) - unsupervised learning
4. (2) - unsupervised learning
5. (1) - supervised learning
6. (2) - unsupervised learning

(3 points for each correct answer, maximum 18 points)

</mark>

> Here's the elaboration on why each approach (supervised or unsupervised learning) is suitable for the given problems:
>
> 1. **Develop a profile for credit card customers likely to carry an average monthly balance of more than $1000.00**:
>  - Approach: Supervised Learning
>  - Reason: This problem involves predicting a specific numeric value (average monthly balance) based on known features (customer profiles). Supervised learning, with labeled data, is appropriate for regression tasks like predicting a continuous value.
>
> 2. **Determine the characteristics of a successful used car salesperson**:
> - Approach: Unsupervised Learning
> - Reason: This problem doesn't involve predicting a specific value but rather identifying patterns or clusters in the data that define successful characteristics. Unsupervised learning, such as clustering or dimensionality reduction, can reveal hidden patterns in the absence of labeled outcomes.
>
> 3. **Find attribute similarities of a group of customers holding one or several insurance policies**:
> - Approach: Unsupervised Learning
> - Reason: Unsupervised learning can help identify similarities or clusters among customers based on attributes without predefined categories. This can be useful for market segmentation or customer profiling.
>
> 4. **Do meaningful attribute relationships exist in a database containing information about credit card customers?**:
> - Approach: Unsupervised Learning
> - Reason: This problem is about exploring data relationships without specifying a target variable. Unsupervised techniques like principal component analysis (PCA) or association rule mining can reveal hidden patterns and relationships in the data.
>
> 5. **Determine whether a credit card transaction is valid or fraudulent**:
> - Approach: Supervised Learning
> - Reason: This problem involves classification, where each transaction needs to be categorized as valid or fraudulent based on known historical data. Supervised learning algorithms, like decision trees or neural networks, are commonly used for classification tasks.
>
> 6. **Discriminate some animals according to their weights and heights**:
>  - Approach: Unsupervised Learning
>  - Reason: Here, the goal is to identify natural groupings or clusters of animals based on their characteristics (weights and heights). Unsupervised learning, particularly clustering algorithms, can be applied to classify animals into groups without prior labels.
>
>In summary, the choice between supervised and unsupervised learning depends on the nature of the problem, whether it involves predicting specific outcomes (supervised) or discovering patterns, clusters, or relationships in the data (unsupervised).

</details>

***
\n\n---\n\n## Navigation\n\n- **Parent**: [[education.academic.data-science.iu-dlmbdsa01.exam-prep]]\n- **Course**: [[education.academic.data-science.iu-dlmbdsa01]]\n