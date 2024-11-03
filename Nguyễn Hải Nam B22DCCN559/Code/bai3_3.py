import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv('results.csv')

# Xác định các thuộc tính sử dụng để phân cụm
features = ['Age', 'MP', 'Starts', 'Min', '90s', 'Gls', 'Ast', 'G+A', 'G-PK', 'PK', 'PKatt', 'CrdY', 'CrdR', 'xG', 'npxG', 'xAG', 'npxG+xAG', 'PrgC',
            'PrgP', 'PrgR', 'Gls', 'Ast', 'G+A', 'G-PK', 'G+A-PK', 'xG', 'xAG', 'xG+xAG', 'npxG', 'npxG+xAG']
X = df[features]

# Chuyển cột 'Min' thành kiểu số, loại bỏ dấu phẩy và xử lý lỗi
X['Min'] = pd.to_numeric(X['Min'].str.replace(',', ''), errors='coerce')

# Kiểm tra và điền giá trị thiếu nếu có
X = X.fillna(0)  # Điền giá trị NaN bằng 0, hoặc bạn có thể dùng các phương pháp xử lý khác

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Áp dụng KMeans clustering
n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X_scaled)
df['Cluster'] = kmeans.labels_

# Áp dụng PCA để giảm xuống 2 chiều
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Vẽ biểu đồ phân tán các cụm
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['Cluster'], cmap='viridis')
plt.title('Clusters of Football Players (PCA)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()