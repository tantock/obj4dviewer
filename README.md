# obj4dviewer
[![Unit Tests](https://github.com/tantock/obj4dviewer/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/tantock/obj4dviewer/actions/workflows/unit-tests.yml) [![Coverage](https://github.com/tantock/obj4dviewer/actions/workflows/coverage.yaml/badge.svg)](https://github.com/tantock/obj4dviewer/actions/workflows/coverage.yaml)

Python 4D Engine (Object Renderer) with Pygame, Numpy, Numba

![sofware_renderer](screenshots/1.png "sofware_renderer")

## About The Project
This is a viewer for 4D objects. It projects a 4D object onto a 3D plane, and then from a 3D plane to a 2D screen. It is backwards compatible with regular 3D obj files. A 4d obj file specified with the .obj4 extension.

# Getting Started
## Installation
Clone the repo with
```
git clone https://github.com/tantock/obj4dviewer.git
```
In the project root directory, run
```
pip install -e .
```
to install the obj4drender library and the project dependencies.

### Optional Dependencies

To install other optional dependencies (test/build) run
```
pip install -e .[test]
```
```
pip install -e .[build]
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This software is covered by the MIT License. To read more about the MIT License, see [License](https://github.com/tantock/obj4dviewer/blob/main/LICENSE).

## Acknowledgments

- [StanislavPetrovV](https://github.com/StanislavPetrovV) 
    - This project would not have been possible without the base code provided by [StanislavPetrovV](https://github.com/StanislavPetrovV). Many thanks for their hard work and their accompanying video at [YT video](https://www.youtube.com/watch?v=M_Hx0g5vFko)