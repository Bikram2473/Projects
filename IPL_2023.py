""" IPL 2023 Analysis """

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("IPL_2023.csv")
print(data.head())

figure = px.bar(data, x = data["team_won"], title = "Number of matches won in IPL 2023")
figure.show()

data["team_won"] = data["won_by"].map({"Wickets": "Chasing", "Runs": "Defending"})
won_by = data["won_by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['gold', 'lightgreen']

fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = "Number of matches won by Defending or Chasing")
fig.update_traces(hoverinfo = 'label + percent', textinfo = 'value', textfont_size = 30, marker = dict(colors = colors,
                    line = dict(color = 'black', width = 3)))
fig.show()

toss = data["toss_decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['skyblue', 'yellow']

fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Toss Decision')
fig.update_traces(hoverinfo = 'label + percent', textinfo = 'value', textfont_size = 30, marker = dict(colors = colors,
                    line = dict(color = 'black', width = 3)))
fig.show()

figure = px.bar(data, x = data["top_scorer"], title = "Top Scorers in IPL 2023")
figure.show()

figure = px.bar(data, x = data["top_scorer"], y = data["highest_score"], color = data["highest_score"],
                title = "Highest Run Getters in IPL 2023")
figure.show()

figure = px.bar(data, x = data["best_bowler"], title = "Best Bowlers in IPL 2023")
figure.show()

figure = go.Figure()
figure.add_trace(go.Bar(
    x=data["venue"],
    y=data["first_innings_wickets"],
    name='First Innings Wickets',
    marker_color='gold'
))

figure.add_trace(go.Bar(
    x=data["venue"],
    y=data["second_innings_wickets"],
    name='Second Innings Wickets',
    marker_color='lightgreen'
))

figure.update_layout(barmode='group', xaxis_tickangle = -45)
figure.show()

