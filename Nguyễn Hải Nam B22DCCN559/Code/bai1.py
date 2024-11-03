import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Tạo danh sách lưu thông tin cầu thủ
player_list = []
 
url = ['https://fbref.com/en/squads/b8fd03ef/2023-2024/Manchester-City-Stats'
       ,'https://fbref.com/en/squads/18bb7c10/2023-2024/Arsenal-Stats',
       'https://fbref.com/en/squads/8602292d/2023-2024/Aston-Villa-Stats',
        'https://fbref.com/en/squads/4ba7cbea/2023-2024/Bournemouth-Stats',
        'https://fbref.com/en/squads/cd051869/2023-2024/Brentford-Stats',
        'https://fbref.com/en/squads/d07537b9/2023-2024/Brighton-and-Hove-Albion-Stats',
        'https://fbref.com/en/squads/943e8050/2023-2024/Burnley-Stats',
        'https://fbref.com/en/squads/cff3d9bb/2023-2024/Chelsea-Stats',
        'https://fbref.com/en/squads/47c64c55/2023-2024/Crystal-Palace-Stats',
        'https://fbref.com/en/squads/d3fd31cc/2023-2024/Everton-Stats',
        'https://fbref.com/en/squads/fd962109/2023-2024/Fulham-Stats',
        'https://fbref.com/en/squads/822bd0ba/2023-2024/Liverpool-Stats',
        'https://fbref.com/en/squads/e297cd13/2023-2024/Luton-Town-Stats',
        'https://fbref.com/en/squads/19538871/2023-2024/Manchester-United-Stats',
        'https://fbref.com/en/squads/b2b47a98/2023-2024/Newcastle-United-Stats',
        'https://fbref.com/en/squads/e4a775cb/2023-2024/Nottingham-Forest-Stats',
        'https://fbref.com/en/squads/1df6b87e/2023-2024/Sheffield-United-Stats',
        'https://fbref.com/en/squads/361ca564/2023-2024/Tottenham-Hotspur-Stats',
        'https://fbref.com/en/squads/7c21e445/2023-2024/West-Ham-United-Stats',
        'https://fbref.com/en/squads/8cec06e1/2023-2024/Wolverhampton-Wanderers-Stats']

for _ in range(0,len(url)):
    # Gửi yêu cầu và lấy nội dung trang
    r = requests.get(url[_])
    r.encoding = 'utf-8'
    soup = bs(r.content, 'html.parser')

    # Tìm đội và mùa giải
    main_squad = soup.find('div', {'id': 'info'})
    squad_tag = main_squad.find('span') if main_squad else None

    # Tìm bảng thống kê chính của đội
    main_table = soup.find('table', {'id': 'stats_standard_9'})
    rows = main_table.find_all('tr') if main_table else []

    for row in rows:
        # Kiểm tra hàng có chứa tên cầu thủ và quốc tịch không
        name_tag = row.find('th', attrs={'data-stat': 'player'})
        position_tag = row.find('td', attrs={'data-stat': 'position'})
        nation_tag = row.find('span', style="white-space: nowrap")

        if name_tag and nation_tag:
            # Lấy tên cầu thủ, đội và quốc tịch
            name = name_tag.text.strip()
            position = position_tag.text.strip()
            squad = ''.join(squad_tag.text.strip().split()[1:-1]) if squad_tag else 'N/A'
            nation = nation_tag.text.strip().split()[-1]

            # Lấy các dữ liệu từ cột thứ 3 đến cuối cùng
            row_data = [cell.text.strip() for cell in row.find_all('td')[2:-1]]

            minutes_tag = row.find('td', attrs={'data-stat': 'minutes'})
            minutes = minutes_tag.text.strip() if minutes_tag else 'N/A'

            minutes = minutes.replace(',', '') if minutes else 'N/A'
            if minutes.isdigit() and int(minutes) > 90:
                # Lưu thông tin cầu thủ
                player_info = [name, squad, nation, position] + row_data






                # Tìm bảng phụ để lấy thêm dữ liệu
                secondary_table = soup.find('table', {'id': 'stats_keeper_9'})
                rows_2 = secondary_table.find_all('tr') if secondary_table else []
                found = False
                for row_2 in rows_2:
                    # Kiểm tra hàng có chứa tên cầu thủ không
                    name_tag_2 = row_2.find('th', attrs={'data-stat': 'player'})
                    if name_tag_2 and name_tag_2.text.strip() == name:
                        # Lấy tất cả các cột từ cột 8 đến cột cuối cùng
                        columns_2 = row_2.find_all('td')[7:-1]  # Cột từ thứ 8 đến cuối
                        # additional_data2 = [col.text.strip() for col in columns_2]
                        additional_data2 = [(col.text.strip() if col.text.strip() else 'N/A') for col in columns_2]

                        
                        # Kết hợp thông tin cầu thủ với dữ liệu từ bảng phụ
                        player_info += additional_data2
                        found = True
                        break
                if not found:
                    player_info += ['N/A'] * 15




                third_table = soup.find('table', {'id': 'stats_shooting_9'})
                rows_3 = third_table.find_all('tr') if third_table else []
                for row_3 in rows_3:
                    # Kiểm tra hàng có chứa tên cầu thủ không
                    name_tag_3 = row_3.find('th', attrs={'data-stat': 'player'})
                    if name_tag_3 and name_tag_3.text.strip() == name:
                        # Lấy tất cả các cột từ cột 8 đến cột cuối cùng
                        columns_3 = row_3.find_all('td')[4:-1]
                        additional_data3 = [(col.text.strip() if col.text.strip() else 'N/A') for col in columns_3]
                        
                        # Kết hợp thông tin cầu thủ với dữ liệu từ bảng phụ
                        player_info += additional_data3
                        break
                

                fourth_table = soup.find('table', {'id': 'stats_passing_9'})
                rows_4 = fourth_table.find_all('tr') if fourth_table else []
                found = False
                for row_4 in rows_4:
                    name_tag_4 = row_4.find('th', attrs={'data-stat': 'player'})
                    if name_tag_4 and name_tag_4.text.strip() == name:
                        columns_4 = row_4.find_all('td')[4:-1]
                        additional_data4 = [(col.text.strip() if col.text.strip() else 'N/A') for col in columns_4]

                        player_info += additional_data4
                        found = True
                        break
                if not found:
                    player_info += ['N/A'] * 23




                fifth_table = soup.find('table', {'id': 'stats_passing_types_9'})
                rows_5 = fifth_table.find_all('tr') if fifth_table else []
                found = False
                for row_5 in rows_5:
                    name_tag_5 = row_5.find('th', attrs={'data-stat': 'player'})
                    if name_tag_5 and name_tag_5.text.strip() == name:
                        columns_5 = row_5.find_all('td')[5:-1]
                        additional_data5 = [(col.text.strip() if col.text.strip() else 'N/A') for col in columns_5]

                        player_info += additional_data5
                        found = True
                        break
                if not found:
                    player_info += ['N/A'] * 14
                




                sixth_table = soup.find('table', {'id': 'stats_gca_9'})
                rows_6 = sixth_table.find_all('tr') if sixth_table else []
                found = False
                for row_6 in rows_6:
                    name_tag_6 = row_6.find('th', attrs={'data-stat': 'player'})
                    if name_tag_6 and name_tag_6.text.strip() == name:
                        columns_6 = row_6.find_all('td')[4:-1]
                        additional_data6 = [(col.text.strip() if col.text.strip() else 'N/A') for col in columns_6]

                        player_info += additional_data6
                        found = True
                        break
                if not found:
                    player_info += ['N/A'] * 16



                seventh_table = soup.find('table', {'id': 'stats_defense_9'})
                rows_7 = seventh_table.find_all('tr') if seventh_table else []
                found = False
                for row_7 in rows_7:
                    name_tag_7 = row_7.find('th', attrs={'data-stat': 'player'})
                    if name_tag_7 and name_tag_7.text.strip() == name:
                        columns_7 = row_7.find_all('td')[4:-1]
                        additional_data7 = [(col.text.strip() if col.text.strip() else 'N/A') for col in columns_7]

                        player_info += additional_data7
                        found = True
                        break
                if not found:
                    player_info += ['N/A'] * 16




                eighth_table = soup.find('table', {'id': 'stats_possession_9'})
                rows_8 = eighth_table.find_all('tr') if eighth_table else []
                found = False
                for row_8 in rows_8:
                    name_tag_8 = row_8.find('th', attrs={'data-stat': 'player'})
                    if name_tag_8 and name_tag_8.text.strip() == name:
                        columns_8 = row_8.find_all('td')[4:-1]
                        additional_data8 = [(col.text.strip() if col.text.strip() else 'N/A') for col in columns_8]

                        player_info += additional_data8
                        found = True
                        break
                if not found:
                    player_info += ['N/A'] * 22





                ninth_table = soup.find('table', {'id': 'stats_playing_time_9'})
                rows_9 = ninth_table.find_all('tr') if ninth_table else []
                found = False
                for row_9 in rows_9:
                    name_tag_9 = row_9.find('th', attrs={'data-stat': 'player'})
                    if name_tag_9 and name_tag_9.text.strip() == name:
                        columns_9 = row_9.find_all('td')[3:-1]
                        additional_data9 = [(col.text.strip() if col.text.strip() else 'N/A') for col in columns_9]

                        player_info += additional_data9
                        found = True
                        break
                if not found:
                    player_info += ['N/A'] * 22






                tenth_table = soup.find('table', {'id': 'stats_misc_9'})
                rows_10 = tenth_table.find_all('tr') if tenth_table else []
                found = False
                for row_10 in rows_10:
                    name_tag_10 = row_10.find('th', attrs={'data-stat': 'player'})
                    if name_tag_10 and name_tag_10.text.strip() == name:
                        columns_10 = row_10.find_all('td')[4:-1]
                        additional_data10 = [(col.text.strip() if col.text.strip() else 'N/A') for col in columns_10]

                        player_info += additional_data10
                        found = True
                        break
                if not found:
                    player_info += ['N/A'] * 16



                player_list.append(player_info)



player_list.sort(key=lambda x: (x[0], int(x[4])))

 # Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(player_list, columns=['Name', 'Squad', 'Nation', 'Position' , 'Age', 'MP', 'Starts', 'Min', '90s', 'Gls', 'Ast', 'G+A', 
                                        'G-PK', 'PK', 'PKatt', 'CrdY', 'CrdR', 'xG', 'npxG', 'xAG', 'npxG+xAG', 'PrgC',
                                        'PrgP', 'PrgR', 'Gls', 'Ast', 'G+A', 'G-PK', 'G+A-PK', 'xG', 'xAG', 'xG+xAG', 'npxG', 'npxG+xAG', 'GA', 
                                        'GA90', 'SoTA', 'Saves', 'Save%', 'W', 'D', 'L', 'CS', 'CS%', 'PKatt', 'PKA', 'PKsv', 'PKm', 'Save%', 
                                        'Gls','Sh','SoT', 'Sot%', 'Sh/90', 'SoT/90', 'G/Sh', 'G/SoT', 'Dist', 'FK', 'PK', 'PKatt', 'xG', 'npxG',
                                        'npxG/Sh', 'G-xG', 'np:G-xG','Cmp', 'Att', 'Cmp%','TotDist','PrgDist', 'Cmp','Att',
                                        'Cmp%','Cmp','Att','Cmp%','Cmp','Att','Cmp%','Ast','xAG','xA','A-xAG','KP','1/3.','PPA','CrsPA','PrgP',
                                        'Live','Dead','FK','TB','Sw','Crs','TI','CK','In','Out','Str','Cmp','Off','Blocks','SCA','SCA90','PassLive',
                                        'PassDead','TO','Sh','Fld','Def','GCA','GCA90','PassLive','PassDead','TO','Sh','Fld','Def',
                                        'Tkl','TklW','Def3rd','Mid3rd','Att3rd','Tkl','Att','Tkl%','Lost','Blocks','Sh','Pass','Int','Tkl+Int','Clr','Err',
                                        'Touches','DefPen','Def3rd','Mid3rd','Att3rd','AttPen','Live','Att','Succ','Succ%','Tkld','Tkld%','Carries',
                                        'TotDist','PrgDist','PrgC','1/3.','CPA','Mis','Dis','Rec','PrgR',
                                        'MP','Min','Mn/MP','Min%','90s','Starts','Mn/Start','Compl','Subs','Mn/Sub','unSub','PPM','onG',
                                        'onGA','+/-','+/-90','On-Off','onxG','onxGA','xG+/-','xG+/-90','On-Off',
                                        'CrdY','CrdR','2CrdY','Fls','Fld','Off','Crs','Int','TklW','PKwon','PKcon','OG','Recov','Won','Lost','Won%'])

print(df)

# Lưu DataFrame vào tệp CSV
df.to_csv('results.csv', index=False)


# len(row_data) + len(additional_data2) +  len(additional_data3) + len(additional_data4)