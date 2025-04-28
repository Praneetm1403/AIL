import numpy as np

def create_mlp(N, hidden1, hidden2):
    # Random initialization
    W1 = np.random.rand(N, hidden1)
    B1 = np.random.rand(hidden1)
    W2 = np.random.rand(hidden1, hidden2)
    B2 = np.random.rand(hidden2)
    W3 = np.random.rand(hidden2, 1)
    B3 = np.random.rand(1)

    steps = np.random.randint(5, 15)

    print("Weight Matrix 1:\n", W1)
    print("Bias 1:\n", B1)
    print("Weight Matrix 2:\n", W2)
    print("Bias 2:\n", B2)
    print("Weight Matrix 3:\n", W3)
    print("Bias 3:\n", B3)
    print("Total Steps:", steps)

N = int(input("Enter number of input neurons: "))
create_mlp(N, 4, 3)
