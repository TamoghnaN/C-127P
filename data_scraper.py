from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

Url = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(Url)

scrape_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")
    
    bright_star_table = soup.find("table", attrs = ("class","wikitable" ))
    
    table_body = bright_star_table.find('tbody')
    
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols  = table_row.find_all('td')
        print (table_cols)
        
        temp_list = []
        
        for col_data in table_cols:
            data =cols_data.text.strip()
            
            temp_list.append(data)
        
        scrape_data.append(temp_list)
    
scrape()

star_data = []
for i in range(0,len(scrape_data)):
    Star_names  = scrape_data[i][1]
    Distance = scrape_data[i][3]
    Mass = scrape_data[i][5]
    Radius = scrape_data[i][6]
    Luminosity = scrape_data[i][7]
    
    required_data = [Star_names, Distance, Mass, Radius, Luminosity]
    star_data.append(required_data)
print (star_data)

headers = ['Star_name','Distance','Mass','Radius','Luminosity']

star_df_1 = pd.DataFrame(stars_data, colums = headers)

star_df_1.to_csv('scraped_data.csv', index = True, index_label="id")