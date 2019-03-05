# Hierarchical-JSON-maker
A small python script that takes a csv file and converts it into a hierarchical JSON. 
The script is esentially a modified version of the Python script created by [hettmett](https://github.com/hettmett/csv_to_json), with the key difference being that the last column of the CSV file is instead put into an attribute of the final set of children. This was done for the purpose of using the scipt to create data visualizations structures based on hierarchical data such as sunburst or treemaps in modules such as D3.js. 

Example: I used data from [gapminder](https://www.gapminder.org/) to obtain some data about the world population in 2019 for a [small visualization project](https://github.com/wska/Sunburst-Population-Visualization). A small snippet of the CSV file after rearranging the columns could look like this:

~~~~
Root,Continent,Country,2019
The World,Asia,Afghanistan,37200000
The World,Europe,Albania,2940000
The World,Africa,Algeria,42700000
The World,Europe,Andorra,77100
The World,Africa,Angola,31800000
~~~~

Running it through the script 
~~~~
python jsonmaker.py example.csv > example.json
~~~~
outputs (though on a single line) the following in example.json:

~~~~
{"name": "The World", 
 "children": [
     {"name": "Africa", "children": [
         {"name": "Angola", "value": "31800000"}, 
         {"name": "Algeria", "value": "42700000"}]
     }, 

     {"name": "Asia", 
      "children": [
         {"name": "Afghanistan", "value": "37200000"}]
     },

     {"name": "Europe", 
      "children": [
         {"name": "Andorra", "value": "77100"}, 
         {"name": "Albania", "value": "2940000"}]
      }
    ]
}
~~~~
