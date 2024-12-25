import dash
from dash import dcc, html
import plotly.graph_objs as go

# Correct Tailwind CSS CDN
# Tailwind CSS CDN
externalScripts=[
    {'src': 'https://cdn.tailwindcss.com'},
]

app = dash.Dash(
    title='Ecoi Analytics',
    update_title='Loading...',
    external_scripts=externalScripts,
    assets_external_path='./assets',
    suppress_callback_exceptions=True,
)

graphStyles = {
    "graphTitleStyle": "text-sans text-2xl text-gray-900",
    "axisTitleStyle": "text-sans text-lg font-semibold text-gray-700",
    "graphStyleTypes": {
        "shadowed": "shadow-lg shadow-cyan hover:shadow-xl rounded-lg p-6"
    }
}

# Example graph data for demonstration purposes
trace = go.Bar(x=[1, 2, 3], y=[4, 1, 3])

# Favicon
html.Header([
    html.Link(
        rel='icon',
        href='https://via.placeholder.com/250'  # Ensure you have favicon.ico in the assets folder
    )
])

# Layout for the Dash application
app.layout = html.Div([
    html.Div([
        html.H1("Ecoi Analytics", className="text-4xl text-bold text-sky-400 text-center mt-3 mb-5 pb-5"),
        # Grid layout with two rows, each having two graphs
        html.Div([
            html.H1("Real Time", className=graphStyles["graphTitleStyle"]),
            html.Div([
                html.Div([
                    dcc.Graph(id='activeGraph', figure={
                        'data': [trace],
                        'layout': go.Layout(
                            title="Active",
                            xaxis={'title': 'Time', 'showgrid': True},
                            yaxis={'title': 'Usage', 'showgrid': True},
                        )
                    }),
                ]),

                html.Div([
                    dcc.Graph(id='liveEventsGraph', figure={
                        'data': [trace],
                        'layout': go.Layout(
                            title="Top 5 Live Events",
                            xaxis={'title': 'Events', 'showgrid': True},
                            yaxis={'title': 'Counts', 'showgrid': True},
                        )
                    }),
                ]),
            ], className="grid grid-cols-2 gap-4 mb-5 "+ graphStyles["graphStyleTypes"]["shadowed"]),

            html.Hr(),

            html.Div([
                html.Div([
                    html.H2("Top 5 Events", className=graphStyles["graphTitleStyle"]),
                    dcc.Graph(id='top5EventsGraph', figure={
                        'data': [trace],
                        'layout': go.Layout(
                            xaxis={'title': 'Events', 'showgrid': True},
                            yaxis={'title': 'Counts', 'showgrid': True},
                        )
                    }),
                ], className=graphStyles["graphStyleTypes"]["shadowed"]),

                html.Div([
                    html.H2("Graph 4", className=graphStyles["graphTitleStyle"]),
                    dcc.Graph(id='graph4', figure={
                        'data': [trace],
                        'layout': go.Layout(
                            title="Sample Graph 4",
                            xaxis={'title': 'X Axis', 'showgrid': True},
                            yaxis={'title': 'Y Axis', 'showgrid': True},
                        )
                    }),
                ], className=graphStyles["graphStyleTypes"]["shadowed"]),
            ], className="grid grid-cols-2 gap-4"),

        ], className="grid grid-cols-1 gap-4 mt-5")
    ], style={
        'padding': '30px 30px',
        'margin': '30px 20px 10px 20px',
        'box-shadow': '0 0 1000px rgba(0, 0, 255, 0.4)',  # External container shadow
        'width': '95%',
        'border-radius': '25px',
        'height': '95%',
        'background-color': '#ffffff',
    },
    className='font-sans'
    ),
], style={
    'width': '100%',
    'height': '100%',
    'background-color': 'smokewhite',
    'display': 'flex',
    'padding': 0,
    'margin': 0
})

app.run_server(debug=False)