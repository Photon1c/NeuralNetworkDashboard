import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

data = pd.read_csv('test_data.csv')

iterations = data['iteration']
costs = data['cost']
accuracy = data['accuracy']



# Initialize the Dash app
app = dash.Dash(__name__)

# Example data for cost, accuracy, and iterations
# You should replace this with the actual data from your neural network training
iterations = np.arange(1, 101)  # Example: 100 iterations
costs = np.random.random(100)   # Replace with actual cost data
accuracy = np.random.random(100)  # Replace with actual accuracy data

# App layout
app.layout = html.Div(children=[
    html.H1(children='Neural Network Training Dashboard'),

    dcc.Graph(
        id='cost-graph',
        figure={
            'data': [
                go.Scatter(
                    x=iterations,
                    y=costs,
                    mode='lines+markers',
                    name='Cost'
                )
            ],
            'layout': go.Layout(
                title='Cost vs Iterations',
                xaxis={'title': 'Iterations'},
                yaxis={'title': 'Cost'},
            )
        }
    ),

    dcc.Graph(
        id='accuracy-graph',
        figure={
            'data': [
                go.Scatter(
                    x=iterations,
                    y=accuracy,
                    mode='lines+markers',
                    name='Accuracy'
                )
            ],
            'layout': go.Layout(
                title='Accuracy vs Iterations',
                xaxis={'title': 'Iterations'},
                yaxis={'title': 'Accuracy'},
            )
        }
    ),

    # Add more graphs or metrics as needed
])

html.Video(src='/assets/neuralnetwork.mp4', controls=True, autoPlay=False),


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
