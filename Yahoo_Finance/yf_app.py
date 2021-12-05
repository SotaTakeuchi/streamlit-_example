import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st

st.title("米国株価可視化")

st.sidebar.write(
    '''
    # GAFA株価
    こちらは株価可視化ツールです。以下のオプションから表示日数を指定可能です
    '''
)

st.sidebar.write(
    '''
    ## 表示日数
    '''
)

days = st.sidebar.slider('日数', 1, 50, 20)

st.write(
    f'''
    ### 過去**{days}日間**のGAFAの株価
    '''
)

@st.cache
def get_data(days,tickers):
    df = pd.DataFrame()
    for company in Tickers.keys():
        tkr = yf.Ticker(Tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    return df

st.sidebar.write(
    '''
    ## 株価の範囲指定
    '''
)

ymin, ymax = st.sidebar.slider(
    '範囲を指定してください',
    0.0,
    4000.0, 
    (0.0, 4000.0)
)

Tickers = {
    'apple': 'AAPL',
    'facebook' : 'FB',
    'google': 'GOOGL',
    'microsoft':'MSFT',
    'netfilx':'NFLX',
    'amazon':'AMZN'
}

df = get_data(days, Tickers)

companies = st.multiselect(
    '会社名を選択してください',
    list(df.index),#リスト候補,
    ['google', 'amazon', 'facebook', 'apple']
)
if not companies:
    st.error('最低でも一社は選択してください')
else:
    data = df.loc[companies]
    st.write(
        '''
        ### 株価(USD)
        ''',
        data.sort_index()
    )
    data = data.T.reset_index()#グラフにするために転地する必要があった
    data = pd.melt(data, id_vars=['Date']).rename(columns = {'value' : 'Stock Prices(USD)'})
    chart = (
        alt.Chart(data)
        .mark_line(opacity = 0.8, clip = True)#折れ線グラフ
        .encode(#軸
            x = "Date:T",#Tはタイム。スペース開けてはいけない
            y = alt.Y("Stock Prices(USD):Q", stack = None, scale = alt.Scale(domain = [ymin, ymax])),
            color = 'Name:N'
        )
    )
    st.altair_chart(chart, use_container_width=True)
