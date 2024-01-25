import pandas as pd


def calculate_race(input_df):
    series_1 = input_df['race'].value_counts()
    series_1.name = 'Total'
    return series_1


def average_men_age(input_df):
    df2 = input_df.set_index('sex')
    df2 = round(df2.groupby('sex')['age'].mean().reset_index(), 1)
    men_mean_age = df2.loc[df2['sex'] == 'Male', 'age'].iloc[0]
    return men_mean_age


def bachelor_percentage(input_df):
    df3 = round((input_df['education'].value_counts(normalize=True) * 100).reset_index(), 1)
    df3.columns = ['Education', 'Percentage']
    bachelors_percentage = df3.loc[df3['Education'] == 'Bachelors','Percentage'].iloc[0]
    return bachelors_percentage


def advanced_education(input_df):
    advanced_education = ['Masters', 'Bachelors', 'Doctorate']
    df4 = input_df[(input_df['education'].isin(advanced_education)) & (input_df['salary'] == '>50K')]
    total_advanced_education = input_df[input_df['education'].isin(advanced_education)].shape[0]
    percentage_advanced_education = round((df4.shape[0] / total_advanced_education * 100), 1)
    return percentage_advanced_education


def without_advanced_education(input_df):
    advanced_education = ['Masters', 'Bachelors', 'Doctorate']
    without_advanced_education = input_df[~input_df['education'].isin(advanced_education)]
    df5 = without_advanced_education[without_advanced_education['salary'] == '>50K']
    percentage_without_advanced_education = round((df5.shape[0] / without_advanced_education.shape[0] * 100), 1)
    return percentage_without_advanced_education


def minimum_hour(input_df):
    return input_df['hours-per-week'].min()


def percentage_min_hour(input_df):
    min_work_hour = input_df['hours-per-week'].min()
    total_minimum_salary = input_df[input_df['hours-per-week'] == min_work_hour]
    df7 = total_minimum_salary[total_minimum_salary['salary'] == '>50K']
    min_percentage = round((df7.shape[0] / total_minimum_salary.shape[0] * 100), 1)
    return min_percentage


def percentage_highest_earning_country(input_df):
    salary_50K = input_df.query('salary ==">50K"')
    highest_earning_country = salary_50K['native-country'].value_counts(normalize=True).idxmax()
    percentage_highest_earning_country = round((salary_50K['native-country'].value_counts(normalize=True).max() * 100), 2)
    return highest_earning_country, percentage_highest_earning_country

  
def most_popular_occupation(input_df):
    df9 = input_df.query('salary ==">50K" & `native-country`== "India" ')
    popular_occupation = df9['occupation'].value_counts(normalize=True).idxmax()
    return popular_occupation


def main():
    df = pd.read_csv("adult.data.csv") 

    # Question 1: How many people of each race are represented in this dataset?
    print(f"Number of each race:\n{calculate_race(df)}")

    # Question 2: What is the average age of men?
    print(f"Average age of men: {average_men_age(df)}%")

    # Question 3: What is the percentage of people who have a Bachelor's degree?
    print(f"Percentage with Bachelors degrees: {bachelor_percentage(df)}%")

    # Question 4: What percentage of people with advanced education (Bachelors,Masters,or Doctorate) make more than 50K?
    print(f"Percentage with higher education that earn >50K: {advanced_education(df)}%")

    # Question 5: What percentage of people without advanced education make more than 50K?
    print(f"Percentage without higher education that earn >50K: {without_advanced_education(df)}%")

    # Question 6: What is the minimum number of hours a person works per week?
    print(f"Min work time {minimum_hour(df)} hour")

    # Question 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    print(f"The percentage of people who work the minimum hours per week and have a salary of more than 50K is: {percentage_min_hour(df)}% ")

    # Question 8: What country has the highest percentage of people that earn >50K and what is that percentage?
    result_country, result_percentage = percentage_highest_earning_country(df)
    print(f"The country that has the highest percentage of people that earn >50K is: {result_country} with {result_percentage}%")

    # Question 9: Identify the most popular occupation for those who earn >50K in India.
    print(f"The most popular occupation for those who earn >50K in India is: {most_popular_occupation(df)}")

if __name__ == "__main__":
    main()