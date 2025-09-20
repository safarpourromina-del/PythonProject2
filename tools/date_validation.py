from datetime import datetime
import re
from time import strptime


def date_validation(x):
    if strptime( x,"%Y/%m/%d %H:%M:%S" )!=None:
        return x
    else:
        raise ValueError("Invalid Date Format")

def product_validation(w):
    if re.match(r"^[A-Za-z/s]{3,15}$",w)!=None:
        return w
    else:
        raise ValueError("Invalid Product Format")