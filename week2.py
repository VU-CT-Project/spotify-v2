""" 
A user opens the app and is looking for new suggestions on “Discover.”  
 
There are three types of music only: pop, rock, and techno.  
 
You want to find which style the user has listened to the most, of those three. Define in your own terms what this should mean. For example, you can say that if the user has listened to 20 rock songs and 2 techno songs, and 3 pop songs, this is a rock music fan. Or you can work with percentages: you can find a user that played 80% techno and 20% pop. You can make your algorithm disregard a difference of 10% and say that if a user played pop 45 percent of the time and rock 50 percent of the time, the difference is small and both styles should be considered equally important to him or her. Outline your scale and assumptions in your work. 

In the second week, your algorithm should suggest 5 songs again, this time based on the above-mentioned, i.e. based on style. 
 



"""



"""Follow these steps to complete the assignment:

1.Read the data from the spotify-dataset.csv file and store it in a variable called data.
2.Iterate over the rows in data and count the number of times the user has listened to each of the three styles of music (pop, rock, and techno).
3.Calculate the percentage of songs listened to for each music style by dividing the number of songs listened to for that style by the total number of songs listened to by the user.
4.If the percentage difference between the user's two favorite styles is less than 10%, consider both styles to be equally important to the user.
5.Use the user's favorite style(s) to suggest 5 songs from that style.

"""


# Import necessary libraries
import pandas as pd

# Read in data from spotify-dataset.csv file
data = pd.read_csv("spotify-dataset.csv")

# Set threshold for style importance
threshold = 50

# Initialize variables to store song counts for each style
pop_count = 0
rock_count = 0
techno_count = 0

# Iterate over rows in data
for index, row in data.iterrows():
    # Check the genre of each song and increment the appropriate counter scaleable
    if row["the genre of the track"] == "pop":
        pop_count += 1
    elif row["the genre of the track"] == "rock":
        rock_count += 1
    elif row["the genre of the track"] == "techno":
        techno_count += 1

# Calculate total number of songs listened to by user
total_songs = pop_count + rock_count + techno_count

# Calculate percentage of songs listened to for each style
pop_percent = pop_count / total_songs * 100
rock_percent = rock_count / total_songs * 100
techno_percent = techno_count / total_songs * 100

# Determine user's favorite style(s)
favorite_genres = []

for style, percent in {"pop": pop_percent, "rock": rock_percent, "techno": techno_percent}.items():
    if percent > threshold:
        favorite_genres.append(style)

# Initialize list to store suggested songs
suggested_songs = []

# Iterate over rows in data
for index, row in data.iterrows():
    # Check if song's style matches user's favorite style(s)
    if row["the genre of the track"] in favorite_genres:
        # Add song to suggested_songs list
        suggested_songs.append(row["title"])
        # Stop suggesting songs once 5 songs have been suggested
        if len(suggested_songs) == 5:
            break

# Print suggested songs
print(suggested_songs)

