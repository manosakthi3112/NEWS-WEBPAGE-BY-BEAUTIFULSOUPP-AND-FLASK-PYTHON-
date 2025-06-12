from bs4 import BeautifulSoup
import requests
import html
import re
import base64
import os
import json
url = "https://tamil.news18.com/news/"
def tot():
    req = requests.get(url)
    d = []
    soup = BeautifulSoup(req.content, "html.parser")
    
    # Use lambda to match both dynamic jsx class and cn-left
    table = soup.find('div', class_=lambda c: c and 'cn-left' in c and 'jsx-' in c)
    if not table:
        return d

    _rt = table.find('ul', class_=lambda c: c and 'cn-videoList' in c and 'jsx-' in c)
    if not _rt:
        return d

    list_ = _rt.find_all('li')
    for i in list_:
        f = {}
        f['text'] = i.text.strip()
        
        link_tag = i.find('a')
        if link_tag:
            href = link_tag.get('href')
            if href and not href.startswith('http'):
                href = url.replace('/news/', href)
            f['href'] = href

        tn_a_img = i.find_all('img')
        for tn_img in tn_a_img:  
            img_src = tn_img.get('src')
            if img_src:
                if img_src.startswith("data:image"): 
                    base64_data = img_src.split(",")[1]  # Not used here
                else:
                    img_src = img_src.replace('amp;', '')
                    f['img_link'] = img_src
        
        d.append(f)
    return d
def cinema_1(href):
    f={}
    cinema_1_request=requests.get(href)

    cinema_1_soup=BeautifulSoup(cinema_1_request.content,'html.parser')

    
    try :
        cinema_1_table=cinema_1_soup.find('div', attrs = {'class':'nwrow clearfix'})
        cinema_1_heading=cinema_1_table.find('h1')
        f['heading']=cinema_1_heading.text
        cinema_1_heading_2=cinema_1_table.find('h2')
        f['heading_2']=cinema_1_heading_2.text
        cinema_1_updated=cinema_1_table.find('time')
        f['last_updated']=cinema_1_updated.text
        cinema_1_para=cinema_1_table.find_all('p')
        s=""
        for i in cinema_1_para:
            s+=i.text+"\n"
        f['para']=s
        return f
    except:
        cinema_1_table=cinema_1_soup.find('div', attrs = {'class':'jsx-4271798382'})
        cinema_1_heading=cinema_1_table.find('h1')
        f['heading']=cinema_1_heading.text
        cinema_1_heading_2=cinema_1_table.find('h2')
        f['heading_2']=cinema_1_heading_2.text
        cinema_1_updated=cinema_1_table.find('time')
        f['last_updated']=cinema_1_updated.text 
        cinema_1_=cinema_1_table.find_all('div', attrs = {'class':'jsx-1629146367 newphtbox'})
        d=''
        for i in cinema_1_:
            img_data=i.find_all('p',attrs={'class':'jsx-4271798382'})
            d+=i.text+"\n"
        f['para']=d
        return f
            
            
def common(url,f):
    cinema_request=requests.get(url)

    cinema_soup=BeautifulSoup(cinema_request.content, "html.parser")
    p=[]
    cinema_table=cinema_soup.find('div',class_=re.compile(r'^jsx-.*\scn-left$'))
    cinema_=cinema_table.find('ul', class_=re.compile(r'jsx-[\w\d]+ cn-videoList'))
    cinema_list=cinema_.find_all('li')
    
    for  i in cinema_list:
        data={}
        data['text'] = i.text.strip() 
        tn_a=i.find('a')
        if tn_a:
            tn_a_link = tn_a.get('href')
            href = url.replace('/news/',tn_a_link)

            data['href'] = href
        tn_a_img = i.find_all('img')
        for tn_img in tn_a_img:  
            img_src = tn_img.get('src')
            if img_src.startswith("data:image"): 
                base64_data = img_src.split(",")[1]  
            else:
                img_src = img_src.replace('amp;', '')
                data['img_link']=img_src
            #print(f"Valid Image Source URL: {img_src}")
        p.append(data)
    return p
# tamilnadu news
def tamilnadu():
    tamilnadu_url=url.replace('news/','tamil-nadu/')
    tn_request=requests.get(tamilnadu_url)

    tn_soup=BeautifulSoup(tn_request.content, "html.parser")

    s=[]
    tn_table=tn_soup.find('div',class_=re.compile(r'^jsx-.*\scn-left$'))

    tn_=tn_table.find('ul',class_=re.compile(r'jsx-[\w\d]+ cn-videoList'))
    tn_list=tn_.find_all('li')

    for  i in tn_list:
        data={}
        data['text']=i.text
        tn_a=i.find('a')
        tn_a_link=tn_a.get('href')
        href=url.replace('/news/',tn_a_link)
        data['href']=href
        tn_a_img = i.find_all('img')
        for tn_img in tn_a_img:  
            img_src = tn_img.get('src')
            if img_src.startswith("data:image"): 
                base64_data = img_src.split(",")[1]  
            else:
                img_src = img_src.replace('amp;', '')
                data['img_link']=img_src
            #print(f"Valid Image Source URL: {img_src}")
        s.append(data)
    return s
#cinema
def cinema():
    cinema_url=url.replace('news/','entertainment/')
    f='/entertainment/'
    s=common(cinema_url,f)
    return s
#lifestyle
def lifestyle():
    cinema_url=url.replace('news/','lifestyle/')
    f='/lifestyle/'
    s=common(cinema_url,f)
    return s
#sports
def sports():
    cinema_url=url.replace('news/','sports/')
    f='/sports/'
    s=common(cinema_url,f)
    return s
#business
def business():
    business_url=url.replace('news/','business/')
    f="/business/"
    s=common(business_url,f)
    return s

#india
def india():
    business_url=url.replace('news/','national/')
    f="/national/"
    s=common(business_url,f)
    return s
#world
def world():
    business_url=url.replace('news/','international/')
    f="/international/"
    s=common(business_url,f)
    return s
#spiritual
def spiritual():
    business_url=url.replace('news/','spiritual/')
    f="/spiritual/"
    s=common(business_url,f)
    return s
#print(cinema())
#print(tamilnadu())
#business()
#lifestyle()
#sports()
#print(tot())
#india()
#world()
#spiritual()
#cinema_1('https://tamil.news18.com/photogallery/business/today-gold-rate-and-silver-rate-in-chennai-december-20-2024-1681769.html')
