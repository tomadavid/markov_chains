""" 
    The bellow class Markov_chain offers the utility functions 
    for solving basic problems with discrete-time Markov Chains (DTMC).
"""
import copy

class Markov_chain:
    # A Markov_chain object is characterized by its transition matrix
    def __init__(self, matrix: int):
        stochastic_check(matrix) # check if matrix is stockastic
            
        self.matrix = matrix
        self.num_states = len(matrix)


    # Calculates the n-step transition probablity matrix of the Markov's chain.
    #
    # Follows one important result of the Kolmogorov-Chapman's equation, that 
    # the n-step transition probablity matrix is equal to the Markov Chain's 
    # transition matrix to the power of n.
    #
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
    #
    # Calculates the n-step transition probablity matrix 
    # and gets the entry corresponding to the wanted transition
    #
    def transition_prob(self, start: int, end: int, steps: int):
        return self.n_step_matrix(steps)[start-1][end-1]
    

    # Given an initial state vector with the displacement of probability in each state
    # it returns an array with the probability of the chain being in each state 
    # after n transitions from the initial state
    #
    # Result vector is obtained by multiplying the n-step transition probability matrix 
    # with the initial state vector
    #
    def state_after_n_steps(self, initial: int, steps: int):
        check_initial_vector(initial)

        prob_vector = []
        for i in range(self.num_states): prob_vector += [0]

        n_step_mtrx = self.n_step_matrix(steps)
        for row in range(self.num_states):
            for col in range(self.num_states):
                prob_vector[row] += n_step_mtrx[row][col]*initial[col]

        return prob_vector
    

    # Given an array containing a certain state trajectory with shape
    #   [t0, t1, t2, ...]
    # where tn is the state of the chain when time is equal to n (t = n)
    # (consecutive elements are allways one transition appart)
    # it returns the probability of the chain following that trajectory.
    #
    # The result is the product of the probability of the first state of the trajectory in the initial state, 
    # with the probabilities of each transition of the trajectory, found in the transition matrix
    #
    def trajectory(self, initial: int, path: int, n: int):
        check_initial_vector(initial)

        p0 = initial[path[0]-1]
        for i in range(1, n):
            p0 *= self.matrix[path[i-1]-1][path[i]-1]

        return p0


# Error verification functions

# check if matrix is stochastic
def stochastic_check(matrix: int):

    for row in matrix:
        row_sum = 0
        for elem in row:
            row_sum += elem
        if round(row_sum) != 1:
            raise ValueError('invalid value: Matrix is not stochastic')

# check if vector's entries add up to 1
def check_initial_vector(vec: int):
    sum = 0
    for elem in vec:
        sum += elem
    if round(sum) != 1:
        raise ValueError('invalid value: initial vector\'s probabilities do not add up to 1')
    
# running example
if __name__ == "__main__":

    matrix = [[0.5, 0.5, 0.0], 
              [0.0, 0.5, 0.5],
              [0.5, 0.0, 0.5]]
    
    initial = [0.7, 0.2, 0.1]

    path = [1, 3, 3, 2]

    markov_chain = Markov_chain(matrix)
    
    ex_1 = markov_chain.transition_prob(1, 3, 2)
    ex_2 = markov_chain.transition_prob(2, 3, 3)

    ex_3 = markov_chain.state_after_n_steps(initial, 2)
    ex_4 = markov_chain.trajectory(initial, path, 4)