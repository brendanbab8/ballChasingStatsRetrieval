# Ballchasing.com Group Stats Retrieval for user Bricks
Developer: Brendan Boyer

## Running the Script
1. Runs on Windows, no guarantees about Macs
2. You need Python 3.9.6 installed. Find the download link [here](https://www.python.org/downloads/).
3. Install XlsxWriter. Run from the command prompt: `pip install XlsxWriter`. <br>
  NOTE: There may be other dependency issues, depending on what's installed with Python. YMMV
4. After obtaining the source code, run this command from the command prompt: `py script.py`. You will need your API token from the site.

## Current Capabilities
1. Retrieves all groups created by Bricks and prints them to the command line.
2. Parses the group data to retrieve the group IDs.
3. Makes calls to retrieve group-specific stats via ID
4. Creates a Excel spreadsheet with a page per player in the teams requested.
5. Columns in the spreadsheet have titles.
6. Group metadata and core stats now populate.

### Known Errors and their Remedies
1. Permission Denied- This is probably due to you having the spreadsheet open. Close the spreadsheet and try again.
2. Extra Data Error- This is probably due to you pasting data using ctrl+v. Instead, paste your date by right-clicking in the command line.

### Note: If you modify the spreadsheet after the code runs, save it as a separate file with a different name. Otherwise, you will lose your modifications.
### Note: Let me know any errors/ issues you may have!