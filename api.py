from urllib2 import Request, urlopen, URLError

MACHINES = "machines"
PULLS = "pulls"


class JackpotApi:
    def __init__(self, url):
        self.url = url
        self.machines = self.call(MACHINES)
        self.pulls = self.call(PULLS)

    def call(self, param, pull=False):
        url = "{}/{}".format(self.url, param)
        req = Request(url)
        """
        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
            if pull: return 0
            else: exit()
        else:
            return int(response.read())
        """
        response = urlopen(req)
        return int(response.read())

    def pull(self, bandit, sequence_n):
        return self.call("{}/{}".format(bandit, sequence_n), pull=True)
