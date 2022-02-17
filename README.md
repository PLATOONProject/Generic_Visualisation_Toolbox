
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

Each of the visualization tools that form the toolbox is defined as a separate Python Function:

•	heatmap: 
Description: Plot heatmap.
Inputs:
obj: input data.
xvar: column from input data to on x axis.
yvar: column from input data to plot on y axis.
value: column from input data (of format int or float) to format the colors.
width: width of plot.
height: height of plot.
hoover_format: variables to include in the hoover tool. Default None.v.g. [('label1', '@column_name1'), ('label2', '@column_name2')]
color_low: value in data to match with the end of the color map.
color_high: value in data to match with the start of the color map.
title: title of plot. Default None.
colorbar: plot color bar to the right of the plot.
xrange: list of x axis tickers.
yrange: list of y axis tickers.
palette: name of color palette or list of HEX color codes. Default None. If None the palette brewer 'orange-yellow-green' is used. Accepts any brewer palette name that contains at least a 9 colours.
reverse: reverse color mapping.
Output: bokeh figure.

•	histograms
Description: create a histogram figure for each column in obj that are of type bool, int or float.
Inputs:
obj: input data.
groupby: name of column to group columns in independent correlation matrices.
width: width of plot in pixels.
height: height of plot in pixels.
title: title of plot.
color: color or palette of colors to use in the plot.
bins: number of bins in histograms.
hoover: include a hoover tool. Default True.
Output: bokeh figure

•	correlation
Description: plot correlation matrix between columns in pandas data frame.
Inputs:
obj: input data
method: correlation method. Default 'spearman'. Accepted values are 'spearman', ‘pearson’and ‘kendall’.
groupby: name of column to group columns in independent correlation matrices.
plot_unique: plot unique correlation pairs only (triangular shape).
width: width of plot in pixels.
height: height of plot in pixels.
title: title of plot.
color_palette: color palette for plot.
add_text: print the correlation coefficient inside each square.
hoover: add hoover tool to plot.
Output: bokeh figure

•	time_lines
Description: Creates a time series line plot.
Inputs:
obj: input data.
yvar: columns names in data to plot in the y axis.
xvar: column or index name to plot in the x axis. Default None. If None the indexwill plot on the x axis.
xrange: x range in the format (min, max) or bokeh.figure.x_range. Default None.
                If None the x axis shows the first 1/10 of the x variable data.
yrange: y range in the format (min, max). If None the default y axis range is shown.
groupby: name of column to used to group the data. If None data is not grouped.
highlight: columns names of variables in the y axis to be ploted with a thicker line.
line_width: width of lines.
color: color of line.
color_palette: palette of color as list of HEX codes to use in case of more than one group of data or variable per plot. Default None. In None, a comination of brewerpalettes is used.
height: height of plot in pixels. Default 400.
width: width of plot in pixels. Default 1600.
legend_location: legend location.
title: title of plot. Default None. If None the title is a list of the names of the variables plotted in the y axis.
toolbar: tools to include in the tool bar.
hoover: include a hoover tool. Default True.
hoover_tips: variables to include in the hoover tool. Default None. If None the hoover tool shows the y axis value. v.g. [('label', '@column_name')]
Output: bokeh figure.

•	time_lines_and_dots
Description: Plot a combination of time series line and scatter graph.
Inputs:
obj: input table for line plot.
yvar: column name or list of column names from the input table to plot on the y axis.
xvar: column name from table to plot on the x axis. Default None. If None, the index
of the input table will be plotted on the x axis.
xrange: range of x axis in format (min, max).
yrange: range of y axis in format (min, max).
groupby: name of column in input table to use to group samples in plot.
line_color_palette: palette of color as list of HEX codes to use in case of more than
one group of data or variables per plot. Default None. In None, a combination of brewer palettes is used.
line_width: width of lines.
dots_color_palette: palette of color as list of HEX codes to use in case of more than
one group of data or variables per plot. Default None. In None, a combination of brewer palettes is used.
dots: input table for scatter plot.
dots_yvar: column name or list of column names from input scatter table to plot on the y axis.
dots_size: size of dots.
dots_groupby: name of column in input scatter table to use to group samples in plot.
dots_xvar: column name from dots table to plot on the x axis. Default None. If None, the index of the input dots table will be plotted on the x axis.
height: height of figure in pixels.
width: width of figure in pixels.
title: title of figure.
hoover: include a hoover tool. Default True.
hoover_tips: variables to include in the hoover tool. Default None. If None the
hoover tool shows the y axis value. v.g. [('label', '@column_name')]
toolbar: tools to include in the tool bar.
legend_location: legend location in figure. Default 'center_right'.
Output: bokeh figure

•	time_bars
Description: Plot a time series bar plot.
Inputs:
obj: input data.
yvar: columns names in data to plot in the y axis.
xvar: column or index name to plot in the x axis. Default None. If None the index will plot on the x axis.
xrange: x range in the format (min, max) or bokeh.figure.x_range. Default None. If None the x axis shows the first 1/10 of the x variable data.
yrange: y range in the format (min, max). If None the default y axis range is shown.
groupby: name of column to used to group the data. If None data is not grouped.
color: color of bars, only effective when groupby is None. Default None. If None, the brewer['Set3'] palette is used.
color_palette: palette of color as list of HEX codes to use in case of more than
one group of data or variables per plot. Default None. In None, a combination of brewer palettes is used.
bar_width: width of bars. Default 1.
height: height of plot in pixels. Default 400.
width: width of plot in pixels. Default 1600.
title: title of plot. Default None. If None the title is a list of the names of the variables plotted in the y axis.
toolbar: tools to include in the tool bar.
legend_location: legend location.
hoover: include a hoover tool. Default True.
hoover_tips: variables to include in the hoover tool. Default None. If None the
hoover tool shows the y axis value. v.g. [('label', '@column_name')]
Output: bokeh figure.

•	time_scatter: 
Description:Creates a time series scatter plot.
Inputs:
obj: input data.
yvar: columns names in data to plot in the y axis.
xvar: column or index name to plot in the x axis. Default None. If None the index will plot on the x axis.
xrange: x range in the format (min, max) or bokeh.figure.x_range. Default None.If None the x axis shows the first 1/10 of the x variable data.
yrange: y range in the format (min, max). If None the default y axis range is shown.
groupby: name of column to used to group the data. If None data is not grouped.
color: color of dots, only effective when groupby is None. Default None. If None,the brewer['Set3'] palette is used.
color_palette: palette of color as list of HEX codes to use in case of more than one group of data or variable per plot. Default None. In None, a combination of brewer 'Set' palettes is used.
height: height of plot in pixels. Default 400.
width: width of plot in pixels. Default 1600.
legend_location: legend location.
size: size of dots. Default 12.
alpha: transparency factor of dots (0->transparent, 1->non-transparent). Default 0.8
title: title of plot. Default None. If None the title is a list of the names of the
 variables plotted in the y axis.
toolbar: tools to include in the tool bar.
hoover: include a hoover tool. Default True.
hoover_tips: variables to include in the hoover tool. Default None. If None the
hoover tool shows the y axis value. v.g. [('label', '@column_name')]
Output: bokeh figure.
•	time_range_tool
Description: Plots a range selection tool for time series plots with xpan tools.
Inputs:
obj: input data.
yvar: columns name in data to plot in the y axis.
xrange: x range in the format (min, max) or a bokeh.figure.x_range.
xvar: column or index name to plot in the x axis. Default None. If None the index will plot on the x axis.
yrange: y range in the format (min, max). If None the default y axis range is shown.
height: height of plot in pixels. Default 120.
width: width of plot in pixels. Default 1600.
Output bokeh figure.
TypeError: if yvar column is not data type numeric.

•	scatter:
Description: Scatter plot + Histograms on x and y axis + regression line/curve.
Inputs:
obj: input table.
xvar: name of column in table to plot on the x axis.
yvar: name of column in table to plot on the y axis.
size: size of radius of markers in units, or name of the column on table to use
as marker size. Default 1 unit.
size_type: measure size in 'radius' or 'size'.
colorvar: name of column in table to map the color of the markers to. Column must be
dtype numerical.
color_asc: indicate if maximum colors are red (True) or blue(False).
color_max: indicate maximum value to colour as red (if asc), instead of variable maximum
marker_color: color of marker.
color_palette: palette of color as list of HEX codes to use in case of more than one
group of data or variable per plot. Default None. In None, a combination of
brewer 'Set' palettes is used.
color_alpha: transparency of fill color of marker (0-transparent, 1-opaque). Default 0.6.
groupby: name of column in table to group data in plot. Groups are differentiated
by marker color. Default None.
legend_location: legend location in figure. Default 'center_right'.
xrange: x range in the format (min, max) or bokeh.figure.x_range. Default None.
yrange: y range in the format (min, max) or bokeh.figure.y_range. Default None.
height: height of plot in pixels. Default 700.
width: width of plot in pixels. Default 700.
x_jitter: add jitter to categorical groups in x axis. Default 0, or no jitter.
hist_axes: plot histograms at the x and y axes. Default False.
nbins: number of bins to divided the histograms into. Default 10.
get_regression: compute and plot a regression estimator for each group in the data.
Default, False.
deg: degrees of freedom of the regression estimator. Default 1.
add_regression: regression fit function of the type returned by the numpy.poly1d.Default None.
hoover: display hoover tool tips. Default True.
hoover_tips: variables to include in the hoover tool v.g. [('label', '@column_name')].Default None. If None the hoover tool shows the y axis value.
toolbar: bokeh figure tools to include. Default 'pan,box_zoom,reset'.
title: title of plot.
xaxis_labels_map: dict used to override major x axis labels. Default None.
yaxis_labels_map: dict used to override major y axis labels. Default None.
Output: bokeh figure.

•	lines:
Description: Plot a line graph.
Inputs:
obj: input data.
yvar: columns names in data to plot in the y axis.
xvar: column or index name to plot in the x axis. Default None. If None the index
will plot on the x axis.
xrange: x range in the format (min, max) or bokeh.figure.x_range. Default None.If None the x axis shows the first 1/10 of the x variable data.
yrange: y range in the format (min, max). If None the default y axis range is shown.
groupby: name of column to used to group the data. If None data is not grouped.
highlight: columns names of variables in the y axis to be plotted with a thicker line.
line_width: width of lines.
hline: positions in the y axis where to draw a span line.
vline: positions in the x axis where to draw a span line.
color: color of lines, only effective when groupby is None. Default None. If None,
the brewer['Set1'] and brewer['Set2'] palette is used.
color_palette: palette of color as list of HEX codes to use in case of more than one group of data or variables per plot. Default None. In None, a combination of brewer
palettes is used.
legend_location: legend location in figure. Default 'center_right'.
height: height of plot in pixels. Default 400.
width: width of plot in pixels. Default 1600.
title: title of plot. Default None. If None the title is a list of the names of the variables plotted in the y axis.
toolbar: tools to include in the tool bar.
background: color of background. Default None. If None the background color is gray.
hoover: include a hoover tool. Default True.
hoover_tips: variables to include in the hoover tool. Default None. If None the hoover tool shows the y axis value. v.g. [('label', '@column_name')]
Output: bokeh figure.

•	plot_blanks:
Description: Plot data frame values as pixel intensity, using index as y axis values.
Inputs:
df: input data.
title: title of plot.
width: plot width in pixels.
height: plot height in pixels.
palette: name of bokeh color palette.
datetime_index: index of input data is of type datetime.
Output: bokeh figure.


•	plot:table:
Description: plot column data table.
Inputs:
obj: input data.
column_names: names of columns in obj to include in table. Default None. If None, all columns in obj will be included.
height: table height in pixels.
width: table width in pixels.
datetime_index: format the index column as datetime.
decimals: decimal places to show on numeric columns.
title: title of table. Default None.
Output: bokeh figure.

•	plot_text:
Description: Plot text box.
Inputs:
text: text to plot.
width: width of text box. Default 50.
height: height of tect box. Default 50.
angle: angle (radiants) to rotate the text from the horizontal. Default 0.
fontsize: font size of text. Default 12.
color: font color of text (HEX codes or English names). Default 'black'.
outline_color: color of outline around the text box. Default None (without outline).
Output: bokeh figure.

 

## 3 Built With

* [Bokeh](https://github.com/bokeh/bokeh)
* [Itertools](https://github.com/rust-itertools/itertools)
* [Logging](https://pypi.org/project/logging/)
* [Numpy] (https://github.com/numpy/numpy/)
* [Pandas] (https://github.com/pandas-dev/pandas/)
* [Typping]	(https://github.com/python/typing/)

## 4 License

Licensed under the Apache 2.0. See LICENSE.txt for more details. For respective licenses of individual components and libraries please refer to section 3.

## 5 Demo
A demo ("Platoon_demo.py") is provided which uses a Open Source Meteorological data from Copernicus Climate Data Store (meteo_cds.pkl)