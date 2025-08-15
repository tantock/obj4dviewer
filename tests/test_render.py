from obj4dviewer.render import *

def test_backface_culling():
    assert backface_cull(np.array([0,0,0,1]), np.array([0,0,0,1])) == True
    assert backface_cull(np.array([0,0,0,-1]), np.array([0,0,0,1])) == False
    assert backface_cull(np.array([0,0,1,0]), np.array([0,0,1,0])) == True
    assert backface_cull(np.array([0,0,-1,0]), np.array([0,0,1,0])) == False
    assert backface_cull(np.array([0,1,0,0]), np.array([0,0,1,0])) == False
    assert backface_cull(np.array([0,-1,0,0]), np.array([0,0,1,0])) == False