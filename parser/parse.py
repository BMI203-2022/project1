class Parser:
    """
    Base Class for Parsing Algorithms
    """
    def __init__(filename: str):
        """
        """

class FastaParser(Parser):
    """
    Fasta Specific Parsing
    """
    def __iter__(self):
        """
        Overwritten iter method
        """

class FastqParser(Parser):
    """
    Fastq Specific Parsing
    """
    def __iter__(self):
        """
        Overwritten iter method
        """

