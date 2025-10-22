# 5.5 Linear Regression

The goal of a regression model is to forecast the value of a dependent (target) variable in a new scenario based on other independent (predictor) variables and the historical behavior of the target variable in previous scenarios. The regression model provides a simplified representation of how data performs, relying on a fundamental modeling assumption. In linear regression, the primary assumption is that there are linear relationships among the data variables (as stated by Runkler in 2012). Constructing the model involves an iterative process to create a model that best explains the relationships between the independent and dependent variables. To assess the model's effectiveness, a validation step is crucial in determining how well the model aligns with the actual data records.

## 5.5.1 Linear Regression Model

Let’s assume we have a dataset with m variables $$[x_1, x_2, …, x_m]$$ and n data records $$(1, 2, …, n)$$.

**Example Dataset Table for Linear Regression:**\\

| i | $$x_1$$ | $$x_2$$ | … | $$x_m$$ | $$\hat{y}$$ |
| - | ------- | ------- | - | ------- | ----------- |
| 1 |         |         |   |         |             |
| 2 |         |         |   |         |             |
| … |         |         |   |         |             |
| n |         |         |   |         |             |

If a linear regression model has to be developed to predict the values of $$\hat{y}$$ (target variable) using the other variables $$[x_1, x_2, …, x_m]$$ (independent variables), this model is formed as:

$$\hat{y} = w_0 + w_1x_1 + w_2x_2 + … + w_mx_m$$

where $$w_0$$ is the bias and $$(w_1, w_2, …, w_m)$$ are the weights.

Unfortunately the output $$y$$ differs slightly from $$\hat{y}$$ by an error term $$\varepsilon$$ because in the input dataset there is not an exact linear relationship between the dependent variables and the target variable.

## 5.5.2 Simple Linear Regression Model

For a simple case of one independent variable $$x$$, the linear regression model will be written as in the following equation and schematically shown as in the succeeding figure:

$$y = w_0 + w_1x$$

![Simple Linear Regression Model](assets/images/data-science/iu-dlmbdsa01/Simple-Liniar-Regression-Model.png)

The bias $$w_0$$ represents the model intercept, and the weight $$w_1$$ represents the model slope. In such a scenario, the best model is the one which has the minimum error term values. Consequently, our task is to find the values of $$w_0$$ and $$w_1$$ which minimize the sum of the squared error $$\sum_{i=1}^{n} \varepsilon_i^2$$ (called the least-squares method). Mathematically, the error term has its minimum value at the instances where its derivative is zero

$$\frac{\partial}{\partial w_0} \sum_{i=1}^{n} \varepsilon_i^2 = 0$$

and

$$\frac{\partial}{\partial w_1} \sum_{i=1}^{n} \varepsilon_i^2 = 0$$

Therefore,

$$\sum_{i=1}^{n} \varepsilon_i^2 = \sum_{i=1}^{n} (y_i - \hat{y_i})^2 = \sum_{i=1}^{n} (y_i - w_0 - w_1x_i)^2$$

and

$$\frac{\partial}{\partial w_0} \sum_{i=1}^{n} \varepsilon_i^2 = 0$$

results in

$$2 \sum_{i=1}^{n} (\hat{y} - w_0 - w_1x_i) (-1) = 0$$

$$\sum_{i=1}^{n} (\hat{y} - w_0 - w_1x_i) = 0$$

$$w_0 = \frac{1}{n} \sum_{i=1}^{n} (\hat{y} - \frac{w_1}{n} \sum_{i=1}^{n} x_i)$$

and

$$\frac{\partial}{\partial w_1} \sum_{i=1}^{n} \varepsilon_i^2 = 0$$

results in

$$2 \sum_{i=1}^{n} (\hat{y} - w_0 - w_1x_i) (-x_i) = 0$$

$$-2 \sum_{i=1}^{n} (\hat{y}x_i +2w_0 \sum_{i=1}^{n} x_i + 2w_1 \sum_{i=1}^{n} x_i^2) = 0$$

$$-2 \sum_{i=1}^{n} \hat{y}x_i +2 \Bigg( \frac{1}{n} \sum_{i=1}^{n} (\hat{y} - \frac{w_1}{n} \sum_{i=1}^{n} x_i \Bigg) \sum_{i=1}^{n} x_i + 2w_1 \sum_{i=1}^{n} x_i^2 = 0$$

$$-2 \sum{x_i} \hat{y}x + \frac{2}{n} \sum_{i=1}^{n} \hat{y} \sum_{i=1}^{n} x_i - \frac{2 \cdot w_1}{n} \Bigg( \sum_{i=1}^{n} x_i \Bigg)^2 + 2w_1 \sum_{i=1}^{n} x_i^2 = 0$$

$$w_1 \Bigg ( \frac{-2}{n} \Bigg ( \sum_{i=1}^{n} x_i \Bigg )^2 + 2 \sum_{i=1}^{n} x_i^2 \Bigg ) = \frac{2}{n} \sum_{i=1}^{n} \hat{y}x - \frac{2}{n} \sum_{i=1}^{n} \hat{y} \sum_{i=1}^{n} x_i$$

$$w_1 = \cfrac{\sum_{i=1}^{n} \hat{y}x - \frac{1}{n} \sum_{i=1}^{n} \hat{y} \sum_{i=1}^{n} x_i}{\frac{-2}{n} \big ( \sum_{i=1}^{n} x_i \big )^2 + 2 \sum_{i=1}^{n} x_i^2}$$

The algorithm to construct the linear regression model which predicts a target variable (y) from the input data variables (x and ) can be concluded in the following steps:

1. Calculate w1:

$$w_1=\cfrac{\sum_{i=1}^{n} \hat{y}x - \frac{1}{n} \sum_{i=1}^{n} \hat{y} \sum_{i=1}^{n} x_i}{-\big ( \sum_{i=1}^{n} x_i \big )^2 + n \sum_{i=1}^{n} x_i^2}$$

2. Calculate w0:

$$w_0 = \frac{1}{n} \sum_{i=1}^{n} (\hat{y} - \frac{w_1}{n} \sum_{i=1}^{n} x_i)$$

3. Insert w1 and w0 into the linear model equation y = w0 + w1x
4. To use the developed model for forecasting the value of the target variable at a new data entry , substitute in the model equation $$\hat{y} = w_0 + w_1\hat{x}$$

### 5.5.2.1 Example: Simple Linear Regression Model

Develop a linear regression model to predict the revenue of a company in 2017, given its revenues from 2011 to 2015.

**Company Revenues:**

| x (year) | $$\hat{y}$$ (million USD) |
| -------- | ------------------------- |
| 2011     | 50                        |
| 2012     | 54                        |
| 2013     | 58                        |
| 2014     | 55                        |
| 2015     | 60                        |

First we calculate the following values:

$$\sum_{i=1}^{n} x, \sum_{i=1}^{n} x^2, \sum_{i=1}^{n} \hat{y}x, \sum_{i=1}^{n} \hat{y}$$

**Calculations:**

| x (year)                     | $$\hat{y}$$ (million USD)        | $$x^2$$                           | $$x\hat{y}$$                         |
| ---------------------------- | -------------------------------- | --------------------------------- | ------------------------------------ |
| 2011                         | 50                               | 4044121                           | 100550                               |
| 2012                         | 54                               | 4048144                           | 108648                               |
| 2013                         | 58                               | 4052169                           | 116754                               |
| 2014                         | 55                               | 4056196                           | 110770                               |
| 2015                         | 60                               | 4060225                           | 120900                               |
| $$\sum_{i=1}^{n} x = 10065$$ | $$\sum_{i=1}^{n} \hat{y} = 277$$ | $$\sum_{i=1}^{n} x^2 = 20260855$$ | $$\sum_{i=1}^{n} \hat{y}x = 557622$$ |

Then we calculate w1:

1. w1 =

$$\cfrac{n\sum_{i=1}^{n} \hat{y}x - \sum_{i=1}^{n} \hat{y} \sum_{i=1}^{n} x_i}{- \big(\sum_{i=1}^{n} x \big)^2 +n \sum_{i=1}^{n} x^2} = \cfrac{5.557622-277 \cdot 10065}{-(10065)^2+5 \cdot 20260855} = \cfrac{105}{50} = 2.1$$

2. Calculate w0:

$$w_0 = \frac{1}{n} \sum_{i=1}^{n} (\hat{y} - \frac{w_1}{n} \sum_{i=1}^{n} x_i) = \frac{1}{5} \sum_{i=1}^{5} (\hat{y} - \frac{2.1}{5} \cdot 10065) = \frac{1}{5} \cdot 277 - \frac{2.1}{5} \cdot 20130 = -4171.9$$

3. Insert w1 and w0 into the linear model equation:

$$\hat{y} = w_0 + w_1x = -4171.9 + 2.1x$$

4. At $$x = 2017$$, the revenue is predicted to be $$y = –4171.9 + 2.1 · 2017 = 63.8 millionUSD$$.

## 5.5.3 Multiple Linear Regression Model

In cases where a dataset involves more than one independent variable $$(x_1, x_2, … x_m)$$, the regression model is expanded to incorporate a term for each variable. This results in the general linear regression equation:

$$y = w_0 + w_1x_1 + w_2x_2 + … + w_mx_m$$

To determine the values of the weights $$(w_0, w_1, w_2, …, w_m)$$ that best fit the model to the data, we set the derivative of the error term with respect to each weight to zero. This involves equations like:

$$\frac{\partial}{\partial w_0} \sum_{i=1}^{n} \varepsilon_i^2 = 0$$

$$\frac{\partial}{\partial w_1} \sum_{i=1}^{n} \varepsilon_i^2 = 0$$

$$\vdots$$

$$\frac{\partial}{\partial w_m} \sum_{i=1}^{n} \varepsilon_i^2 = 0$$

These equations are solved to calculate the weights $$(w_0, w_1, w_2, …, w_m)$$. The values of these weights offer insights into the relationship between the target variable and each independent variable. For example, a large value for $$w_m$$ indicates a strong correlation between the target variable y and the variable $$x_m$$, and vice versa.

However, when dealing with datasets that contain numerous independent variables, the assumption of a linear relationship between the target variable and the other variables may become less valid. In such cases, nonlinear regression models are often better suited to provide more accurate predictions.

{% content-ref url="codes/04-LinearRegression/4.1-LinearRegression.md" %}
[4.1-LinearRegression.md](codes/04-LinearRegression/4.1-LinearRegression.md)
{% endcontent-ref %}

{% content-ref url="codes/04-LinearRegression/4.2-LinearRegression.md" %}
[4.2-LinearRegression.md](codes/04-LinearRegression/4.2-LinearRegression.md)
{% endcontent-ref %}

{% content-ref url="codes/04-LinearRegression/4.3-LiniarRegressionCompleteExample.md" %}
[4.3-LiniarRegressionCompleteExample.md](codes/04-LinearRegression/4.3-LiniarRegressionCompleteExample.md)
{% endcontent-ref %}
\n\n---\n\n## Navigation\n\n- **Parent**: [[data-science.iu-dlmbdsa01.mathematical-techniques]]\n- **Course**: [[data-science.iu-dlmbdsa01]]\n