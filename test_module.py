import unittest
import pandas as pd
from demographic_data_analyzer import (calculate_race, average_men_age, bachelor_percentage, advanced_education, without_advanced_education, minimum_hour, percentage_min_hour, percentage_highest_earning_country, most_popular_occupation)


class TestRaceStatistics(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv("adult.data.csv")

    def test_calculate_race(self):
        expected_series1 = pd.Series([27816, 3124, 1039, 311, 271], index=['White','Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'], name='Total')
        expected_series1.index.name = 'race'
        result_series = calculate_race(self.df)
        pd.testing.assert_series_equal(result_series, expected_series1)

        
class TestAgeAndEducationStatistics(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv("adult.data.csv")
       
    def test_average_men_age(self):
        mean = 39.4
        result_mean = average_men_age(self.df)
        self.assertAlmostEqual(result_mean, mean, places=1)
   
    def test_bachelor_percentage(self):
        percentage = 16.4
        result_percentage = bachelor_percentage(self.df)
        self.assertEqual(result_percentage, percentage)
    
    def test_advanced_education(self):
        percentage_4 = 46.5 
        result_percentage_4 = advanced_education(self.df)
        self.assertEqual(result_percentage_4, percentage_4)

    def test_without_advanced_education(self):
        percentage_5 = 17.4
        result_percentage_5 = without_advanced_education(self.df)
        self.assertEqual(result_percentage_5, percentage_5)

  
class TestWorkStatistics(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv("adult.data.csv")
   
    def test_minimum_hour(self):
        min_hour = 1
        result_min_hour = minimum_hour(self.df)
        self.assertEqual(result_min_hour, min_hour)

    def test_percentage_min_hour(self):
        minimum_percentage = 10.0
        result_minimum_percentage = percentage_min_hour(self.df)
        self.assertEqual(minimum_percentage, result_minimum_percentage)


class TestEarningAndOccupationStatistics(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv("adult.data.csv")

    def test_percentage_highest_earning_country(self):
        country, percentage = 'United-States', 91.46
        result_country, result_percentage = percentage_highest_earning_country(self.df)
        self.assertEqual((country, percentage), (result_country, result_percentage))

    def test_most_popular_occupation(self):
        occupation = "Prof-specialty"
        result_occupation = most_popular_occupation(self.df)
        self.assertEqual(occupation, result_occupation)

    
if __name__ == "__main__":
    unittest.main()
