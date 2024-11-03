import pandas as pd

df = pd.read_csv('results.csv')
for column in df.columns[5:]:  # Bắt đầu từ cột 5 ('MP')
    try:
        max_value = df[column].max()  # Tìm giá trị lớn nhất
        top_teams = df[df[column] == max_value]  # Lọc các hàng có giá trị lớn nhất
        team_names = top_teams['Squad'].unique()  # Lấy tên đội duy nhất
        print(f"Đội bóng có chỉ số {column} cao nhất: {team_names}")
    except TypeError:  # Xử lý các cột không phải số
        print(f"Bỏ qua cột '{column}' (kiểu dữ liệu không phải số)")