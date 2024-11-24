import pandas as pd
import os

# Load processed data
data = pd.read_csv('../data/processed_data.csv')

# Filter data for visualization
visualization_data = data[['FL_DATE', 'TEMPERATURE', 'WIND_SPEED', 'DEP_DELAY']]

# Define the output directory
output_dir = '../unity_project/Assets/Data'
output_file = os.path.join(output_dir, 'visualization_data.csv')

# Ensure the directory exists
os.makedirs(output_dir, exist_ok=True)

# Save the visualization data
visualization_data.to_csv(output_file, index=False)

print(f"Visualization data saved successfully to '{output_file}'.")
