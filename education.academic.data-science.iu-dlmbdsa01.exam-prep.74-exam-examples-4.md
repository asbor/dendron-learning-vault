# 7.4 Exam Examples 4

In this test you will find 9 questions. Each question has a weight of 3 points, except for question 8 and 9 which have a weight of 6 and 18 points respectively. The maximum score is therefore 40 points. The minimum score to pass the exam is 24 points.

## Question 1

Which file is used for inter-applications communication at Google to transfer small structured data sizes across programs?

1. CSV
2. XML
3. PROTOBUF
4. JSON

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">3. PROTOBUF</mark>

**Context:**

Google Protocol Buffers (GPB) is a binary serialization format that allows you to define data structures in a language-neutral way. You can then use special generated source code to easily write and read your structured data to and from a variety of data streams and using a variety of languages. It is used for inter-applications communication at Google to transfer small structured data sizes across programs.

</details>

***

## Question 2

Which of these sentences is correct?

1. Outliers should be identified and removed from a dataset.
2. Outliers should be part of the test dataset but should not be present in the training data.
3. Outliers should be part of the training dataset but should not be present in the test data.
4. The nature of the problem determines how outliers are used.

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">4. The nature of the problem determines how outliers are used.</mark>

**Context:**

Outliers are extreme values that deviate from other observations on data, they may indicate a variability in a measurement, experimental errors or a novelty. Outliers can have a disproportionate effect on statistical analysis, such as the mean, which can lead to misleading results. They can also provide useful information about the data itself, such as the presence of a population variance. Therefore, the nature of the problem determines how outliers are used.

</details>

***

## Question 3

The idea of the auto-regressive model is that the current value of the dependent variable is a function of the …

1. past values of the dependent variable.
2. past values of the independent variables.
3. past values of external variables.
4. current values of the independent variables.

**(3 points)**

<details>

<summary>Answer</summary>

<mark style="color:green;">1. past values of the dependent variable.</mark>

**Context:**

In auto-regressive modeling, the current value of the dependent variable is primarily influenced by its own past values. This concept is fundamental to understanding and implementing auto-regressive models.

</details>

***

## Question 4

The model's evaluation metrics are important to measure …

1. how successfully the missing data values are estimated.
2. the accuracy of the developed prediction model.
3. how successfully the prediction model outputs are applied to improve business.
4. how successfully the relevant variables are selected.

**(3 points)**

<details>

<summary>Answer</summary>

<mark style="color:green;">2. the accuracy of the developed prediction model.</mark>

**Context:**

Evaluation metrics for prediction models are primarily used to assess the model's accuracy and effectiveness in making predictions. These metrics provide insights into how well the model's predictions align with the actual outcomes and are crucial for determining the model's reliability and performance.

</details>

***

## Question 5

Which of the following is utilized to calculate the weights values in a linear regression model?

1. The average value of each variable
2. Principal component analysis
3. The derivatives of the error term
4. The most noticed value of each variable

**(3 points)**

<details>

<summary>Answer</summary>

<mark style="color:green;">3. The derivatives of the error term</mark>

**Context:**

In linear regression, the weight values are determined through a process that involves minimizing the error between the model's predictions and the actual data. This process often relies on calculus, specifically the derivatives of the error term with respect to the model's weights, to find the optimal weight values that best fit the data.

</details>

***

## Question 6

Naïve Bayes approach assumes that the independent variables are …

1. aggregated variables.
2. random variables.
3. normalized variables.
4. decomposed variables.

**(3 points)**

<details>

<summary>Answer</summary>

<mark style="color:green;">2. random variables.</mark>

**Context:**

In Naïve Bayes, the independent variables are assumed to be random variables. This assumption is fundamental to the Naïve Bayes approach and is used to calculate the probability of a particular class given the values of the independent variables.

</details>

***

## Question 7

The computational complexity as well as the explanation offered by a genetic algorithm is largely determined by …

1. techniques used for crossover and mutation.
2. fitness function.
3. population of elements.
4. training data.

**(3 points)**

<details>

<summary>Answer</summary>

<mark style="color:green;">1. techniques used for crossover and mutation.</mark>

**Context:**

The crossover and mutation techniques used in a genetic algorithm are crucial for determining the algorithm's computational complexity and the explanation it offers. These techniques are used to generate new solutions from the existing ones and are fundamental to the genetic algorithm.

</details>

***

## Question 8

If the PACF plot cuts off sharply at lag k while there is a more gradual decay in the ACF plot beyond lag k, what should be the values of p and q in the developed ARIMA(p,1,q) model?

**(6 points)**

<details>

<summary>Answer</summary>

<mark style="color:green;">p=0 and q=k</mark>

**Context:**

In time series analysis and ARIMA modeling, the behavior of the Partial Autocorrelation function (PACF) and Autocorrelation Function (ACF) plots provides insights into the order of differencing (d) and the orders of autoregressive (AR) and moving average (MA) components. When the PACF plot exhibits a sharp cutoff at lag k, it suggests that there is a strong correlation with the past k lags but no correlation with lags beyond k. In this case, setting p (the AR order) to 0 and q (the MA order) to k is appropriate for the ARIMA(p,1,q) model, where d (the differencing order) is set to 1 to make the data stationary.



[5.7-Time-Series-With-ARIMA-Models.md](../5.-selected-mathematical-techniques/codes/05-time-series-forcasting/5.7-Time-Series-With-ARIMA-Models.md "mention")\




</details>

***

## Question 9

Mention six value propositions obtainable through applying data science to “fraud” linked use cases.

**(18 points)**

<details>

<summary>Answer</summary>

<mark style="color:green;">Applying data science use cases has many value propositions, for example:</mark>

1. <mark style="color:green;">Is someone accessing unauthorized data?</mark>
2. <mark style="color:green;">At which level is the fraud occuring?</mark>
3. <mark style="color:green;">From where are the hacking attempts originating?</mark>
4. <mark style="color:green;">Which kind of customer is targeted by fraud?</mark>
5. <mark style="color:green;">What customer behavior signals potential fraud?</mark>
6. <mark style="color:green;">Is this customer too high risk to service?</mark>

<mark style="color:green;">(3 points for each valid and related example, maximum 18 points)</mark>

</details>

***
\n\n---\n\n## Navigation\n\n- **Parent**: [[education.academic.data-science.iu-dlmbdsa01.exam-prep]]\n- **Course**: [[education.academic.data-science.iu-dlmbdsa01]]\n