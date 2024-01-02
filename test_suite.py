import unittest
import pandas as pd
import os
from myFunctions import read_data, dataset_folder_path, dnf_count

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

if __name__ == '__main__':
    unittest.main()