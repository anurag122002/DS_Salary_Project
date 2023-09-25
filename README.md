# Data Science Salary Estimator: Project Overview 

- Created a tool with the help of Ken Jee's Youtube walkthrough that estimates data_science salaries to help data scientists negotiate their income when they get a job. 
- Scraped over 500 job descriptions from glassdoor using python and selenium.
- Engineered features from the text of each job description to quantify the value companies put on python, sql, excel, spark, and aws.
- Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
- Built a client facing API using flask.

## Code and Resources used :-

1. **Python Version**: 3.10.13
2. **Packages**: Pandas, Numpy, Matplotlib, Seaborn, Selenium, Flask, Json, Pickle
3. **For Web Framework Requirements**: `pip install requirements.txt`
4. **Scraper Github**: https://github.com/arapfaik/scraping-glassdoor-selenium
5. **Scraper Article**: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
6. **Ken Jee's Github**: https://github.com/PlayingNumbers/ds_salary_proj
7. **Youtube Guide**: https://www.youtube.com/@KenJee_ds

## Web Scraping :-
**Tweaked both the github codes guides on scarping the webpages as the video was out back in 2020, therefore had to make contrasting changes in order for the code to work**
**Scraped about 500 jobpostings from glassdoor.com. With each job we got the following :-**

- Job Title
- Salary Estimate
- Job Description
- Rating
- Company
- Location
- Size
- Founded
- Type Of Ownership
- Industry
- Sector
- Revenue

## Data Cleaning

One of the most necessary steps in any Data Science related project. In this step I did took a lot of hints from the youtube video and Ken Jee's github, still needed to make a few tweaks to the code for it to run now. These are the following changes made:-

- Parsed numeric data out of salary
- Parsed rating out of company text
- Extracted Job State out of location
- Transformed founded date into age of company
- Made columns for if different skills were listed in the job description:
  - Python
  - Sql
  - excel
  - aws
  - spark

## Few Insights of EDA :-

![image](https://github.com/anurag122002/DS_Salary_Project/assets/111629651/80f0cce9-77cc-486d-9643-fe5934d26b8a)

![image](https://github.com/anurag122002/DS_Salary_Project/assets/111629651/a5a6f925-ca47-4efa-8d11-e2eb15d61610)

![image](https://github.com/anurag122002/DS_Salary_Project/assets/111629651/106c8747-03ee-4b81-8318-8f5759577a10)

## Model Building

First transforming the categorical varaibles into dummy variables. In the process, I got stuck as the dummy variables were coming out in boolean format, therefore had to change them first into 0/1 format. 

After that, I split the dataset into train and test with test being 20% of the size.

- Trained linear regression model first.
- Also, implemented L2 regualarization method as the increase in sparsity of the data due to presence of multiple dummy variables would have hindered the generalization ability of the model.
- Trained a Random Forest Regressor after that.

Finally evaluated the results from the models. Used MAE for the error evaluation, only coz its easy to interpret.

## Productionization

With the best model at hand, finally approached productionization. Shoutout to Ken Jee as his approach is the first I grasped in my journey of learning about deploying models. 

In this step, with the help of the youtube video I built a flask API endpoint that was hosted on a local webserver. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.
