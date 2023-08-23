"""
Programmer: Emily Bodenbender
Class: CPSC 322-02, Spring 2022
Programming Assignment #3
2/22/22

Description: Helper functions for data visualization with matplotlib.
"""
import matplotlib.pyplot as plt

import utils

def make_bar_chart(x, y, title, x_label, y_label, ticks=None, bar_labels=[], rotation=0, figsize=None, color=None,):
    """Plots a bar chart given values for the x and y axes.
    
    Args:
        x (list of int or str): x axis values
        y (list of int): y axis values
        title (str): bar chart title
        x_label (str): x axis label
        y_label (str): y axis label
        ticks (list of int): spacing between xticks
        bar_labels (list of int, double, or str): xtick labels
        rotation (int): rotation (degrees) of xtick labels
        figsize (tuple): figure width, height (in inches)
        color (list of str): colors for each bar
    """
    if figsize != None:
        plt.figure(figsize=figsize)
    else:
        plt.figure()
    plt.bar(x, y, color=color)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if ticks is None:
        ticks = x
    if bar_labels != []:
        plt.xticks(ticks, bar_labels, rotation=rotation)
    plt.show()

def make_pie_chart(x, y, title):
    """Generates a pie chart given labels and percentages.
    
    Args:
        x (list of str): labels
        y (list of float): percentages
        title (str): pie chart title
    """
    plt.figure()
    plt.pie(y, labels=x, autopct="%1.1f%%")
    plt.title(title)
    plt.show()

def make_histogram(data, title, xlabel, ylabel, num_xticks=0):
    """Generates a histogram for the given data.

    Args:
        data (list of int): data to calculate frequencies for
        title (str): histogram title
        xlabel (str): x axis label
        ylabel (str): y axis label
    """
    plt.figure()
    plt.hist(data, bins=10, edgecolor="black")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # optionally change number of ticks on x-axis
    if num_xticks != 0:
        plt.locator_params(axis="x", nbins=num_xticks)
    plt.show()

def make_scatter_plot(x, y, title, xlabel, ylabel, covariance, correlation_coeff):
    """Generate a scatter plot and perform least squares linear regression.
    
    Args:
        x (list of int): x axis values
        y (list of int): y axis values
        title (str): scatter plot title
        xlabel (str): x axis label
        ylabel (str): y axis label
        covariance (float): calculated covariance
        correlation_coeff (float): calculated correlation coefficient
    """
    plt.figure()
    plt.scatter(x, y)
    m, b = utils.compute_slope_intercept(x, y)
    plt.plot([min(x), max(x)], [m * min(x) + b, m * max(x) + b], c="r", lw=5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # label correlation coefficient and covariance
    annotation = "corr: " + "{:.2f}".format(correlation_coeff) + "; cov: " + "{:.2f}".format(covariance)
    plt.annotate(annotation, xy=(0.8, 0.95), xycoords="axes fraction", horizontalalignment="center")
    plt.show()

def make_box_plot(distributions, labels, title, xlabel, ylabel):
    plt.boxplot(distributions)
    plt.xticks(list(range(1, len(distributions) + 1)), labels, rotation=90)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()