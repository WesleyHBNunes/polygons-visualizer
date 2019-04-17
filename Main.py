import random
import numpy as np
import Visualizer
import File


def random_polygons(n, title):
    array_polygons = []
    for i in range(0, n):
        array_point = np.random.rand(random.randint(2, 4), 2)
        polygon = Visualizer.create_polygon(array_point)
        array_polygons.append(polygon)
    Visualizer.plot_polygons(array_polygons, title, 1, 1)


def main():
    # random_polygons(10, "Test of random polygons")
    limits_xls = File.return_limits_of_board_xls("Test/marques.xls", "Marques")
    Visualizer.plot_polygons(File.polygons_from_xls("Test/marques.xls", "Marques"), "Test of instance marques.xls",
                             limits_xls[0], limits_xls[1])
    # limits_txt = File.return_limits_of_board_txt("Test/trousers.txt")
    # Visualizer.plot_polygons(File.polygons_from_txt("Test/trousers.txt"), "Test of instance trousers.txt",
    #                          limits_txt[0], limits_txt[1])


if __name__ == "__main__":
    main()
