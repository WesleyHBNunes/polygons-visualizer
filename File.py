from pyexcel_xls import get_data
import Visualizer
import numpy as np

# CONSTS
COLUMN_LINE_WIDTH_DATA = 3
INITIAL_LINE_POINTS_DATA = 5


def polygons_from_xls(file_name, sheet):
    data = get_data(file_name)
    array_polygons = []
    array_points_x = []
    array_points_y = []
    for i in range(INITIAL_LINE_POINTS_DATA, len(data[sheet])):
        for j in range(len(data[sheet][i])):
            if data[sheet][i][j] == "x":
                amount_polygons = data[sheet][i][j - 1]
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
    return array_polygons


def polygons_from_txt(file_name):
    file = open(file_name, "r")
    line = file.readline()
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
    file.close()
    return array_polygons


def return_limits_of_board_xls(file_name, sheet):
    data = get_data(file_name)
    x_lim = float(data[sheet][COLUMN_LINE_WIDTH_DATA][COLUMN_LINE_WIDTH_DATA])
    y_lim = float(data[sheet][COLUMN_LINE_WIDTH_DATA][COLUMN_LINE_WIDTH_DATA])
    return x_lim, y_lim


def return_limits_of_board_txt(file_name):
    file = open(file_name, "r")
    line = file.readline()
    x_lim = float(line)
    y_lim = x_lim
    file.close()
    return x_lim, y_lim
