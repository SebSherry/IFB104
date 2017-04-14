#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: <REDACTED>
#    Student name: Sebastian Sherry
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files may be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  EASY NEWS READER
#
#  There are many Web sites that give you lists of news stories or
#  similar regularly-updated information.  Here you will create an
#  application that makes it easy to read the stories on such a page
#  by presenting them to the user one at a time, via an intuitive
#  Graphical User Interface.  See the instruction sheet accompanying
#  this file for full details.
#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the task by filling in the template below.
#

#----------
#
# Import the various functions needed to complete this program.
# NB: You may NOT import or use code from any other module
# in your solution.  Also, you do NOT need to use all these
# functions in your solution.

# Import the function for fetching web documents and images
from urllib import urlopen 

# Import all the Tkinter GUI functions
from Tkinter import *

# Import the regular expression search function
from re import findall

# Import the scrolled text widget (Optional - you
# do not need to use this, a standard Text
# widget is adequate)
from ScrolledText import ScrolledText
#
#----------


##### DEVELOP YOUR SOLUTION HERE #####

#RSS FEED CHOICES
#Rolling Stone http://www.rollingstone.com/music.rss (Great amount of Data, some "dodgy" Characters Present)
#title regex: <title><!\[CDATA\[(.+)]]></title>
#article Regex: <content:encoded><!\[CDATA\[(([A-Za-z0-9. :,\'-\n]+) BROKEN

#Music News.com www.music-news.com/rss/news.asp (Working Regex, shorter stories. Less "dodgy" Charaxters)
#title: <title><!\[CDATA\[(.+)\]\]></title>
#date: <pubDate>(.+)</pubDate>
#article: <description><!\[CDATA\[<img src=".+" />]]><!\[CDATA\[(.*)]]></description> 

#Set feed location, open feed, extract stories, close feed
RSS = "http://www.music-news.com/rss/news.asp"
feed = urlopen(RSS)
html = feed.read()
feed.close()

#grab all titles and content
article_dates = findall('<pubDate>(.+)</pubDate>', html)
article_titles = findall('<title><!\[CDATA\[(.+)\]\]></title>', html)
article_content = findall('<description><!\[CDATA\[<img src=".+" />]]><!\[CDATA\[(.*)]]></description>', html)

#variables
numStorys = len(article_titles) #Counts number of stories
curStory = 1  #Tracks the current story number NOT list index value (which is -1 from this number at all times)

#Functions
def storynxt(): #moves to the next story
    global curStory
    if curStory < numStorys:
        curStory += 1       #Moves story to the next
        display.delete(1.0, END)        #resets display
        display.insert(END, createDisplay(curStory - 1))    #Displays new story
        count['text'] = str(curStory) + "/" + str(numStorys)    #updates count

def storyprev(): #moves to the previous story
    global curStory
    if curStory > 1:
        curStory -= 1       #Moves story to the previous
        display.delete(1.0, END)        #resets display
        display.insert(END, createDisplay(curStory - 1))    #Displays new story
        count['text'] = str(curStory) + "/" + str(numStorys)    #updates count

def createDisplay(i):   #Creates the text entry for the story
    story = ''          #Creates string to hold story
    story = article_dates[i] + "\n" + "\n" + article_titles[i] + "\n" + "\n" + article_content[i]
    return story

def fixchar():      #replaces unreadable 's with readable ones
    global article_titles
    global article_content

    def removeNonAscii(s):
        return "".join(i for i in s if ord(i)<128)
    
    for item in range(len(article_content)):
        #replaces non-ascii charaters 
        article_titles[item] = removeNonAscii(article_titles[item])
        article_content[item] = removeNonAscii(article_content[item])
        #Changes &eacute; to é
        article_titles[item] = article_titles[item].replace("&eacute;","é")
        article_content[item] = article_content[item].replace("&eacute;","é")
        #Removes &#8203;
        article_titles[item] = article_titles[item].replace("&#8203;","")
        article_content[item] = article_content[item].replace("&#8203;","")
        
#Create Window 
window = Tk()
window.title('IFB104 Music News')

#Grab image URL:http://www.musicexpos.com/headphones.gif
IMG = "http://www.musicexpos.com/headphones.gif"
img_record = urlopen(IMG).read().encode('base64', 'strict')
logo_img = PhotoImage(data = img_record)

#Create features
Center_frame = Frame(window)

display = Text(window, width = 20, height = 18, wrap = WORD, font = ('Verdana', 12), borderwidth = 2, relief = 'groove')
heading = Label(window, text = 'Music News', font = ('Verdana', 24), justify = CENTER)
count = Label(window, text = '1/'+str(numStorys), justify = CENTER)
nextbtn = Button(window, text = 'Next', command = storynxt)
prevbtn = Button(window, text = 'Prev', command = storyprev)
logo = Label(window, text='', image = logo_img)   

#place widgets
heading.grid(row = 1, column = 1, columnspan = 5)
display.grid(row = 2, column = 1, columnspan = 3)
logo.grid(row = 2, column = 4, columnspan = 2)
prevbtn.grid(row = 3, column = 2)
count.grid(row = 3, column = 3)
nextbtn.grid(row = 3, column = 4)

#Fix all unusual charcters in the articles
fixchar()

#Generate Starting Story
display.insert(END, createDisplay(curStory - 1))    
count['text'] = str(curStory) + "/" + str(numStorys)

#start the loop
window.mainloop()

#
#--------------------------------------------------------------------#
