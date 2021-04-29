import streamlit as st
import yfinance as yf
import datetime
import pandas as pd
#import calendar Not working with Horuko



def main ():
    st.title("Stock Price")
    year=range(2005,2021)
    month=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ticker=st.sidebar.text_input('Ticker (e.g. AAPL):')

    Year_choice=st.sidebar.selectbox("Year",year)
    Month_choice_1=st.sidebar.selectbox('Month',month)
    tickerdata=yf.Ticker(ticker)
    Month_choice=month.index(Month_choice_1)+1
    end_date=datetime.date(Year_choice,Month_choice+1,1)
    #end_date=end_date-datetime.timedelta(days=1)
    tickerDf=tickerdata.history(period='1d',start=datetime.date(Year_choice,int(Month_choice),1),end=end_date)
    st.write('{} {} {}'.format(ticker,Month_choice_1,Year_choice))

    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)




if __name__ =='__main__':
    main()
