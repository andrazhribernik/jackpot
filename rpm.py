import random
from collections import deque


def ind_max(x):
    m = max(x)
    return x.index(m)


class RPM():
    def __init__(self, counts, values):
        self.counts = counts
        self.values = values
        return

    def initialize(self, n_arms):
        self.counts = [0 for col in range(n_arms)]
        self.values = [0 for col in range(n_arms)]
        return

    def select_arm(self):
        n_arms = len(self.counts)
        rpm_values = [0.0 for arm in range(n_arms)]
        for arm in range(n_arms):
            rpm_values[arm] = random.betavariate(self.values[arm] + 1, self.counts[arm] - self.values[arm] + 1)
        return ind_max(rpm_values)

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        self.values[chosen_arm] += reward
        return


class RPMTime():
    def __init__(self, history):
        self.history = history
        self.counts = []
        self.values = []
        return

    def initialize(self, n_arms):
        self.counts = [deque([]) for col in range(n_arms)]
        self.values = [deque([]) for col in range(n_arms)]
        return

    def select_arm(self):
        n_arms = len(self.counts)
        rpm_values = [0.0 for arm in range(n_arms)]
        for arm in range(n_arms):
            rpm_values[arm] = random.betavariate(sum(self.values[arm]) + 1, sum(self.counts[arm]) - sum(self.values[arm]) + 1)
        return ind_max(rpm_values)

    def update(self, chosen_arm, reward):
        for arm in range(len(self.counts)):
            if arm == chosen_arm:
                self.counts[arm].append(1)
                self.values[arm].append(reward)
            else:
                self.counts[arm].append(0)
                self.values[arm].append(0)
            if len(self.values[arm]) > self.history:
                self.counts[arm].popleft()
                self.values[arm].popleft()
        return