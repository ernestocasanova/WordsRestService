from enum import Enum
import random

class Colors(Enum):
    A = '#FFEEFF'
    B = '#000000'
    C = '#FFFFFF'
    D = '#EEEEEE'
    E = '#D3D3D3'

    @classmethod
    def get_color(self, words, len):
        """Manipulate the hexa color in count of words geting one of the random colors defined in the enum
		   if is less than 100 choose between A and D, if not returns the E HEXA
		"""
        if len < 100:
            letter = random.choice('ABCD')
            return Colors[letter].value
        else:
            return Colors['E'].value