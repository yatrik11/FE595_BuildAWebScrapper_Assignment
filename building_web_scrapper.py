# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:18:11 2019

@author: Yatri Kalathia
"""

import requests
from bs4 import BeautifulSoup
import re

characters = [] #creating list to store fictional characters

for i in range(50):
    page = requests.get("https://theyfightcrime.org/") #requesting web page
    soup = BeautifulSoup(page.content,'html.parser') #fetching page contents
    fict_char = soup.find_all('p')[1].get_text() #getting first appearing paragraph tag
    fict_char = re.split(r'(?<=\w[,\.])\s', fict_char) #splitting contents of the paragraph by fullstop
    characters.append(fict_char) #appending sentences to the list
    
characters

#creating 2 seperate files for male and female characters
fw1 = open('C:/Users/Yatri Kalathia/Downloads/male.txt','w')
fw2 = open('C:/Users/Yatri Kalathia/Downloads/female.txt','w')


for i in range(len(characters)):
        fw1.write(characters[i][0]+'\n')
        fw2.write(characters[i][1]+'\n')
        
fw1.close()
fw2.close()
