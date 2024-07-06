# helpscout-email-exporter

**Export the body of every thread & conversation to a CSV file.**

There is currently no feature to export conversation data directly from Helpscout or easily via their API.

## Getting Started
- Install Python3
- Add the following package `pip install python-helpscout-v2`
- Open `export.py` and on `line 6` add your credentials from a created Helpscout APP:
  
  ```
  hs = HelpScout(app_id='{YOUR_APP_ID}', app_secret='{YOUR_APP_SECRET}')
  ```
- In the terminal run `python3 export.py`
- CSV file will be generated within the folder
