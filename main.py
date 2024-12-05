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

# Calculate the start date (current date minus 18 months)
end_date = datetime.now()
start_date = end_date - timedelta(days=18*30)  # Approximate 18 months

# Iterate over the date range
current_date = start_date
while current_date <= end_date:
    # Generate the file name
    file_name = f"BTC_USDT-Min5-{current_date.strftime('%Y-%m-%d')}.csv"
    file_path = os.path.join(save_dir, file_name)
    file_url = base_url + file_name

    # Check if the file already exists
    if os.path.exists(file_path):
        print(f"File {file_name} already exists, skipping download.")
    else:
        # Download the file
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {file_name}")
        else:
            print(f"Failed to download {file_name}")

    # Increment by one day
    current_date += timedelta(days=1)

print("All files downloaded.")