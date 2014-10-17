from api import JackpotApi
from python.algorithms.epsilon_greedy.standard import EpsilonGreedy
from python.algorithms.ucb.ucb1 import UCB1
from python.algorithms.ucb.ucb2 import UCB2
from rpm import RPM
import analyzer
import sys


def simulate(api):
    #algo = EpsilonGreedy(0.2, [], [])
    #algo = UCB1([], [])
    #algo = UCB2(0.1, [], [])
    algo = RPM([], [])
    algo.initialize(api.machines)
    arm_pulls = [0 for i in range(api.machines)]
    reward_sum = 0
    for pull in range(api.pulls):
        pull += 1

        chosen_arm = algo.select_arm()
        reward = api.pull(chosen_arm + 1, pull)
        algo.update(chosen_arm, reward)

        reward_sum += reward
        arm_pulls[chosen_arm] += 1
    print arm_pulls
    return reward_sum

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Wrong arguments"
        exit()

    api = JackpotApi(sys.argv[1])
    print simulate(api)
    #analyzer.analyse_constant(api)
    #analyzer.analyse(api)