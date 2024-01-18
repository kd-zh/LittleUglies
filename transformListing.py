import os
import ast
import pandas as pd

LISTING_NAMES_LIST = ['Name of pet:', 'Nickname of pet: (optional)', 'Colour:', 'Species:', 'Your main account:', 'Your name: (optional)', 'Blurb: (optional)']

# do something to transform the above, note what is optional and put down somewhere..

COLUMNS_LIST = ['Petname', 'Nickname', 'Colour', 'Species', 'Main', 'Owner', 'Blurb']
OPTIONAL_FIELDS_LIST = ["Nickname", "Owner", "Blurb"]

INPUT_TEXT_FILE = "Test1.txt"

try:
    with open(INPUT_TEXT_FILE, 'r') as file:
        listing = file.read()
        listingList = ast._splitlines_no_ff(listing)
        # testttt = ast.literal_eval(listing)
except FileNotFoundError:
    print(f"File not found: {listing}")
except Exception as e:
    print(f"An error occurred: {e}")
# Not a line input, need to do it by ":" or by COLUMNS_LIST

appendingData = []
for i, text in enumerate(listingList):
    # Split at the first ":" and drop
    splits = text.split(LISTING_NAMES_LIST[i])
    splits = splits.pop()
    # Clean new lines and spaces in front
    splits = splits.strip("\n")
    splits = splits.strip(" ")
    # eval(COLUMNS_LIST[i]) = splits
    appendingData.append(splits)
    print(splits)

# Keep if splitting by above does not work
# for item in listingList:
    # Split at the first ":" and drop
    # splits = text.split(":")
    # splits = splits.pop()
    # # Clean new lines and spaces in front
    # splits = splits.strip("\n")
    # splits = splits.strip(" ")
    # print(splits)

petname = "Tleilaxu"
nickname = "Lei"
colour = "Mutant"
species = "Ixi"
main = "Candy_Fizz"
owner = "Candy"
blurb = "Such a cute boy!"

# Path to the Excel file
excel_filename = "listings.xlsx"
excel_path = os.path.join(excel_filename)

 # Check if the file exists
if os.path.exists(excel_path):
    # Read the existing Excel file
    dfExisting = pd.read_excel(excel_path)
else:
    # Create a new DataFrame if the file does not exist
    dfExisting = pd.DataFrame(columns=COLUMNS_LIST)

if len(appendingData) == 0:
    appendingData = [petname, nickname, colour, species, main, owner, blurb]

# Append the new data
dfExisting.loc[len(dfExisting)] = appendingData

# Write the DataFrame back to Excel
dfExisting.to_excel(excel_path, index=False)
print(f"!!!!!!!! Excel file updated at {excel_path}")

