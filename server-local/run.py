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
            '3': '3',
            '4': '4',
            '5': '10',
            '6': '2'
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
            '3': '1000',
            '4': '10000',
            '5': '10000',
            '6': '1000'
        }[example]
    except:
        return "ERR"

@app.route('/<example>/<bandit>/<sequence>')
def pull(example, bandit, sequence):
    try:
        return {
            '1': {
                '1': ("1" if random.random() < 0.4 else "0") if 1 <= int(sequence) <= 500 else "ERR",
                '2': ("1" if random.random() < 0.6 else "0") if 1 <= int(sequence) <= 500 else "ERR"
            },
            '2': {
                '1': ("1" if random.random() < 0.03 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '2': ("1" if random.random() < 0.015 else "0") if 1 <= int(sequence) <= 10000 else "ERR"
            },
            '3': {
                '1': ("1" if random.random() < 0.2 else "0") if 1 <= int(sequence) <= 1000 else "ERR",
                '2': ("1" if random.random() < 0.15 else "0") if 1 <= int(sequence) <= 1000 else "ERR",
                '3': ("1" if random.random() < 0.1 else "0") if 1 <= int(sequence) <= 1000 else "ERR"
            },
            '4': {
                '1': ("1" if random.random() < 0.02 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '2': ("1" if random.random() < 0.0175 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '3': ("1" if random.random() < 0.02375 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '4': ("1" if random.random() < 0.0228 else "0") if 1 <= int(sequence) <= 10000 else "ERR"
            },
            '5': {
                '1': ("1" if random.random() < 0.010420 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '2': ("1" if random.random() < 0.010300 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '3': ("1" if random.random() < 0.010020 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '4': ("1" if random.random() < 0.010260 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '5': ("1" if random.random() < 0.010540 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '6': ("1" if random.random() < 0.009480 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '7': ("1" if random.random() < 0.009360 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '8': ("1" if random.random() < 0.010180 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '9': ("1" if random.random() < 0.009520 else "0") if 1 <= int(sequence) <= 10000 else "ERR",
                '10': ("1" if random.random() < 0.012880 else "0") if 1 <= int(sequence) <= 10000 else "ERR"
            },
            '6': {
                '1': ("1" if random.random() < 0.6 else "0") if 1 <= int(sequence) < 500
                else ("1" if random.random() < 0.4 else "0") if 500 <= int(sequence) <= 1000
                else "ERR",
                '2': ("1" if random.random() < 0.4 else "0") if 1 <= int(sequence) < 500
                else ("1" if random.random() < 0.6 else "0") if 500 <= int(sequence) <= 1000
                else "ERR",
            },

        }[example][bandit]
    except:
        return "ERR"

if __name__ == '__main__':
    app.run(debug=True)