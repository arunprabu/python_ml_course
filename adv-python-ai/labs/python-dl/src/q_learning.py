"""Q-Learning on the OpenAI Gym "Taxi" environment (reinforcement learning).

This program mirrors the ``Q-Learning.ipynb`` notebook. It builds a
self-driving taxi that picks up passengers at one of a set of fixed
locations, drops them off at another location, and gets there in the
quickest amount of time while avoiding obstacles.

The world is a 5x5 grid with 4 pickup/dropoff locations (R, G, B, Y).
The state of the world is fully described by:

- Where the taxi is (5x5 = 25 locations),
- What the current destination is (4 possibilities),
- Where the passenger is (5 possibilities: at one of the destinations,
  or inside the taxi),

giving 25 x 4 x 5 = 500 possible states. For each state there are six
possible actions: move South, East, North, or West, pickup, or dropoff.

Rewards/penalties per step:
- Successful dropoff:           +20
- Time step while driving:       -1
- Illegal pickup/dropoff:       -10
- Moving across a wall:          not allowed

Flow
----
1. Create the ``Taxi-v3`` environment and render the initial grid.
2. Define an initial state (taxi at (2, 3), passenger at pickup 2,
   destination 0) and inspect its reward table.
3. Train a Q-table over 10,000 simulated taxi runs using epsilon-greedy
   exploration and the standard Q-learning update rule.
4. Inspect the learned Q-values for the initial state.
5. Play 10 trips with the trained policy, rendering each step.

Run it with::

    python src/q_learning.py

Requires ``gym`` and ``numpy`` (``pip install gym numpy``).
"""

import random
from time import sleep

import gym
import numpy as np

# Hyper-parameters for Q-learning
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.6
EXPLORATION = 0.1      # probability of taking a random action while training
EPOCHS = 10000         # number of simulated taxi runs during training


def create_environment():
    """Create the Taxi environment and seed the RNG for reproducibility."""
    random.seed(1234)

    # New gym versions keep getting released; if -v3 doesn't work,
    # try -v2 or -v4.
    streets = gym.make("Taxi-v3").env
    streets.render()
    return streets


def show_initial_state(streets):
    """Encode a known initial state and render the grid for inspection.

    Initial state: taxi at location (2, 3), passenger waiting at pickup
    location 2, and the destination is location 0.
    """
    initial_state = streets.encode(2, 3, 2, 0)
    streets.s = initial_state
    streets.render()
    return initial_state


def train_q_table(streets):
    """Train a Q-table over ``EPOCHS`` simulated taxi runs.

    At each time step we take a random, exploratory action with probability
    ``EXPLORATION``; otherwise we pick the action with the highest Q-value.
    The Q-value is then updated with the classic update rule::

        new_q = (1 - alpha) * old_q
                + alpha * (reward + gamma * max(q(next_state)))

    Returns
    -------
    numpy.ndarray
        The learned Q-table of shape [num_states, num_actions].
    """
    q_table = np.zeros([streets.observation_space.n, streets.action_space.n])

    for taxi_run in range(EPOCHS):
        state = streets.reset()
        done = False

        while not done:
            random_value = random.uniform(0, 1)
            if random_value < EXPLORATION:
                action = streets.action_space.sample()  # explore a random action
            else:
                action = np.argmax(q_table[state])     # exploit best Q-value

            next_state, reward, done, info = streets.step(action)

            prev_q = q_table[state, action]
            next_max_q = np.max(q_table[next_state])
            new_q = ((1 - LEARNING_RATE) * prev_q
                     + LEARNING_RATE * (reward + DISCOUNT_FACTOR * next_max_q))
            q_table[state, action] = new_q

            state = next_state

    return q_table


def play_trips(streets, q_table, num_trips=10, animate=False):
    """Run ``num_trips`` trips using the greedy policy from the Q-table.

    Parameters
    ----------
    streets : gym.Env
        The Taxi environment.
    q_table : numpy.ndarray
        The trained Q-table.
    num_trips : int
        How many trips to simulate.
    animate : bool
        If True, render each step with a small delay (useful for demos,
        slows things down considerably).
    """
    total_steps = 0

    for tripnum in range(1, num_trips + 1):
        state = streets.reset()
        done = False
        trip_length = 0

        while not done and trip_length < 25:
            action = np.argmax(q_table[state])
            next_state, reward, done, info = streets.step(action)

            if animate:
                print("Trip number %d Step %d" % (tripnum, trip_length))
                print(streets.render(mode='ansi'))
                sleep(0.5)

            state = next_state
            trip_length += 1

        if animate:
            sleep(2)

        total_steps += trip_length

    print("Total time steps across %d trips: %d" % (num_trips, total_steps))
    print("Average time steps per trip: %.2f" % (total_steps / num_trips))


def main():
    """Run the full Q-learning pipeline: train, inspect, and play."""
    streets = create_environment()

    # Inspect the reward table for a known initial state. Each row is
    # (probability, next_state, reward, done) for one of the six actions.
    initial_state = show_initial_state(streets)
    print("Reward table for the initial state:")
    print(streets.P[initial_state])

    q_table = train_q_table(streets)

    # Sanity check: for our initial state the lowest Q-value should be the
    # action "go West", the most direct route toward the destination.
    print("Learned Q-values for the initial state:")
    print(q_table[initial_state])

    # Play some trips. Set animate=True to watch the taxi live.
    play_trips(streets, q_table, num_trips=10, animate=False)


if __name__ == '__main__':
    main()