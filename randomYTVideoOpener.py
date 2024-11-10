import webbrowser
import random
import yt_dlp

# Open the file
indexFile = open("infile.txt", "r+")

# Read the first line of the file
nullChecker = indexFile.readline()

# If the line is empty, run this
if nullChecker == "":

    # Open the file
    ytLinksFile = open("ytLinks.txt", "r")

    # Initialize count
    count  = 0
    
    # Loop for every line in the file
    for line in ytLinksFile:

        # Increment count
        count +=1

    # Close the file
    ytLinksFile.close()

    # Loop for the length of count
    for i in range(count):

        # Print i to the file
        print(str(i), file = indexFile)

    # Open the file
    dataFile = open("dataFile.txt", "w")

    # Close the file
    dataFile.close()

# Initialize nums
nums = []

# Go back to the first line in the file
indexFile.seek(0)

# Loop for every line in the file
for line in indexFile:

    # Strip the line of extra white spice and convert to int
    line = int(line.strip())

    # Add the line to the list
    nums += [line]

# Get a random index value for the list
randomIndex = random.randint(0, len(nums) - 1)

# Get the random value from the list
randomIndex = nums[randomIndex]

# Initialize the list
ytLinks = []

# Open the file
ytLinksFile = open("ytLinks.txt", "r")

# Loop for every line in the file
for line in ytLinksFile:

    # Add the line to the list
    ytLinks += line.split()

# Close the file
ytLinksFile.close()

# Get the random YouTube video from the list
ytVideoURL = ytLinks[randomIndex]

# Create the object
ytVideo = yt_dlp.YoutubeDL()

# Get all info about the video
ytVideoInfo = ytVideo.extract_info(ytVideoURL, download=False)

# Get the length of the video
ytVideoLength = ytVideoInfo.get('duration', None)

# Get a random time stamp in the video
randomVideoTime = random.randint(0, ytVideoLength - 75)

# Open the video at the random time stamp
webbrowser.open(ytVideoURL + f"&t={randomVideoTime}")

# Close the file
indexFile.close()

# Open the files
indexFile = open("infile.txt", "w")
dataFile = open("dataFile.txt", "r+")

# Initialize the list
data = []

# Loop for every line in the file
for line in dataFile:

    # Strip the line of extra white space and add it to the list
    data += [line.strip()]

# Loop for the amount of YouTube videos
for i in range(len(ytLinks)):

    # Initialize checker to true
    checker = True

    # Loop for the length of data
    for j in range(len(data)):

        # If index i == the value at data[j], run this
        if i == int(data[j]):

            # Set checker to false
            checker = False
    # Run if checker is true
    if checker:

        # Run if i does not equal randomIndex
        if i != randomIndex:

            # Print i to the file
            print(str(i), file = indexFile)
        
        # Otherwise, run this
        else:

            # Print i to the file
            print(str(i), file = dataFile)

# Close the files
dataFile.close()
indexFile.close()