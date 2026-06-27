import streamlit as st
import matplotlib.pyplot as plt

# 網頁標題
st.title("手機品牌市占率圓餅圖")

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Heiti TC', 'Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 資料
labels = ['Nokia', 'Samsung', 'Apple', 'Lumia']
sizes = [20, 30, 45, 10]
colors = ['yellow', 'green', 'red', 'blue']
explode = [0.3, 0, 0, 0]  # 第一塊 Nokia 突出顯示

# 繪製圓餅圖
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    shadow=True,
    autopct='%1.1f%%',
    startangle=180
)

# 使用 st.pyplot 顯示圖表
st.pyplot(fig)
