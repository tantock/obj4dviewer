import numpy as np
from obj4dviewer.projection import Perspective
from obj4dviewer.camera_view_settings import CameraViewSettings

def init():
    camera_config = CameraViewSettings(90, 9/16, 9/16, 1, 100)
    return Perspective(camera_config)

def test_perspective_depth():
    projection = init()
    x, y, z, w = -10,-20,-30,-40
    H = 1

    v1 = projection.projection_matrix @ np.array([x,y,z,w,H])
    v2 = projection.projection_matrix @ np.array([x,y,z,w*2,H])

    v1ndc = v1/v1[-1]
    v2ndc = v2/v2[-1]
    
    assert np.abs(v1ndc[3]) < np.abs(v2ndc[3])

def test_perspective_depth_transform():
    projection = init()
    x, y, z, w = -10,-20,-30,-40
    H = 1

    v1 = projection.projection_matrix @ np.array([x,y,z,w,H])
    v2 = projection.projection_matrix @ np.array([x,y,z,w*2,H])

    v1ndc = v1/v1[-1]
    v2ndc = v2/v2[-1]
    
    for i in range(3):
        assert np.abs(v1ndc[i]) > np.abs(v2ndc[i])

def test_orthogonality():
    projection = init()
    x, y, z, w = -10,-20,-30,-40
    H = 1
    v1 = projection.projection_matrix @ np.array([x,y,z,w,H])

    v1ndc = v1/v1[-1]
    
    for i in range(3):
        arr = [x,y,z,w,H]
        arr[i] += 10
        v2 = projection.projection_matrix @ np.array(arr)
        v2ndc = v2/v2[-1]
        for j in range(3):
            if i != j:
                assert np.isclose(v1ndc[j],v2ndc[j])