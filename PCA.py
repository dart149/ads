from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
data = load_iris()
X = data.data
pca = PCA(n_components=2)
print("before reduction")
print(X[:5])
reduced_data = pca.fit_transform(X)
print("Reduced Data:")
print(reduced_data[:5])
