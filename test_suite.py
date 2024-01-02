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

if __name__ == '__main__':
    unittest.main()



class TestDnfCountFunction(unittest.TestCase):0

dnf_counter = 0
def test_dnf_count_1(self):
        # Create a sample results DataFrame for testing
        data = {'raceId': [1, 1, 1, 2, 2, 2],
                'statusId': [1, 11, 4, 12, 1, 3]}
        results_df = pd.DataFrame(data)

        # Test with a specific raceId (1 in this case)
        result = dnf_count(results_df, 1)

        # Assert that the result matches the expected value
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()