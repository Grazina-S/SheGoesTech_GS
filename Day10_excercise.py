# # Day 10 - Work in Class - Classes and Objects
# 1. Song class
# define a class Song
# The class constructor needs to have three additional 3 parameters (self and 3 more!)
# title defaults to empty string
# author defaults to empty string
# lyrics by default empty tuple
# inside constructor method:
# set/store these three parameters inside objects variables of the same name (remember to use self!)
#  print on the screen "New Song made" - (try also printing here author and title!)
# Minimum:

# Write a method sing that prints the song line by line on the screen, first printing the author and title, if any.
# Write a method yell that prints the song in capital letters line by line on the screen, first printing the author and title, if any.

# Bonus: make the above sing and chain methods chainable, so we can call them several times (chained)

# Bonus: create an additional parameter max_lines to yell and sing methods that prints only a certain number of lines for both sing and yell. Better do with some default value e.g. -1, at which all rows are then printed.

# Create multiple songs with lyrics
# 2. Rap class
# For those feeling comfortable with class syntax, create a Rap class that inherits from Song
# # no new constructor method is necessary (you can if you want)

class Song:
    def __init__(self, title = "", author = "", lyrics = ()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New song made,the author is {self.author} and the title is {self.title}.")
   
    def sing (self):
        print(self.author)
        print(self.title)
        for line in self.lyrics:
            print(line)
        return self
    def yell(self):
        print(self.author)
        print(self.title)
        for line in self.lyrics:
            print(line.upper())       
        return self
   # bonus with additional parameter
    def sing_bonus (self, max_lines = -1):
       print(self.author)
       print(self.title)
    #    if max_lines == -1:
    #       max_lines = len(self.lyrics)   ### sitas if statement buvo destytojo sprendime. Nesuprantu kam jo reikia? Be jo veikia kuo puikiausiai
       for line in self.lyrics[:max_lines]:
            print(line)
       return self
    def yell_bonus (self, max_lines = -1):
        print(self.author)
        print(self.title)
        for line in self.lyrics[:max_lines]:
            print(line.upper())
        return self
       
        
     
  
   
   
   
Song1 = Song(title="Nothing else matters", author="Metallica", lyrics= (["So close no matter how far", "Couldn't be much more from the heart", "Forever trusting who we are", "And nothing else matters"]))
Song2 = Song("People are strange", "The Doors", ["People are strange", "When you're a stranger", "Faces look ugly", "When you're alone", "Women seem wicked", "When you're unwanted", "Streets are uneven", "When you're down"])
#lyrics gaunasi list sudarytas is 4 stringu. To reikia kad butu galima is naujos eilutes ir didziosios raides, nes tuplo negalima kaitalioti o stringus galima
#tik nelabai suprantu kaip ten su tuo tuple salygoj? Nesigauna cia joks tuple
Song1.sing_bonus(2).yell().yell_bonus(2)
Song2.sing().sing_bonus(3).yell().yell_bonus(1)

# 2. Rap class
# For those feeling comfortable with class syntax, create a Rap class that inherits from Song
# # no new constructor method is necessary (you can if you want)
#  add a new method break_it with two default parameters max_lines=-1 and drop equal to "yeah", which is similar to sing, but adds a drop after each word 
class Rap(Song):
    def break_it(self, max_lines= -1, drop="yeah"):
        print(f"Breaking down rap by {self.author} called {self.title}")
        # if max_lines == -1:
        #     max_lines = len(self.lyrics) # NESUPRANTU KAM SITAS REIKALINGAS?
        for line in self.lyrics[:max_lines]:
            words = line.split()        ### split komanda eilute kuri pati viena yra tiesiog stringas suskaldo pazodziui i lista is stringu
            new_line = f" {drop} ".join(words) + " " + drop # add drop at the end #### join komanda sujungia tuo kas pries taska nurodyta, veikia tik su stringais berods
            # # using replace as long as lyrics do not have extra whitespaces
            # new_line = line.replace(" ", f" {drop} ") + " " + drop
            # # the replace approach is more prone to input errors
            print(new_line)
        return self

rap1 = Rap("Tiems, kurie nieko nebijo", "G&G Sindikatas", ["Tie kurių bijo visi", "Bijo tų kurie nieko nebijo!", "Tie kurių bijo visi", "Bijo tų kurie nieko nebijo!"])
rap1.break_it(2)
