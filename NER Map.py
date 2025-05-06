# Import necessary libraries
import pandas as pd
import plotly.express as px

# Load NER-extracted counts (January 2024)
ner_df = pd.read_csv("../ner_counts.tsv", sep="\t")
ner_df.columns = ner_df.columns.str.strip()

# Load coordinates from geocoded gazetteer
gazetteer_df = pd.read_csv("../NER_gazetteer.tsv", sep="\t")
gazetteer_df.columns = gazetteer_df.columns.str.strip()
# Clean column names
ner_df.columns = ner_df.columns.str.strip()
gazetteer_df.columns = gazetteer_df.columns.str.strip()
# Merge on the shared column: 'name' chatgpt sol-1
merged_df = pd.merge(ner_df, gazetteer_df, left_on="name", right_on="Name", how="inner")

 
# Drop rows with missing data
merged_df = merged_df.dropna(subset=["Latitude", "Longitude", "frequency"])

# Create the static map
fig = px.scatter_geo(
    merged_df,
    lat="Latitude",
    lon="Longitude",
    hover_name="name",
    text="name",
    size="frequency",

    color="frequency",
    zoom=5,
    height=600,
    color_continuous_scale=px.colors.sequential.YlOrRd,
    title="NER-Extracted Place Names (January 2024)"
)
# Better map style with labels
fig.update_layout(
    mapbox_style="carto-positron",
    margin={"r":0,"t":40,"l":0,"b":0}
)
# Set map style
fig.update_layout(mapbox_style="carto-positron-nolables")

 # Save both formats
fig.write_html("ner_map.html")
fig.write_image("ner_map.png", width=800, height=600, scale=2)   
