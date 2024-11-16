data = np.random.rand(10)
window = 3
moving_avg = np.convolve(data, np.ones(window)/window, mode='valid')
weights = np.array([0.1, 0.3, 0.6])
weighted_avg = np.convolve(data, weights, mode='valid')
print("Moving Average:", moving_avg)
print("Weighted Moving Average:", weighted_avg)
