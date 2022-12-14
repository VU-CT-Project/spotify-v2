""" Week 3
Excercise:
In the third week after the launch, you want to account for a user's mood shift. 
We have a few types of songs: “happy”, “party”, “calming”, and “lounge.” 
Define in your own algorithm if you think one song can be classified as two of those at the same time.  
 
This week you need to select 5 more songs to suggest to each user, again. 
If last week the user was playing a lot of songs from one of those types, this week we want to suggest more of the same type. 
Define, in your own terms what this should mean: if the user listened to 3 “calming” songs, 
should we provide 3 more without considering other factors? What if he or she also listened to 3 “party” songs and 4 “lounge” style songs?

Steps:
    1. Read the data from the spotify-dataset.csv file.
    2. 
    ...
"""

import pandas as pd

# read dataset
data = pd.read_csv("spotify-dataset.csv")
