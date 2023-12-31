import unittest
import pandas as pd
from myFunctions import read_data, dataset_folder_path

class testFunction(unittest.TestCase):

    def test_read_data(self):
        # Define a sample CSV file for testing
        sample_data = "sample.csv"
        sample_content = "column1,column2\nvalue1,value2"

        # Write the sample content to the file
        with open(f"{dataset_folder_path}{sample_data}", "w") as file:
            file.write(sample_content)

        # Call the function to read the data
        result_df = read_data(sample_data)

        # Define the expected DataFrame based on the sample content
        expected_df = pd.DataFrame({"column1": ["value1"], "column2": ["value2"]})

        # Compare the actual result with the expected DataFrame
        pd.testing.assert_frame_equal(result_df, expected_df)

        # Clean up the sample file after the test
        import os
        os.remove(f"{dataset_folder_path}{sample_data}")

if __name__ == '__main__':
    unittest.main()
