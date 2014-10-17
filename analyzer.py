from api import JackpotApi
import matplotlib.pyplot as plt
import sys

REPEAT = 3000
REPEAT_CONSTANT = 50000


def analyse(api, interval=1000, repeat=1000):
    machines = []
    for machine in range(api.machines):
        results = []
        for pull in range(0, api.pulls, interval):
            success = 0
            for i in range(repeat):
                if api.pull(machine + 1, pull + 1):
                    success += 1
            print "%d: %f"% (pull, success / float(REPEAT))
            results.append(success / float(REPEAT))
        machines.append(results)

    results = "%s / %d / %d \n" % (api.url, interval, repeat)
    for i, m in enumerate(machines):
        #plt.plot(range(0, api.pulls, interval), m, label="machine %d" % (i + 1))
        results += str(m) + "\n"
    #plt.legend(loc=2)
    #plt.show()
    f = open(api.url.replace('http://', '').replace('/','-'), "w")
    f.write(results)
    f.close()



def analyse_constant(api):
    for machine in range(api.machines):
        success = 0
        for i in range(REPEAT_CONSTANT):
            if api.pull(machine + 1, 1):
                success += 1
        print "machine %d: %f" % (machine + 1, success / float(REPEAT_CONSTANT))



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Wrong arguments"
        exit()
    api = JackpotApi(sys.argv[1])
    analyse(api, interval=int(sys.argv[2]), repeat=int(sys.argv[3]))