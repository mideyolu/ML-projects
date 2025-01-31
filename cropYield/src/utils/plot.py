# src/utils/plot.py

import matplotlib.pyplot as plt
import seaborn as sns


def hist_plot(data, column, bins=10, title=None, xlabel=None, ylabel=None, figsize=(None, None), ax=None):
    """
    Create a histogram for a specific column in a dataset.

    Parameters:
        data (DataFrame): The dataset containing the column.
        column (str): The column to plot.
        bins (int): Number of bins for the histogram.
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
        figsize (tuple): Size of the figure.
    """
    if ax is None:
        fig , ax = plt.subplots(figsize=figsize)

    ax.hist(data[column], bins=bins)
    ax.set_title(title or f'Histogram of {column}')
    ax.set_xlabel(xlabel or column)
    ax.set_ylabel(ylabel or 'Frequency')
    plt.grid(True)
    plt.show()

def scatter_plot(data, x_col=None, y_col= None, title=None, xlabel=None, ylabel=None, figsize=(None, None)):
    """
       Function to plot scatterplot

       Parameters:
            data(Dataframe): The dataset containing the column
            x_col (str): The column on the x-axis
            y_col (str): The column on the y-axis
            title (str): Title of the plot.
            xlabel (str): Label for the x-axis.
            ylabel (str): Label for the y-axis.
            figsize (tuple): Size of the figure.
    """
    plt.figure(
        figsize=figsize
    )

    sns.scatterplot(
        data=data, x=x_col, y=y_col
    )
    plt.title(title or f'Scatter Plot of {x_col} vs {y_col}')
    plt.xlabel(xlabel or x_col)
    plt.ylabel(ylabel or y_col)
    plt.grid(True)
    plt.show()



def box_plot(data, column, title=None, xlabel= None, ylabel=None, figsize=(None,None)):
    """
        Function to plot box plot

        Parameters:
            data (dataframe): Teh dataset containing the coulmn.
            columm (str): The column to plot
            title (str): Title of the plot.
            xlabel (str): Label for the x-axis.
            ylabel (str): Label for the y-axis.
            figsize (tuple): Size of the figure.
    """
    plt.figure(
        figsize=figsize
    )

    sns.boxplot(
        data=data, y=column
    )

    plt.title(
        title or f"Box Plot of {column}"
    )

    plt.ylabel(ylabel or column)
    plt.show()
