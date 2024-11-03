import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
df = pd.read_csv('results.csv')

# Xác định các chỉ số cụ thể để vẽ histogram
stat_columns = ['Age', 'MP', 'Starts', '90s', 'Gls', 'Ast']

# 1. Vẽ histogram phân bố cho mỗi chỉ số trên toàn giải
for col in stat_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f'Phân bố {col} - Toàn giải')
    plt.xlabel(col)
    plt.ylabel('Tần suất')
    plt.show()

# 2. Vẽ histogram phân bố cho mỗi chỉ số cho từng đội
teams = df['Squad'].unique()
for team in teams:
    team_data = df[df['Squad'] == team]
    for col in stat_columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(team_data[col].dropna(), kde=True)
        plt.title(f'Phân bố {col} - {team}')
        plt.xlabel(col)
        plt.ylabel('Tần suất')
        plt.show()   