from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def plot_well_curve(well_name, info, well_depth=None, col_one=None, col_two=None, col_three=None):
    """
    @author Ling LUO
    :param well_name The name of the well
    :param info The data(A DataFrame) of the well
    :param well_depth The depth of well
    :param col_one: The first column name
    :param col_two: The second column name
    :param col_three: The third column name
    :return: fig path
    To plot the relevant well curve
    """
    well_info = info
    # Check for incoming well depth
    if well_depth is None:
        try:
            well_depth = well_info['depth'].tolist()
        except ValueError:
            print("Enter the well depth data as a list or add a 'Depth' column to the incoming file.")

    # Get col data
    assert 'wellname' in well_info.columns
    well_info = info[info['wellname'] == well_name]

    col_one_data = well_info[col_one].tolist()
    col_two_data = well_info[col_two].tolist()
    col_three_data = well_info[col_three].tolist()

    # Start plot
    fig = make_subplots(rows=1, cols=3, subplot_titles=(col_one, col_two, col_three))
    fig.add_trace(go.Scatter(
        y=well_depth,
        x=col_one_data),
        row=1, col=1
    )
    fig.add_trace(go.Scatter(
        y=well_depth,
        x=col_two_data),
        row=1, col=2
    )
    fig.add_trace(go.Scatter(
        y=well_depth,
        x=col_three_data),
        row=1, col=3
    )
    fig.update_layout(height=600,
                      width=800,
                      showlegend=False,
                      )
    fig.update_yaxes(range=[3000, 0])

    res = plotly.offline.plot(fig, filename=f'{col_one}and{col_two}and{col_three}.html')
    return res


def plot_lines_hot(line_number, info):
    """
    @author Ling LUO
    :param line_number: Line ID
    :param info: The Data as a dataframe
    :return: fig path
    """
    col = list(info.columns)
    assert 'line_number_id' in col
    line_info = info[info['line_number_id'] == line_number]
    value = line_info.iloc[:, 3:].values
    fig, ax = plt.subplots()
    im = ax.imshow(value, cmap='seismic', interpolation='nearest', aspect=0.1, alpha=0.6)
    ax.xaxis.set_ticks_position('top')  # the rest is the same
    fig.colorbar(im, ax=ax, fraction=0.02)
    xminorLocator = MultipleLocator(10)
    xmajorLocator = MultipleLocator(50)
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.xaxis.set_minor_locator(xminorLocator)
    plt.tick_params(labelsize=8)
    plt.savefig(f"{line_number} + '.png'")

    return f"{line_number} + '.png'"
