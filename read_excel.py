import pandas as pd

# Excelファイルを読み込む（1行目をスキップ）
df = pd.read_excel('sheet.xlsx', skiprows=1, header=None)

# 2行目以降のA列（インデックス0）とB列（インデックス1）を連結
for index, row in df.iterrows():
    # A列とB列の値を文字列に変換して連結
    a_value = str(row.iloc[0]) if pd.notna(row.iloc[0]) else ''
    b_value = str(row.iloc[1]) if pd.notna(row.iloc[1]) else ''
    concatenated = a_value + " + " + b_value
    print(concatenated)

