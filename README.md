## How to Run
```
pip3 install matplotlib
pip3 install pyexcel-xls
sudo apt-get install python3-tk
python3 main.py
```
## Functions: file (Visualizer.py)

### Constructor
`
constructor = parameters: array_polygons (array of type Polygon, required), title (String, required), x_lim (Integer, required) y_lim (Integer, required)
`

### plot_polygons

### plot_animation

## Functions: file (File.py)
###  polygons_from_xls
`
parameters: file_name (String, required), sheet (String, required):
`

`
return: List of type Polygon(), limit_x (int)
`

###  polygons_from_txt
`
parameters: file_name (String, required):
`

`
return: List of type Polygon(), limit_x (int)
`

###  return_limits_of_board_xls
`
parameters: file_name (String, required), sheet (String, required):
`

`
return: x_lim (float)
`

###  return_limits_of_board_txt
`
parameters: file_name (String, required), sheet (String, required):
`

`
return: x_lim (float)
`
## Functions: file (Polygon.py)
### create_polygon
`
parameters: polygon_points (array of typle (x,y), required):
`

`
return: Polygon()
`
### set_points_to_positive
`
parameters: polygon_points (array of tuple (x,y), required):
`

`
return: array of tuple (x,y)
`
