import pandas as pd

# Load cleaned data
flight_data = pd.read_csv('../data/cleaned_flight_data.csv')
weather_data = pd.read_csv('../data/cleaned_weather_data.csv')

# Ensure date columns are properly converted to datetime
flight_data['FL_DATE'] = pd.to_datetime(flight_data['FL_DATE'], errors='coerce')  # Coerce invalid values to NaT
weather_data['DATE'] = pd.to_datetime(weather_data['DATE'], errors='coerce')

# Check for any invalid date entries
invalid_flight_dates = flight_data[flight_data['FL_DATE'].isna()]
invalid_weather_dates = weather_data[weather_data['DATE'].isna()]

if not invalid_flight_dates.empty or not invalid_weather_dates.empty:
    print("Invalid date entries found. Please review:")
    print("Invalid FL_DATE entries:", invalid_flight_dates)
    print("Invalid DATE entries:", invalid_weather_dates)
    exit()

# Merge datasets using nearest timestamp
merged_data = pd.merge_asof(
    flight_data.sort_values('FL_DATE'),
    weather_data.sort_values('DATE'),
    left_on='FL_DATE',
    right_on='DATE',
    direction='backward'
)

# Save merged data
merged_data.to_csv('../data/processed_data.csv', index=False)

print("Merged data saved successfully to '../data/processed_data.csv'.")
