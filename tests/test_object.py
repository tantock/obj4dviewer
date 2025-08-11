from obj4dviewer.object import *

def test_axes3():
    axis = Axes3()
    assert np.all(axis.vertices == np.array([(0, 0, 0, 0, 1), (1, 0, 0, 0, 1), (0, 1, 0, 0, 1), (0, 0, 1, 0, 1)]))
    faces = np.array([(0, 1), (0, 2), (0, 3)])
    assert np.all(axis.faces == faces)
    colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
    assert np.all(axis.colors == colors)
    assert np.all([face == [(color, face) for color, face in zip(colors, faces)]][idx] for idx, face in enumerate(axis.color_faces))
    assert axis.draw_vertices == False
    assert axis.label == 'XYZ'

def test_axes4():
    axis = Axes4()
    assert np.all(axis.vertices == np.array([(0, 0, 0, 0, 1), (1, 0, 0, 0, 1), (0, 1, 0, 0, 1), (0, 0, 1, 0, 1), (0, 0, 0, 1, 1)]))
    faces = np.array([(0, 1), (0, 2), (0, 3), (0, 4)])
    assert np.all(axis.faces == faces)
    colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue'), pg.Color('yellow')]
    assert np.all(axis.colors == colors)
    assert np.all([face == [(color, face) for color, face in zip(colors, faces)]][idx] for idx, face in enumerate(axis.color_faces))
    assert axis.draw_vertices == False
    assert axis.label == 'XYZW'

def test_transformations(mocker):
    mock_translate = mocker.patch('obj4dviewer.object.translate', return_value = np.identity(5))
    mock_scale = mocker.patch('obj4dviewer.object.scale', return_value = np.identity(5))
    mock_rotate_x = mocker.patch('obj4dviewer.object.rotate_x', return_value = np.identity(5))
    mock_rotate_y = mocker.patch('obj4dviewer.object.rotate_y', return_value = np.identity(5))
    mock_rotate_z = mocker.patch('obj4dviewer.object.rotate_z', return_value = np.identity(5))
    
    mock_rotate_zw = mocker.patch('obj4dviewer.object.rotate_zw', return_value = np.identity(5))
    mock_rotate_yw = mocker.patch('obj4dviewer.object.rotate_yw', return_value = np.identity(5))
    mock_rotate_yz = mocker.patch('obj4dviewer.object.rotate_yz', return_value = np.identity(5))
    mock_rotate_xw = mocker.patch('obj4dviewer.object.rotate_xw', return_value = np.identity(5))
    mock_rotate_xz = mocker.patch('obj4dviewer.object.rotate_xz', return_value = np.identity(5))
    mock_rotate_xy = mocker.patch('obj4dviewer.object.rotate_xy', return_value = np.identity(5))

    pos = np.array([1,2,3,4])
    angle = np.pi/4
    scale_to = 2
    verts = np.array([(0, 0, 0, 0, 1), (1, 0, 0, 0, 1)])

    obj = Object(vertices=verts)

    obj.translate(pos)
    mock_translate.assert_called_once_with(pos)
    assert np.all(obj.vertices == verts) # multiplied by identity matrix

    obj.scale(scale_to)
    mock_scale.assert_called_once_with(scale_to)
    assert np.all(obj.vertices == verts) # multiplied by identity matrix

    obj.rotate_x(angle)
    mock_rotate_x.assert_called_once_with(angle)
    assert np.all(obj.vertices == verts) # multiplied by identity matrix

    obj.rotate_y(angle)
    mock_rotate_y.assert_called_once_with(angle)
    assert np.all(obj.vertices == verts) # multiplied by identity matrix

    obj.rotate_z(angle)
    mock_rotate_z.assert_called_once_with(angle)
    assert np.all(obj.vertices == verts) # multiplied by identity matrix

    obj.rotate_zw(angle)
    mock_rotate_zw.assert_called_once_with(angle)
    assert np.all(obj.vertices == verts) # multiplied by identity matrix

    obj.rotate_yw(angle)
    mock_rotate_yw.assert_called_once_with(angle)
    assert np.all(obj.vertices == verts) # multiplied by identity matrix

    obj.rotate_yz(angle)
    mock_rotate_yz.assert_called_once_with(angle)
    assert np.all(obj.vertices == verts) # multiplied by identity matrix

    obj.rotate_xw(angle)
    mock_rotate_xw.assert_called_once_with(angle)
    assert np.all(obj.vertices == verts) # multiplied by identity matrix

    obj.rotate_xz(angle)
    mock_rotate_xz.assert_called_once_with(angle)
    assert np.all(obj.vertices == verts) # multiplied by identity matrix

    obj.rotate_xy(angle)
    mock_rotate_xy.assert_called_once_with(angle)
    assert np.all(obj.vertices == verts) # multiplied by identity matrix

def test_any_func():
    arr = np.array([1,2,3])
    assert any_func(arr, 1,2,3) == True
    assert any_func(arr, 4,5,6) == False
    
    assert any_func(arr, 1,5,6) == True
    assert any_func(arr, 4,2,6) == True
    assert any_func(arr, 4,5,3) == True

    assert any_func(arr, 1,2,6) == True
    assert any_func(arr, 4,2,3) == True
    assert any_func(arr, 1,5,3) == True

def test_obj_init_pos():
    obj = Object()
    assert np.all(obj.position == np.array([0,0,0,0,1]))