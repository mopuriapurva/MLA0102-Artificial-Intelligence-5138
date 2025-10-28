import numpy as np

# ----------------------------
# Activation Functions
# ----------------------------

def sigmoid(x):
    """Sigmoid activation function."""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Derivative of sigmoid (for learning, optional)."""
    return x * (1 - x)

# ----------------------------
# Neural Network Definition
# ----------------------------

class FeedforwardNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases with small random values
        self.W1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.random.randn(1, hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.random.randn(1, output_size)

    def forward(self, X):
        """Perform forward propagation."""
        # Hidden layer
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = sigmoid(self.z1)

        # Output layer
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.output = sigmoid(self.z2)
        return self.output

# ----------------------------
# Example: XOR Problem
# ----------------------------

if __name__ == "__main__":
    # XOR input and output
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    y = np.array([
        [0],
        [1],
        [1],
        [0]
    ])

    # Create network with 2 inputs, 2 hidden neurons, 1 output
    nn = FeedforwardNeuralNetwork(input_size=2, hidden_size=2, output_size=1)

    # Print initial forward pass (untrained network)
    print("Initial Forward Propagation Results (Random Weights):\n")
    outputs = nn.forward(X)
    for i in range(len(X)):
        print(f"Input: {X[i]} → Output: {outputs[i][0]:.4f}")

    print("\n(Note: These are raw outputs before training. You can extend this with backpropagation.)")
