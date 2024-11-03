import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Hàm để vẽ biểu đồ radar
def radar_chart(df, player1, player2, attributes):
    # Lấy dữ liệu của hai cầu thủ
    player1_data = df[df['Player'] == player1].iloc[0][attributes].values
    player2_data = df[df['Player'] == player2].iloc[0][attributes].values

    # Tạo các góc cho biểu đồ radar
    num_vars = len(attributes)
    angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
    angles += angles[:1]  # Đóng vòng tròn

    # Chuyển dữ liệu cầu thủ thành vòng tròn
    player1_data = np.append(player1_data, player1_data[0])
    player2_data = np.append(player2_data, player2_data[0])

    # Vẽ biểu đồ radar
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], attributes, color='grey', size=8)

    # Vẽ dữ liệu của cầu thủ thứ nhất
    ax.plot(angles, player1_data, linewidth=1, linestyle='solid', label=player1)
    ax.fill(angles, player1_data, 'b', alpha=0.1)

    # Vẽ dữ liệu của cầu thủ thứ hai
    ax.plot(angles, player2_data, linewidth=1, linestyle='solid', label=player2)
    ax.fill(angles, player2_data, 'r', alpha=0.1)

    # Cài đặt tên cầu thủ trong phần chú thích
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    plt.title(f"So sánh cầu thủ {player1} và {player2}")
    plt.show()

# Hàm chính để xử lý tham số đầu vào
def main():
    parser = argparse.ArgumentParser(description="Vẽ biểu đồ radar để so sánh các chỉ số của hai cầu thủ.")
    parser.add_argument("--p1", required=True, help="Tên cầu thủ thứ nhất")
    parser.add_argument("--p2", required=True, help="Tên cầu thủ thứ hai")
    parser.add_argument("--Attribute", required=True, help="Danh sách các chỉ số cần so sánh, cách nhau bởi dấu phẩy")

    args = parser.parse_args()
    player1 = args.p1
    player2 = args.p2
    attributes = args.Attribute.split(',')

    # Đọc dữ liệu từ file CSV
    df = pd.read_csv('results.csv')

    # Kiểm tra các cầu thủ có tồn tại trong dữ liệu hay không
    if player1 not in df['Player'].values or player2 not in df['Player'].values:
        print(f"Không tìm thấy dữ liệu của {player1} hoặc {player2}.")
        return

    # Kiểm tra các thuộc tính có tồn tại trong dữ liệu hay không
    missing_attributes = [attr for attr in attributes if attr not in df.columns]
    if missing_attributes:
        print(f"Các thuộc tính không tồn tại trong dữ liệu: {', '.join(missing_attributes)}")
        return

    # Vẽ biểu đồ radar
    radar_chart(df, player1, player2, attributes)

if __name__ == "__main__":
    main()




# python radarChartPlot.py --p1 "Tên cầu thủ 1" --p2 "Tên cầu thủ 2" --Attribute "Age,MP,Starts"