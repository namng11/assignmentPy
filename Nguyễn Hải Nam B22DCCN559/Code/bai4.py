from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Hàm để lấy dữ liệu từ một URL
def get_player_data(url):
    driver.get(url)
    time.sleep(5)  # Đợi trang tải hoàn tất

    # Tìm phần tử <tbody> chứa thông tin cầu thủ
    table_body = driver.find_element(By.ID, 'player-table-body')
    rows = table_body.find_elements(By.TAG_NAME, 'tr')

    # Tạo danh sách để lưu thông tin cầu thủ
    player_list = []

    # Duyệt qua từng hàng trong bảng
    for row in rows:
        # Tạo một danh sách để lưu dữ liệu của từng ô trong hàng
        row_data = []

        # Lấy tên cầu thủ
        name_tag = row.find_element(By.CLASS_NAME, 'td-player').find_element(By.TAG_NAME, 'a')
        name = name_tag.text.strip() if name_tag else "N/A"
        row_data.append(name)

        # Lấy câu lạc bộ chuyển đi
        club_from_tag = row.find_element(By.CLASS_NAME, 'transfer-club--from')
        club_from_name_tag = club_from_tag.find_element(By.CLASS_NAME, 'transfer-club__name') if club_from_tag else None
        club_from = club_from_name_tag.text.strip() if club_from_name_tag else "N/A"
        row_data.append(club_from)

        # Lấy câu lạc bộ chuyển đến
        club_to_tag = row.find_element(By.CLASS_NAME, 'transfer-club--to')
        club_to_name_tag = club_to_tag.find_element(By.CLASS_NAME, 'transfer-club__name') if club_to_tag else None
        club_to = club_to_name_tag.text.strip() if club_to_name_tag else "N/A"
        row_data.append(club_to)

        # Lấy ngày chuyển nhượng
        date_tag = row.find_element(By.CLASS_NAME, 'td-date')
        transfer_date = date_tag.text.strip() if date_tag else "N/A"
        row_data.append(transfer_date)

        # Lấy phí chuyển nhượng
        price_tag = row.find_element(By.CLASS_NAME, 'td-price')
        transfer_fee = price_tag.text.strip() if price_tag else "N/A"
        row_data.append(transfer_fee)

        # Thêm thông tin của cầu thủ vào danh sách
        player_list.append(row_data)

    return player_list

driver = webdriver.Chrome()

urls = ['https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024',
       'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/2',
       'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/3',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/4',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/5',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/6',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/7',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/8',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/9',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/10',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/11',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/12',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/13',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/14',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/15',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/16',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/17',
        'https://www.footballtransfers.com/us/leagues-cups/national/uk/premier-league/transfers/2023-2024/18']


all_players = []


for url in urls:
    players = get_player_data(url)
    all_players.extend(players)


driver.quit()

# Chuyển danh sách thành DataFrame và hiển thị kết quả
df = pd.DataFrame(all_players, columns=['Tên cầu thủ', 'Câu lạc bộ chuyển đi', 'Câu lạc bộ chuyển đến', 'Ngày chuyển nhượng', 'Phí chuyển nhượng'])
print(df)