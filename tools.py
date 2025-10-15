from random import choice
import string

ABCDIG = string.ascii_letters + string.digits

def generate_short_name(length: int=8) -> str:
    """
    Generate short unique name with lngth `length` (8 by default) 
    based by random
    """
    return ''.join([choice(ABCDIG) for _ in range(length)])
