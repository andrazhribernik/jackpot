from api import JackpotApi
import analyzer
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Wrong arguments"
        exit()

    api = JackpotApi(sys.argv[1])
    #analyzer.analyse_constant(api)
    analyzer.analyse(api)