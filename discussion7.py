import unittest
import os
import csv


def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    # use this 'full_path' variable as the file that you open
    d = {}
    with open(full_path, mode='r') as inFile:
        reader = csv.reader(inFile)
        headers = next(reader)

    # read the rest of the lines from the file handler
        for row in reader:
            if len(row) == 4: 
                month = row[0]  
                
                
                for i in range(1, len(headers)):  # Loop through each year starting from index 1
                    year = headers[i]  
                    if year not in d: 
                        d[year] = {}
                    d[year][month] = str(row[i])  # Assign the month value to the year dictionary

    return d 
                
        

def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
        max is the maximum value for a month in that year, month is the corresponding month

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        You'll have to change vals to int to compare them. 
    '''
    result = []  # List to store the resulting tuples
    
    # Iterate through each year and its corresponding month dictionary
    for year, months in d.items():
        max_month = max(months, key=months.get)  # Find the month with the maximum value
        max_value = int(months[max_month])  # Get the maximum value for that month
        result.append((year, max_month, max_value))  # Append a tuple (year, month, max_value)
    
    return result
    


def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    
    avg_d = {}
    for year, months in d.items():
        # Calculate the average value for the current year
        avg_value = sum(int(value) for value in months.values()) / len(months)
        # Store the rounded average in the dictionary
        avg_d[year] = round(avg_value)
    
    return avg_d


class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
