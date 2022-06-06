import math
import wget
from stl import mesh


def rotate_model(url):
    # Function that take url
    # for a model and rotate
    # 180 degree around y-axix
    wget.download(url, 'raw_039.stl')
    your_mesh = mesh.Mesh.from_file('raw_039.stl')
    your_mesh.rotate([0.0, 0.5, 0.0], math.radians(180))
    your_mesh.save('raw_039_rotated.stl')


if __name__ == '__main__':
    rotate_model(url='https://nervous-mouse.s3.eu-central-1.amazonaws.com/raw_039.stl')
