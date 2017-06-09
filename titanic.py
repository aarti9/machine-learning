import numpy as np
import pandas as pd
from IPython.display import display

import visuals as vs

'''%matplotlib inline'''

in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

display(full_data.head())

outcomes = full_data['Survived']
data = full_data.drop('Survived', axis=1)

display(data.head())

def accuracy_score(truth, pred):
    if len(truth) == len(pred):
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    else:
        return "number of predictions does not match number of outcomes!"
    
predictions = pd.Series(np.ones(5, dtype=int))
print accuracy_score(outcomes[:5], predictions)

def predictions_3(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        # Remove the 'pass' statement below 
        # and write your prediction conditions here
        predictions.append((passenger['Sex']=='female' and (passenger['Parch'] == 0 
                                                            or passenger['SibSp'] <2 
                                                            or passenger['Pclass'] == 1                                                             
                                                           )
                                        
                           )or
                           (passenger['Sex']=='male' and  (passenger['Age'] < 5 )
                           )
                          )
    
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_3(data)