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

    def get_record(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        a method that returns a tuple of strings.
        Will either return a tuple of two strings
        or a tuple of three strings
        """
        return self.__get_record__(f_obj)

    def __get_record__(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        a method to be overwritten by inherited classes
        """

class FastaParser(Parser):
    """
    Fasta Specific Parsing
    """
    def __iter__(self):
        """
        Overwritten iter method
        """

    def __get_record__(self, f_obj: io.TextIOWrapper) -> Tuple[str, str]:
        """
        returns the next fasta record
        """

class FastqParser(Parser):
    """
    Fastq Specific Parsing
    """
    def __iter__(self):
        """
        Overwritten iter method
        """

    def __get_record__(self, f_obj: io.TextIOWrapper) -> Tuple[str, str, str]:
        """
        returns the next fastq record
        """

