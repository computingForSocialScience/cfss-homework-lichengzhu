import unicodecsv as csv   #import necessary libraries, particularly for reading csv files containing unicodes
import matplotlib.pyplot as plt   #import necessary libraries, particularly for ploting

def getBarChartData():
    f_artists = open('artists.csv')  # open the csv file we created before   # double open, yay!!!!!!!!!!!!!!!!
    f_albums = open('albums.csv') # open the csv file we created before

    artists_rows = csv.reader(f_artists)  # reading the information by rows, and save it to a variable
    albums_rows = csv.reader(f_albums)  # reading the information by rows, and save it to a variable

    artists_header = artists_rows.next()  # move to next row (cause the first row is the header, not the data we want)
    albums_header = albums_rows.next()  # move to next row (cause the first row is the header, not the data we want)

    artist_names = []   # creating an empty list
    
    decades = range(1900,2020, 10)   # creading years from 1900 to 2020 by each 10 years
    decade_dict = {} # empty dictionary
    for decade in decades:   # looping through created years, make the years a the keys in the new dictionary and give each year a value of 0
        decade_dict[decade] = 0
    
    for artist_row in artists_rows: 
        if not artist_row:  #skipping empty cells
            continue
        artist_id,name,followers, popularity = artist_row  #unpack the row information (artist) to four different variables
        artist_names.append(name)  # get all artists' names

    for album_row  in albums_rows:
        if not album_row:  # skipping empty cells
            continue
        artist_id, album_id, album_name, year, popularity = album_row   # unpack the row information (about albums) and store them in four variables
        for decade in decades:
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)): # loop breaks when the year exceeds the boundary of range(1900, 2020, 10)
                decade_dict[decade] += 1
                break

    x_values = decades  # set the values for x-axis
    y_values = [decade_dict[d] for d in decades]  # set the values for y-axis
    return x_values, y_values, artist_names # return the values

def plotBarChart():
    x_vals, y_vals, artist_names = getBarChartData()  #unpack the values returned from getBarChartData() and store them in three valieables
    
    fig , ax = plt.subplots(1,1)  # creat a fiture with one subplot (just one set of bars)
    ax.bar(x_vals, y_vals, width=10)  # set the data for the bar chart and defining the width of bars
    ax.set_xlabel('decades')  # give the label for x-axis
    ax.set_ylabel('number of albums')  # give the label for y-axis
    ax.set_title('Totals for ' + ', '.join(artist_names)) # give the label for the title of the bar chart
    plt.show()  # tell python that this is the end of "prparing the bar charty" and ask python to present the chart

#plotBarChart()
#getBarChartData()
    
