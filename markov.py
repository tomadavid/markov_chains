# TODO check if transition matrix is stochastic ERROR
# TODO check if initial state's probability add up to 1 ERROR
# TODO check if n = lenght of matrix and initial
# TODO make comments more mathematically accurate


""" 
    The bellow class Markov_chain offers the utility functions 
    for solving basic problems with Markov Chains.
"""
import copy

class Markov_chain:
    def __init__(self, matrix: int, num_states: int):
        self.matrix = matrix
        self.num_states = num_states

    # Calculates the n-step transition probablity matrix of the Markov's chain.
    def n_step_matrix(self, n: int):
        if n == 1:
            return self.matrix

        n_step = copy.deepcopy(self.matrix)
        for i in range(n-1):
            current = copy.deepcopy(n_step)
            for row in range(self.num_states):
                for col in range(self.num_states):
                    elem = 0
                    for j in range(self.num_states):
                        elem += current[row][j]*self.matrix[j][col]
                    n_step[row][col] = elem
        return n_step
    
    # Returns the probability of a transition with n steps from start state to end state.
        # Calculates the n-step transition probablity matrix 
        # and gets the value of the transition from start to end state
    def transition_prob(self, start: int, end: int, steps: int):
        return self.n_step_matrix(steps)[start-1][end-1]
    
    # Given an initial vector with the displacement of probability in each state
    # it returns an array with the probability of the chain being in each state 
    # after n transitions
    def state_after_n_steps(self, initial: int, steps: int):
        prob_vector = []
        for i in range(self.num_states): prob_vector += [0]

        n_step_mtrx = self.n_step_matrix(steps)
        for row in range(self.num_states):
            for col in range(self.num_states):
                prob_vector[row] += n_step_mtrx[row][col]*initial[col]

        return prob_vector
    
    # Given an array containing the trajectory of the chain, 
    # it returns the probability of it following that trajectory
    def trajectory(self, initial: int, path: int, n: int):
        p0 = initial[path[0]-1]
        for i in range(1, n):
            p0 *= self.matrix[path[i-1]-1][path[i]-1]
        return p0

# testing
if __name__ == "__main__":

    matrix = [[0.1, 0.5, 0.4], 
              [0.6, 0.2, 0.2],
              [0.3, 0.4, 0.3]]
    
    initial = [0.7, 0.2, 0.1]

    path = [1, 3, 3, 2]

    markov_chain = Markov_chain(matrix, 3)
    
    ex_1 = markov_chain.transition_prob(1, 3, 2)
    ex_2 = markov_chain.transition_prob(2, 3, 3)

    ex_3 = markov_chain.state_after_n_steps(initial, 2)
    ex_4 = markov_chain.trajectory(initial, path, 4)

    print(ex_3)
    print(ex_4)
