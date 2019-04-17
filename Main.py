import random

import numpy as np
from pyexcel_xls import get_data

import Visualizer

# CONSTS
COLUMN_LINE_WIDTH_DATA = 3
INITIAL_LINE_POINTS_DATA = 5


def random_polygons(n, title):
    array_polygons = []
    for i in range(0, n):
        array_point = np.random.rand(random.randint(2, 4), 2)
        polygon = Visualizer.create_polygon(array_point)
        array_polygons.append(polygon)
    Visualizer.plot_polygons(array_polygons, title, 1, 1)


def plot_polygons_from_file_txt(file_name, title):
    file = open(file_name, "r")
    line = file.readline()
    x_lim = float(line)
    y_lim = x_lim
    array_polygons = []
    amount_polygons = 0
    while line != "#":
        if line == "QUANTITY":
            amount_polygons = int(file.readline())
            line = amount_polygons
        elif line == "VERTICES (X,Y)":
            line = file.readline()
            array_points_tuple = []
            while line != "\n":
                points = line.split()
                array_points_tuple.append((float(points[0]), float(points[1])))
                line = file.readline()
            for i in range(amount_polygons):
                array_polygons.append(Visualizer.create_polygon(np.array(array_points_tuple)))
        else:
            line = file.readline().strip()
    Visualizer.plot_polygons(array_polygons, title, x_lim, y_lim)


def plot_polygons_from_file_xls(file_name, sheet, title):
    data = get_data(file_name)
    x_lim = data[sheet][COLUMN_LINE_WIDTH_DATA][COLUMN_LINE_WIDTH_DATA]
    y_lim = data[sheet][COLUMN_LINE_WIDTH_DATA][COLUMN_LINE_WIDTH_DATA]
    array_polygons = []
    array_points_x = []
    array_points_y = []
    for i in range(INITIAL_LINE_POINTS_DATA, len(data[sheet])):
        for j in range(len(data[sheet][i])):
            if data[sheet][i][j] == "x":
                amount_polygons = data[sheet][i][j-1]
                j = j + 1
                while j < len(data[sheet][i]):
                    array_points_x.append(data[sheet][i][j])
                    array_points_y.append(data[sheet][i + 1][j])
                    j = j + 1
                i = i + 1
                array_points_tuple = list(zip(array_points_x, array_points_y))
                array_points_x = []
                array_points_y = []
                for _ in range(amount_polygons):
                    array_polygons.append(Visualizer.create_polygon(np.array(array_points_tuple)))
    Visualizer.plot_polygons(array_polygons, title, x_lim, y_lim)


def main():
    # random_polygons(10, "Test of random polygons")
    # plot_polygons_from_file_xls("Test/dighe.xls", "Dighe1", "Test of instance Dighe.xls")
    # plot_polygons_from_file_xls("Test/dighe.xls", "Dighe2", "Test of instance Dighe.xls")
    # plot_polygons_from_file_xls("Test/albano.xls", "Albano", "Test of instance Albano.xls")
    # plot_polygons_from_file_xls("Test/fu.xls", "Fu", "Test of instance Fu.xls")
    # plot_polygons_from_file_xls("Test/han.xls", "Han", "Test of instance Han.xls")
    # plot_polygons_from_file_xls("Test/jakobs.xls", "Jakobs1", "Test of instance jakobs.xls")
    # plot_polygons_from_file_xls("Test/jakobs.xls", "Jakobs2", "Test of instance jakobs.xls")
    # plot_polygons_from_file_xls("Test/mao.xls", "Mao", "Test of instance mao.xls")
    plot_polygons_from_file_xls("Test/marques.xls", "Marques", "Test of instance marques.xls")
    # plot_polygons_from_file_xls("Test/dagli.xls", "Dagli", "Test of instance dagli.xls")
    # plot_polygons_from_file_txt("Test/shapes.txt", "Test of instance shapes.txt")
    # plot_polygons_from_file_txt("Test/blaz.txt", "Test of instance blaz.txt")
    # plot_polygons_from_file_txt("Test/shirts.txt", "Test of instance shirts.txt")
    # plot_polygons_from_file_txt("Test/swim.txt", "Test of instance swim.txt")
    # plot_polygons_from_file_txt("Test/trousers.txt", "Test of instance trousers.txt")


if __name__ == "__main__":
    main()
