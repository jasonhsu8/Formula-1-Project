Test Suite for myFunctions.py Module
=====================================
This text file is a documentation for all the unit test done on the functions in myFunctions.py

------

Function 1: read_data(x)
=

Setup:
------
- Create the Dataset directory if it doesn't exist

Teardown:
---------
- Clean up the Dataset directory after the test

Test 1:
------
To test this function, a sample dataset is created with two columns with two inputs. The funciton is then called and put into a variable. Another variable is then defined as the expected DataFrame based on the sample content. The actual result of the function is then comapred with the expected result. If they both equate to the same exact thing, then the test has passed. The sample dataframe is then removed.

----------------------------------------------------------------------------------
- Input: 

        "column1": ["v1"], 
        "column2": ["v2"]

- Expected Output: 

        "column1": ["v1"], 
        "column2": ["v2"]

- Result: Pass

Dependencies:
-------------
- Python 3.7 or higher
- unittest library
- pandas library

Function 2: dnf_count(results_df, race_id_in_results)
=

Setup:
------
- A sample results DataFrame is created for testing. That is then read through pandas and put into a variable. 

------
Test 1: 
------
result1 is a variable that calls the function which uses the sameple DataFrame and test the raceId "1". It is then asserted that the result matches the expected value.

----------------------------------------------------------------------------------
- Input: 

        'raceId': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'statusId': [1, 11, 4, 200, 200, 200, 14, 120, 122]

- Expected Output: 

        1
- Result: Pass

Test 2: 
------
result2 is a variable that calls the function which uses the sameple DataFrame and test the raceId "2". It is then asserted that the result matches the expected value.

----------------------------------------------------------------------------------
- Input: 

        'raceId': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'statusId': [1, 11, 4, 200, 200, 200, 14, 120, 122]

- Expected Output: 

        3

- Result: Pass

Test 3: 
------
result3 is a variable that calls the function which uses the sameple DataFrame and test the raceId "3". It is then asserted that the result matches the expected value.

----------------------------------------------------------------------------------
- Input: 

        'raceId': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'statusId': [1, 11, 4, 200, 200, 200, 14, 120, 122]

- Expected Output: 

        0
- Result: Pass

Dependencies:
-------------
- Python 3.7 or higher
- unittest library
- pandas library




Function 3: coef_linear_regression(x,y) 
====

Setup:
------
- Create the sample x and y arrays

Test 1: 
------
There are two arrays, "x1" and "y1". The variable result1 calls the function using the "x1" and "y1". result1 is then compared to the expected result and this uses np.allclose with the parameter atol set to 0.01. So if the result is less than or equal to 0.01 of the expected result, then the test was pass. This is done as calculations could lead to long decimal places. 

----------------------------------------------------------------------------------
- Input:    

        x1 = np.array([1, 2, 3, 4, 5])
        y1 = np.array([2, 4, 5, 4, 5])

- Expected Output: 

        2.2, 0.6

- Result: Pass

Test 2: 
------
There are two arrays, "x2" and "y2". The variable result2 calls the function using the "x2" and "y2". result2 is then compared to the expected result and this uses np.allclose with the parameter atol set to 0.01. So if the result is less than or equal to 0.01 of the expected result, then the test was pass. This is done as calculations could lead to long decimal places. 

----------------------------------------------------------------------------------
- Input: 

        x2 = np.array([0, 1, 2, 3, 4])
        y2 = np.array([1, 3, 7, 9, 11])

- Expected Output: 

        1.0, 2.6

- Result: Pass

Dependencies:
-------------
- Python 3.7 or higher
- unittest library
- numpy library as np

Issues/Limitations:
--------------------
- if the mean of x equates to 0, the function would have to divide by 0 which is impossible. 



Function 4: correlation_coefficient(x,y)
=

Setup:
------
- Create the sample x and y arrays

Test 1: 
------
There are two arrays, "x1" and "y1". The variable result1 calls the function using the "x1" and "y1". result1 is then compared to the expected result and this uses np.allclose with the parameter atol set to 0.1. So if the result is less than or equal to 0.1 of the expected result, then the test was pass. This is done as calculations could lead to long decimal places. 

----------------------------------------------------------------------------------
- Input: 

        x1 = np.array([1, 2, 3, 4, 5])
        y1 = np.array([2, 4, 5, 4, 5])

- Expected Output: 

        0.8
- Result: Pass

Test 2: 
------
There are two arrays, "x2" and "y2". The variable result2 calls the function using the "x2" and "y2". result2 is then compared to the expected result and this uses np.allclose with the parameter atol set to 0.01. So if the result is less than or equal to 0.01 of the expected result, then the test was pass. This is done as calculations could lead to long decimal places. 

----------------------------------------------------------------------------------
- Input:

        x2 = np.array([0, 1, 2, 3, 4])
        y2 = np.array([1, 3, 7, 9, 11])

- Expected Output: 

        1.0

- Result: Pass

Dependencies:
-------------
- Python 3.7 or higher
- unittest library
- numpy library as np

Issues/Limitations:
--------------------
- If the mean of x and the mean of y both equate to 0, the function would have to divide by 0 which is impossible. 
- If the the x denominator in the calculation and the y denominator of the calculation both equate to 0, the function would have to divide by 0 which is impossible. 


Function 5: overtaking_count(laptimes, race_id)
=

Setup:
------
- A sample results DataFrame is created for testing. That is then read through pandas and put into a variable. 

Test 1: 
------
result is a variable that calls the function which uses the sameple DataFrame. It is then asserted that the result matches the expected value.

----------------------------------------------------------------------------------
- Input:
            
            'raceId': [1, 1, 1, 1, 2, 2, 2, 2],
            'driverId': [1, 2, 3, 4, 1, 2, 3, 4],
            'position': [1, 2, 3, 4, 4, 3, 2, 1]
            
- Expected Output: 

        2

- Result: Pass


Dependencies:
-------------
- Python 3.7 or higher
- unittest library
- pandas library

