
__all__ = [
    '__content_dictionary_mapping__',
]

from .println import (
    DPrint,
    DPrintLine,
)

__content_dictionary_mapping__ = {
    'print': DPrint,
    'println': DPrintLine,
}
