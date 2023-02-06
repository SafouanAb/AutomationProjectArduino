import pandas as pd

# Define the data for the report
data = {
    'Test Case': ['Test Case 1', 'Test Case 2', 'Test Case 3'],
    'Result': ['Pass', 'Fail', 'Pass']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Generate the report
print('Test Report')
print(df)