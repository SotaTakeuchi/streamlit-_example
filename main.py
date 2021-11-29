import streamlit as st#これは外部ライブラリ
#import numpy as np
#import pandas as pd
#from PIL import Image 
import time #pythonの標準ライブラリなのでrequirements.txtに書く必要なし


st.title('Streamlit first class')

#st.write('DataFrame')
#st.write('Display Image')
#st.write('Interactive Widgets')
st.write('プログレスバーの表示')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)#バーを用意

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)#バーの進捗
    time.sleep(0.1)

'Done!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を開く')
expander.write('問い合わせ内容を開く')
expander.write('問い合わせ内容を開く')


# text = st.text_input('your favorite')#サイドバーに記載したい時はst.sidebar.text_inputにする
# 'あなたの趣味：', text, 'です'

# condition = st.slider('your fine?', 0, 100, 50)#50はスタートの値
# 'condition', condition

# option = st.selectbox(
#     'あなたの好きな数字を教えて下さい',
#     list(range(1, 11))
# )

# '貴方の好きな数字は？', option , 'です'

# if st.checkbox('Show Image'):
#     img = Image.open('IMG_2007.JPG')
#     st.image(img, caption= '清野菜名', use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(20,3),#20行3列乱数生成(正規分布を元に)
#     columns= ['a', 'b', 'c']
# )

#st.line_chart(df)#折れ線グラフ
#st.area_chart(df)#特殊折れ線グラフ
#st.bar_chart(df)#棒グラフ→グラフの書き方種類はリファレンス参照

#st.table(df.style.highlight_max(axis = 0))

# df2 = pd.DataFrame(
#     np.random.rand(100, 2) / [50,50] + [35.69, 139.70],#大きすぎるので縮小して(1/50)新宿の緯度経度足す
#     columns= ['lat', 'lon']#緯度と軽度
# )

# st.map(df2)#新宿付近の情報を得る。ランダムに生成された緯度経度対して





