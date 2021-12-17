import io
from typing import Tuple, Union


class Parser:
    """
    Base Class for Parsing Algorithms
    """
    def __init__(self, filename: str):
        """
        Initialization to be shared by inherited classes
        """
        self.filename = filename

    def get_record(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        a method that returns a tuple of strings.
        Will either return a tuple of two strings
        or a tuple of three strings

        it is common in python to see a public method calling a private method
        with a similar name. 
        """
        return self.__get_record__(f_obj)

    def __iter__(self):
        """
        This is an overriding of the Base Class Iterable function. All classes in python
        have this function, but it is not implemented for all classes in python. 

        # Note on the `__iter__` method
            Generally one doesn't call this method directly as `obj.__iter__()`. Instead it
            lets you use the object itself as an iterable. This is really useful in OOP because it
            allows you to represent and use iterable objects very cleanly. You still can call this
            method directly, but it really takes the fun out of python...

            ## How to use the `__iter__` method
            ```
            parser_obj = Parser(filename)
            for record in parser_obj:
              # do something
            ```

        # Why you should care about generators

            The expected behavior of this function is to create a generator which will lazily load
            the next item in its queue. These are very useful for many bioinformatic tools where you
            don't need everything loaded at once and instead are interested in interacting with the 
            stream (i.e. you need every value once and won't need it again after you use it). This saves
            quite a bit of memory, especially when you are working with billions of sequences and don't 
            need to keep all of them in memory. 
        
        # Distinction between generator functions and other functions
        
            instead of returning a value with the keyword `return`
            a generator must return a value with the keyword `yield`.

            This `yield` keyword will not shortcut the loop it is nested in like a return will
            and instead will pause the loop until the object is taken from it. 
        """

        # The proper way to open a file for reading and writing in python3 is to use the `with` / `as` keywords.
        # and keep the I/O within the nested code block. This will save you from some really nasty bugs that
        # sometimes close a file before everything you expect to be written/read is written/read. 
        # 
        # the interpretation of the following code is that for the lifetime of the filebuffer 
        # returned by the `open` function it will be accessible as the variable `f_obj`
        with open(self.filename, "r") as f_obj:
            
            # this loop will break at some point! 
            # but I will leave it up to you to implement the fix! 

            # You will need to look at the `Try` / `Except` keywords in python
            # and implement an exception for the error you will find in
            # the error message you receive. 
            while True:

                rec = self.get_record(f_obj)
                yield rec

    def __get_record__(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        a method to be overridden by inherited classes.
        """
        raise NotImplementedError(
                """
                This function is not meant to be called by the Parser Class.
                It is expected to be overridden by `FastaParser` and `FastqParser`""")

class FastaParser(Parser):
    """
    Fasta Specific Parsing
    """
    def __get_record__(self, f_obj: io.TextIOWrapper) -> Tuple[str, str]:
        """
        returns the next fasta record
        """

class FastqParser(Parser):
    """
    Fastq Specific Parsing
    """
    def __get_record__(self, f_obj: io.TextIOWrapper) -> Tuple[str, str, str]:
        """
        returns the next fastq record
        """

