from sklearn.manifold import MDS
import matplotlib.pyplot as plt
X = np.random.rand(10, 5)
mds = MDS(n_components=2, random_state=42)
transformed = mds.fit_transform(X)
plt.scatter(transformed[:, 0], transformed[:, 1])
plt.title('MDS Projection')
plt.show()
