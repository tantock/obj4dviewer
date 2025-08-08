from obj4dviewer.subject_observer import Subject, Observer
from obj4dviewer.camera_controller import CameraController
from typing import List
class MouseScrollSubject(Subject):
    _state: tuple[int,int] = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def update_scroll_direction(self, direction:tuple) -> None:
        self._state = direction
        self.notify()

class CameraMouseScrollObserver(Observer):
    def __init__(self, camera_controller:CameraController, mouse_factor, mouse_speed):
        super().__init__()
        self.mouse_factor = mouse_factor
        self.mouse_speed = mouse_speed
        self.camera_controller = camera_controller
    def update(self, subject: Subject) -> None:
        self.camera_controller.camera_PitchRoll(subject._state[1]*self.mouse_factor*self.mouse_speed*100)