import random

import numpy as np
from pyexcel_xls import get_data

import Visualizer

# CONSTS
COLLUM_LINE_WIDTH_DATA = 3
INITIAL_LINE_POINTS_DATA = 5


def random_polygons(n, title):
    array_polygons = []
    for i in range(0, n):
        array_point = np.random.rand(random.randint(2, 4), 2)
        polygon = Visualizer.create_polygon(array_point)
        array_polygons.append(polygon)
    Visualizer.plot_polygons(array_polygons, title)


def polygons_from_file_xls(file_name, sheet, title):
    data = get_data(file_name)
    x_lim = data[sheet][COLLUM_LINE_WIDTH_DATA][COLLUM_LINE_WIDTH_DATA]
    y_lim = data[sheet][COLLUM_LINE_WIDTH_DATA][COLLUM_LINE_WIDTH_DATA]
    array_polygons = []
    array_points_x = []
    array_points_y = []
    for i in range(INITIAL_LINE_POINTS_DATA, len(data[sheet])):
        for j in range(len(data[sheet][i])):
            if data[sheet][i][j] == "x":
                j = j + 1
                while j < len(data[sheet][i]):
                    array_points_x.append(data[sheet][i][j])
                    array_points_y.append(data[sheet][i + 1][j])
                    j = j + 1
                i = i + 1
                array_points_tuple = list(zip(array_points_x, array_points_y))
                array_points_x = []
                array_points_y = []
                array_polygons.append(Visualizer.create_polygon(np.array(array_points_tuple)))
    Visualizer.plot_polygons(array_polygons, title, x_lim, y_lim)


def main():
    # random_polygons(5, "Test of random polygons")
    polygons_from_file_xls("Test/dighe.xls", "Dighe1", "Test of instance Dighe.xls")
    # polygons_from_file_xls("Test/dighe.xls", "Dighe2", "Test of instance Dighe.xls")
    # polygons_from_file_xls("Test/albano.xls", "Albano", "Test of instance Albano.xls")


if __name__ == "__main__":
    main()
