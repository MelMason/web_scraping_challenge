#!/usr/bin/env python
# coding: utf-8

# # NASA Mars News

# In[3]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd
from splinter import Browser
import time
import urllib.request as request
from selenium import webdriver

def init_browser():
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    return browser


def scrape_info():
    browser = init_browser()




    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'lxml')


    # In[7]:


    # scrape the article title
    news_title = soup.find("div", class_="content_title").text
        
    # scrape the article paragraph text
    news_p = soup.find("div", class_="article_teaser_body").text
        
        
    # print article data
    print('-----------------')
    print(news_title)
    print(news_p)
        


    # # JPL Mars Space Images-Featured Image



    # In[36]:


    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)


    # In[37]:


    url_2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    # In[44]:


    # result = soup.find_all("div", class_="fancybox-inner fancybox-skin fancybox-dark-skin fancybox-dark-skin-open")
    # result = soup.find_all("li", class_="fancybox-thumb-active")

    image = soup.find("img", class_="thumb")["src"]


    # In[45]:


    # relative_image_path = soup.find_all('img')[1]["src"]
    image_url = 'https://www.jpl.nasa.gov/'+ image
    featured_image_url = image_url
    featured_image_url


    # # Mars Weather

    # In[17]:





    # In[18]:


    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)


    # In[19]:


    # URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'lxml')


    # In[20]:


    # Retrieve the parent divs for all articles
    results = soup.find("div", class_="js-tweet-text-container")

    weather = results.text

    # # Mars Facts

    # In[23]:


    url = 'https://space-facts.com/mars/'


    # In[24]:


    tables = pd.read_html(url)
    tables


    # In[25]:


    df = tables[0]
    df.columns = ['Description', 'Value']
    df


    # In[26]:


    df.set_index("Description", inplace = True)
    df


    # In[27]:


    html_table=df.to_html()
    html_table


    # In[28]:


    html_table.replace('\n', '')


    # In[ ]:


    df.to_html('table.html')



    # # Mars Hemispheres

    # In[ ]:


    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"},
    ]
    hemisphere_image_urls





    # Get the first news article
    news = soup.find('div', id='weather')

    # Get the featured image
    jpl_img = featured_image_url


    # Mars facts
    facts = html_table

    # Hemisphere pictures
    hemispheres = hemisphere_image_urls

    # # BONUS: Find the src for the sloth image
    # relative_image_path = soup.find_all('img')[2]["src"]
    # sloth_img = url + relative_image_path

    # Store data in a dictionary
    mars_data = {
        "news": news,
        "jpl_img": jpl_img,
        "weather": weather,
        "facts": facts,
        "hemispheres": hemispheres
    }

    print("mars_data")
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data



# In[ ]:




