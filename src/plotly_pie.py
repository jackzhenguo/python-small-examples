import plotly.graph_objects as go

labels = ['照明与插座用电', '空调用电', '动力用电', '特殊用电']
values = [4500, 2500, 1053, 500]
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()
