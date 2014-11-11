from urllib2 import Request, urlopen, URLError

MACHINES = "machines"
PULLS = "pulls"


class JackpotApi:
    def __init__(self, url):
        self.url = url
        self.machines = self.call(MACHINES)
        self.pulls = self.call(PULLS)

    def call(self, param):
        url = "{}/{}".format(self.url, param)
        consecutive_err = 0
        while True:
            try:
                response = urlopen(url)
                return int(response.read())
            except URLError as e:
                if hasattr(e, 'reason'):
                    print 'We failed to reach a server.'
                    print 'Reason: ', e.reason
                    print url
                elif hasattr(e, 'code'):
                    print 'The server couldn\'t fulfill the request.'
                    print 'Error code: ', e.code
                consecutive_err += 1
            except:
                consecutive_err += 1
            if consecutive_err > 5:
                print "Program has been stopped due to max. number of consecutive errors was reached."
                exit()

    def pull(self, bandit, sequence_n):
        return self.call("{}/{}".format(bandit, sequence_n))
