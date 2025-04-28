import numpy as np

# Sigmoid activation and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)

# Define a basic MLP class
class SimpleMLP:
    def __init__(self, input_size, h1_neurons, h2_neurons, learning_rate):
        self.input_size = input_size
        self.h1_neurons = h1_neurons
        self.h2_neurons = h2_neurons
        self.lr = learning_rate

        # Random weights and biases
        self.w1 = np.random.rand(input_size, h1_neurons)
        self.b1 = np.random.rand(h1_neurons)

        self.w2 = np.random.rand(h1_neurons, h2_neurons)
        self.b2 = np.random.rand(h2_neurons)

        self.w3 = np.random.rand(h2_neurons, 1)
        self.b3 = np.random.rand(1)

    def forward(self, X):
        self.z1 = sigmoid(np.dot(X, self.w1) + self.b1)
        self.z2 = sigmoid(np.dot(self.z1, self.w2) + self.b2)
        self.output = sigmoid(np.dot(self.z2, self.w3) + self.b3)
        return self.output

    def backward(self, X, y):
        error = y - self.output
        d_output = error * sigmoid_derivative(self.output)

        error_z2 = d_output.dot(self.w3.T)
        d_z2 = error_z2 * sigmoid_derivative(self.z2)

        error_z1 = d_z2.dot(self.w2.T)
        d_z1 = error_z1 * sigmoid_derivative(self.z1)

        self.w3 += self.z2.T.dot(d_output) * self.lr
        self.b3 += np.sum(d_output, axis=0) * self.lr

        self.w2 += self.z1.T.dot(d_z2) * self.lr
        self.b2 += np.sum(d_z2, axis=0) * self.lr

        self.w1 += X.T.dot(d_z1) * self.lr
        self.b1 += np.sum(d_z1, axis=0) * self.lr

    def train(self, X, y, epochs=10000):
        for epoch in range(epochs):
            self.forward(X)
            self.backward(X, y)
            if epoch % 2000 == 0:
                loss = np.mean((y - self.output) ** 2)
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

        print("\nFinal Rounded Output:")
        print(np.round(self.output))


# Define your dataset (for N = 2)
# You can later change this for larger N (like 3-input logic gates)
def get_dataset(n_inputs):
    if n_inputs == 2:
        X = np.array([
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ])
        y = np.array([[0], [0], [0], [1]])  # AND gate
    else:
        print("Defaulting to random binary inputs.")
        X = np.random.randint(0, 2, size=(8, n_inputs))
        y = np.random.randint(0, 2, size=(8, 1))
    return X, y

# === MAIN PROGRAM ===
for i in range(1, 4):
    print(f"\n=== Combination {i} ===")
    n_inputs = int(input("Enter number of inputs (e.g., 2): "))
    h1 = int(input("Enter number of neurons in Hidden Layer 1: "))
    h2 = int(input("Enter number of neurons in Hidden Layer 2: "))
    lr = float(input("Enter learning rate (e.g., 0.1): "))

    X, y = get_dataset(n_inputs)
    print("\nTraining Data (X):\n", X)
    print("Expected Output (y):\n", y)

    mlp = SimpleMLP(input_size=n_inputs, h1_neurons=h1, h2_neurons=h2, learning_rate=lr)
    mlp.train(X, y)
