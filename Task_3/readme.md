#  3. Regression on the tabular data

You have a dataset (*internship_train.csv*) that contains 53 anonymized features and a target column. 
Your task is to build model that predicts a target based on the proposed features. Please provide predictions for *internship_hidden_test.csv* file. 
Target metric is **RMSE**. The main goal is to provide github repository that contains:
* jupyter notebook with analysis
* code for modeling (Python 3)
* file with model predictions
* readme file
* requirements.txt file

## My solution

In 'Task_3.ipynb' I implemented analysis and modeling for the given data. Firstly, I checked for missing or duplicating values in the training data.  Then viewed statistics, heatmap, and correlation between features and target values. We have poorly correlated values, so I implemented Random Forest Regression because it showed the best value during the tests. You can find model predictions for the test data in 'model_predictions.csv'.
