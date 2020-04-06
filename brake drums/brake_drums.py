# product wala
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup as soup
import time
import sqlite3
import datetime
import threading
import pymysql  
import pandas as pd 
import ast
import requests
from bs4 import BeautifulSoup as soup
import codecs
from lxml import html
import json
import re
r="https://www.empoweredautoparts.com.au"

try:
    page = requests.get(r,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"})
except:
    print(r)
    # in case connection with proxy is having problem
    print('error in connection')
    time.sleep(2)

Soup1 = soup(page.content) #, "html5lib")
# Need to check input wala hi field ho
if 'type the characters you see in this image' in str(Soup1).lower():
    print('captcha')
    time.sleep(10) 

elif '502 bad gateway' in str(Soup1).lower():
    print('Bad Gateway')

elif 'something went wrong' in str(Soup1).lower():
    print('something went wrong')

elif 'device is blocked' in str(Soup1).lower():
    print('device is blocked')

elif '404 page not found' in str(Soup1).lower():
    print('404 page not found')
    time.sleep(20)

elif '404 - not found' in str(Soup1).lower():
    print('404 - Not Found')
    time.sleep(20)

else:
    with open(str('sub_r')+'.html', "w",encoding="utf-8") as f:
         f.write(str(Soup1))
    tree = ''
    soup_object = ''
    try:
        f=codecs.open(str('sub_r') + '.html', 'r',encoding="utf-8")
        tree = html.fromstring(f.read())
        f=codecs.open(str('sub_r') + '.html', 'r',encoding="utf-8")
        tree = html.fromstring(page.content)
        soup_object = soup(f.read(),features = 'html.parser')
    except:
        pass

nav_bar = Soup1.find('ul',class_="nav navbar-nav mega-menu").find_all('li',class_="dropdown dropdown-hover")
brand_list_main=[]
for j in range(len(Soup1.find('ul',class_="nav navbar-nav mega-menu").find_all('li',class_="dropdown dropdown-hover"))):
    brand_inner_list =[]
    for i in nav_bar[j].find('ul',class_="dropdown-menu dropdown-menu-horizontal").find_all("li"):
        #print(i.find('a').text)
        #print(r+i.find('a')['href'])
        brand_inner_list.append(i.find('a')['href'])
    brand_list_main.append(brand_inner_list) 


brand_list_parts = ['Brake drums']



dic={}
for i in range(len(brand_list_parts)):
    dic[brand_list_parts[i]] = brand_list_main[i]





r_1="https://www.empoweredautoparts.com.au"
# product_urls_main_list=[]
# for i_brand_list_parts in range(len(brand_list_parts)):
#     for j_brand_list_main in range(len(brand_list_main[i_brand_list_parts])):
#         r_2 = r_1+brand_list_main[i_brand_list_parts][j_brand_list_main]
#         print(r_2)
for i_brand_list_parts in range(len(brand_list_parts)):
    for j_brand_list_main in range(len(brand_list_main[3])):
        r_2 = r_1+brand_list_main[3][j_brand_list_main]
        print('subrrrrrrrrrrrrrrrrrrrrrrrrr',r_2)
        count=1
        sub_r = r_2
        counter = 0
        while True:
            try:
                page = requests.get(sub_r,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"})
            except:
                print(sub_r)
                # in case connection with proxy is having problem
                print('error in connection')
                time.sleep(2)

            Soup1 = soup(page.content)#, "html5lib")
            # Need to check input wala hi field ho
            if 'type the characters you see in this image' in str(Soup1).lower():
                print('captcha')
                time.sleep(10) 

            elif '502 bad gateway' in str(Soup1).lower():
                print('Bad Gateway')

            elif 'something went wrong' in str(Soup1).lower():
                print('something went wrong')

            elif 'device is blocked' in str(Soup1).lower():
                print('device is blocked')

            elif '404 page not found' in str(Soup1).lower():
                print('404 page not found')
                time.sleep(20)

            elif '404 - not found' in str(Soup1).lower():
                print('404 - Not Found')
                time.sleep(20)

            else:
                with open(str('sub_r')+'.html', "w",encoding="utf-8") as f:
                     f.write(str(Soup1))
                tree = ''
                soup_object = ''
                try:
                    f=codecs.open(str('sub_r') + '.html', 'r',encoding="utf-8")
                    tree = html.fromstring(f.read())
                    f=codecs.open(str('sub_r') + '.html', 'r',encoding="utf-8")
                    tree = html.fromstring(page.content)
                    soup_object = soup(f.read(),features = 'html.parser')
                except:
                    pass
            product_urls_list = []
            product_variants_list = []
            
            try:
                product_list = Soup1.find('div',class_="thumb").find('div',class_="row").find_all('div',class_="wrapper-thumbnail col-xs-6 col-sm-6 col-md-4 col-lg-3")
                for k in product_list:
                    product_url = k.find('div',class_="thumbnail").find('div',class_="wrapper-thumbnail-img").find('a',class_="thumbnail-image")['href']
                    product_urls_list.append(product_url)
                    #print(product_url)

                    product_variants = k.find('div',class_="caption").find_all('p')
                    product_variants=product_variants[1].text.strip()
                    product_variants_list.append(str(product_variants))

                    print(product_variants)
            except:
                product_urls_list = ''
                product_variants_list = ''
                print(count)
                break
            
            if(counter == 0):
                r=page.url
                
            count = count+1
            sub_r = r+'?pgnum='+str(count)
            #print(count)
            #print(sub_r)
            counter += 1
        #product_urls_main_list.append(product_urls_list)
            varient = ''
            for k in range(len(product_urls_list)):
                varient = product_variants_list[k]
                k = product_urls_list[k]
                
                print(k)
                try:
                    page = requests.get(k,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"})
                except:
                    #print(k)
                    # in case connection with proxy is having problem
                    print('error in connection')
                    time.sleep(2)

                Soup1 = soup(page.content)#, "html5lib")
                # Need to check input wala hi field ho
                if 'type the characters you see in this image' in str(Soup1).lower():
                    print('captcha')
                    time.sleep(10) 

                elif '502 bad gateway' in str(Soup1).lower():
                    print('Bad Gateway')

                elif 'something went wrong' in str(Soup1).lower():
                    print('something went wrong')

                elif 'device is blocked' in str(Soup1).lower():
                    print('device is blocked')

                elif '404 page not found' in str(Soup1).lower():
                    print('404 page not found')
                    time.sleep(20)

                elif '404 - not found' in str(Soup1).lower():
                    print('404 - Not Found')
                    time.sleep(20)

                else:
                    with open(str('sub_r')+'.html', "w",encoding="utf-8") as f:
                         f.write(str(Soup1))
                    tree = ''
                    soup_object = ''
                    try:
                        f=codecs.open(str('r') + '.html', 'r',encoding="utf-8")
                        tree = html.fromstring(f.read())
                        f=codecs.open(str('r') + '.html', 'r',encoding="utf-8")
                        tree = html.fromstring(page.content)
                        soup_object = soup(f.read(),features = 'html.parser')
                    except:
                        pass

                
                try:
                    product_name = Soup1.find('div',id="_jstl__header_r").find('h1',{'itemprop':'name'}).text.strip()
                except:
                    product_name=''
                #print(product_name)
                
                try:
                    product_id = Soup1.find('div',id="_jstl__header_r").find('span',{'itemprop':'productID'}).text.strip()
                except:
                    product_id=''
                #print(product_id)
                
                try:
                    current_price = Soup1.find('div',id="_jstl__header_r").find('div',{'itemprop':'offers'}).find('div',{'itemprop':'price'}).text.strip()
                except:
                    current_price=''
                #print(current_price)
                
                try:
                    list_price = Soup1.find('div',id="_jstl__header_r").find('div',{'itemprop':'offers'}).find('div',class_="productrrp text-muted").text.strip()
                except:
                    list_price=''
                
                if list_price=='':
                    list_price=current_price
                #print(list_price)
                
                try:
                    category = Soup1.find('div',id="main-content").find('ul',class_="breadcrumb").text.replace('\n','/')
                except:
                    category=''
                #print(category)
                
                try:
                    stock = Soup1.find('span',{'itemprop':'availability'}).text
                except:
                    stock=''
                #print(stock)
                try:
                    local_pick_up = Soup1.find('div',class_="panel-body").find('i',class_="text-muted").text
                except:
                    local_pick_up=''
                #print(local_pick_up)

                try:
                    discount = Soup1.find('div',class_="productsave").text.replace('\n','')
                except:
                    discount=''
                #print(discount)
                
                discription_list = Soup1.find('div',id="main-content").find('div',class_="productdetails open")
                
                try:
                    items= Soup1.find('div',id="main-content").find('div',class_="productdetails open").find('div',{'typeof':'Product'})
                    list_text=items.text.split('\n')
                except Exception as e:
                    items= Soup1.find('div',class_="productdetails open")
                    list_text=items.text.split('\n')
                
              
                dicription_tittle = ''
                try:
                    for each in list_text:
                        if each!='':
                            dicription_tittle=each
                            break
                except:
                    dicription_tittle = ''

                for i,each in enumerate(items.text.split('\n')):
                    if ('compatible model' in each.lower()) or ('compatable model' in each.lower()):
                        comp_index=i
                    if ('product specification' in each.lower()) or ('product highlight' in each.lower()):
                        spec_index=i
                    if 'you are buying' in each.lower():
                        buy_index=i
                    if 'empowered auto parts is an authorised' in each.lower():
                        gunuine_index=i
                
                try:
                    discription = ''
                    try:
                        discription=list_text[list_text.index(dicription_tittle)+1:comp_index]
                    except:
                        discription = ''

                    compatible_model=''
                    try:
                        compatible_model=list_text[comp_index+1:spec_index]
                    except Exception as e:
                        if 'spec_index' in str(e):
                            try:
                                compatible_model=list_text[comp_index+1:buy_index]
                            except Exception as e:
                                if 'buy_index' in str(e):
                                    try:
                                        compatible_model=list_text[comp_index+1:gunuine_index-1]
                                    except:
                                        print('not speci and no buying' )
                    prod_spec=''
                    try:
                        prod_spec=list_text[spec_index+1:buy_index]
                    except Exception as e:
                        if 'buy_index' in str(e):
                            prod_spec=list_text[spec_index+1:gunuine_index-1]
                    you_are_buying=''
                    try:
                        you_are_buying=list_text[buy_index+1:gunuine_index-1]
                    except Exception as e:
                        you_are_buying=[]
                except Exception as e:
                    df_loc = pd.read_csv('empoweredautoparts222.csv')
                    if 'comp_index' in e:
                        with open(str(df_loc.shape[0])+'.html', "w",encoding="utf-8") as f:
                             f.write(str(discription_list))

                    
                    

                
                image_url = ''
                try:
                    image_url = Soup1.find('img',id="main-image")['src']
                    image_url = 'https://www.empoweredautoparts.com.au' + image_url
                except:
                    image_url = ''
                #print(image_url)
                
                
                productdetails = []
                try:
                    for i in Soup1.find_all('div',class_="productdetails")[1].find('table',class_='table').find_all('tr'):
                        name = i.find_all('td')[0].text
                        value = i.find_all('td')[1].text
                        productdetails.append(name.replace('\n','')+' : '+value.replace('\n',''))
                except:
                    productdetails = ''
                #print(productdetails)

                dictionary = {
                    'Url': k,
                    'Make':brand_list_main[3][j_brand_list_main].replace('brake-drums','').replace('/',''),
                    'Model':'',
                    'Category': brand_list_parts[i_brand_list_parts],
                    'No. of Products': '',
                    'Product Variants': varient,
                    'Cateogry Descritption': category.replace('/','->'),
                    'Product  No': product_id,
                    'Product Title': product_name,
                    'Product Discounted Price': current_price,
                    'Product Original Price': list_price,
                    'Discount %': discount,
                    'Availability': stock,
                    'Image URL': image_url,
                    'DescriptionTitle': dicription_tittle,
                    'Description': " ".join(discription),
                    'Compatible Models': '\n'.join(compatible_model),
                    'Product Specifications': '\n'.join(prod_spec),
                    'You are buying': '\n'.join(you_are_buying),
                    'Product Speicifications': '\n'.join(productdetails).replace('::',':'),
                    'Local Pickup': str(local_pick_up).replace('\n','')
                }
                #print(dictionary)
                
                temp_df = pd.DataFrame(dictionary,index=[0])
                try:
                    try:
                        df = pd.read_csv('empoweredautoparts222.csv')
                    except:
                        temp_df.to_csv('empoweredautoparts222.csv') 
                        
                    df = df.append(temp_df,sort = False)
                    df.to_csv('empoweredautoparts222.csv',index = False)
                except:
                    df=temp_df.copy()
                    #temp_df.to_csv('empoweredautoparts222.csv') 
                    #temp_df.to_csv('empoweredautoparts222.csv') 
                try:
                    del df
                    del comp_index
                    del spec_index
                    del buy_index
                    del gunuine_index
                except:
                    pass
                    
                                #.next_element
#                 with open(str(df.shape[0])+'.html', "w",encoding="utf-8") as f:
#                      f.write(str(discription_list))

                
