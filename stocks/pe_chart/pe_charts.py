import json
import pandas as pd
import glob
import os
import sys
import plotly.graph_objs as go

def load_and_process(filepath, rolling_window):
    """Load a single JSON file and compute moving average."""
    with open(filepath) as f:
        json_data = json.load(f)

    data = json_data['datasets'][0]['values']
    df = pd.DataFrame(data, columns=['date', 'value'])
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = pd.to_numeric(df['value'])
    df['ma'] = df['value'].rolling(window=rolling_window).mean()

    return df

def plot_moving_averages(data_dir, moving_average):
    """Plot interactive moving average chart for all JSON files in data_dir."""
    json_files = glob.glob(os.path.join(data_dir, '*.json'))
    if not json_files:
        print(f'No JSON files found in directory: {data_dir}')
        return

    fig = go.Figure()

    for file_path in json_files:
        filename = os.path.basename(file_path)
        legend_label = filename.split('_')[0]

        df = load_and_process(file_path, moving_average)

        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['ma'],
            mode='lines',
            name=f'{legend_label} {moving_average}d MA',
            hovertemplate=
                f'<b>Dataset</b>: {legend_label}<br>' +
                '<b>Date</b>: %{x|%Y-%m-%d}<br>' +
                '<b>PE (MA)</b>: %{y:.2f}<extra></extra>'
        ))

    # Layout customization
    fig.update_layout(
        title=f'{moving_average}-Day Moving Averages',
        xaxis_title='Date',
        yaxis_title=f'PE Value ({moving_average}d MA)',
        legend_title='Datasets',
        hovermode='x',  # Crosshair vertical line
        xaxis=dict(
            showgrid=True,
            gridwidth=1,
            gridcolor='LightGray',
            dtick="M12",  # Major grid every year
            tickformat="%Y"
        ),
        yaxis=dict(showgrid=True, gridwidth=1, gridcolor='LightGray')
    )

    fig.show()

if __name__ == '__main__':
    # Command-line argument parsing
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <moving_average>')
        sys.exit(1)

    try:
        moving_average = int(sys.argv[1])
    except ValueError:
        print('Error: moving_average must be an integer.')
        sys.exit(1)

    data_dir = 'data'

    plot_moving_averages(data_dir=data_dir, moving_average=moving_average)

