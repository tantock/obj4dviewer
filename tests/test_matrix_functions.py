from obj4drender.matrix_functions import *

def init_vector():
        return np.array([1,2,3,4,1]) #x,y,z,w,h
def test_translate():
    vec = init_vector()
    np.testing.assert_array_equal(vec @ translate([0,0,0,0]), init_vector())
    np.testing.assert_array_equal(vec @ translate([5,1,2,8]), np.array([6,3,5,12,1]))
    np.testing.assert_array_equal(vec @ translate([-5,-1,-2,-8]), np.array([-4,1,1,-4,1]))

def test_scale():
    vec = init_vector()
    np.testing.assert_array_equal(vec @ scale(1), init_vector())
    np.testing.assert_array_equal(vec @ scale(2), np.array([2,4,6,8,1]))

def test_rotate():
    vec = init_vector()
    np.testing.assert_array_almost_equal(vec @ rotate_zw(0), init_vector())

    np.testing.assert_array_almost_equal(vec @ rotate_zw(np.pi/2), np.array([-2,1,3,4,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_yw(np.pi/2), np.array([-3,2,1,4,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_yz(np.pi/2), np.array([-4,2,3,1,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_xw(np.pi/2), np.array([1,-3,2,4,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_xz(np.pi/2), np.array([1,-4,3,2,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_xy(np.pi/2), np.array([1,2,-4,3,1]))

    
    np.testing.assert_array_almost_equal(vec @ rotate_zw(-np.pi/2), np.array([2,-1,3,4,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_yw(-np.pi/2), np.array([3,2,-1,4,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_yz(-np.pi/2), np.array([4,2,3,-1,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_xw(-np.pi/2), np.array([1,3,-2,4,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_xz(-np.pi/2), np.array([1,4,3,-2,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_xy(-np.pi/2), np.array([1,2,4,-3,1]))
    
    np.testing.assert_array_almost_equal(vec @ rotate_zw(np.pi), np.array([-1,-2,3,4,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_yw(np.pi), np.array([-1,2,-3,4,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_yz(np.pi), np.array([-1,2,3,-4,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_xw(np.pi), np.array([1,-2,-3,4,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_xz(np.pi), np.array([1,-2,3,-4,1]))
    np.testing.assert_array_almost_equal(vec @ rotate_xy(np.pi), np.array([1,2,-3,-4,1]))