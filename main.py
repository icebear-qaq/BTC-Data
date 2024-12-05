import os
import requests
from datetime import datetime, timedelta

# Base URL
base_url = "https://d2s4an60yebwep.cloudfront.net/SPOT2/kline/2fb942154ef44a4ab2ef98c8afb6a4a7/daily/Min5/"

# Directory to save files
save_dir = "downloads"

# Create the save directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Function to input date range
def input_date(prompt):
    while True:
        try:
            date_str = input(prompt)
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

# Input start and end dates
start_date = input_date("Enter the start date (YYYY-MM-DD): ")
end_date = input_date("Enter the end date (YYYY-MM-DD): ")

# Ensure the start date is before or equal to the end date
if start_date > end_date:
    print("Start date must be before or equal to the end date.")
    exit()

# Iterate over the date range
current_date = start_date
while current_date <= end_date:
    # Generate file name
    file_name = f"BTC_USDT-Min5-{current_date.strftime('%Y-%m-%d')}.csv"
    file_url = base_url + file_name

    # Download the file
    response = requests.get(file_url)
    if response.status_code == 200:
        with open(os.path.join(save_dir, file_name), 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {file_name}")

    # Increment the date by one day
    current_date += timedelta(days=1)

print("All files downloaded.")