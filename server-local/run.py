from flask import Flask
import random
app = Flask(__name__)

@app.route('/<example>/machines')
def machines(example):
    print example
    try:
        return {
            '1': '2',
            '2': '2',
            '3': '3'
            }[example]
    except:
        return "ERR"

@app.route('/<example>/pulls')
def pulls(example):
    print example
    try:
        return {
            '1': '500',
            '2': '10000',
            '3': '1000'
        }[example]
    except:
        return "ERR"

@app.route('/<example>/<bandit>/<sequence>')
def pull(example, bandit, sequence):
    try:
        return {
            '1': {
                    '1': "1" if random.random() < 0.4 else "0",
                    '2': "1" if random.random() < 0.6 else "0"
                  }

        }[example][bandit]
    except:
        return "ERR"

if __name__ == '__main__':
    app.run(debug=False)