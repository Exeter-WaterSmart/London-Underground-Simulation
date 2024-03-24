import json

# Load the Japan and London data
with open("japan_edges.geojson") as file:
    data_format_1 = json.load(file)

with open("london_edges.geojson") as file:
    data_format_2 = json.load(file)

# Replace coordinates in data_format_1 with those from data_format_2 for matching indices
for idx, feature in enumerate(data_format_1['features']):
    if idx < len(data_format_2['features']):
        feature['geometry']['coordinates'] = data_format_2['features'][idx]['geometry']['coordinates']

# Append the extra features from data_format_2 to data_format_1
if len(data_format_2['features']) > len(data_format_1['features']):
    extra_features = data_format_2['features'][len(data_format_1['features']):]
    data_format_1['features'].extend(extra_features)

# Output or save the modified data_format_1
with open("transformed_japan_edges_2.geojson", 'w') as file:
    json.dump(data_format_1, file, indent=2)
    
