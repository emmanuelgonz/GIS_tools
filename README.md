# GIS_tools
A collection of python scripts for various GIS tasks. 

## Adding GPS coordinates to EXIF metadata
The script `add_exif_tif.py` adds EXIF metadata to TIF files. Just feed it the directory where your files are located. 

## Collecting GPS coordinates in CSV file
The script `img_coords_b2t_up.py` collects all corner coordinates (upper left, lower left, etc.). It generates a CSV file with filename and all coordinates. Just feed it the directory where your files are located.  

## Editing GPS coordinates
The script `edit_gps.py` edits the corner coordinates within your TIF file. Just feed it the directory where your files are located and a CSV file with your coordinates which must contain the headers: Filename, Upper left, Lower right.

