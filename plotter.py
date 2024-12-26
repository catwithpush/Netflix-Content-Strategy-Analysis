import pandas as pd
import numpy as np
import plotly.graph_objects as go


def plot_bar_chart_univariate(data, column, title, x_axis_title, y_axis_title, height=600, width=800):
    """
    Plots a univariate bar chart for a specified column with count data

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data.
    column (str): The column name to plot.
    title (str): The title of the chart.
    x_axis_title (str): The title of the x-axis.
    y_axis_title (str): The title of the y-axis.
    height (int, optional): The height of the chart. Default is 600.
    width (int, optional): The width of the chart. Default is 800.

    Returns:
    plotly.graph_objs._figure.Figure: The bar chart figure.
    """


    # Calculate value counts and convert to DataFrame
    value_counts = data[column].value_counts().reset_index()
    value_counts.columns = [column, 'count']
    
    # Sort by count values
    sorted_data = value_counts.sort_values(by='count', ascending=False)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=sorted_data[column], 
        y=sorted_data['count'],
        marker_color='#db0000'
    ))
    fig.update_layout(
        title={
            'text': f"<b>{title}</b>",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title=x_axis_title,
        yaxis_title=y_axis_title,
        height=height,
        width=width,
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
        paper_bgcolor='rgba(0,0,0,0)', # Transparent paper background
        xaxis=dict(showgrid=False),    # Hide x-axis grid lines
        yaxis=dict(showgrid=False)     # Hide y-axis grid lines
    )
    
    
    return fig

def plot_bar_chart_univariate_y_col(data, x_column, y_column, title, x_axis_title, y_axis_title, height=600, width=800):

    """
    Plots a univariate bar chart using specified x and y columns in the data.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data.
    x_column (str): The column name for the x-axis.
    y_column (str): The column name for the y-axis.
    title (str): The title of the chart.
    x_axis_title (str): The title of the x-axis.
    y_axis_title (str): The title of the y-axis.
    height (int, optional): The height of the chart. Default is 600.
    width (int, optional): The width of the chart. Default is 800.

    Returns:
    plotly.graph_objs._figure.Figure: The bar chart figure.
    """


    sorted_data = data[[x_column, y_column]].sort_values(by=y_column, ascending=False)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=sorted_data [x_column].value_counts().index, 
        y=sorted_data [y_column],
        marker_color='#db0000'
    ))
    fig.update_layout(
        title={
            'text': f"<b>{title}</b>",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title=x_axis_title,
        yaxis_title=y_axis_title,
        height=height,
        width=width,
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
        paper_bgcolor='rgba(0,0,0,0)', # Transparent paper background
        xaxis=dict(showgrid=False),    # Hide x-axis grid lines
        yaxis=dict(showgrid=False)     # Hide y-axis grid lines
    )
    
    return fig


def plot_bar_chart_multivariate_y_col(data, x_column, y_column, group_column,  title, x_axis_title, y_axis_title, height=600, width=800):
    """
    Plots a multivariate bar chart using specified x, y, and group columns in the data.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data.
    x_column (str): The column name for the x-axis.
    y_column (str): The column name for the y-axis.
    group_column (str): The column name for grouping the data.
    title (str): The title of the chart.
    x_axis_title (str): The title of the x-axis.
    y_axis_title (str): The title of the y-axis.
    height (int, optional): The height of the chart. Default is 600.
    width (int, optional): The width of the chart. Default is 800.

    Returns:
    plotly.graph_objs._figure.Figure: The bar chart figure.
    """

    sorted_data = data[[x_column, group_column, y_column]].sort_values(by=y_column, ascending=False)
    fig = go.Figure()
    color_list = ['#831010', '#564d4d','#db0000', ]
    for i, group in enumerate(data[group_column].unique()):
        group_data = sorted_data[sorted_data[group_column] == group]
        fig.add_trace(go.Bar(
            x=group_data[x_column], 
            y=group_data[y_column],
            name=group,
            marker_color=color_list[i]
        ))

    fig.update_layout(
        title={
            'text': f"<b>{title}</b>",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title=x_axis_title,
        yaxis_title=y_axis_title,
        height=height,
        width=width,
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
        paper_bgcolor='rgba(0,0,0,0)', # Transparent paper background
        xaxis=dict(showgrid=False),    # Hide x-axis grid lines
        yaxis=dict(showgrid=False)     # Hide y-axis grid lines
    )
    fig.update_layout(barmode='group')
    
    return fig


def plot_scatter_plot(data, x_column, y_column, title, color_column=None, height=600, width=800):
    """
    Plots a scatter plot for the specified x and y columns in the data.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data.
    x_column (str): The column name for the x-axis.
    y_column (str): The column name for the y-axis.
    title (str): The title of the chart.
    x_axis_title (str): The title of the x-axis.
    y_axis_title (str): The title of the y-axis.
    color_column (str, optional): The column name for coloring the points. Default is None.
    height (int, optional): The height of the chart. Default is 600.
    width (int, optional): The width of the chart. Default is 800.

    Returns:
    plotly.graph_objs._figure.Figure: The scatter plot figure.
    """
    fig = go.Figure()

    if color_column:
        unique_groups = data[color_column].unique()
        for group in unique_groups:
            group_data = data[data[color_column] == group]
            fig.add_trace(go.Scatter(
                x=group_data[x_column],
                y=group_data[y_column],
                mode='markers',
                name=str(group),
                marker=dict(size=10),
                text=group_data[color_column]
            ))
    else:
        fig.add_trace(go.Scatter(
            x=data[x_column],
            y=data[y_column],
            mode='markers',
            marker=dict(color='#db0000')
        ))

    fig.update_layout(
        title={
            'text': f"<b>{title}</b>",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title=x_column,
        yaxis_title=y_column,
        height=height,
        width=width,
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
        paper_bgcolor='rgba(0,0,0,0)', # Transparent paper background
        xaxis=dict(showgrid=False),    # Hide x-axis grid lines
        yaxis=dict(showgrid=False)     # Hide y-axis grid lines
    )

    return fig