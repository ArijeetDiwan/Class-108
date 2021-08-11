import random
import plotly.express as px
import plotly.figure_factory as ff

dice_result=[8,4,8,6,7,6,3,4,2,12]
fig=ff.create_distplot([dice_result],["Result"])
fig.show()