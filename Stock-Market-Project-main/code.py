#Importing the libraries 

import time               # representing time in code, such as objects, numbers, and strings
import numpy as np        # used for working with arrays
import yfinance as yf     #enables us to fetch historical market data from Yahoo Finance API in a Pythonic way
import streamlit as st    # helps us create web apps for data science and machine learning
from streamlit_option_menu import option_menu
import pandas as pd       # provides high-performance data manipulation in Python. 
from PIL import Image     # help us to import images and to display on web pages
import requests

#Creating the menu on the pages
selected =option_menu(
    menu_title = "Main Menu",
    options = ["Home","Project","Contact"],
    icons =["house","book","envelope"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal",
    styles={
        "container":{"padding":"0!important","background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "20px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},

    }
)

if selected== "Home" :
    st.title(f"About Our Project ")
    image = Image.open("C:/Users/Hello/StockProject/project.png")       #importing images
    st.image(image,use_column_width= True)
    st.header(f"What is the Stock Market?")          #intro
    st.caption("""The stock market is a place where people buy and sell shares, or little parts of 
                companies. Companies offer these shares for sale so they can get money to improve their
                businesses. Investing in shares can be a good way to make money.Buyers and sellers can 
                trade equity shares of public firms in stock exchanges.Due to their ability to democratise 
                access to investor trading and capital exchange, stock markets are essential elements of a 
                free-market economy. Markets for stocks produce effective price discovery and dealing .""")
    st.header(f"Two Basic Approaches to Stock Market Investing –")  
    st.caption("""Value investors frequently make investments in long-standing businesses that have 
                demonstrated consistent profitability over an extended period of time and may provide
                a constant dividend income. While value investors do look to acquire stocks when they 
                believe the stock price to be an inexpensive bargain, value investing is more risk-
                averse than growth investment.""")
    st.caption("""In order to achieve the greatest possible increase in share price, growth investors 
                look for businesses with particularly high growth potential. They typically place 
                less importance on dividend income and are more prepared to take a chance when 
                investing in small companies. Growth investors frequently prefer technology stocks 
                due to their great growth potential.""")          
    image = Image.open("C:/Users/Hello/StockProject/images2.jpg")
    st.image(image,use_column_width= True)

if selected== "Project":
    st.title(""" **Stock Market Data Analysis** """)
    image = Image.open("C:/Users/Hello/StockProject/images.jpg")
    st.image(image,use_column_width= True)
    #creating a sidebar header
    st.sidebar.header('User Input Data')           

    def about():
        requestString = f"""https://query1.finance.yahoo.com/v10/finance/quoteSummary/{tickerSymbol}?modules=assetProfile%2Cprice"""
        request = requests.get(f"{requestString}",headers={"USER-AGENT":"Mozilla/5.0"})
        json = request.json()
        # serializing structured data and exchanging it over a network, typically between a server and web applications.
        data = json["quoteSummary"]["result"][0]

        #directly connecting the data from website 
        st.header("Profile")
        st.metric("Sector",data['assetProfile']["sector"])
        st.metric("Industry",data["assetProfile"]["industry"])
        st.metric("Website",data["assetProfile"]["website"])
        st.metric("MarketCap",data["price"]['marketCap']['fmt'])
        with st.expander("About company"):
            st.write(data["assetProfile"]["longBusinessSummary"])

    # creating a function to get the user input 
    def get_input():
        tickerSymbol = st.sidebar.selectbox("Stock Select",["TCS.NS","IRCTC.NS","LICI.NS","WIPRO.NS","MRF.NS","COALINDIA.NS","TITAN.NS","ICICIBANK.NS","TATAMOTORS.NS","SBIN.NS"])
        start_date = st.sidebar.date_input("Start Date - (YY-MM-DD)",value = pd.to_datetime("01-01-2010"))
        end_date = st.sidebar.date_input("End Date - (YY-MM-DD) ",value = pd.to_datetime("today"))
        return tickerSymbol , start_date , end_date
    
    # calling the data directly from yfinance website all the history of stock 
    def get_data(tickerSymbol,start_date,end_date):
        if tickerSymbol=='TCS.NS' or tickerSymbol=='LICI.NS' or tickerSymbol=='IRCTC.NS' or tickerSymbol=='WIPRO.NS' or tickerSymbol=='MRF.NS' or tickerSymbol=='COALINDIA.NS':
            tickerData = yf.Ticker(tickerSymbol)
        elif tickerSymbol=='TITAN.NS' or tickerSymbol=='ICICIBANK.NS' or tickerSymbol=='TATAMOTORS.NS' or tickerSymbol=='SBIN.NS':
            tickerData = yf.Ticker(tickerSymbol)  
        else:
            tickerData =pd.DataFrame(column = ['Date','Close','Open','Volume','Adj Close','High','Low'])

        df = tickerData.history(period='1d' , start=start_date,end=end_date)
        return df
        
    tickerSymbol , start_date , end_date = get_input()
    df = get_data(tickerSymbol , start_date , end_date)
    about()
    st.header(tickerSymbol+" Open Price\n")
    st.line_chart(df.Open)
    st.header(tickerSymbol+" Close Price\n")
    st.line_chart(df.Close)
    st.header(tickerSymbol+" Volume\n")
    st.bar_chart(df.Volume)
    st.header(tickerSymbol+" High\n")
    st.area_chart(df.High)
    st.header('Data Statistics')
    st.write(df.describe()) 

    click = st.sidebar.checkbox("All Information")   # display all the information to buy or sell
    if click:
        #stored in google excel sheet 
        st.header('ALL INFORMATION')
        sheet_id = '1ZEIhZijTWNZFYmnBSFX7hbPxzzpNRU'
        df =pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
        st.write(df)

# contact part of the project
if selected== "Contact" :
    st.title(f"CONTACT US! ")
    my_form = st.form(key = "Form")
    name = my_form.text_input(label = "Enter your name : ")
    number = my_form.slider("Rating ", min_value=10, max_value = 100 )
    submit = my_form.form_submit_button(label = "Submit this form")

