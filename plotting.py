from turtle import title
from app2 import df 
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.plotting import figure,show,output_file

df["Start_string"]=df["start"].dt.strftime("%Y-%M-%D %H:%M:%S")
df["End_string"]=df["end"].dt.strftime("%Y-%M-%D %H:%M:%S")
 
cds = ColumnDataSource(df)

p=figure(x_axis_type="datetime",height=200,width=800,title="Motion Graph")
p.yaxis.minor_tick_line_color=None

hover=HoverTool(tooltips=[("Start","@Start_string"), ("End","@End_string")])
p.add_tools(hover)

q=p.quad(left=df["start"],right=df["end"],bottom=0,top=100,color="green")

output_file("Graph2.html")
show(p)

