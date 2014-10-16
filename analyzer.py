import matplotlib.pyplot as plt

REPEAT = 3000
REPEAT_CONSTANT = 50000


def analyse(api):
    machines = []
    for machine in range(api.machines):
        results = []
        for pull in range(0, api.pulls, 100):
            success = 0
            for i in range(REPEAT):
                if api.pull(machine + 1, pull + 1):
                    success += 1
            print "%d: %f"% (pull, success / float(REPEAT))
            results.append(success / float(REPEAT))
        machines.append(results)

    for i, m in enumerate(machines):
        plt.plot(range(0, api.pulls, 100), m, label="machine %d" % (i + 1))
    plt.legend(loc=2)
    plt.show()

def analyse_constant(api):
    for machine in range(api.machines):
        success = 0
        for i in range(REPEAT_CONSTANT):
            if api.pull(machine + 1, 1):
                success += 1
        print "machine %d: %f" % (machine + 1, success / float(REPEAT_CONSTANT))
