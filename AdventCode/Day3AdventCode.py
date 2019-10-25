import re
import pandas as pd

text_file = open("input_day3.txt", "r")
lines = text_file.read().split('\n')
ids = []
left_edge = []
top_edge = []
width = []
height = []

for i in lines:
    a = re.split(' ', i)
    ids.append(a[0][1:])
    left_edge.append(a[2][0:].split(':')[0].split(',')[0])
    top_edge.append(a[2][0:].split(':')[0].split(',')[1])
    width.append(a[3][0:].split('x')[0])
    height.append(a[3][0:].split('x')[1])
    
data = {'Id':ids, 'Left Edge':left_edge, 'Top Edge': top_edge, 'Width': width, 'Height': height}
   
df = pd.DataFrame(data) 
 
print(df)

