#MLP Using Backpropagation (Sigmoid Activation)
"""Implement a simple Multi-Layer Perceptron with N binary inputs, two
hidden layers and one output. Use backpropagation and Sigmoid function
as activation function. """

import numpy as np

# Sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    sx = sigmoid(x)
    return sx * (1 - sx)

# Binary Cross-Entropy Loss
def binary_cross_entropy(y_true, y_pred):
    return -np.mean(y_true*np.log(y_pred+1e-8) + (1 - y_true)*np.log(1 - y_pred + 1e-8))

# MLP class
class MLP:
    def __init__(self, input_size, hidden1_size, hidden2_size, learning_rate=0.1):
        self.lr = learning_rate
        
        self.w1 = np.random.randn(input_size, hidden1_size)
        self.b1 = np.zeros((1, hidden1_size))
        
        self.w2 = np.random.randn(hidden1_size, hidden2_size)
        self.b2 = np.zeros((1, hidden2_size))
        
        self.w3 = np.random.randn(hidden2_size, 1)
        self.b3 = np.zeros((1, 1))
    
    def forward(self, X):
        self.z1 = np.dot(X, self.w1) + self.b1
        self.a1 = sigmoid(self.z1)
        
        self.z2 = np.dot(self.a1, self.w2) + self.b2
        self.a2 = sigmoid(self.z2)
        
        self.z3 = np.dot(self.a2, self.w3) + self.b3
        self.a3 = sigmoid(self.z3)
        
        return self.a3
    
    def backward(self, X, y, output):
        m = X.shape[0]
        error = output - y
        
        dz3 = error * sigmoid_derivative(self.z3)
        dw3 = np.dot(self.a2.T, dz3) / m
        db3 = np.sum(dz3, axis=0, keepdims=True) / m
        
        dz2 = np.dot(dz3, self.w3.T) * sigmoid_derivative(self.z2)
        dw2 = np.dot(self.a1.T, dz2) / m
        db2 = np.sum(dz2, axis=0, keepdims=True) / m
        
        dz1 = np.dot(dz2, self.w2.T) * sigmoid_derivative(self.z1)
        dw1 = np.dot(X.T, dz1) / m
        db1 = np.sum(dz1, axis=0, keepdims=True) / m
        
        # Update weights
        self.w3 -= self.lr * dw3
        self.b3 -= self.lr * db3
        
        self.w2 -= self.lr * dw2
        self.b2 -= self.lr * db2
        
        self.w1 -= self.lr * dw1
        self.b1 -= self.lr * db1

    def train(self, X, y, epochs=10000, verbose=False):
        for epoch in range(epochs):
            output = self.forward(X)
            loss = binary_cross_entropy(y, output)
            self.backward(X, y, output)
            if verbose and epoch % 1000 == 0:
                print(f"Epoch {epoch}, Loss: {loss:.4f}")
        print("Training complete.")

# Sample binary input data (N = 3)
X = np.array([
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

y = np.array([[0], [1], [1], [0]])  # XOR-like output

# Create and train model
mlp = MLP(input_size=3, hidden1_size=4, hidden2_size=3, learning_rate=0.5)
mlp.train(X, y, epochs=10000, verbose=True)

# Final outputs
print("\nPredictions:")
print(mlp.forward(X))

print("\nFinal weights and biases:")
print("w1:\n", mlp.w1)
print("b1:\n", mlp.b1)
print("w2:\n", mlp.w2)
print("b2:\n", mlp.b2)
print("w3:\n", mlp.w3)
print("b3:\n", mlp.b3)
