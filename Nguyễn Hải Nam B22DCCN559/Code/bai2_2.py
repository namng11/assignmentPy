import pandas as pd

df = pd.read_csv('results.csv')

# Lấy danh sách các cột chỉ số (loại trừ 'Name' và 'Squad')
attribute_cols = df.select_dtypes(include=['number']).columns.tolist()

# Tạo một DataFrame rỗng với hàng là các đội và 'all' cho toàn bộ giải đấu
teams = ['all'] + df['Squad'].unique().tolist()
results = pd.DataFrame(index=teams)

# Tính toán trung vị, trung bình, và độ lệch chuẩn cho toàn bộ giải đấu
for col in attribute_cols:
    # Tính cho toàn bộ giải đấu
    results.at['all', f'{col}_Median'] = df[col].median()
    results.at['all', f'{col}_Mean'] = df[col].mean()
    results.at['all', f'{col}_Std'] = df[col].std()

    # Tính cho từng đội
    for squad in df['Squad'].unique():
        results.at[squad, f'{col}_Median'] = df[df['Squad'] == squad][col].median()
        results.at[squad, f'{col}_Mean'] = df[df['Squad'] == squad][col].mean()
        results.at[squad, f'{col}_Std'] = df[df['Squad'] == squad][col].std()

# Lưu kết quả vào tệp CSV
results.to_csv('results2.csv')