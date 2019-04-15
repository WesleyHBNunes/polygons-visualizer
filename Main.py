import Visualizer
import random
import numpy as np


def main():
    array_polygons = []
    for i in range(0, 10):
        array_point = np.random.rand(random.randint(2, 4), 2)
        polygon = Visualizer.create_polygon(array_point)
        array_polygons.append(polygon)
    Visualizer.plot_polygons(array_polygons, "Test to plot random polygons")


if __name__ == "__main__":
    main()
