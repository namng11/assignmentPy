

import pandas as pd

df = pd.read_csv('results.csv')
df['Min'] = df['Min'].str.replace(',', '').astype(int)
df.to_csv('results.csv', index=False)
df = pd.read_csv('results.csv')
for column in df.columns[4:]:
    try:
        df[column] = pd.to_numeric(df[column], errors='coerce') 
        
        # Sắp xếp theo cột hiện tại theo thứ tự giảm dần và lấy 3 hàng đầu
        top_3 = df.sort_values(by=column, ascending=False).head(3)
        
        # Sắp xếp theo cột hiện tại theo thứ tự tăng dần và lấy 3 hàng cuối (loại trừ NaN)
        bottom_3 = df.sort_values(by=column, ascending=True).dropna(subset=[column]).head(3)
        
        print(f"Top 3 cho {column}:\n{top_3[['Name', column]]}\n") 
        print(f"3 cầu thủ cuối bảng cho {column}:\n{bottom_3[['Name', column]]}\n")
    except (TypeError, ValueError): # Xử lý các cột không thể chuyển đổi thành số
        print(f"Bỏ qua cột '{column}' (kiểu dữ liệu không phải số hoặc hỗn hợp)\n")