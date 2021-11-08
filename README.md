# hw_03
This is a homework assignment for CSCI 40 class at Claremont McKenna College. Go to the [project page](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03) to learn more!

The ebay-dl.py file converts ebay's html files into JSON files. I also modified the ebay-dl.py file so it also 
covert ebay's html file files into CSV files when adding --csv to the command line. For commands below, I only showed the first page results from Ebay. 

# Commands to convert HTML files to JSON files
```
python3 ebay-dl.py 'chair' --num_page=1
```
```
python3 ebay-dl.py 'iphone' --num_page=1
```
```
python3 ebay-dl.py 'phone case' --num_page=1
```

# Commands to convert HTML files to CSV files when adding --csv
```
python3 ebay-dl.py 'chair' --csv --num_page=1
```
```
python3 ebay-dl.py 'iphone' --csv --num_page=1
```
```
python3 ebay-dl.py 'phone case' --csv --num_page=1
```