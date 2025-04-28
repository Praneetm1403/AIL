#MLP Using Backpropagation (Sigmoid Activation)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Dummy example of simple forward and backward pass
inputs = np.random.rand(3)
weights = np.random.rand(3)
target = np.array([1])

for epoch in range(5):
    z = np.dot(inputs, weights)
    a = sigmoid(z)
    error = target - a
    gradient = error * a * (1 - a)
    weights += 0.1 * gradient * inputs

print("Final weights:", weights)
