import random 
import plotly.express as px 

dice_result=[]
count=[]

#we want to add it 100 times 
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    #print(dice1,dice2)
    dice_result.append(dice1+dice2)
    count.append(i)

#print(dice_result)
fig=px.bar(x=dice_result,y=count)



fig.show()
#if you join all the left edges of the bar graph you would see that distribution  of the number all most like a bell shape 
#bell shape distribution that is why it is called normal distribution most of that data in the universe  follow these pattern 
#y axis the  frequency of the sum 

