import re
import csv
from helpscout.client import HelpScout

# Initialize HelpScout client
hs = HelpScout(app_id='{YOUR_APP_ID}', app_secret='{YOUR_APP_SECRET}')

# Function to fetch and process conversations
def fetch_conversations():
    with open('conversations_bodies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        for page in range(1, 100):  # Loop from page 1 to 100
            params = f'status=all&embed=threads&page={page}'
            conversations = hs.conversations.get(params=params)

            for data in conversations:
                # Ensure that data is converted to a string representation before using regex
                data_str = str(data)
                body_pattern = re.compile(r"'body': '([^']*)'")
                body_contents = body_pattern.findall(data_str)
                # Write the body contents to the CSV file
                csvwriter.writerow(body_contents)

# Call the function to fetch conversations
fetch_conversations()
