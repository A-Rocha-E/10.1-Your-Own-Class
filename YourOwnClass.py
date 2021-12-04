#Alejandro Rocha
#10.1 Your Own Class

#create a class that has the can take the version that the reader wants audio or digital
#the bookname, author and the year 

class ReadingDevice:
    def __init__(self, readtype, bookname, author, year):
        #define the arguments
        self._readtype = readtype #private
        self._bookname = bookname #private
        self.author = author #public
        self.year = year #public
    
    #first set-get function, asks what the new reading type will be
    def set_readtype(self, readtype):
        #if statment to 
        #makes the readtype lowercase
        if readtype.lower() == "text":
            #redefines the readtype to the new format
            self._readtype = "Text"
        #accepts the words audio or audiobook    
        elif readtype.lower() == "audio" or  readtype == "audio book":
            #redefines the readtype to the new format
            self._readtype = "Audio"
        #if the readtype is something else then there will be an error
        else:
            return ("Error: Format not supported")
    #returns the readtype
    def get_readtype(self):
        return (f"Format: {self._readtype}")

    #second set-get function
    def set_bookname(self, bookname):
    #assigns the new bookname
        self._bookname = bookname

    #returns the name of the book
    def get_bookname(self):
        return (f"Book Name: {self._bookname}")

    #allows for the user to set a page number
    def set_pagenum(self, page):
        self._page = page
    #returns the page number
    def get_pagenum(self):
        return (f"Book open to page {self._page}")

    #creates a citation
    def citation(self):
        #gives the citation
        return (f"Citation: {self.author}, {self._bookname}, {self.year}")
    #lets you now what you have selected, readtype, bookname, and author
    def selected(self):
        return (f"You have selected a {self._readtype}, version of {self._bookname} by the author {self.author}")


#print you have selected an ___readtype__ version of __bookname__ by __ author name__

def main():
    
    #create a variable that has the ReadingDevice initalized
    test = ReadingDevice("Text", "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "1997")
    #print out the selected version
    print (test.selected())
    #print out the citation
    print (test.citation())
    #set the readtype to audio from digital
    test.set_readtype("audio")
    #print out the new way to read
    print (test.get_readtype())
    #print out the name of the book
    print (test.get_bookname())
    
    print (" ")

    #Initalize the ReadingDevice class
    pageset = ReadingDevice("Text", "Gilgamesh", "Steven Mitchell", "Unknown")
    #print out the selected version
    print (pageset.selected())
    #print out the citation
    print (pageset.citation())
    #set the readtype to audio from digital
    pageset.set_readtype("audio")
    #print out the new way to read
    print (pageset.get_readtype())
    #print out the name of the book
    print (pageset.get_bookname())
    
    #use the set page function
    #set the page number
    pageset.set_pagenum(25)
    #get the page number that was set
    print (pageset.get_pagenum())
    

if __name__ == "__main__":
    main()