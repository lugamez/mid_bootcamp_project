import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, cohen_kappa_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import scipy.stats as st
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency
import pickle
import os

def grouping_age(column: str) -> str:
    '''
    This function groups the categories in a column.
    Input: column -> str
    Output: Grouped categories in a column to reduce cardinality.
    '''
    age = {"18 to 29": ["18 to 24", "25 to 29"],
              "30 to 39": ["30 to 34", "35 to 39"],
              "40 to 49": ["40 to 44", "45 to 49"],
              "50 to 59": ["50 to 54", "55 to 59"],
              "60 to 69": ["60 to 64", "65 to 69"],
              "70 to 79": ["70 to 74", "75 to 79"],
                "80 or older": ["80 or older"]}
    new_age = [ key for key, value in age.items() if column in value ]
    
    return new_age[0]

def grouping_sleeping_hours(column: str) -> str:
    '''
    This function groups the categories in a column.
    Input: column -> str
    Output: Grouped categories in a column to reduce cardinality.
    '''
    hours = { "1 to 5": [1, 2, 3, 4, 5],
              "6 to 9": [6, 7, 8, 9],
              "10 to 15": [10, 11, 12, 13, 14, 15],
              "16 to 24": [16, 17, 18, 19, 20, 21, 22, 23, 24]}
    new_hours = [ key for key, value in hours.items() if column in value ]
    return new_hours[0]
def rename_values(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function picks a Pandas DataFrame and renames values for dataset consistency
    
    Inputs:
    df: Pandas DataFrame
    
    Outputs:
    Pandas DataFrame with corrected values
    '''
    
    df['state'].replace('Guam', 'Territory outside US', inplace=True)
    df['state'].replace('Puerto Rico', 'Territory outside US', inplace=True)
    df['state'].replace('Virgin Islands', 'Territory outside US', inplace=True)
    df['had_diabetes'].replace('No, pre-diabetes or borderline diabetes', 'No', inplace=True)
    df['had_diabetes'].replace('Yes, but only during pregnancy (female)', 'No', inplace=True)
    df['smoker_status'].replace('Current smoker - now smokes every day', 'Current smoker', inplace=True)
    df['smoker_status'].replace('Current smoker - now smokes some days', 'Current smoker', inplace=True)
    df['e_cigarette_usage'].replace('Never used e-cigarettes in my entire life', 'Never used', inplace=True)
    df['e_cigarette_usage'].replace('Not at all (right now)', 'Former user', inplace=True)
    df['e_cigarette_usage'].replace('Use them some days', 'Current user', inplace=True)
    df['e_cigarette_usage'].replace('Use them every day', 'Current user', inplace=True)
    df['covid_tested_positive'].replace('Tested positive using home test without a health professional', 'Yes', inplace=True)
    
    heart_data['age_category'] = heart_data['age_category'].apply(lambda x: x.replace('Age ', ''))
    
    return df

def chi2_all_columns(df: pd.DataFrame, target_column: str) -> pd.DataFrame:
    '''
    Apply chi2 test between the column we will want to predict and all other columns in the dataframe

    Input: df.DataFrame and the target column
    Output: df.DataFrame with the chi2 and p-values
    '''

    chi2_results = pd.DataFrame(columns = ['column', 'chi2', 'p-value'])

    for column in df.columns:
        if column != target_column:
            contingency_table = pd.crosstab(df[target_column], df[column])
            chi2, p, _, _ = chi2_contingency(contingency_table)
            result = pd.DataFrame({'column': [column], 'chi2': [chi2], 'p-value': [p]})
            chi2_results = pd.concat([chi2_results, result], ignore_index = True)

    return chi2_results

def hist_out_plot(df: pd.DataFrame, column: str) -> None:
    '''
    This function plots two types of graphs for the same column, in a way one can compare them: one can see
    the quartiles, means, and outliers due to their shared x-axis. 
    Input: pd.DataFrame
    Output: Boxplot and histogram for each column. 
    '''

    fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
    sns.boxplot(data=df, x=column, ax=ax_box)
    sns.histplot(data=df, x=column, ax=ax_hist)
    plt.show()

def change_binary(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function changes the column value to a numerical one based on the type of value.
    Input: the df: pd.DataFrame and the column to be changed in this df 
    Output: pd.DataFrame with the changed column. 
    '''
    for column in df.columns:
        df[column] = df[column].apply(lambda x: 1 if x == 'Yes' else 0)
    return df

def metrics_report(y_test: list, y_test_pred: list) -> pd.DataFrame:
    '''
    Function: Calculate the various metrics for a given set of test data prediction and 
    organises them into a dataframe for easier visualisation
    Inputs: y_test and y_test_pred
    Outputs: Dataframe with metrics column for the test set 
    '''
    
    accuracy_test = accuracy_score(y_test,y_test_pred)
    precision_test = precision_score(y_test,y_test_pred)
    recall_test = recall_score(y_test,y_test_pred)
    F1_test = f1_score(y_test,y_test_pred)
    Kappa_test = cohen_kappa_score(y_test,y_test_pred)
    

    results = {"Metric": ['accuracy', 'precision', 'recall', 'F1', 'Kappa'], 
               "Test":  [accuracy_test, precision_test, recall_test, F1_test, Kappa_test]}

    results_df = pd.DataFrame(results)

    return results_df

def cm_matrix(y_test_list) -> None:
    '''
    This function creates confusion matrix for all the y_test and their predictions given in a list.
    Input: List
    Output: Confusion Matrix for each element of the list. 
    '''
      
    for element in y_test_list:
        cm_test = confusion_matrix(element[0], element[1])
        disp = ConfusionMatrixDisplay(confusion_matrix = cm_test, display_labels = lr.classes_)
        disp.plot()
        plt.show()