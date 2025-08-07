from obj4dviewer.object import Object

def handle_obj_file(filename):
    extra_dim = [0, 1]
    return tokenize_obj_file(filename, extra_dim)

def handle_obj4_file(filename):
    extra_dim = [1]
    return tokenize_obj_file(filename, extra_dim)

def tokenize_obj_file(filename, extra_dim:list[int]) -> Object:
    vertex, faces = [], []
    with open(filename) as f:
        for line in f:
            if line.startswith('v '):
                vertex.append([float(i) for i in line.split()[1:]] + extra_dim)
            elif line.startswith('f'):
                faces_ = line.split()[1:]
                faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
    return Object(vertex, faces)