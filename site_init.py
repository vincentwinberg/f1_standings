from flask import Flask, render_template
import bs4 as bs
import urllib.request

app = Flask(__name__)

@app.route("/")
def index():
    driver_data = [] #initiates driver data
    points_data = [] #inititates points data

    source = urllib.request.urlopen('https://www.bbc.com/sport/formula1/drivers-world-championship/standings').read() #current standings on bbc
    soup = bs.BeautifulSoup(source, 'lxml')

    table = soup.find('table') #finds all tables

    table_rows = table.find_all('tr') #finds all table rows

    for points in table_rows: #finds points in table rows
        cols = points.find_all('td', class_="table__cell table__cell--right")
        cols = [ele.text.strip() for ele in cols]
        points_data.append([ele for ele in cols if ele])

    for driver in table_rows: #finds driver names in table rows
        cols = driver.find_all('abbr', class_="medium-abbr-off")
        cols = [ele.text.strip() for ele in cols]
        driver_data.append([ele for ele in cols if ele])

    points_data.remove([]) #removes fluff

    points = [] #creates new lists which will store the flattened lists
    driver = []

    for sublist in points_data: #flattens the points data list
        for item in sublist:
            points.append(item)

    for sublist in driver_data: #flattens the driver names list
        for item in sublist:
            driver.append(item)

    return render_template('index.html', points=points, names=driver) #returns template assigns the lists to the objects points and names

if __name__ == '__main__':
    app.run()

#used for when debugging
"""if __name__ == '__main__':
    app.run(debug=True)"""    
