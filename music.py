from selenium import webdriver
import requests
import bs4
import os

#urls
top_url="http://soundcloud.com/charts/top"
new_url="http://soundcloud.com/charts/new"
track_url="http://soundcloud.com/search/sounds?q="
artist_url="http://soundcloud.com/search/people?q="


borowser = webdriver.Chrome("chromedriver_win32 (1).zip")
borowser.get("http://soundcloud.com")