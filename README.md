# Mid bootcamp project - Women's health

# Purpose of the study

In the United States, heart disease takes the forefront as the leading cause of mortality. The likelihood of experiencing heart disease varies based on factors such as race, pre-existing health conditions, and daily habits. Delving into a specific segment of the population, women often find themselves overlooked by healthcare professionals when presenting suspicions of a heart attack at the emergency room, with a common misconception that men are more prone to such incidents. 
With this study, our aim was to gain insights into the overall health status of women and identify the factors contributing to their susceptibility to heart attacks. By acquiring this knowledge, healthcare workers can access more precise data regarding the current health landscape among women, while patients gain valuable insights into potential risks from pre-existing conditions or habits, enabling them to make informed choices about their health.

# Dataset selected

The dataset heart_2022_no_nans.csv was downloaded from Kaggle.com (https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease/data). It comes from the annual CDC survey and is a major part of the Behavioral Risk Factor Surveillance System (BRFSS), which conducts annual telephone surveys to collect data on the health status of U.S. residents. The CDC is the Center of Disease Control and Prevention and is one of the major operating components of the Department of Health and Human Services in the United States. Their main goal is the protection of public health and safety through the control and prevention of disease, injury, and disability in the US and worldwide.
	The dataset used in this analysis has 40 columns but some of them were dropped during the data cleaning process for the purpose of our study. In the end, 22 columns remained in our cleaned dataset and those are the following ones:

1. state: state of the respondent
2. sex: sex of the respondent
3. general_health: general health of the respondent based on own opinion
4. physical_activities: if the respondent practices physical activities
5. sleep_hours: how many hours does the respondent get in a period of 24 hours
6. had_heart_attack: if the respondent had a heart attack or not
7. had_angina: if the respondent had angina or not
8. had_stroke: if the respondent had a stroke or not
9. had_asthma: if the respondent suffered from asthma or not
10. had_skin_cancer: if the respondent suffered from skin cancer or not
11. had_copd: if the respondent suffered from COPD (Chronic obstructive pulmonary disease) or not
12. had_depressive_disorder: if the respondent suffered from a depressive disorder or not
13. had_kidney_disease: if the respondent suffered from a kidney disease or not
14. had_arthritis: if the respondent suffered from arthritis or not
15. had_diabetes: if the respondent suffered from diabetes or not
16. smoker_status: has the respondent ever smoked? If yes, what's the current consumption?
17. e-cigarette_usage: has the respondent ever used e-cigarettes? If yes, what's the current consumption?
18. race_ethnicity_category: in which race/ethnicity category the respondent identifies himself/herself
19. age_category: age of the respondent
20. bmi: body mass index of the respondent
21. alcohol_drinker: does the respondent drink alcohol?
22. covid_tested_positive: has the respondent ever tested positive for covid or not?
	

# Questions and findings

1. What's the overall health status of women in the US?

The less amount of hours women sleep, the poorer their general health is.
Most of the women consider their health to be very good. From this group, around 40k practice physical activities while 7k don't. Only a small portion consider their health as poor.
From women who drink alcohol, c.42% consider their health to be very good while only c.2% consider it to be poor. When talking about women that don't smoke, c.30% consider their health to be very good while 34% consider it only good.
Women that never smoked are said to have better health than those who are former and current smokers.

2. Which are the 3 most common health conditions that women affected by heart disease suffer from? 

The most common health conditions are:
Angina
Stroke
Diabetes

3. Among women, which ethnicity suffers more from a heart attack? And in which age range? 

From the dataset presented, the ethnicity that suffers the most from a heart attack are white women, non-hispanic in the range of 70 to 79 years old.* 

4. Are women who use e-cigarette more prone to suffer from a heart disease than those who don't use it? 

Yes. We reject the null hypothesis and confirm that women who use e-cigarette are more prone to suffer from a heart attack than those who don't use them.

5. Women from which states suffer the most of a heart attack? 

Women from the states of Washington, Ohio and Florida suffer the most from a heart attack.


# Next steps

Following a thorough analysis of the dataset and an examination of the relationships between its variables, we have derived valuable insights into the health conditions of women in the United States. However, our study revealed significant imbalances in data distribution across various health conditions and ethnic groups, introducing complexities to the project. Recognizing this challenge, we emphasize the importance of collecting data from a more homogenous group of individuals to enhance the accuracy of our conclusions. This step will contribute to a more robust and reliable foundation for future research endeavors.

# Limitations of the study*

The conclusions of this study are merely limited to the dataset used and they don't represent the full spectrum of the population in the US. Therefore, they should not be considered for medical references. This could clearly be seen in the conclusion from question 3) which aims to explain that white women suffer more from a heart attack than black women do, when in reality it's the opposite situation. The study threw this conclusion because the amount of women interviewed on it is bigger than the one represented by the black population. 


# List of references

1. American Heart Association Journals (2021), Volume Number(Issue Number), Page Range ( https://www.ahajournals.org/doi/10.1161/JAHA.121.024199)
2. Centers for Disease Control and Prevention (2020). Behavioral Risk Factor Surveillance System (BRFSS), Overview 2020 (https://www.cdc.gov/brfss/annual_data/2020/pdf/overview-2020-508.pdf)
3. Centers for Disease Control and Prevention. "Defining Adult Overweight and Obesity." (https://www.cdc.gov/obesity/basics/adult-defining.html#:~:text=If%20your%20BMI%20is%20less,falls%20within%20the%20obesity%20range)
4. CNN Health (2015). CNN (https://edition.cnn.com/2015/12/31/health/where-we-stand-now-e-cigarettes/index.html)
5. National Heart, Lung, and Blood Institute (n.d.). "Coronary Heart Disease in Women." (https://www.nhlbi.nih.gov/health/coronary-heart-disease/women)

