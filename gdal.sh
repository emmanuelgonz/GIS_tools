#!/usr/bin/env bash

sudo apt-get install python3.6-dev
sudo apt install python3-pip
pip3 install numpy
pip3 install matplotlib
pip3 install rasterio
pip3 install shapely
pip3 install geopandas
pip3 install earthpy
wget http://download.osgeo.org/libspatialindex/spatialindex-src-1.7.1.tar.gz
tar -xvf spatialindex-src-1.7.1.tar.gz
cd spatialindex-src-1.7.1/
sudo ./configure; sudo make; sudo make install
sudo ldconfig
pip3 install Rtree
pip3 install earthpy
pip3 install seaborn
sudo add-apt-repository ppa:ubuntugis/ppa
sudo apt-get update
sudo apt-get install gdal-bin
sudo apt-get install libgdal-dev
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal
sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
sudo apt-get update
sudo apt-get install libgdal-dev
pip3 install GDAL==3.0.4
