from obj4dviewer.camera_controller import *
from unittest.mock import MagicMock
import numpy as np

def mock_keydown(keydown:list[int]):
    def mock_get_item(index):
        if index in keydown:
            return True
        else:
            return False
    mock_get_pressed_return = MagicMock()
    mock_get_pressed_return.__getitem__.side_effect = mock_get_item
    
    return mock_get_pressed_return

def test_control_lshift(mocker):
    mock_projection = mocker.Mock()
    position = [1,2,3,4]
    camera = Camera(position, mock_projection)
    mock_axiiIdentity = mocker.patch('obj4dviewer.camera_controller.Camera.axiiIdentity')

    mocker.patch('obj4dviewer.camera_controller.pg.key.get_pressed', return_value=mock_keydown([pg.K_LSHIFT]))
    
    camera_controller = CameraController(camera)
    camera_controller.control()

    mock_axiiIdentity.assert_called_once()

def test_movement(mocker):
    mock_projection = mocker.Mock()
    position = [1,2,3,4]
    position_h = np.array([*position, 1.0])
    
    keys = [pg.K_a, pg.K_d, pg.K_w, pg.K_s, pg.K_q, pg.K_e, pg.K_SPACE, pg.K_LCTRL]

    for idx, keydown in enumerate(keys):
        camera = Camera(position, mock_projection)
        expect_pos = [
                    position_h - (camera.right * camera.moving_speed),
                    position_h + (camera.right * camera.moving_speed),
                    position_h + (camera.forward * camera.moving_speed),
                    position_h - (camera.forward * camera.moving_speed),
                    position_h + (camera.there * camera.moving_speed),
                    position_h - (camera.there * camera.moving_speed),
                    position_h + (camera.up * camera.moving_speed),
                    position_h - (camera.up * camera.moving_speed)]
        mocker.patch('obj4dviewer.camera_controller.pg.key.get_pressed', return_value=mock_keydown([keydown]))

        camera_controller = CameraController(camera)
        camera_controller.control()
        assert np.allclose(camera.position, expect_pos[idx])

def test_rotation3(mocker):
    mock_projection = mocker.Mock()
    position = [1,2,3,4]
    
    keys = [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN]

    for idx, keydown in enumerate(keys):
        camera = Camera(position, mock_projection)
        expect_pos = [
                        [-camera.rotation_speed, 0, 0],
                        [camera.rotation_speed, 0, 0],
                        [0, -camera.rotation_speed, 0],
                        [0, camera.rotation_speed, 0],
                        [0, 0,camera.rotation_speed],
                        [0, 0, -camera.rotation_speed ],]
        mocker.patch('obj4dviewer.camera_controller.pg.key.get_pressed', return_value=mock_keydown([keydown]))

        camera_controller = CameraController(camera)
        camera_controller.control()
        assert np.allclose([camera.angleYaw, camera.anglePitch, camera.angleRoll], expect_pos[idx])

def test_rotation4(mocker):
    mock_projection = mocker.Mock()
    position = [1,2,3,4]
    
    keys = [pg.K_j, pg.K_l, pg.K_u, pg.K_o, pg.K_k, pg.K_i]

    for idx, keydown in enumerate(keys):
        camera = Camera(position, mock_projection)
        expect_pos = [
                        [-camera.rotation_speed, 0, 0],
                        [camera.rotation_speed, 0, 0],
                        [0, -camera.rotation_speed, 0],
                        [0, camera.rotation_speed, 0],
                        [0, 0,camera.rotation_speed],
                        [0, 0, -camera.rotation_speed ],]
        mocker.patch('obj4dviewer.camera_controller.pg.key.get_pressed', return_value=mock_keydown([keydown]))

        camera_controller = CameraController(camera)
        camera_controller.control()
        assert np.allclose([camera.angleYawRoll, camera.anglePitchRoll, camera.anglePitchYaw], expect_pos[idx])

def test_mouse_input(mocker):
    mock_projection = mocker.Mock()
    position = [1,2,3,4]
    camera = Camera(position, mock_projection)

    mocker.patch('obj4dviewer.camera_controller.pg.mouse.get_rel', return_value=(-2,3))

    camera_controller = CameraController(camera)
    camera_controller.mouse_input(5)
    assert np.allclose([camera.angleYawRoll, camera.anglePitchYaw], [-2*5,-3*5])