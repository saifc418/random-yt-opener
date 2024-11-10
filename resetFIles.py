# Open and close the file
dataFile = open("dataFile.txt", "w")
dataFile.close()

# Open the files
inFile = open("infile.txt", "w")
ytLinksFile = open("ytLinks.txt", "r")

# Initialize count
count  = 0

# Loop for every line in the file
for line in ytLinksFile:

    # Increment count
    count +=1

# Close the file
ytLinksFile.close()

# Loop for length of count
for i in range(count):

    # Print i to the file
    print(i, file = inFile)

# Close the file
inFile.close()

# Inform user file reset completed
print("File reset completed.")