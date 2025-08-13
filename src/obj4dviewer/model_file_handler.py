from obj4dviewer.object import Object

def handle_obj_file(filename):
    extra_dim = [0, 1]
    return tokenize_obj_file(filename, extra_dim)

def handle_obj4_file(filename):
    extra_dim = [1]
    return tokenize_obj_file(filename, extra_dim)

def tokenize_obj_file(filename, extra_dim:list[int]) -> Object:
    vertex, vertex_normals, faces, cells = [], [], [], []
    with open(filename) as f:
        for line in f:
            if line.startswith('v '):
                vertex.append([float(i) for i in line.split()[1:]] + extra_dim)
            elif line.startswith('vn '):
                vertex_normals.append([float(i) for i in line.split()[1:]] + extra_dim)
            elif line.startswith('f '):
                faces_ = line.split()[1:]
                faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
            elif line.startswith('c '):
                cells_ = line.split()[1:]
                cells.append([int(cell_.split('/')[0]) - 1 for cell_ in cells_])
        if len(vertex) == 0:
            vertex = None
        if len(vertex_normals) == 0:
            vertex_normals = None
        if len(faces) == 0:
            faces = None
        if len(cells) == 0:
            cells = None

    return Object(vertices=vertex, faces=faces, vertex_normals=vertex_normals, cells=cells)