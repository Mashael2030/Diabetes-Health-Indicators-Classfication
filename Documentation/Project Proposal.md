# Diabetes Health Indicators Classfication Model
![Diabetes-Care-Plan](https://user-images.githubusercontent.com/63130647/145462347-2a3806ba-5dd7-4f7f-ad80-8249ae28b1cd.jpg)

# Overview 
As one of the most prevalent chronic diseases in the United States, diabetes, especially type 2 diabetes, affects the health of millions of people and puts an enormous financial burden on the US economy. We aimed to develop predictive models to identify risk factors for type 2 diabetes, which could help facilitate early diagnosis and intervention and also reduce medical costs.

# Questions
#### Exploratory data analysis (EDA) :
1. What are the risk factors most predictive of diabetes risk?
2. What is the most age of infection with diabetes?
3. What most genders to have diabetes?
#### Modeling :
1. Classify the people who have diabetes, prediabetes or don't have diabetes?
2. The most important factors that refer to prediabetes?
3. The main factors that effect on diabetes?

# Needs 
This model helps public health officials and the community to absorb and  predict the risks of diabetes and also contribute to spreading health awareness to reduce it.

# Data Description
The dataset is provided in .csv format. It contains **254000 observation** , each has **22 features**. The most relevant feature to this project is the **Diabetes_012 (response)** 

| Feature               | Description                                                                     |
|-----------------------|---------------------------------------------------------------------------------|
| Diabetes_012          | 0 = no diabetes 1 = prediabetes 2 = diabetes.
| High blood pressure   | 0 = no high BP 1 = high BP.
| high cholesterol      | 0 = no high cholesterol 1 = high cholesterol.
| Cholesterol Check     | 0 = no cholesterol check in 5 years 1 = yes cholesterol check in 5 years.
| BMI                   | Body Mass Index.
| Smoker                | Have you smoked at least 100 cigarettes in your entire life? 0 = no 1 = yes.
| Stroke                | you had a stroke. 0 = no 1 = yes .
| HeartDiseaseorAttack  | coronary heart disease (CHD) or myocardial infarction (MI) 0 = no 1 = yes .
| PhysActivity          | physical activity in past 30 days - not including job 0 = no 1 = yes . 
| Fruits                |Consume Fruit 1 or more times per day 0 = no 1 = yes .
| Veggies               | Consume Vegetables 1 or more times per day 0 = no 1 = yes.
| HvyAlcoholConsump     | Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) 0 = no 1 = yes.
| AnyHealthcare         | Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc. 0 = no 1 = yes.
| NoDocbcCost           | Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? 0 = no 1 = yes.
| GenHlth               | Would you say that in general your health is: scale 1-5 1 = excellent 2 = very good 3 = good 4 = fair 5 = poor.
| MentHlth              | mental health scale , scale 1-30 days .
| PhysHlth              | Now thinking about your physical health , for how many days during the past 30 days was your physical health not good? scale 1-30 days .
| DiffWalk              | Do you have serious difficulty walking or climbing stairs? 0 = no 1 = yes.
| Sex                   | 0 = female 1 = male
| Age                   | 13-level age category (_AGEG5YR see codebook) 1 = 18-24 9 = 60-64 13 = 80 or older .
|Sex                    | 0 = female 1 = male.
|Education              |Education level (EDUCA see codebook) scale 1-6 1 = Never attended school or only kindergarten , 2 = Grades 1 through 8 (Elementary) ,3 = Grades 9                               throug 11 (Some high school), 4 = Grade 12 or GED (High school graduate) , 5 = College 1 year to 3 years (Some college or technical school) , 6 = College                         4 years or more (College graduate).   
| Income                | Income scale, scale 1-8 1 = less than $10,000 5 = less than $35,000 8 = $75,000 or more.

The data that will be used in this project has been downloaded from Kaggle (https://www.kaggle.com/alexteboul/diabetes-health-indicators-dataset).

# Tools
* **Technologies:** Python, Jupyter notebook.
* **Libraries:** NumPy, Pandas, Sklearn, Matplotlib, Seaborn, Plotly.
