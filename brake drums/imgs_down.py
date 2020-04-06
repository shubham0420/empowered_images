import pandas as pd
from urllib.request import Request, urlopen
import urllib
import requests
import os
img_list=[]
df=pd.read_csv('empoweredautoparts222.csv')

for index,each in df.iterrows():
    #print(each)
    try:
        print(each['Product  No'],each['Image URL'])
        if each['Product  No']+".jpg" not in img_list:
            try:
                img_list.append(each['Product  No']+".jpg")
                txt=open("imgss/"+each['Product  No']+'.jpg','wb')
                download_img=Request(each['Image URL'], headers={'User-Agent': 'Mozilla/5.0'})
                download_img_=urlopen(download_img)
                txt.write(download_img_.read())
                txt.close()
                print('Images_downloaded')
            except KeyError:
                pass
    except:
        pass