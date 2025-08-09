from obj4dviewer.camera import *

def test_camera_init(mocker):
    mock_projection = mocker.Mock()
    position = [1,2,3,4]
    camera = Camera(position, mock_projection)
    assert camera.projection == mock_projection
    assert np.all(camera.position == np.array([*position, 1.0]))
    assert np.all(camera.forward == np.array([0, 0, 1, 0, 1]))
    assert np.all(camera.up == np.array([0, 1, 0, 0, 1]))
    assert np.all(camera.right == np.array([1, 0, 0, 0, 1]))
    assert np.all(camera.there == np.array([0, 0, 0, 1, 1]))
    assert camera.moving_speed == 0.3
    assert camera.rotation_speed == 0.015

    assert camera.anglePitch == 0
    assert camera.angleYaw == 0
    assert camera.angleRoll == 0

    assert camera.angleYawRoll == 0 #yz
    assert camera.anglePitchRoll == 0 #xz
    assert camera.anglePitchYaw == 0 #xy
    assert camera.four_rotation == False

def test_axiiIdentity(mocker):
    mock_projection = mocker.Mock()
    position = [1,2,3,4]
    camera = Camera(position, mock_projection)

    camera.forward = np.array([0, 1, 0, 0, 1])
    camera.up = np.array([0, 0, 1, 0, 1])
    camera.right = np.array([0, 0, 0, 1, 1])
    camera.there = np.array([1, 0, 0, 0, 1])

    assert np.all(camera.forward == np.array([0, 1, 0, 0, 1]))
    assert np.all(camera.up == np.array([0, 0, 1, 0, 1]))
    assert np.all(camera.right == np.array([0, 0, 0, 1, 1]))
    assert np.all(camera.there == np.array([1, 0, 0, 0, 1]))

    camera.axiiIdentity()

    assert np.all(camera.forward == np.array([0, 0, 1, 0, 1]))
    assert np.all(camera.up == np.array([0, 1, 0, 0, 1]))
    assert np.all(camera.right == np.array([1, 0, 0, 0, 1]))
    assert np.all(camera.there == np.array([0, 0, 0, 1, 1]))

def test_rotate_matrix(mocker):
    rx, ry, rz, rw, h = np.array([1, 0, 0, 0, 1])
    ux, uy, uz, uw, h = np.array([0, 1, 0, 0, 1])
    fx, fy, fz, fw, h = np.array([0, 0, 1, 0, 1])
    tx, ty, tz, tw, h = np.array([0, 0, 0, 1, 1])
    expect_matrix =  np.array([
        [rx, ux, fx, tx, 0],
        [ry, uy, fy, ty, 0],
        [rz, uz, fz, tz, 0],
        [rw, uw, fw, tw, 0],
        [0, 0, 0, 0, 1]
    ])

    mock_projection = mocker.Mock()
    position = [1,2,3,4]
    camera = Camera(position, mock_projection)
    assert np.all(camera.rotate_matrix() == expect_matrix)
