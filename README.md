
# PLATOON Generic Visualisation Toolbox

Set of Open Source Generic Visualisation tools. The Visualisation Toolbox includes different plotting tools for different type of charts such as Line Plots, Bar Plots, Scatter Plots, Histograms, Heatmaps and others. 
The Open-source Generic Visualisation Toolbox has been funded by the PLATOON H2020 project funded by the EU commission.

## 1. Purpose

The Visualisation Toolbox is coded in Python and makes use of existing open source libraries .
The are several advanced plotting libraries in Python that offer multiple  capabilities . However, some of these libraries are  difficult to configure and reuse by users with low coding skills. 
In this project we have developed a top-level soft layer formed of several functions that facilitates the configuration and implementation of thesse libraries by energy experts with low-medium coding skills.
The individual visualisation tools can be combined to create dynamic dashboards

## 2. Repository Structure

The Generic Visualisation Toolbox is formed of 13 different tools listed below that provide a separate functionality:
1.	Heatmap: heatmap plot.
2.	Histograms: histogram plot.
3.	Correlation: correlation matrix plot.
4.	Time_lines: time series line plot.
5.	Time_lines_and_dots: combination of time series line and scatter graph.
6.	Time_bars: time series bar plot.
7.	Time_scatter: time series scatter plot.
8.	Time_range_tool: Plots a range selection tool for time series plots with xpan tools.
9.	Scatter: Scatter plot with histograms on x and y axis and regression line/curve.
10.	Lines: line graph
11.	Plot_blanks: plots data frame values as pixel intensity, using index as y axis values.
12.	Plot_table: plot column data table.
13.	Plot_text: plots a text box.

Each of the visualization tools that form the toolbox is defined as a separate Python Function.


## 3 Built With

* [Bokeh](https://github.com/bokeh/bokeh)
* [Itertools](https://github.com/rust-itertools/itertools)
* [Logging](https://pypi.org/project/logging)
* [Numpy] (https://github.com/numpy/numpy)
* [Pandas] (https://github.com/pandas-dev/pandas)
* [Typping] (https://github.com/python/typing)

## 4 License

Licensed under the Apache 2.0. See LICENSE.txt for more details. For respective licenses of individual components and libraries please refer to section 3.

## 5 Demo
A demo ("Platoon_demo.py") is provided which uses a Open Source Meteorological data from Copernicus Climate Data Store (meteo_cds.pkl)