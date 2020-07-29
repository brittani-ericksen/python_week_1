title = "Howl's Moving Castle"
# STOP = 10
counter = 0

while counter < len(title):
    if (counter % 2) == 0 and title[counter] != " ":
        print (title[counter], end = " ")
    counter += 1