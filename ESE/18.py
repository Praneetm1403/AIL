#MLP – 4 Binary Inputs, 1 Hidden Layer, 2 Binary Outputs
def create_simple_mlp():
    W1 = np.random.rand(4, 3)
    B1 = np.random.rand(3)
    W2 = np.random.rand(3, 2)
    B2 = np.random.rand(2)

    steps = np.random.randint(5, 15)

    print("Weight Matrix 1:\n", W1)
    print("Bias 1:\n", B1)
    print("Weight Matrix 2:\n", W2)
    print("Bias 2:\n", B2)
    print("Total Steps:", steps)

create_simple_mlp()
