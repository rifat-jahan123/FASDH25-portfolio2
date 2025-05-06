# FASDH25-portfolio2
A repository for students' portfolios for mini-project 2
 
#2A Use gazetteer and regex to extract places in Gaza from the corpus:

##imported the necesssary libraries

##defined the funnctions that writes a list of data into tsv file
##convert the list of rows into pandas dataframe and write to tsv

##defined the folder where the articles are located

##defined the path and loaded tsv from gazetteer

##setted a dictionary to store regex patterns for each place
##started with the main name (ascinames)
##added with alterante names
##create a regex pattern using alteration
##storing the compiled patterns and initial counts

##defiened the start date of the Gaza war

##looping through all the text files in the folder
##extracted data from filename
##reding the text content
##extracting months
##searched for pattern in text

##exported the tsv

##finalised the tsv file

#Task 2B.Place Name Extraction and Geocoding from Articles
This part involved extracting place names from a collection of articles, specifically from January 2024, using Natural Language Processing (NLP) techniques. After extraction, the project uses geocoding to find the coordinates of each place and compiles the data into a gazetteer.
Folder Structure
bash
Copy code
- 2b_task/
  - build_gazetteer.py                # Python script for geocoding the extracted place names
  - ner_counts.tsv                    # File containing extracted place names and their counts
  - ner_gazetteer.tsv                 # File with place names, their latitudes, and longitudes
  - README.md                         # The readme file describing the project
 
##	build_gazetteer.py: The Python script that fetches coordinates for each place name using the GeoNames API.
##	ner_counts.tsv: A tab-separated file containing place names from the articles and their occurrence counts.
##	ner_gazetteer.tsv: A tab-separated file with place names along with their corresponding latitude and longitude.
##	README.md: This file, explaining the project and its components.
# Use Stanza to Extract All Place Names from (Part of) the Corpus
The Stanza library was used because it is highly accurate for NER tasks, and it is capable of identifying a wide range of places, even those that might not strictly match a predefined gazetteer.
Key Points:
•	Advantages: Stanza is capable of handling ambiguous place names, and it can extract place names from different contexts, making it more versatile than traditional regex.
•	Disadvantages: Stanza can be slower for larger datasets and may still miss some place names or misclassify entities due to ambiguity in text.
# Create a Gazetteer for the NER Places
The next step was to create a gazetteer for the place names identified in Task 2B by geocoding each place name to obtain its geographical coordinates. This process involved the following steps:
1.	Geocoding the Place Names: The get_coordinates function was created to query the GeoNames API to find the latitude and longitude of each extracted place.
2.	Handling Missing Data: If no coordinates were found for a place, "NA" was recorded for both latitude and longitude.
3.	Storing the Results: The coordinates were stored in a new file called ner_gazetteer.tsv. This file contains the place names, their corresponding latitudes, and longitudes (or "NA" if no coordinates were found).
4.	Manual Lookups: For places where the geocoding API failed to return results, manual lookups were done using Google to find the coordinates. These were then added to the final gazetteer.
Key Points:
•	Geocoding with GeoNames: The GeoNames API was used for geocoding due to its wide coverage and accessibility. It allows for efficient retrieval of place coordinates.
•	Manual Lookups: Some place names could not be geocoded automatically, requiring manual lookups. These entries were marked with "NA" initially, and the missing data was updated after manual intervention.
Techniques Used
1. Stanza for Named Entity Recognition (NER)
Stanza's NER model was used for extracting place names from the articles. This approach is robust because Stanza's pre-trained models are capable of recognizing a wide variety of place names, even those with complex or ambiguous spellings.
2. GeoNames for Geocoding
For geocoding, the GeoNames API was used to retrieve the geographical coordinates (latitude and longitude) for each place name extracted from the articles. If the coordinates could not be found, "NA" was used as a placeholder. The geocoded data was saved in a gazetteer for future analysis.
Advantages and Disadvantages
Advantages of Stanza: It handles a variety of linguistic nuances and can detect a wide range of place names, even in complex sentences.
Disadvantages of Stanza: It can be computationally intensive and may sometimes misclassify entities, especially in cases of ambiguity.
Advantages of GeoNames: The API provides a reliable source of geospatial data, and it covers a wide range of places.
Disadvantages of GeoNames: It occasionally fails to locate coordinates for certain ambiguous or less common places.

##Manually added the coordinates of places names:
Zababdeh,Shujayea,Rafidiya,Philadelphia, Asiapacific 

##WRONGLY ADDED PLACE NAMES
There were names of the people which were in the list of places and also some names with a "@". I manually removed those and added the coordinates of the places only.
 
While the project achieved its goals, there are areas for improvement:
Accuracy: Some places may have been missed or misclassified, especially if they are ambiguous or non-standard.
Efficiency: The geocoding process could be optimized by handling retries more effectively for places that may have failed in the initial pass.
Manual Lookups: The reliance on manual lookups for some places is a weakness; automating this process with a more advanced geocoding service could improve the results.

#Map the NER-extracted placenames
## Load coordinates from geocoded gazetteer
## Clean column names
## Merge on the shared column: 'name' chatgpt solution-1
## Drop rows with missing data
## Create the static map
## Better map style with labels , chatgpt solution -2



## Set map style
 ## Save both formats #chatgpt-sol 3 

Conversation 3: 
I’ve finished creating my map, but now I want to save it. I want to save it in html and png format. how should i do it. dont give me the code just give me instructions
Great! Here are the steps to save your map in both **HTML** and **PNG** formats:

1. **Save as HTML**:
   Use your plotting library's built-in function to save the interactive version of the map as an HTML file. This version will let you zoom, pan, and hover over points. Choose a meaningful file name like `map_output.html`.

2. **Save as PNG**:
   To save a static image version, you'll usually need to use an export function that supports static rendering (some libraries may need additional setup like installing *kaleido* or *orca*). Make sure your map is properly zoomed and styled before exporting.

3. **Check your output folder**:
   Make sure both files were saved in your desired directory, and give them clear, related names (e.g., `map_output.html` and `map_output.png`).

4. **Test both files**:
   Open the HTML file in a browser to check interactivity, and open the PNG in an image viewer to confirm the appearance is correct.

Let me know what plotting library you're using (like Plotly or Folium), and I can tailor the steps if needed.

2.can i also use ner_map.png for  map_output.png

Yes, absolutely! You can name the file **`ner_map.png`** instead of `map_output.png` — the filename is completely up to you. Just make sure the name is:

* **Descriptive** (like `ner_map.png` if it's a Named Entity Recognition map),
* **Consistent** (use a similar name for the HTML version, like `ner_map.html`),
* And has the correct **file extension** (`.png` for the image, `.html` for the interactive version).

This makes your files easier to organize and understand later. Want help coming up with a good naming system for your project files?


#Map the regex-extracted placenames
##importing the necessary libraries
##loading the regex-extracted place frequencies with month
##Cleaning the column names (remove extra spaces)
##loading the coordinates
##coordinates_df = pd.read_csv(coordinates_path, sep="\t")

##print the dataframe
##print(coordinates_df)

##merging regex data with coordinates using the common column "asciiname"

##print(merged_df)
## Cleaning data (remove rows with missing lat, lon, or frequency) #chatgpt sol-4

## Check the merged dataframe for correctness
#print(merged_df.head())
  
## Creating animated map of all the place names

##  Setting map style 
## Save outputs

## Show the map
##fig.show()

