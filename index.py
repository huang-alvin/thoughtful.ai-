from enum import Enum

class Status(Enum):
    STANDARD = 'STANDARD'
    SPECIAL = 'SPECIAL'
    REJECTED = 'REJECTED'

MAX_DIMENSION_CM = 150 # cm  
MAX_VOLUME_CM_SQR = 1000000 # 1,000,000 cm^3
MAX_MASS_KG = 20 # kg

def sort(width, height, length, mass) -> str: 
    is_bulky = False
    is_heavy = False

    if ( width >= MAX_DIMENSION_CM or
        height >= MAX_DIMENSION_CM or
        length >= MAX_DIMENSION_CM ):
        is_bulky = True
    
    area = width * height * length
    if area >= MAX_VOLUME_CM_SQR:
        is_bulky = True
    
    if mass >= MAX_MASS_KG:
        is_heavy = True
    
    if is_bulky and is_heavy:
        return Status.REJECTED

    if is_bulky or is_heavy:
        return Status.SPECIAL
    
    return Status.STANDARD
    
    

    

    
