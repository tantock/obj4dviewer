from obj4dviewer.camera_view_settings import *
from math import isclose

def test_init():
    cvs = CameraViewSettings(10,0.5, 0.2, 0.5, 12)
    assert cvs.h_fov == 10
    assert isclose(cvs.v_fov, 5)
    assert isclose(cvs.d_fov, 2)
    assert cvs.near_plane == 0.5
    assert cvs.far_plane == 12
