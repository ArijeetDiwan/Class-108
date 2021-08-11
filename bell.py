import plotly.figure_factory as ff 
import pandas as pd 
import csv 

df=pd.read_csv("data.csv")
#fig=ff.create_distplot([df["Height(Inches)"].tolist()],["okmam"],show_hist=False)
fig=ff.create_distplot([df["Weight(Pounds)"].tolist()],["okmam"],show_hist=True)
fig.show()

#y axis can be any str example-"abc"
#frequency shows in y axis out of (1)
