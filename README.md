## How to Run
```
pip3 install matplotlib
pip3 install pyexcel-xls
sudo apt-get install python3-tk
python3 main.py
```
## Functions: file (Visualizer.py)

### create_polygon
`
parameters: polygon_points (numpy array, required)
`

`
return: Polygon()
`
### plot_polygons
`
parameters: array_polygons (array of type Polygon, required), title (String, required), x_lim (Integer, required) y_lim (Integer, required)
`
## Functions: file (File.py)

###  polygons_from_xls
`
parameters: file_name (String, required), sheet (String, required):
`

`
return: List of type Polygon()
`

###  polygons_from_txt
`
parameters: file_name (String, required):
`

`
return: List of type Polygon()
`

###  return_limits_of_board_xls
`
parameters: file_name (String, required), sheet (String, required):
`

`
return: tuple(float, float)
`

###  return_limits_of_board_txt
`
parameters: file_name (String, required), sheet (String, required):
`

`
return: tuple(float, float)
`

