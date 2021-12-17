"""
A Python module for FAST[AQ] IO and DNA->RNA Transcribing
"""

from .parse import (
        FastaParser,
        FastqParser)
from .seq import (
        transcribe,
        reverse_transcribe)

__version__ = "0.1.1"
