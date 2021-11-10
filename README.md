# hw_03
<b>This is a homework assignment for CSCI 40 class at Claremont McKenna College. Go to the [project page](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03) to learn more!</b>

The ```ebay-dl.py``` file converts Ebay's html files into JSON files. I also modified the ```ebay-dl.py``` file so it will also covert Ebay's html files into CSV files when adding ```--csv``` to the command line. For commands below, I only showed the first page results from Ebay using ```---num_pages=1```. 

# Commands to convert HTML files to JSON files
The commands below will convert HTML files to JSON files for search term ```chair```, ```iphone```, and ```phone case```. The default number of pages is 10, but I specified the number of pages using the flag ```--num_pages=1```.
```
python3 ebay-dl.py 'chair' --num_pages=1
```
```
python3 ebay-dl.py 'iphone' --num_pages=1
```
```
python3 ebay-dl.py 'phone case' --num_pages=1
```
# Default number of pages
```
python3 ebay-dl.py 'chair' 
```
```
python3 ebay-dl.py 'iphone' 
```
```
python3 ebay-dl.py 'phone case' 
```

# Commands to convert HTML files to CSV files when adding --csv
Whenever the flag ```--csv``` is specified, the output file will be saved in CSV format instead of JSON format. Below are the commands that will convert HTML files to CSV files when adding ```--csv```. For example, when you add the flag ```--csv```to the command for ```chair```, it will create a new CSV file for ```chair```. If there is no ```--csv``` in the command line, it will create a new JSON file instead.
```
python3 ebay-dl.py 'chair' --csv --num_pages=1
```
```
python3 ebay-dl.py 'iphone' --csv --num_pages=1
```
```
python3 ebay-dl.py 'phone case' --csv --num_pages=1
```
# Default number of pages
```
python3 ebay-dl.py 'chair' --csv 
```
```
python3 ebay-dl.py 'iphone' --csv 
```
```
python3 ebay-dl.py 'phone case' --csv 
```
