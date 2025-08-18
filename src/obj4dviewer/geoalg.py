import numpy as np

def product(u:np.ndarray,v:np.ndarray):
    a1,b1,c1,d1 = u
    a2,b2,c2,d2 = v

    scalar = (a1*a2) + (b1*b2) + (c1*c2) + (d1*d2)

    bivector = [(a1*b2)-(b1*a2), #xy
                (b1*c2)-(c1*b2), #yz
                (a1*c2)-(c1*a2), #xz
                (a1*d2)-(d1*a2), #xw
                (b1*d2)-(b2*d1), #yw
                (c1*d2)-(d1*c2)  #zw
                ]
    
    return (scalar, bivector)
