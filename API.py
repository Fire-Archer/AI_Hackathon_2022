
import requests
import numpy as np
import csv   

#url = "https://api.bmreports.com/BMRS/B1620/V1?APIKey=csleg6qvoe0i1kf&SettlementDate={0}-{1}-{2}&Period=*&ServiceType=csv".format(year,month,day)

# =============================================================================
# 
# data = requests.get(url)
# 
# lines = []
# for line in data.text:
#     lines.append(line)
# =============================================================================

years = [2019, 2020, 2021]
months = np.arange(1, 13, 1)
days = [31,28,31,30,31,30,31,31,30,31,30,31]
#with open('Generation.csv','a') as fd:
csv_file = open('Generation.csv', 'ab')
for year in years:
    for month in months:
        print('month', month)
        padding_month= 2 - len(str(month))
        padded_month = '0' * padding_month + str(month)
        for day in range(days[month-1]):
            day += 1
            padding_day= 2 - len(str(day))
            padded_day = '0' * padding_day + str(day)
            #print(year)
            
            
            
            url = "https://api.bmreports.com/BMRS/B1620/V1?APIKey=csleg6qvoe0i1kf&SettlementDate={0}-{1}-{2}&Period=*&ServiceType=csv".format(year,padded_month,padded_day)
            req = requests.get(url)
            url_content = req.content
            csv_file.write(url_content)
            #fd.write(url_content)  

#csv_file = open('downloaded.csv', 'wb')

            #req = requests.get(url)
            #url_content = req.content

#csv_file.write(url_content)
csv_file.close()



