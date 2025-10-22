# 2.4 Performance Evaluation

The overall evaluation of how well a DSUC has been modeled and its predictive values applied successfully within a business can be divided into two parts. The first part involves evaluating the developed prediction model and measuring its performance through a list of known numerical metrics. The second part involves evaluating how the model’s outputs (i.e., the DSUC values) are used to better understand and improve a business. The latter is usually accomplished using a defined list of key performance indicators (KPIs).

### 2.4.1 Model-Centric Evaluation: Performance Metrics

In this section we discuss several metrics for measuring how well a prediction model performs its classification or regression task.

#### 2.4.1.1 Classification Model Evaluation Metrics

{% embed url="https://youtu.be/qHosBSw_71o?si=6OtiFK1yTJpDtWzV" %}

In a classification problem with two output classes, typically labeled as "yes" and "no," a prediction model generates probabilities that, based on a set threshold, determine the class assignment. There are four potential outcomes when applying a classification prediction model to a data record:

1. **True Positive (TP)**: This occurs when the classifier correctly labels a "yes" data record as "yes," resulting in an accurate prediction.
2. **True Negative (TN)**: In this case, the classifier correctly labels a "no" data record as "no," leading to an accurate prediction.
3. **False Positive (FP)**: An FP happens when the classifier wrongly labels a "no" data record as "yes," causing a Type I classification error.
4. **False Negative (FN)**: An FN occurs when the classifier mistakenly labels a "yes" data record as "no," resulting in a Type II classification error.

These four possible outcomes are used to create a vital metric known as the "confusion matrix." When assessing the model based on these outcomes, several key metrics come into play:

![](<../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1).png>)

**Accuracy**: This metric measures the ratio of correct predictions to the total number of predictions. It provides an overall assessment of the model's correctness in its classifications.

![](<../../.gitbook/assets/image (2) (1) (1).png>)

$$Accuracy=\frac{Number Of Correct Predictions}{Total Number Of Predictions}=\frac{TP+TN}{TP+TN+FP+FN}$$

**Precision**: Precision measures how accurate a model is when it returns a positive result. It tells us how many of the positive predictions were actually correct. In essence, it gauges the model's ability to avoid false positives.

![](<../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png>)

$$Precision=\frac{Number Of Real Positives}{Number Of Predicted Positives}=\frac{TP}{TP+FP}$$

**Recall**: Recall measures how often a model produces true positives. It's especially useful when we want to be cautious about false negatives, where an actual positive case is missed by the model, which can have serious consequences (e.g., a misdiagnosis leading to harm).

![](<../../.gitbook/assets/image (2) (1) (1) (1).png>)

$$Recall=\frac{Number Of Real Positives}{Number Of Real Positives+Number Of False Negatives}=\frac{TP}{TP+FN}$$

**Cutoff Values**: A classification model often uses a threshold (cutoff) to determine whether an output belongs to one of two classes (e.g., "yes" or "no"). By adjusting this cutoff value (e.g., setting it to 80 percent), we can change how the model assigns data records to classes, affecting the numbers of TP, TN, FP, and FN.

**Receiver Operator Characteristic (ROC) Curve**: The ROC curve displays the trade-off between the true positive rate and the false positive rate at various cutoff values. An ideal model would have a 100 percent TP rate and a 0 percent FP rate, which would place the curve in the upper-left corner. The ROC curve helps identify the optimal realistic cutoff value that maximizes TP rate while minimizing FP rate.

{% embed url="https://youtu.be/4jRBRDbJemM?si=CisPRt3nba8zoEOC" %}

**Creating an ROC Curve**: To generate an ROC curve:

1. Choose cutoff values within the range of 0 to 100 percent of the maximum model output.
2. Assign the testing set data to their classes and count TP, TN, FP, and FN values.
3.  Calculate the false positive rate and true positive rate for each cutoff value.

    $$FalsePositiveRate=\frac{NuberOfFalsePositive}{NumberOfFalsePositive+NumberOfTrueNegative}$$

    and

    $$TruePositiveRate=\frac{NuberOfTruePositive}{NumberOfTruePositive+NumberOfFalseNegative}$$
4. Plot each point on the ROC curve with coordinates (false positive rate, true positive rate).
5. Repeat steps 2 to 4 for different cutoff values.

**Area Under the Curve (AUC)**: The AUC is a measure of the ROC curve's efficiency. An ideal model would have an AUC of 1, indicating perfect performance. The closer the curve is to the upper-left corner and the larger the AUC, the more efficient the model is at distinguishing between classes.

![](<../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png>)

In summary, precision and recall evaluate a model's performance in terms of accuracy and true positive identification, while the ROC curve and AUC help in determining the optimal cutoff value for a classification model.

#### 2.4.1.2 Regression model evaluation metrics

Evaluation Metrics for Regression Models

In the realm of regression models, the output is typically a probability density distribution, which needs to be converted into a single numeric estimate, often referred to as the optimal point estimator, to be practically useful. When assessing the performance of a regression model on a testing set, the primary focus is on measuring how closely the model's output (y) aligns with the desired output (d). Several key metrics are commonly used for this purpose:

1. **Absolute Error:** Absolute error quantifies the absolute difference between the model's output and the desired output. It provides a straightforward measure of how much the model's predictions deviate from the actual values.

$$AE=|d-y|$$

2. **Relative Error:** Relative error is a normalized version of absolute error, expressing the error as a unit-less percentage relative to the desired output. This normalization is crucial because absolute error alone lacks context without considering the units involved.
   * Note: Relative error may not be representative for small values unless the desired output (d) is consistently greater than zero for all cases.

$$RE=\frac{|d-y|}{d}\cdot100\%$$

3. **Mean Absolute Percentage Error (MAPE):** MAPE calculates the average relative error across the entire testing set, consisting of n data records. It offers valuable insights when the underlying probability density distribution of values is significantly distant from zero, as it ensures zero does not disproportionately impact the result.

$$MAPE=\frac{1}{n}\sum_{i=1}^{n}\frac{|d_{i}-y_{i}|}{d_{i}}\cdot100\%$$

4. **Squared Error:** Squared error involves squaring the error, which helps in obtaining a positive quantity. It places more emphasis on larger error values, especially when they occur in certain records within the testing set. For instance, if there are two testing records (ε1 = 1 and ε2 = 2), squaring them (ε12 = 1 and ε22 = 4) assigns greater weight to the larger error ε2.

$$SE=(d-y)^{2}$$

5. **Mean Square Error (MSE):** MSE computes the average squared error over the entire testing set, comprising n data records. However, it can be sensitive to outliers, depending on the underlying probability density distribution.

$$MSE=\frac{1}{n}\sum_{i=1}^{n}(d_{i}-y_{i})^{2}$$

6. **Mean Absolute Error (MAE):** MAE, an alternative to MSE, is more robust when dealing with datasets containing outliers. It computes the average absolute error over the testing set and is less influenced by extreme values.

$$MAE=\frac{1}{n}\sum_{i=1}^{n}|d_{i}-y_{i}|$$

7. **Root Mean Square Error (RMSE):** RMSE is the square root of the mean squared error. This metric provides a result with a magnitude that is easier to interpret and is on the same scale as the desired and predicted outputs. It can facilitate better comprehension of the model's overall performance.

$$RMSE=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(d_{i}-y_{i})^{2}}$$

These evaluation metrics play a crucial role in assessing the accuracy and effectiveness of regression models, allowing practitioners to gauge how well their models approximate the desired outcomes and identify areas for improvement.

### 2.4.2 Business-Centric Evaluation: The Role of KPIs

Once the prediction model has undergone thorough evaluation using the previously mentioned metrics, it becomes ready for implementation to calculate the DSUC (Data Science Utility and Confidence) value for the relevant business problem. However, it's equally important for the end user, typically a decision-maker, to assess whether the DSUC value has been effectively integrated into their business processes. This assessment is achieved through a set of Key Performance Indicators (KPIs) designed to gauge the extent to which business objectives are being met. These KPIs often revolve around areas such as revenue improvement, cost reduction, efficiency enhancement, and customer satisfaction.

#### 2.4.2.1 Characteristics of Effective KPIs

For a KPI to serve as a valuable metric for evaluating business improvements and the attainment of business goals, it should exhibit the following characteristics:

* **Simplicity:** It should be easy to understand and straightforward to measure.
* **Measurability:** KPIs should consist of quantifiable elements, such as the number of daily operations, daily production volume, or employee workload.
* **Responsibility:** Each KPI should be assigned to the appropriate task manager or responsible party.
* **Sensitivity:** KPIs should be capable of indicating both positive and negative deviations from the business objectives.
* **Feasibility:** They should be achievable within the constraints of available resources, including staff, machinery, and processes.
* **Time-Bounded:** KPIs should have defined start and end dates for measurement.
* **Visibility:** KPIs should be visible and accessible throughout the entire organization, ensuring transparency.

#### 2.4.2.2 Examples of KPIs

Here are some examples of effective KPIs that are commonly implemented in organizations to measure DSUC performance:

* **Annual Growth/Shrinkage:** Measures the yearly growth or reduction in specific business metrics.
* **Task Completion Time:** Evaluates the time taken to complete specific tasks or projects.
* **Percentage of Timely Task Completion:** Tracks the percentage of tasks completed within predefined timeframes.
* **Service Delivery Cost:** Assesses the cost associated with delivering services.
* **Machine Downtime and Availability:** Monitors the downtime and availability of machinery or equipment.
* **Customer Complaints:** Measures the number of customer complaints received.
* **Staff Workload:** Evaluates the workload of employees or teams.
* **Revenue per Employee:** Calculates the revenue generated per employee.
* **Production Yield:** Assesses the output quality in terms of production.
* **Employee/Customer Satisfaction Index:** Gauges satisfaction levels among employees or customers.

Once a KPI is defined, it's essential to determine the most suitable method for assessing performance against it. Often, breaking down the assessment into smaller, manageable components and measuring them separately can provide valuable insights into the achievement of business objectives.

### 2.4.3 Cognitive Biases and Decision-Making Fallacies

Montibeller and Winterfeldt (2015, p.1230) highlighted that "\[b]ehavioral decision research has shown that both ordinary individuals and experts are susceptible to various biases in their judgments and decision-making." In the context of data science, cognitive and motivational biases can pose significant challenges not only during data collection but also at various stages of data processing. These biases can have a profound impact on the quality of prediction models developed from the data, ultimately leading to inaccurate decision-making. While it may be challenging to eliminate all biases, awareness of their existence empowers data scientists to account for them in their work and decision-making processes.

![Cognitive Bias](https://upload.wikimedia.org/wikipedia/commons/6/65/Cognitive\_bias\_codex\_en.svg)

* **Relevant cognitive biases**: The list provided below is for the common cognitive and motivationa

| Bias                         | Description                                                                                                                                    |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Anchoring                    | Occurs when the estimation of a numerical value is based on an initial value (anchor) and insufficiently adjusted to provide the final answer. |
| Affect-Influenced Bias       | Occurs when there is an emotional predisposition for or against a specific outcome or option that taints judgments.                            |
| Ambiguity Aversion           | People tend to prefer gambles with explicitly stated probabilities over gambles with diffuse or unspecified probabilities.                     |
| Equalizing Bias              | Occurs when decision makers allocate similar weights to all objectives.                                                                        |
| Confirmation Bias            | Occurs when there is a desire to confirm one's beliefs, leading to unconscious selectivity in the acquisition and use of evidence.             |
| Base Rate Fallacy            | People tend to ignore base rates when making probability judgments and rely instead on specific individuating information.                     |
| Desirability of Options      | This bias leads to over- or underestimating probabilities and consequences in a direction that favors a desired alternative.                   |
| Insensitivity to Sample Size | People tend to ignore sample size and consider extremes equally likely in small and large samples.                                             |

* **De-biasing techniques**: De-biasing techniques attempt to eliminate, or at least reduce, the effect of the cognitive and motivational biases and avoid any related strategy- and association-based errors.

| Bias                         | De-biasing Techniques                                                                                                                                                                                                                                                                                                                   |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anchoring                    | <ul><li>Avoid anchors when making estimates.</li><li>Provide multiple and counter anchors to prompt adjustments.</li><li>Use different experts who use different anchors to diversify perspectives.</li></ul>                                                                                                                           |
| Affect-Influenced Bias       | <ul><li>Avoid using emotionally loaded descriptions of consequences in the attributes.</li><li>Cross-check judgments with alternative elicitation protocols when eliciting value functions, weights, and probabilities.</li><li>Seek input from multiple experts with alternative points of view to counter emotional biases.</li></ul> |
| Ambiguity Aversion           | <ul><li>Model and quantify ambiguity as a probability distribution.</li><li>Represent ambiguity as parametric uncertainty, such as uncertainty over the bias parameter of a Bernoulli process or as a secondary probability distribution.</li></ul>                                                                                     |
| Equalizing Bias              | <ul><li>Rank events or objectives first and then assign ratio weights accordingly.</li><li>Elicit weights or probabilities hierarchically, considering the relative importance of each aspect.</li></ul>                                                                                                                                |
| Confirmation Bias            | <ul><li>Engage multiple experts with different points of view about hypotheses.</li><li>Challenge probability assessments with counterfactual scenarios to encourage a balanced perspective.</li><li>Probe for evidence that supports alternative hypotheses to reduce confirmation bias.</li></ul>                                     |
| Base Rate Fallacy            | <ul><li>Split the task into two parts: assess the base rates for the events and evaluate the likelihood or likelihood ratio of the data given the events separately. This separation helps prevent the neglect of base rates when making probability judgments.</li></ul>                                                               |
| Desirability of Options      | <ul><li>Utilize analysis involving multiple stakeholders providing different value perspectives to counter bias.</li><li>Involve multiple experts with diverse opinions to ensure balanced assessments.</li><li>Implement incentives and accountability measures to promote objective evaluations.</li></ul>                            |
| Insensitivity to Sample Size | <ul><li>Employ statistical methods to determine the probability of extreme outcomes in samples of varying sizes.</li><li>Use the sample data to illustrate why extreme statistics are logically less likely in larger samples, addressing the bias toward considering extremes equally likely across different sample sizes.</li></ul>  |
\n\n---\n\n## Navigation\n\n- **Parent**: [[data-science.iu-dlmbdsa01.use-cases-evaluation]]\n- **Course**: [[data-science.iu-dlmbdsa01]]\n