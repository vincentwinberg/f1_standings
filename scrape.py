import bs4 as bs
import urllib.request
import numpy as np

header_data = [] #initiates header data
row_data = [] #inititates row data
drivers = [] #initiates drivers list & their standing

source = urllib.request.urlopen('https://www.bbc.com/sport/formula1/drivers-world-championship/standings').read() #current standings on bbc
soup = bs.BeautifulSoup(source, 'lxml')

table = soup.find('table') #finds all tables

table_rows = table.find_all('tr') #finds all table rows

for row in table_rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    row_data.append([ele for ele in cols if ele])

for header in table_rows:
    cols = header.find_all('th')
    cols = [ele.text.strip() for ele in cols]
    header_data.append([ele for ele in cols if ele])

header_data.remove(['Rank', 'Driver', 'Team', 'Wins', 'Points']) #removes fluff
header_data.remove([]) #this too

test = []
x = 0

for n in header_data:
    drivers.append(n)
    x = (x + 1)

for n in range(0, 21):
    drivers = (drivers[n][1])
    n += 1
#print(test)
#print(header_data)