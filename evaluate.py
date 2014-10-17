from api import JackpotApi
from python.algorithms.epsilon_greedy.standard import EpsilonGreedy
from python.algorithms.ucb.ucb1 import UCB1
from python.algorithms.ucb.ucb2 import UCB2
from python.algorithms.exp3.exp3 import Exp3
from rpm import RPM
from rpm import RPMTime
import sys


def evaluate(api, repeat=20):
    #algo = EpsilonGreedy(0.2, [], [])
    #algo = UCB1([], [])
    #algo = UCB2(0.1, [], [])
    #algo = RPM([], [])
    print "repeat: "+str(repeat)
    algos = [
        ('usb1', UCB1([], [])),
        ('ucb2 a=0.05', UCB2(0.05, [], [])),
        ('ucb2 a=0.1', UCB2(0.1, [], [])),
        ('ucb2 a=0.3', UCB2(0.3, [], [])),
        ('ucb2 a=0.5', UCB2(0.5, [], [])),
        ('ucb2 a=0.7', UCB2(0.7, [], [])),
        ('exp3 a=0.1', Exp3(0.1, [])),
        ('exp3 a=0.3', Exp3(0.3, [])),
        ('rpm', RPM([], [])),
        ('rpmTime: 0.1', RPMTime(int(api.pulls * 0.1))),
        ('rpmTime: 0.2', RPMTime(int(api.pulls * 0.2))),
        ('rpmTime: 0.3', RPMTime(int(api.pulls * 0.3)))
    ]

    """
    algos = [
        ('rpm', RPM([], [])),
        ('rpmTime: 0.1', RPMTime(int(api.pulls * 0.1))),
        ('rpmTime: 0.15', RPMTime(int(api.pulls * 0.15))),
        ('rpmTime: 0.2', RPMTime(int(api.pulls * 0.2))),
        ('rpmTime: 0.3', RPMTime(int(api.pulls * 0.3)))
    ]
    """
    for name, algo in algos:
        reward_sum = 0
        for r in range(repeat):
            algo.initialize(api.machines)
            arm_pulls = [0 for i in range(api.machines)]

            for pull in range(api.pulls):
                pull += 1

                chosen_arm = algo.select_arm()
                reward = api.pull(chosen_arm + 1, pull)
                algo.update(chosen_arm, reward)

                reward_sum += reward
                arm_pulls[chosen_arm] += 1
        print name + ": " + str(reward_sum / float(repeat))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Wrong arguments"
        exit()

    api = JackpotApi(sys.argv[1])
    evaluate(api)
