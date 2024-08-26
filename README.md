# markov_chains
Python class with utility functions for solving basic problems with discrete-time Markov Chains (DTMC).

The constructor receives a stochastic matrix that respresents the chain's transition model.

From there we can calculate:
- the probability of ocurring a transition with n steps between two states
- the probability of the chain being in each state after n transitions given an initial probability displacement
- the probability of the chain following a certain trajectory between states

In most cases the calculations involve computing the n-step transition probability matrix.
This result can be obtained by elevating the Markov Chain's transition matrix to the power of n, as it's deduced from the Kolmogorov-Chapman's equation.
