# 2.2 Data Science Use Cases (DSUCs)

### 2.3.1 Identifying DSUCs and Their Value Propositions

Unlocking a business's true potential requires a thorough exploration of its data. This involves not only effectively managing the data but also pinpointing the right **Data Science Use Case (DSUC)** that aligns with the organization's goals. When chosen wisely, a DSUC can provide valuable insights for tackling business challenges and enhancing future success.

DSUCs, which employ predictive techniques to extract value from data, can vary significantly from one organization to another. However, in general, the identification of a DSUC in any business revolves around three key aspects: the value it brings, the effort required, and the associated risks. Managers typically evaluate new projects based on their potential to enhance operational efficiency or the bottom line. Consequently, when analyzing a business, the focus should be on increasing profits, reducing risks, and minimizing effort.

![Identification of an Organization's Use Cases](assets/images/data-science/iu-dlmbdsa01/IdentificationOfOrganizationsUseCases.png)

Every organization must identify the specific use cases they aim to address and ensure that the necessary datasets are accessible. Additionally, they should address the following critical questions:

1. **Value Assessment:** What is the worth of the insights gained from utilizing data science tools on the dataset? In other words, what benefits will the organization derive from this data analysis?
2. **Dataset Understanding:** What insights will be gained about the dataset itself? This involves understanding the data's characteristics, patterns, and anomalies.
3. **Hypothesis Testing:** What insights will be gained about the hypotheses that data science tools will investigate? This pertains to the specific questions or assumptions the analysis seeks to confirm or refute.
4. **Business Impact:** What is the significance of the knowledge gained if the prediction model yields positive business performance? Conversely, what are the implications if it results in a negative business outcome?

For most organizations, the value propositions of employing data science tools can typically be summarized using three key metrics, as outlined by Datameer in 2016.

![Value Propositions in Customer-Related DSUCs](assets/images/data-science/iu-dlmbdsa01/ValuePropositionsInCSUCs.png)

![Value Propositions in Operational-Related DSUCs](assets/images/data-science/iu-dlmbdsa01/ValuePropositionInOperationalDSUCs.png)

![Value Propositions in Fraud-Related DSUCs](assets/images/data-science/iu-dlmbdsa01/ValuePropositionsInFraudDSUCs.png)

### 2.3.2 Learning the Dataset and Building the Prediction Modelor

1. **Data Collection**: When identifying a Data Science Use Case (DSUC), the first step is to gather the relevant dataset. This dataset can come from various sources, including internal and external databases, sensor data, static files, and web scraping. It's important to note that this process can be expensive, especially if human intervention is required to add tags, labels, or comments to the data.
2. **Data Preprocessing**: After collecting the data, it goes through a preprocessing phase. During this stage, we clean the data by removing noise, redundant records, and handling missing values. This often requires domain knowledge to make informed decisions. By the end of preprocessing, the dataset is refined, removing misleading information and reducing its size. It may contain various types of variables, such as numerical, categorical, and textual values. Careful feature selection is essential to ensure that the chosen variables are relevant to the DSUC.
3. **Model Building**: With the prepared data, the next step is to build a prediction model. The goal is to establish mathematical relationships between the input features and the DSUC output values. This is done by defining mathematical functions that connect inputs to outputs. Typically, the dataset is divided into a training set for model building and a testing set to assess the model's accuracy. The developed model can not only provide current DSUC values but also predict them for new scenarios with different data records. It's important to note that the model may need updates if the dataset changes or new data records are introduced.
4. **Approaches**: There are various numerical approaches, particularly machine learning techniques, for constructing prediction models from datasets. The choice of approach depends on the nature of the dataset's outputs. Classification approaches are used when categorizing outputs into classes (e.g., "sunny" or "windy" for weather datasets), while regression approaches are employed when dealing with probability density distributions (e.g., "profits" for customer purchasing datasets).

### 2.3.3 Making Predictions and Decisions

Certainlhere's a clearer

1. **Model Building and Iteration**: Once the prediction model is constructed, it aims to establish the relationship between selected data features (inputs) and the objective DSUC value (output). The model may need multiple iterations to achieve a high level of accuracy with the testing set. The output of the model can be a probability (for classification) or a probability density distribution, along with a degree of uncertainty (for regression).
2. **Thresholds and Accuracy**: For classification models, determining accuracy involves setting a threshold (e.g., flagging transactions with a probability over 80% as fraud). In regression, finding an optimal point estimator from the predicted probability distribution is key (e.g., ensuring the error between predicted and target output is less than 5%).
3. **End-User Presentation**: The DSUC value is presented to the end user, such as a manager, who decides on appropriate actions or decisions. Sometimes, the model itself is presented, and the user interprets probabilities and thresholds. Therefore, a user-friendly front-end interface is crucial. End users align the model's outputs with business objectives and project goals, making trade-offs, like accepting higher false positives for fewer false negatives.
4. **Threshold Choices**: For instance, in fraud analysis, model outputs are fraud probabilities. Deciding on the threshold is strategic—low thresholds identify more false fraud cases, high thresholds miss real fraud. The choice depends on the specific use case.
5. **Impact on Data Records**: In some cases, end user decisions affect data records. For instance, if product prices change, the model should accommodate such changes with a feedback loop for retraining.
6. **Automation**: The ultimate goal is to automate end users' decisions based on the model's confidence. For instance, a model predicting hotel review authenticity could automatically accept or reject reviews when confident, reducing the need for user intervention.

This approach ensures that the model's outputs align with business needs and adapts to changing conditions, ultimately enhancing decision-making efficiency.

### 2.3.4 Machine Learning Canvas

![Machine Learning Canvas](assets/images/data-science/iu-dlmbdsa01/MachineLearningCanvas.png)

![Using the Machine Learning Canvas for Real Estate Deals](assets/images/data-science/iu-dlmbdsa01/UsingTheMachineLearningCanvas.png)

The tool collects in one place all the steps required to identify a use case and achieve its value proposition. For example, we can use the machine learning canvas in the case of real estate deals. Our value proposition is to make more lucrative real estate investments by comparing the price predictions for properties with their actual asking prices in order to identify the best deals. The procedure of the analysis using Dorard’s machine learning canvas is summarized in the following figure.
\n\n---\n\n## Navigation\n\n- **Parent**: [[education.academic.data-science.iu-dlmbdsa01.use-cases-evaluation]]\n- **Course**: [[education.academic.data-science.iu-dlmbdsa01]]\n