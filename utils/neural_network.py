# This class are based on post: https://enlight.nyc/projects/neural-network/
# Special thanks the creator. <3

import random
import math


# PS: The structure of this neural network is:
#   O  O
#      O  O
#   O  O
#
# This neural network is not dynamic. For works with more neurons is necessary adaptations

class NeuralNetwork:
    # Constants
    INPUT_SIZE = 2
    HIDDEN_SIZE = 3
    OUTPUT_SIZE = 1

    def __init__(self):
        # Create vars
        self.input_weights = []
        self.hidden_weights = []

        self.generate_weights()

    def generate_weights(self):
        # Creates 2x3 matrix (this can easily identify where weights are of first or second input).
        self.input_weights = [0.0] * self.INPUT_SIZE
        for i in range(len(self.input_weights)):
            self.input_weights[i] = [random.uniform(-1, 1) for _ in range(self.HIDDEN_SIZE)]

        # Creates array with weights of hidden layer length
        self.hidden_weights = [random.uniform(-1, 1) for _ in range(self.HIDDEN_SIZE)]

    def get_output(self, input_1, input_2):
        # Creates array to store calculated inputs and weights
        calculated_weights = [0.0] * self.HIDDEN_SIZE

        calculated_weights[0] = self.sigmoid((input_1 * self.input_weights[0][0]) + (input_2 * self.input_weights[1][0]))
        calculated_weights[1] = self.sigmoid((input_1 * self.input_weights[0][1]) + (input_2 * self.input_weights[1][1]))
        calculated_weights[2] = self.sigmoid((input_1 * self.input_weights[0][2]) + (input_2 * self.input_weights[1][2]))

        output = self.sigmoid((calculated_weights[0] * self.hidden_weights[0]) + (calculated_weights[1] * self.hidden_weights[1]) + (calculated_weights[2] * self.hidden_weights[2]))
        return output

    def make_mutation(self):
        # Modify randomly some weights
        for i in range(random.randint(1, 9)):
            weight_index = random.randint(1, 9)
            if weight_index <= 3:
                self.input_weights[0][weight_index - 1] = random.uniform(-1, 1)
            elif weight_index <= 6:
                self.input_weights[1][weight_index - 4] = random.uniform(-1, 1)
            elif weight_index <= 9:
                self.hidden_weights[weight_index - 7] = random.uniform(-1, 1)

    def sigmoid(self, x):
        # This try prevents overflow
        try:
            return 1 / (1 + math.exp(-x))
        except:
            return 0