# Introduction - Random YouTube Video Opener
This project is a Random YouTube Video Opener in Python. This program requires a text file called "ytLinks.txt" with a YouTube video link on each line, a blank text file called "infile.txt", and a blank text file called "dataFile.txt".

# Installation
Download randomYTVideoOpener.py, resetFiles.py, and requirements.txt files. Using pip, run in terminal "pip install -r requirements.txt" to install the necessary python libraries (webbrowser and yt_dlp). Create a text file named "ytLinks.txt" and enter the desired YouTube links on each line. Run resetFiles.py to create and initialize "dataFile.txt" and "infile.txt".  

# Usage
To start, run randomYTVideoOpener.py. A random video at a random time stamp will be opened from ytLinks.txt. The program will then add the index corresponding to the YouTube video which was just opened to dataFile.txt, to keep track of the videos which have already played to ensure a video will not be repeated. The program will also remove the index from infile.txt, to ensure a different video will be randomly selected the next time the program is ran. After all videos have been opened, the program will automatically reinitialize dataFile.txt and infile.txt. However, if the user wishes to reset the two text files prior to all the videos have been opened, they may run resetFiles.py, which will reinitialize dataFile.txt and infile.txt.

# File Format

**NOTE 1:** Ensure ONLY one YouTube video URL per line in ytLinks.txt

# Python Script Explanation

1.  **randomYTVideoOpener.py**
    - This program checks if infile.txt (contains indices corresponding to each YouTube video URL from ytLinks.txt) is empty. If empty, it adds the indices (one index per line) and reinitializes dataFile.txt (makes the file empty). dataFile.txt keeps track of the indices of the YouTube video URLs that have already been opened. The python script then creates a list of every index from infile.txt. Then, the program finds a random index from the list, which corresponds to an index of a URL from ytLinks.txt. To get the URL, the program creates a list containing every URL in ytLinks.txt. The program then uses the random index and indexes into the URL list, returning the YouTube URL. Then, using yt_dlp library, the program gets the video length and opens the video at a random time stamp. The program then gets every index from dataFile.txt and puts them in a list. The program then runs a nested loop, the outter loop loops for the length of YouTube videos, and the inner loop loops for the length of indices in dataFile.txt. The program then places all used YouTube video URL indices in dataFile.txt and unused indices in infile.txt. Finally the files are closed.

2. **resetFiles.py**
    - This program initializes dataFile.txt (makes the file empty). It adds one index per line in infile.txt for the number of YouTube video URLs found in ytLinks.txt.

# Support
For support or contact, reach out to **Saif Chaudhry** via **chaudhrysa@g.cofc.edu** or **saifchaudhry2@gmail.com**.

# Roadmap
In the future, the program will allow the user more customizability, such as determining if the program should open the video at a random time stamp or from the beginning.

# Contribution
Other developers may contribute, edit, or further develop the program, but must cite **Saif Chaudhry** and **chaudhrysa@g.cofc.edu**.

# Authors and Acknowledgment

**Saif Chaudhry:** Fully developed both randomYTVideoOpener.py and resetFiles.py.

# License
Student Programming Project