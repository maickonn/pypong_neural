Hello! First I would like to apologize for the grammar errors. HAHA :D

This source is a simple example of neural network to learning play a pong similar game.
You will need install the **pygame** and **numpy** libraries.

For this case have only 2 generations:

• **Initial generation:** Creates genomes randomly until value of constant **MAX_RANDOM_GENOME**.

• **Post initial generation:** Takes the best genome of initial generation and apply mutations it. Whenever the genome make the new record, we store the weights his on variables **best_genome_input_weights** and **best_genome_hidden_weights**. If he lose, the score will be reseted and a new genome will be created using the weights of the best genome, and applying mutations.

