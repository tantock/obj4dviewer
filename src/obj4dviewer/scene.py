from obj4dviewer.camera import Camera
from obj4dviewer.camera_controller import CameraController
from obj4dviewer.object import Object
from obj4dviewer import model_file_handler
import os

class Scene:
    def __init__(self):
        self.objects = {}
        self.autoincrement_obj_id = 0
        self.camera = None

    def init_camera(self, camera:Camera):
        self.camera = camera
        self.camera_controller = CameraController(camera)

    def load_object_from_file(self, filename) -> int:
        return self.add_object(self.get_object_from_file(filename))
    
    def add_object(self, object:Object) -> int:
        id = self.autoincrement_obj_id
        self.objects[id] = object
        self.autoincrement_obj_id += 1
        return id
    
    def pop_object(self, id:int) -> Object:
        return self.objects.pop(id)
    
    def get_object(self, id:int) -> Object:
        return self.objects[id]

    def get_object_from_file(self, filename):
        file, file_extension = os.path.splitext(filename)
        obj = None
        match file_extension:
            case '.obj':
                obj = model_file_handler.handle_obj_file(filename)
            case '.obj4':
                obj = model_file_handler.handle_obj4_file(filename)
            case _:
                raise NotImplementedError(f"No handler for extension: {file_extension}")
        
        return obj