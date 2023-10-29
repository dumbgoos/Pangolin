# Pangolin
This is a tool used to map seismic data.
***
## plot_well_curve
You can use this function to draw interactive images of different waves at different well depths.You can pass in parameters and draw an image like the following code.
```python
"""
well_name is the well's name in your data. please input 'info' as a Dataframe.
col_one and the rest of the parameters are used to select which waveform to draw.
"""
plot_well_curve(well_name, info, well_depth, col_one, col_two, col_three)
```
***
## plot_lines_hot
You can use this function to draw related images by passing in line's number and your data.
```python
plot_lines_hot(line_number, info)
```
