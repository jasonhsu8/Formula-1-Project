import unittest
import pandas as pd
import numpy as np
import os
from myFunctions import read_data, dataset_folder_path, dnf_count, coef_linear_regression

class testFunction(unittest.TestCase):
    dataset_folder_path = 'Dataset/'
    
    def setUp(self):
        # Create the Dataset directory if it doesn't exist
        os.makedirs(self.dataset_folder_path, exist_ok=True)

    def tearDown(self):
        # Clean up the Dataset directory after the test
        os.rmdir(self.dataset_folder_path)

    def test_read_data(self):
        # Define a sample CSV file for testing
        sample_data = "sample.csv"
        sample_content = "column1,column2\nv1,v2"

        # Write the sample content to the file
        with open(f"{dataset_folder_path}{sample_data}", "w") as file:
            file.write(sample_content)

        # Call the function to read the data
        result_df = read_data(sample_data)

        # Define the expected DataFrame based on the sample content
        expected_df = pd.DataFrame({"column1": ["v1"], "column2": ["v2"]})

        # Compare the actual result with the expected DataFrame
        pd.testing.assert_frame_equal(result_df, expected_df)

        # Clean up the sample file after the test
        os.remove(f"{dataset_folder_path}{sample_data}")


class TestDnfCountFunction(unittest.TestCase):
    def test_dnf_count(self):
        # Create a sample results DataFrame for testing
        data = {'raceId': [1, 1, 1, 2, 2, 2, 3, 3, 3],
                'statusId': [1, 11, 4, 200, 200, 200, 14, 120, 122]}
        results_df = pd.DataFrame(data)

        # Test with a specific raceId
        # 1
        result1 = dnf_count(results_df, 1)
        # 2
        result2 = dnf_count(results_df, 2)
        # 3
        result3 = dnf_count(results_df, 3)

        # Assert that the result matches the expected value
        # result1
        self.assertEqual(result1, 1)
        # result2
        self.assertEqual(result2, 3)
        # result3
        self.assertEqual(result3, 0)

class TestCoefLinearReg(unittest.TestCase):
   def test_coef_linear_regression(self):
        # Test 1
        x1 = np.array([1, 2, 3, 4, 5])
        y1 = np.array([2, 4, 5, 4, 5])
        result1 = coef_linear_regression(x1, y1)
        print(result1)
        self.assertTrue(np.allclose(result1, (2.2, 0.6), atol=1e-2), f"Test 1 failed: {result1}")

        # Test 2
        x2 = np.array([0, 1, 2, 3, 4])
        y2 = np.array([1, 3, 7, 9, 11])
        result2 = coef_linear_regression(x2, y2)
        print(result2)
        self.assertTrue(np.allclose(result2, (1.0, 2.6), atol=1e-2), f"Test 2 failed: {result2}")


if __name__ == '__main__':
    unittest.main()

