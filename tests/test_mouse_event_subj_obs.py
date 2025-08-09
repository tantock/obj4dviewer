from obj4dviewer.mouse_event_subj_obs import *
import pytest

@pytest.fixture
def init_subj_obs():
    subj = MouseScrollSubject()
    obs = CameraMouseScrollObserver(None,None,None)
    subj.attach(obs)
    yield subj, obs
    subj.detach(obs)

def test_subj_attach_obs(init_subj_obs):
    subj , obs = init_subj_obs
    assert len(subj._observers) == 1
    assert subj._observers[0] == obs

def test_subj_detach_obs():
    subj = MouseScrollSubject()
    obs = CameraMouseScrollObserver(None,None,None)
    subj.attach(obs)
    assert len(subj._observers) == 1
    assert subj._observers[0] == obs
    subj.detach(obs)
    assert len(subj._observers) == 0

def test_update(mocker):
    mock_obs = mocker.Mock()
    subj = MouseScrollSubject()
    subj.attach(mock_obs)
    
    subj.update_scroll_direction((0,1))
    mock_obs.update.assert_called_once_with(subj)