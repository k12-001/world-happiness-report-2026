import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


df = pd.read_excel("world_happiness_Update_report_2026.xlsx")
df = df.sort_values(by=['score'], ascending=False)

fig = px.choropleth(
    df,
    locations = 'country',
    locationmode= 'country names',
    color = 'score',
    color_continuous_scale= 'RdYlGn',
    hover_name= 'country',
    hover_data={'rank':True, 'score':':.2f'},
    title = 'Word Happiness Report 2026 based on Ladder Score- Mapping',
    projection = 'natural earth'
)

top_bottom_3 = pd.concat([df.head(3),df.tail(3)]).copy()
top_bottom_3['label'] = top_bottom_3.apply(
    lambda row:f"# {row['rank']} {row['country']} ({row['score']:.2f})",
    axis=1
)

fig.add_trace(
    go.Scattergeo(
        locations=top_bottom_3['country'],
        locationmode='country names',
        text =top_bottom_3['label'],
        mode = 'markers+text',
        textposition = 'bottom center',
        marker = dict(
            size=5,
            color='black'
        ),
        showlegend = False,
        hoverinfo= 'skip'
    )
)


fig.update_geos(
    showcoastlines = True,
    coastlinecolor = 'Gray',
    showland = True,
    landcolor = '#f0f0f0',
)


fig.update_layout(margin={'r':20, 't':40, 'l':0, 'b':0})

fig.show()



