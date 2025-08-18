from obj4dviewer.geoalg import *
def test_product():
    x = np.array([1,0,0,0])
    y = np.array([0,1,0,0])
    z = np.array([0,0,1,0])
    w = np.array([0,0,0,1])
    
    p = product(x,x)
    assert p[0] == 1
    assert np.all(p[1] == [0,0,0,0,0,0])

    p = product(y,y)
    assert p[0] == 1
    assert np.all(p[1] == [0,0,0,0,0,0])

    p = product(z,z)
    assert p[0] == 1
    assert np.all(p[1] == [0,0,0,0,0,0])

    p = product(w,w)
    assert p[0] == 1
    assert np.all(p[1] == [0,0,0,0,0,0])

    p = product(x,y)
    assert p[0] == 0
    assert np.all(p[1] == [1,0,0,0,0,0])

    p = product(y,x)
    assert p[0] == 0
    assert np.all(p[1] == [-1,0,0,0,0,0])

    p = product(y,z)
    assert p[0] == 0
    assert np.all(p[1] == [0,1,0,0,0,0])

    p = product(z,y)
    assert p[0] == 0
    assert np.all(p[1] == [0,-1,0,0,0,0])

    p = product(x,z)
    assert p[0] == 0
    assert np.all(p[1] == [0,0,1,0,0,0])

    p = product(z,x)
    assert p[0] == 0
    assert np.all(p[1] == [0,0,-1,0,0,0])

    p = product(x,w)
    assert p[0] == 0
    assert np.all(p[1] == [0,0,0,1,0,0])

    p = product(w,x)
    assert p[0] == 0
    assert np.all(p[1] == [0,0,0,-1,0,0])

    p = product(y,w)
    assert p[0] == 0
    assert np.all(p[1] == [0,0,0,0,1,0])

    p = product(w,y)
    assert p[0] == 0
    assert np.all(p[1] == [0,0,0,0,-1,0])

    p = product(z,w)
    assert p[0] == 0
    assert np.all(p[1] == [0,0,0,0,0,1])

    p = product(w,z)
    assert p[0] == 0
    assert np.all(p[1] == [0,0,0,0,0,-1])
    
