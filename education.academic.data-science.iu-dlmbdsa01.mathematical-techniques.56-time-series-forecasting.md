# 5.6 Time-Series Forecasting

{% embed url="https://www.youtube.com/playlist?list=PLjwX9KFWtvNnOc4HtsvaDf1XYG3O5bv5s" %}

Many businesses place great emphasis on developing forecasting models for time-series data. These models provide valuable insights and allow organizations to estimate future performance, helping them anticipate and address potential issues. Time-series data, which involves observations recorded over time, often requires predictive analysis and the application of forecasting models. Examples of such data include stock prices, sales figures, traffic flow, and petroleum production.

![Time-Series-Data Example: U.S. Petrolium Products Trade](assets/images/data-science/iu-dlmbdsa01/Time-Series-Data-Example-US-Petrolium-Products-Trade.png)

When analyzing time-series data, it's essential to look for trends, whether the observations consistently increase or decrease over time, identify recurring patterns, and spot any outliers within the data.

In time-series forecasting, we utilize observed input and output instances ($$t_1, t_2, …, t_n$$, $$y_1, y_2, …, y_n$$) to predict the expected output sequence ($$y_{n+1}, y_{n+2}, …$$), without having knowledge of the expected input instances ($$t_{n+1}, t_{n+2}, …$$). One critical distinction between time-series forecasting and basic regression analysis lies in the fact that individual data records are dependent (to some extent) on previous records. This means that each data point relies on its historical context, and any forecasting technique must account for this. Therefore, proper time ordering of observations is essential.

A widely used linear forecasting technique is the autoregressive method (AR), which assumes that the expected output is a linear function of past outputs. However, if the underlying relationship is nonlinear, the AR approach may produce suboptimal results. To address this limitation and achieve better accuracy with nonlinear data, the autoregressive method can be enhanced by incorporating moving average terms, leading to the autoregressive moving average (ARMA) model, and integrating terms, resulting in the autoregressive integrated moving average (ARIMA) model. These extensions are designed to better capture and forecast the complex dynamics of time-series data.

***

## 5.6.1 Concept of Stationary

{% embed url="https://www.youtube.com/watch?index=4&list=PLjwX9KFWtvNnOc4HtsvaDf1XYG3O5bv5s&v=aIdTGKjQWjA" %}
What is Stationarity
{% endembed %}

To apply a forecasting model to time-series data effectively, it's essential that the data exhibits stationarity over time. Stationary data is crucial because it allows the model to accurately predict future responses based on past data points. While most time-series data aren't inherently stationary, we can transform them into a stationary form using the differencing concept, denoted as $$(d_{\Delta_t})$$, which calculates the difference between every two data points with a time interval $$d_{\Delta_t}$$.

![Concept of Stationary](assets/images/data-science/iu-dlmbdsa01/Concept-of-Stationary.png)

Notably, there is an optimal value for $$\Delta_t$$ that results in a fully stationary time-series.

***

## 5.6.2 Auto-regressive (AR) Model

{% embed url="https://www.youtube.com/watch?v=Mc6sBAUdDP4" %}
What are Autoregressive (AR) Models
{% endembed %}

The auto-regressive model is a linear forecasting model designed to predict the value of an observation at the next time point using linear combinations of its past values. Essentially, it resembles a simple linear regression model, earning its name because it utilizes past values of the same variable (hence, "auto-regressive").

An AR(n) model denotes an auto-regressive model of order n, indicating that it uses the previous n observations (lag(n)) to predict the next observation. The formula is represented as:

$$y_t = p_0 + p_1y_{t-1} + p_2y_{t-2} + … + p_ny_{t-n} + \varepsilon_t$$

Where $${p_0, p_1, …, p_n}$$ are the model coefficients, $$ε_t$$ is a white noise term following a normal distribution with mean 0 and variance $$W N (0, σ^2)$$.

{% content-ref url="codes/05-time-series-forcasting/5.1-AutoregressiveExample.md" %}
[5.1-AutoregressiveExample.md](codes/05-time-series-forcasting/5.1-AutoregressiveExample.md)
{% endcontent-ref %}

***

## 5.6.3 Moving Average (MA) Model

{% embed url="https://www.youtube.com/watch?index=6&list=PLjwX9KFWtvNnOc4HtsvaDf1XYG3O5bv5s&v=zNLG8tsA_Go" %}
What are Moving Average (MA) Models
{% endembed %}

The moving average model predicts future observations based on a weighted sum of white noise error terms:

$$y_t = q_0ε_t + q_1ε_{t-1} + q_2ε_{t-2} + … + q_nε_{t-n}$$

Here, $${q_0, q_1, …, q_n}$$ are the model coefficients, and $$ε_t$$ represents white noise error terms following a normal distribution with mean 0 and variance $$σ^2$$.

{% content-ref url="codes/05-time-series-forcasting/5.2-MovingAverageExample.md" %}
[5.2-MovingAverageExample.md](codes/05-time-series-forcasting/5.2-MovingAverageExample.md)
{% endcontent-ref %}

***

## 5.6.4 Autocorrelation

Autocorrelation assesses the degree of correlation between a variable and its previous values, often referred to as lagged values. It helps us understand whether there is a linear relationship between the variable and its historical observations. The autocorrelation coefficient at a specific lag, denoted as lag(n), is computed using the formula:

$$ACF(n) = \frac{C(y_t, y_{t-n})}{\sqrt{V(y_t) \cdot V(y_{t-n})}}$$

Here's what each component represents:

* $$ACF(n)$$: The autocorrelation coefficient at lag(n).
* $$C(y_t, y_{t-n})$$: The covariance between the variable $$y_t$$ and its lagged value $$y_{t-n}$$.
* $$V(y_t)$$: The variance of the variable $$y_t$$.
* $$V(y_{t-n})$$: The variance of the lagged value $$y_{t-n}$$.

Autocorrelation values typically fall within the range of -1 to 1, where:

* A value of 1 indicates a perfect positive correlation (as $$n$$ increases, $$y_t$$ and $$y_{t-n}$$ move together perfectly).
* A value of -1 indicates a perfect negative correlation (as $$n$$ increases, $$y_t$$ and $$y_{t-n}$$ move in opposite directions perfectly).
* A value near 0 suggests little to no significant correlation (past values have little impact on the current value).

Autocorrelation is a valuable tool for understanding the temporal relationships within time-series data and is often used in the analysis and modeling of such data.

{% content-ref url="codes/05-time-series-forcasting/5.3-AutocorrelationExample.md" %}
[5.3-AutocorrelationExample.md](codes/05-time-series-forcasting/5.3-AutocorrelationExample.md)
{% endcontent-ref %}

***

## 5.6.5 Partial Autocorrelation

The Partial Autocorrelation Function (PACF) at lag(k) quantifies the correlation between $$y_t$$ and $$y_{t-k}$$ while excluding the influence of autocorrelations at lags 1 to (k-1). It is computed by solving a specific equation represented as a matrix equation:

$$
\begin{pmatrix} ACF(0) & ACF(1) & \cdots & ACF(k-1) \\ ACF(1) & ACF(0) & \cdots & ACF(k-2) \\ \vdots & \vdots & \ddots & \vdots \\ ACF(k-1) & ACF(k-2) & \cdots & ACF(0) \end{pmatrix} \begin{pmatrix} PACF_1 \\ PACF_2 \\ \vdots \\ PACF_k \end{pmatrix} = \begin{pmatrix} ACF(1) \\ ACF(2) \\ \vdots \\ ACF(k) \end{pmatrix}
$$

In this equation:

* ACF(0), ACF(1), ..., ACF(k) represent the autocorrelation coefficients at various lags.
* PACF\_1, PACF\_2, ..., PACF\_k represent the partial autocorrelation coefficients at lags 1 to k.

The PACF at lag(k) is obtained by solving this matrix equation. It provides valuable information about the direct relationship between $$y_t$$ and $$y_{t-k}$$ while removing the indirect influence of autocorrelations at shorter lags.

{% content-ref url="codes/05-time-series-forcasting/5.4-PartialAutocorrelation.md" %}
[5.4-PartialAutocorrelation.md](codes/05-time-series-forcasting/5.4-PartialAutocorrelation.md)
{% endcontent-ref %}

***

## 5.6.6 Auto Regressive Integrated Moving Average (ARIMA) Model

{% embed url="https://www.youtube.com/watch?index=7&list=PLjwX9KFWtvNnOc4HtsvaDf1XYG3O5bv5s&v=dXND1OEBABI" %}
What are ARIMA Models
{% endembed %}

ARIMA models combine autoregressive (AR) and moving average (MA) components with integrated parameters to analyze and forecast time-series data. The integrated parameter, denoted as (d), represents the number of differencing operations required to make the dataset stationary. An ARIMA model is represented as ARIMA(p, d, q), where:

* p: The number of autoregressive terms.
* d: The degree of differencing.
* q: The number of moving average terms.

The choice of p, d, and q values depends on analyzing autocorrelation and partial autocorrelation plots of the time-series data. Various rules are used to determine these values based on the behavior of these plots.

{% content-ref url="codes/05-time-series-forcasting/5.5-AutoregressiveIntegratedMovingAverageModel.md" %}
[5.5-AutoregressiveIntegratedMovingAverageModel.md](codes/05-time-series-forcasting/5.5-AutoregressiveIntegratedMovingAverageModel.md)
{% endcontent-ref %}

***

## 5.6.7 Seasonal Autoregressive Integrated Model (SARIMA)

{% embed url="https://www.youtube.com/watch?v=IK67f3IItfw" %}
What are Seasonal ARIMA Models
{% endembed %}

ARIMA models are inadequate for handling time-series data with seasonal patterns. For such datasets, the seasonal autoregressive integrated model (SARIMA) is employed. SARIMA is represented as SARIMA(p, d, q)(P, D, Q)s, where (p, d, q) represent the nonseasonal components similar to ARIMA, and (P, D, Q) represent the seasonal components, with s denoting the seasonal period. SARIMA is used to model and forecast cyclical, repeating time-series data, which exhibit seasonal patterns that repeat after a specific period. SARIMA extends the ARIMA model to address these seasonal components and offers valuable forecasting capabilities.

{% content-ref url="codes/05-time-series-forcasting/5.6-SeasonalAutoregressiveIntegratedModel.md" %}
[5.6-SeasonalAutoregressiveIntegratedModel.md](codes/05-time-series-forcasting/5.6-SeasonalAutoregressiveIntegratedModel.md)
{% endcontent-ref %}

***
\n\n---\n\n## Navigation\n\n- **Parent**: [[education.academic.data-science.iu-dlmbdsa01.mathematical-techniques]]\n- **Course**: [[education.academic.data-science.iu-dlmbdsa01]]\n