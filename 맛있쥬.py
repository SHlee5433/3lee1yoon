import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

! pip install chardet
import chardet

# 파일의 인코딩 감지
with open('data/franchise2.csv', 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']

print(f"Detected encoding: {encoding}")

# 감지된 인코딩을 사용하여 파일 읽기
df = pd.read_csv('data/franchise2.csv', encoding=encoding)
df

df2 = df.drop(columns = '주요 업종별') \
        .query('시도별 == "서울특별시" | 시도별 == "부산광역시" | 시도별 == "강원도"') \
        .assign(total = (df['2018'] + df['2019'] + df['2020'] + df['2021'] + df['2022'])) \
        .groupby('total') \
        .agg(mean_year = ('total', 'mean'))
df2

x = df2['mean_year'].value_counts()
x.plot.bar(rot = 0)
plt.show()
