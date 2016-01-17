# FundedProjectsKE
Web map visualizing donor and government funded projects in Kenya

## About
The map is based on [donor and government funded projects in Kenya](https://www.opendata.go.ke/-National-Accounts-And-Inflation/Donor-and-Government-funded-projects-map-2013-2015/5mtp-qs2h) data set and built using [Mapbox.js](https://www.mapbox.com/mapbox.js/) and [Leaflet.js]() plugins.

## Using this code
Download as zip and unzip or clone to your computer

## Approach taken
>#### 1. Getting data
To get the data into GeoJSON format to be used to map the projects, much cleaner and easier to work with JSON structure of the data was required. 
I decided to download the data as CSV and convert to JSON. The JSON generated is in js/projects.json
Then I used a python script to parse and generate the GeoJSON file from the projects json. The script ensures coordinates in the GeoJSON are floating point numbers since the ones provided are strings.

>#### 2. Displaying / Clustering markers
The map has a layerGroup in which other featureLayers are added or removed depending on what is to be displayed. 
I also tried loading the GeoJSON data when the map initially loads and reusing it to display the different layers a little faster. 

## Libraries, plugins and other code used in this project
> 1. jQuery
> 2. Mapbox + Leaflet js
> 3. Browserify
> 4. Bootstrap CSS

> ##### Code
1. [Python script to convert JSON to GeoJSON](http://gis.stackexchange.com/questions/73756/is-it-possible-to-convert-regular-json-to-geojson)
2. [Mapbox API](https://www.mapbox.com/mapbox.js/api/v2.2.4/)
3. [Mapbox Examples](https://www.mapbox.com/mapbox.js/example/v1.0.0/)

## Data Visualization
It'd be helpful if the data can be visualized as a heatmap of the status of projects so as to show which ones are stalling and which ones have been completed or are near completion in specific areas. 
