import matplotlib.pyplot as plt
from datetime import datetime
import csv
#add name of your file between ' '
filename='york.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        high=int(row[6])
        low=int(row[7])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
plt.style.use('seaborn-v0_8-dark-palette')
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='green',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='purple',alpha=0.1)
plt.title("Temperature of NewYork for this year high and low",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()


