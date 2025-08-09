from obj4dviewer.scene import *
from obj4dviewer.object import Object
import pytest

@pytest.fixture
def scene_obj():
    return Scene()

@pytest.fixture
def object():
    return Object()

@pytest.fixture
def add_object(scene_obj, object):
    obj_id = scene_obj.add_object(object)
    yield obj_id
    scene_obj.pop_object(obj_id)
    scene_obj.autoincrement_obj_id = 0

@pytest.fixture
def pop_object(scene_obj, object):
    obj_id = scene_obj.add_object(object)
    yield scene_obj.pop_object(obj_id)
    scene_obj.autoincrement_obj_id = 0

def test_add_object(add_object, scene_obj, object):
    id = add_object

    assert len(scene_obj.objects) == 1
    assert scene_obj.objects[id] == object
    assert scene_obj.autoincrement_obj_id == 1

def test_pop_object(pop_object, object):
    obj = pop_object
    assert obj == object

def test_init_camera(mocker, scene_obj):
    mock_camera = mocker.Mock()
    scene_obj.init_camera(mock_camera)

    assert scene_obj.camera == mock_camera
    assert scene_obj.camera_controller.camera == mock_camera

def test_get_object(scene_obj ,add_object, object):
    id = add_object

    assert scene_obj.get_object(id) == object

def test_get_obj_file(mocker, scene_obj, object):
    mock_file_handler = mocker.patch('obj4dviewer.model_file_handler.handle_obj_file', return_value = object)
    file_obj = scene_obj.get_object_from_file('test.obj')
    mock_file_handler.assert_called_once_with('test.obj')
    assert file_obj == object

def test_get_obj4_file(mocker, scene_obj, object):
    mock_file_handler = mocker.patch('obj4dviewer.model_file_handler.handle_obj4_file', return_value = object)
    file_obj = scene_obj.get_object_from_file('test.obj4')
    mock_file_handler.assert_called_once_with('test.obj4')
    assert file_obj == object

def test_get_unknown_file(mocker, scene_obj, object):
    file_extension = "unknown_file_ext"
    with pytest.raises(NotImplementedError) as err:
        file_obj = scene_obj.get_object_from_file(f'test.{file_extension}')
        assert "No handler for extension: {file_extension}" in str(err.value)

def test_get_obj_file(mocker, scene_obj, object):
    mock_file_handler = mocker.patch('obj4dviewer.model_file_handler.handle_obj_file', return_value = object)
    id = scene_obj.load_object_from_file('test.obj')
    mock_file_handler.assert_called_once_with('test.obj')
    assert scene_obj.objects == {0:object}
