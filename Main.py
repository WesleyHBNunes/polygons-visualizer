import File
from Visualizer import Visualizer


def main():
    polygons, limits = File.polygons_from_xls("Test/han.xls", "Han")
    visualizer = Visualizer(polygons, limits[0], limits[1], "Title animation plot")
    visualizer.plot_polygons()
    # visualizer.plot_animation()


if __name__ == "__main__":
    main()
