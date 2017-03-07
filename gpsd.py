from statistics import mean
from mathplotlib import pyplot as plt

f=open('gpsdata.txt', 'r')
gps_data=f.readlines()
f.close()
#print(*gps_data)
lat_data=[]
lon_data = []
for line in gps_data:
    l=line.split(',')
    print(l)
if l[0]=='$GPRMC'and l[2]=='A':
    lat_data.append(float(l[3] [:2]) +float(l[3] [2:])/60)
    lon_data.append(float(l[5][:3]) +float(l[5][3:])/60)
    print(float(l[3] [:2]) +float(l[3] [2:])/60 +float(l[5][:3]) +float(l[5][3:])/60)

    print(mean(lat_data), mean(lon_data))
    plt.plot(lat_data, lon_data)
    plt.title('RAW GPS DATA')
    plt.xlabel('Lat')
    savefig('test.png')
    plt.show()