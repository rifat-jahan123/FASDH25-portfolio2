#importing the necessary libraries
import re
import os
import pandas as pd


#defining the function that writes a list of data rows into a tsv file using pandas 
def write_tsv(rows, column_list, path):
    #convert the list of rows into pandas DataFrame and writing that to tsv
    df = pd.DataFrame(rows, columns=column_list)
    
    df.to_csv(path, sep="\t", index=False)


# Define the folder where the articles are located
folder = "../articles"

# Defining the path and loading the gazetteer from the tsv file
gazetteer_path = "../gazetteers/geonames_gaza_selection.tsv"
with open(gazetteer_path, encoding="utf-8") as file:
    data = file.read()

# Setting a dictionary to store regex patterns for each place
patterns = {}
rows = data.split("\n")

for row in rows[1:]:
    if not row.strip():  # Skip empty lines
        continue
    columns = row.split("\t")
    if len(columns) < 1:
        continue
    asciiname = columns[0].strip()
    alternate_names = columns[5].strip() if len(columns) > 5 else ""
    
    # Starting with the main name
    names = [asciiname]
    
    # Adding alternate names, if any
    if alternate_names:
        alternate_list = [name.strip() for name in alternate_names.split(",") if name.strip()]
        names.extend(alternate_list)

    # Creating regex pattern using alternation (|)
    regex_pattern = "|".join(re.escape(name) for name in names)

    # Storing the compiled pattern and initial count
    patterns[asciiname] = {"pattern": regex_pattern, "count": 0}

# Defining start date of Gaza war to filter articles
war_start_date = "2023-10-07"

# Dictionary to store counts by place and month
mentions_per_month = {}

# Looping through all text files in the folder
for filename in os.listdir(folder):
    if not filename.endswith(".txt"):
        continue

    # Extracting date from filename
    date_str = filename.split("_")[0]
    if date_str < war_start_date:
        continue

    file_path = os.path.join(folder, filename)

    # Reading the text content
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # Extracting months
    month_str = date_str[:7]

    # Searching each pattern in the text
    for place in patterns:
        pattern = patterns[place]["pattern"]
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        count = len(matches)

        if count > 0:
            patterns[place]["count"] += count

            if place not in mentions_per_month:
                mentions_per_month[place] = {}
            if month_str not in mentions_per_month[place]:
                mentions_per_month[place][month_str] = 0
            mentions_per_month[place][month_str] += count


# Preparing data for exporting to tsv
rows = []
for place in mentions_per_month:
    for month in mentions_per_month[place]:
        count = mentions_per_month[place][month]
        rows.append((place, month, count))

# Writing to final TSV file
write_tsv(rows, ["placename", "month", "count"], "regex_counts.tsv")
