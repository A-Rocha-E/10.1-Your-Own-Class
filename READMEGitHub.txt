10.1 README

The class for my assignment is a Reading Device. It asks for the format that you want to read (audio or text), 
the name of the book, the name of the author and the year the book was published. You are able to change the format and book if you want, 
you can use the selected function to see what format you are in, the name of the author and book. You can also change the page that you 
on using the set get for page number.

readtype - this is the format that you want (audio or text)
bookname - this is the name of the book that you want
author - the name of the author
year - the year that the book was published

The set_readtype function allows the user to change the format that they want. This allows for either a text version or audio version, and
will assign it using an if statment. It will take the argument and make it lower case. 
The get_readtype function returns the format that you are in.
The set_bookname function allows the user to change what book they are reading.
The get_bookname function returns the name of the book.
The set_page function allows the user to change the page that they want to be on.
The get_page function returns the page of the book that was set.
The citation function returns a citation using for the book that you are reading. It uses the author, book name and the year published.
The selected function returns the selected format, bookname, and author. It prints it our in an easy to read format.

The demo program shows what the script can do. It will print out everything that is selected using the selected function. It will also
create a citation using the citation function. It will change the format, and then return it. It will also return the name of the book.
It will also set the page(set to 4 just to test), and it will return the page number. It will do this with two different books.

To run the program you can just run the script in the terminal (python3 YourOwnClass.py). If you want you can change the format, book name
author and year if you want just change it in the argument in the main function. If you want to change the page number you can also do that 
in the main function it is already filled but if you want you can change it.