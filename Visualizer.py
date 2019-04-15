import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection


fig, ax = plt.subplots()


def create_polygon(polygons_points):
    polygon = Polygon(polygons_points, True)
    return polygon


def plot_polygons(array_polygons, title, x_lim, y_lim):
    colors = 100 * np.random.rand(len(array_polygons))
    p = PatchCollection(array_polygons, alpha=0.4)
    p.set_array(np.array(colors))
    ax.set_xlim((0, x_lim))
    ax.set_ylim((0, y_lim))
    ax.set_title(title)
    ax.add_collection(p)
    fig.colorbar(p, ax=ax)
    plt.show()
