import argparse
import requests
from bs4 import BeautifulSoup
import json

def parse_shipping(text):
    '''
    >>> parse_shipping('+$31.86 shipping estimate')
    3186
    >>> parse_shipping('Free 3 day shipping')
    0
    >>> parse_shipping('Free shipping')
    0
    '''
    shipping=None
    if 'Free' in text and 'shipping' in text:
        return 0
    else:
        dollar_sign=text.find('$')
        dot=text.find('.')
        space=text.find(' ')
        shipping=(text[dollar_sign+1:dot] + text[dot+1:space])
        return int(shipping)

def parse_itemcost(text):
    '''
    >>> parse_itemcost('$10.50')
    1050
    >>> parse_itemcost('$5.40')
    540
    >>> parse_itemcost('$20.00 to $40.00')
    2000
    >>> 
    '''
    item_cost=None
    dollar_sign=text.find('$')
    dot=text.find('.')
    item_cost=(text[dollar_sign+1:dot] + text[dot+1:dot+3])
    return int(item_cost)

def parse_itemssold(text):
    '''
    Takes as inpit a string and returns the number of items sold, as sepecified in the string.

    >>> parse_itemssold('38 sold')
    38
    >>> parse_itemssold('14 watchers')
    0
    >>> parse_itemssold('Almost gone')
    0
    '''
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else: 
        return 0

# only run the code below when the python file runs "normally"
if __name__ =='__main__':

    # get command line arguments
    parser = argparse.ArgumentParser(description='Download information from ebay and convert to JSON.')
    parser.add_argument('search_term')
    parser.add_argument('--num_pages', default=10)
    parser.add_argument('--csv', action="store_true")

    args = parser.parse_args()
    print('args.search_terms=', args.search_term)

    # list of all items found in all ebay webpages
    items = []

    # loop over the ebay webpages
    for page_number in range (1,int(args.num_pages)+1):
    
        # build the url
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' 
        url += args.search_term
        url += '&_sacat=0&LH_TitleDesc=0&_pgn=' 
        url += str(page_number)
        url += '&rt=nc'
        print('url=',url)

        # download the html
        r = requests.get(url)
        status = r.status_code
        print('status=',status)
        html = r.text

        # process the html
        soup = BeautifulSoup(html, 'html.parser')

        # loop over the items in the page
        tags_items = soup.select('.s-item')
        for tag_item in tags_items:
            
            name = None
            tags_name = tag_item.select('.s-item__title')
            for tag in tags_name:
                name = tag.text
            
            price = None
            tags_price = tag_item.select('.s-item__price')
            for tag in tags_price:
                price = parse_itemcost(tag.text)

            status = None
            tags_status = tag_item.select('.s-item__subtitle')
            for tag in tags_status:
                status = tag.text

            shipping = None
            tags_shipping = tag_item.select('.s-item__logisticsCost')
            for tag in tags_shipping:
                shipping = parse_shipping(tag.text)

            freereturns = False
            tags_freereturns = tag_item.select('.s-item__free-returns')
            for tag in tags_freereturns:
                freereturns = True

            items_sold = None
            tags_itemssold = tag_item.select('.s-item__hotness, .s-item__additionalItemHotness')
            for tag in tags_itemssold:
                items_sold = parse_itemssold(tag.text)

            item = { 
                'name': name,
                'price': price,
                'status': status,
                'shipping': shipping,
                'free_returns': freereturns,
                'items_sold': items_sold,
            }
            items.append(item)

        print('len(tag_items)=',len(tags_items))
        print('len(items)=',len(items))

    # write the json to a file 
    # extra credit: change it to .csv file
    if args.csv:
        filename = args.search_term + '.csv'
    else:
        filename = args.search_term + '.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))