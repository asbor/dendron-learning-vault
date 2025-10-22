# 7.3 Exam Examples 3

## Question 1

In ARIMA(p,1,q), what are the values of q and p if there is a single positive spike at lag 1 in both the ACF and PACF plots?

1. Set q=1 and p=1
2. Set q=0 and p=0
3. Set q=0 and p=1
4. Set q=1 and p=0

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">3. Set q=0 and p=1</mark>

**Context**:

In time series analysis, the Autoregressive Integrated Moving Average (ARIMA) model is a widely used method for forecasting and modeling time series data. It consists of three main components:

* **p (Autoregressive Order)**: The number of lag observations included in the model. It represents the number of past time steps to consider for predicting the future value of the series. It is determined by observing the Partial Autocorrelation Function (PACF) plot.
* **d (Integrated Order)**: The number of differences needed to make the time series stationary. It represents how many times the data needs to be differenced to stabilize it. In your case, it's set to 1, indicating that you've already differenced the series once.
* **q (Moving Average Order)**: The order of the Moving Average (MA) component. It represents the number of lagged forecast errors included in the model. It is determined by observing the Autocorrelation Function (ACF) plot.

**Answer Explanation**:

In the given question, it's mentioned that there is a single positive spike at lag 1 in both the ACF and PACF plots. This situation suggests that there is a strong correlation between the current observation and the previous observation, which is indicative of an autoregressive order (p) of 1.

However, there is no significant spike at lag 1 in the ACF plot, which means there is no correlation between the current observation and the previous forecast errors. Therefore, the moving average order (q) is 0.

So, the correct answer is:

3. Set q=0 and p=1

See also:

[5.7-Time-Series-With-ARIMA-Models.md](../5.-selected-mathematical-techniques/codes/05-time-series-forcasting/5.7-Time-Series-With-ARIMA-Models.md "mention")

</details>

***

## Question 2

In ARIMA(p,1,q), what are the values of q and p if the ACF plot cuts of sharply at lag k, while there is more gradual decay in the PACF plot beyond lag k?

1. Set q=k and p=k
2. Set q-k and p=0
3. Set q=0 and p=k
4. Set q=0 and p=k-1

_**(3 points)**_

<details>

<summary>Answer</summary>

<mark style="color:green;">2. Set q-k and p=0</mark>

**Context**:

In the context of ARIMA (Autoregressive Integrated Moving Average) models, it's essential to understand the behavior of the Autocorrelation Function (ACF) and the Partial Autocorrelation Function (PACF) plots. These plots help determine the values of p (autoregressive order) and q (moving average order) for the ARIMA(p,1,q) model.

* **ACF (Autocorrelation Function)**: This plot shows the correlation between a time series and its lagged values. It helps identify the value of q in ARIMA(p,1,q). The ACF plot typically exhibits gradual decay if there is a moving average (MA) component.
* **PACF (Partial Autocorrelation Function)**: This plot shows the correlation between a time series and its lagged values while removing the influence of intermediate lags. It helps identify the value of p in ARIMA(p,1,q). The PACF plot is expected to cut off sharply if there is an autoregressive (AR) component.

**Answer Explanation**:

In the given question, it's stated that the ACF plot cuts off sharply at lag k, while there is more gradual decay in the PACF plot beyond lag k. This behavior suggests the following:

* A sharp cutoff in the PACF plot indicates an autoregressive (AR) process, suggesting an autoregressive order (p) of k.
* The gradual decay in the ACF plot suggests a moving average (MA) process, indicating a moving average order (q) of k.

So, the correct answer is:

* 2\. Set q=k and p=0

See also:

[5.7-Time-Series-With-ARIMA-Models.md](../5.-selected-mathematical-techniques/codes/05-time-series-forcasting/5.7-Time-Series-With-ARIMA-Models.md "mention")

</details>

***

\n\n---\n\n## Navigation\n\n- **Parent**: [[education.academic.data-science.iu-dlmbdsa01.exam-prep]]\n- **Course**: [[education.academic.data-science.iu-dlmbdsa01]]\n