# 1.4 Descriptive statistics

## 1.4 Descriptive statistics

$$Mean=\frac{Sum Of All Values}{Number Of Values}$$

$$Median=Middle Value$$

![Mean, Median, and Dataset](assets/images/data-science/iu-dlmbdsa01/mean\_median\_dataset\_line\_chart.png)

### 1.4.1 Probability Theory

Probability theory is the branch of mathematics concerned with probability. It is used to model random phenomena. It is also used to analyze the behavior of random variables. If an event is certain to happen, then its probability is 1. If an event is certain not to happen, then its probability is 0. If an event is neither certain to happen nor certain not to happen, then its probability is between 0 and 1. The probability of an event is the ratio of the number of favorable outcomes to the total number of possible outcomes.

**Mutually exclusive events** are events that cannot occur at the same time. For example, the events "heads" and "tails" are mutually exclusive. The probability of mutually exclusive events is the sum of their individual probabilities.

$$P(A\cup B)=P(A)+P(B)$$

**Independent events** are events that do not affect each other. For example, the events "heads" and "tails" are independent. The probability of independent events is the product of their individual probabilities.

$$P(A\cap B)=P(A)*P(B)$$

**Conditional probability** is the probability of an event given that another event has occurred. For example, the probability of getting a "heads" given that a "tails" has occurred is 1/2.

$$P(A|B)=\frac{P(A\cap B)}{P(B)}$$

**Probability density function** is a function that describes the probability of a random variable taking on a certain value. It is used to describe the probability distribution of a continuous random variable.

![Probability density function](assets/images/data-science/iu-dlmbdsa01/PropabilityDensityFunction.png)

**Cumulative distribution function** is a function that describes the probability of a random variable taking on a value less than or equal to a certain value. It is used to describe the probability distribution of a continuous random variable.

### 1.4.2 Probability Distributions

**Normal distribution** is a probability distribution that is symmetric about the mean. It is used to describe the distribution of a continuous random variable.

![Normal distribution](assets/images/data-science/iu-dlmbdsa01/NormalDistribution.png)

**Binomial distribution** is a probability distribution that describes the number of successes in a sequence of independent trials. It is used to describe the distribution of a discrete random variable.

![Binomial distribution](assets/images/data-science/iu-dlmbdsa01/BinomialDistribution.png)

**Poisson distribution** is a probability distribution that describes the number of events in a given time period. It is used to describe the distribution of a discrete random variable.

$$P(X)=\frac{e^{-\lambda}\lambda^x}{x!}$$

where:

* (P(X)) is the probability of X
* (e) is the base of the natural logarithm
* (λ) is the mean number of events in a given time period
* (x) is the number of events in a given time period
* (x!) is the factorial of x

Example:

if a call center receives an average of ten calls per day, what is the probability that in a given day the call center receives exactly seven calls?

$$P(7)=\frac{e^{-10}10^7}{7!}=0.090$$

![Poisson Distribution](assets/images/data-science/iu-dlmbdsa01/PoissonDistribution.png)

There are many processes which are considered Poisson processes, such as sales records, cosmic rays, and radioactive decay, because they are independent of each other and only one parameter is required (e.g., mean number of occurrences per time).

### 1.4.3 Bayesian Statistics

In general, the Bayes theorem is formulated using the following conditional probability equation for random events A and B:

$$P(A|B) = \frac{{P(B|A) \cdot P(A)}}{{P(B)}}$$

where:

* (P(A|B)) is the posterior probability
* (P(B|A)) is the likelihood
* (P(A)) is the prior probability
* (P(B)) is the marginal evidence or Normalization

Here, P(A) is called the “prior” and represents the strength of our belief in the occurrence of event A. This probability can have any value between 0 and 1. The likelihood,, represents the probability of observing B, given the occurrence of A. The evidence, P(B), represents the probability of the occurrence of all possible values of B, weighted by how strongly we believe in those particular values of B. Finally, is the “posterior belief” of variable A after observing the evidence B.

![Bayesian Statistics](assets/images/data-science/iu-dlmbdsa01/BayesianStatistics.png)

The Bayesian statistical method deduces how the prediction model will behave if a new data record or expert opinion is introduced. Bayesian statistics employs the Bayes theorem to reverse the direction of the dependencies, from the conditional probability of having a predicted output for a given data record, $$P(Output|Data)$$, to the probability of having a possible data record (e.g., new training set) for a predicted output, $$P(Output|Data)$$.

#### Example:

An example of Bayesian statistics is Helmenstine’s (2017) drug test analysis.

![Drug Testing Analyses Using Bayesian Statistics](assets/images/data-science/iu-dlmbdsa01/DrugTestingAnalysisBayesianStatistics.png)

In this example, shown in the related figure, ({U, \overline{U}, +, -}) stand for a drug user, non-user, positive drug test result, and negative drug test result, respectively. Assume 0.5% of the training set are drug users (P(U) = 0.5%) and the probability that a drug test will be positive when taken by a drug user is 99% (P(+|U)=99%) (meaning the test will be negative for (1%) of drug users (P(-|U)+1%). All other conditional probabilities are reported in the figure on drug testing analysis.

What will be the probability that a new data record (i.e., a new person added to the training set) with a positive drug test result is actually a drug user?

$$P(U|+)=\frac{P(+|U)P(U)}{P(+)}$$

$$P(U|+)=\frac{P(+|U)P(U)}{P(+|U)P(U)+P(+|\overline{U})P(\overline{U})}$$

$$P(U|+)=\frac{0.99 \cdot 0.005}{0.99 \cdot 0.005 + 0.01 \cdot 0.995} = 33.2\%$$

Since the probability is only 33.2%, it implies that even if a drug test produces a positive result, it is more likely the person is not a drug user. This result applies if we assume the person has the same prior probability as the general population (i.e., P(U) = 0.5%). However, if we know more about a specific person (e.g., used drugs in the past, has a medical condition that makes recreational drug use dangerous), the prior changes, as does the posterior prediction. Hence, knowledge of the posterior

is critical and represents our best knowledge. This is important because in machine learning, the training data represent our best knowledge about a dataset, and it is crucial to be certain that a dataset is as accurate as possible. This is why assurance of data quality is very important.

The drug test example shows how prior probability (P(U)) is adjusted according to the posterior probability (P(U|+)) defined by the model output (i.e., positive test result). This can be the result of designing a classifier to predict the occurrence of an output for a new training set. This is the main idea behind the Naïve Bayes classifier for categorical data of independent random variables.
\n\n---\n\n## Navigation\n\n- **Parent**: [[education.academic.data-science.iu-dlmbdsa01.introduction]]\n- **Course**: [[education.academic.data-science.iu-dlmbdsa01]]\n