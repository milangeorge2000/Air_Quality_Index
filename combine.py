import pandas as pd 

data = pd.read_html('https://en.tutiempo.net/climate/2013/ws-432950.html')

print(data)