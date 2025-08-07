from obj4dviewer.model_file_handler import *
from unittest.mock import patch, mock_open
import numpy as np
import pygame as pg

def test_obj_file_tokenizer():
    pg.init()
    with patch("builtins.open", mock_open(read_data="v 1 2 3\nv 4 5 6\nv 7 8 9\nf 1 2\nf 2 3")) as mock_file:
        obj = tokenize_obj_file("path/test.obj", [0,1])
        assert len(obj.vertices) == 3
        assert len(obj.faces) == 2
        assert np.allclose(obj.vertices[0], [1.,2.,3.,0.,1.])
        assert np.allclose(obj.vertices[1], [4.,5.,6.,0.,1.])
        assert np.allclose(obj.vertices[2], [7.,8.,9.,0.,1.])
        assert np.all(obj.faces[0] == [0,1])
        assert np.all(obj.faces[1] == [1,2])

    mock_file.assert_called_with("path/test.obj")

def test_handle_obj4_file_open():
    pg.init()
    with patch("builtins.open", mock_open(read_data="v 1 2 3 4\nv 5 6 7 8\nf 1 2")) as mock_file:
        obj = handle_obj4_file("path/test.obj4")
        assert len(obj.vertices) == 2
        assert np.allclose(obj.vertices[0], [1.,2.,3.,4.,1.])
        assert np.allclose(obj.vertices[1], [5.,6.,7.,8.,1.])
        assert np.all(obj.faces[0] == [0,1])

    mock_file.assert_called_with("path/test.obj4")

def test_handle_obj_file_open():
    pg.init()
    with patch("builtins.open", mock_open(read_data="v 1 2 3\nv 4 5 6\nv 7 8 9\nf 1 2\nf 2 3")) as mock_file:
        obj = handle_obj_file("path/test.obj")
        assert len(obj.vertices) == 3
        assert len(obj.faces) == 2
        assert np.allclose(obj.vertices[0], [1.,2.,3.,0.,1.])
        assert np.allclose(obj.vertices[1], [4.,5.,6.,0.,1.])
        assert np.allclose(obj.vertices[2], [7.,8.,9.,0.,1.])
        assert np.all(obj.faces[0] == [0,1])
        assert np.all(obj.faces[1] == [1,2])

    mock_file.assert_called_with("path/test.obj")