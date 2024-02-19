import numpy as np
import pandas as pd

"""
    Create an 3x4 (3 rows x 4 columns) pandas DataFrame in which the columns are named Eleanor, Chidi, Tahani, and Jason. Populate each of the 12 cells in the DataFrame with a random integer between 0 and 100, inclusive.

    Output the following:
        the entire DataFrame
        the value in the cell of row #1 of the Eleanor column

    Create a fifth column named Janet, which is populated with the row-by-row sums of Tahani and Jason.

To complete this task, it helps to know the NumPy basics covered in the NumPy UltraQuick Tutorial. 
"""

#rows = np.array([np.random.randint(1,100,4),np.random.randint(1,100,4),np.random.randint(1,100,4)])
rows = np.random.randint(0,101,(3,4));
columns = ['Eleanor', 'Chidi', 'Tahani', 'Jason']
data_frame = pd.DataFrame(data=rows, columns=columns)

# Entire Frame is here
print("Entire DataFrame\n", data_frame)
# Row #1 is First Row 
print("\nRow #1\n", data_frame.iloc[[0]])

data_frame['Janet'] = data_frame['Tahani'] + data_frame['Jason']

print("\n", data_frame)
