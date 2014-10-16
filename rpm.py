import random


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
