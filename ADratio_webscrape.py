# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:14:30 2020

"""

#necessary libraries
import requests
import urllib.request
from bs4 import BeautifulSoup
import numpy as np

#function - Nifty 100
def GetADRatioHundred():
    url = 'https://www.moneycontrol.com/markets/indian-indices/top-nse-100-companies-list/28?classic=true'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    stk_idx = []
    for i in range(170,369,2): #keep an eye on indexes as they are hard coded for now, might change in future
        stk_idx.append(i)

    ad_list = []
    for i in stk_idx:
        ad_list.append(soup.findAll('span')[i].get('class').pop()) #gives grentxt/ redtxt based on advance or decline change

    values, counts = np.unique(ad_list, return_counts=True)
    AD_ratio = counts[0]/counts[1] #counts[0] is advance and counts[1] is decline
    print(values)
    print(counts)
    return AD_ratio

#function - Nifty 50
def GetADRatioFifty():
    url = 'https://www.moneycontrol.com/markets/indian-indices/top-nse-50-companies-list/9?classic=true'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    stk_idx = []
    for i in range(170,269,2): #keep an eye on indexes as they are hard coded for now, might change in future
        stk_idx.append(i)

    ad_list = []
    for i in stk_idx:
        ad_list.append(soup.findAll('span')[i].get('class').pop()) #gives grentxt/ redtxt based on advance or decline change

    values, counts = np.unique(ad_list, return_counts=True)
    AD_ratio = counts[0]/counts[1] #counts[0] is advance and counts[1] is decline
    print(values)
    print(counts)
    return AD_ratio


#test case
adr1 = GetADRatioHundred()
adr2 = GetADRatioFifty()
avgg = (adr1+adr2)/2


