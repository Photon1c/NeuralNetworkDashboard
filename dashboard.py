import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Initialize the Dash app
app = dash.Dash(__name__)

# Example data for cost, accuracy, and iterations (replace with actual data)
iterations = np.arange(1, 101)  # Example: 100 iterations
costs = np.random.random(100)   # Replace with actual cost data
accuracy = np.random.random(100)  # Replace with actual accuracy data
choices = ["Circle", "Square", "Triangle", "I don't know"]

# App layout (using grid-style layout to structure components)
app.layout = html.Div([
    html.H1("Neural Network Training Dashboard", style={'text-align': 'center'}),

    # Neural network and output labels (center of layout)
    html.Div([
        html.Div([
            dcc.Graph(
                id='cost-graph',
                figure={
                    'data': [
                        go.Scatter(x=iterations, y=costs, mode='lines+markers', name='Cost')
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
                        go.Scatter(x=iterations, y=accuracy, mode='lines+markers', name='Accuracy')
                    ],
                    'layout': go.Layout(
                        title='Accuracy vs Iterations',
                        xaxis={'title': 'Iterations'},
                        yaxis={'title': 'Accuracy'},
                    )
                }
            )
        ], style={'width': '30%', 'display': 'inline-block', 'vertical-align': 'top'}),

        html.Div([
            # Neural Network Visualization (Updated dynamically)
            html.Img(id='neural-network-diagram', src='assets/iterations/iteration_6.png', style={'width': '35%'}),
            
            # Display output categories
            html.Div([
                html.P("Predicted Output: ", style={'font-weight': 'bold'}),
                html.H2(id='prediction-output', style={'color': 'red'}),  # Placeholder for prediction
            ], style={'text-align': 'center', 'margin-top': '20px'})
        ], style={'width': '40%', 'display': 'inline-block', 'text-align': 'center'}),

        # Input image being processed by the neural network
        html.Div([
            html.Img(id='input-image', src='/assets/input_image_1.bmp', style={'width': '100%'}),
            dcc.Interval(id='interval-component', interval=3*1000, n_intervals=0),  # Update every 3 seconds
        ], style={'width': '20%', 'display': 'inline-block'})
    ], style={'display': 'flex', 'justify-content': 'center'}),

    # Add more components as needed
])

# Update input image, metrics, and prediction output every interval
@app.callback(
    [
        dash.dependencies.Output('input-image', 'src'),
        dash.dependencies.Output('neural-network-diagram', 'src'),
        dash.dependencies.Output('cost-graph', 'figure'),
        dash.dependencies.Output('accuracy-graph', 'figure'),
        dash.dependencies.Output('prediction-output', 'children')  # For predicted output
    ],
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_metrics_image_and_prediction(n):
    """
    Function to update the image source, cost, accuracy graphs, neural network diagram, 
    and the prediction output in real-time.
    """
    # Update input image (cycle through 5 images)
    image_path = f'/assets/input_image_{(n % 5) + 1}.bmp'  # n % 5 gives 0-4, so we add 1 for images 1-5

    # Update neural network diagram dynamically based on current iteration
    neural_network_image_path = f'/assets/iterations/iteration_{(n % 5) + 1}.png'

    # Simulate prediction output (you can replace this with actual model prediction logic)
    prediction = choices[n % 4]  # Cycle through Circle, Square, Triangle, I don't know

    # Simulate updating cost and accuracy
    updated_costs = np.random.random(100) * np.exp(-n / 100)  # Simulated decreasing cost
    updated_accuracy = np.random.random(100) * np.log(n + 1) / 5  # Simulated increasing accuracy

    cost_figure = {
        'data': [go.Scatter(x=iterations, y=updated_costs, mode='lines+markers', name='Cost')],
        'layout': go.Layout(
            title='Cost vs Iterations',
            xaxis={'title': 'Iterations'},
            yaxis={'title': 'Cost'},
        )
    }

    accuracy_figure = {
        'data': [go.Scatter(x=iterations, y=updated_accuracy, mode='lines+markers', name='Accuracy')],
        'layout': go.Layout(
            title='Accuracy vs Iterations',
            xaxis={'title': 'Iterations'},
            yaxis={'title': 'Accuracy'},
        )
    }

    return image_path, neural_network_image_path, cost_figure, accuracy_figure, prediction

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
