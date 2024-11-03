import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('results.csv')

features = ['Age', 'MP', 'Starts', 'Min', '90s', 'Gls', 'Ast']  # Thay đổi các features nếu cần
X = df[features]

# Convert 'Min' column to numeric, handling errors by setting non-numeric values to NaN
X['Min'] = pd.to_numeric(X['Min'].str.replace(',', ''), errors='coerce')

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
n_clusters = 5  # Thay đổi số lượng clusters nếu cần

kmeans = KMeans(n_clusters=n_clusters, random_state=42)  # random_state để đảm bảo kết quả nhất quán
kmeans.fit(X_scaled)

df['Cluster'] = kmeans.labels_

print(df[df['Cluster'] == 0])

# Calculate cluster means, ensuring only numeric columns are used
cluster_means = df.groupby('Cluster')[features].mean(numeric_only=True)
print(cluster_means)



df.to_csv('results3.csv', index=False)