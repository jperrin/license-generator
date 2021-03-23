from flask import Flask
from flask import render_template

generator = Flask(__name__)
@generator.route('/')
def home():
    return render_template('index.html')

@generator.route('/build')
def test():
    return render_template('index.html')


if __name__ == '__main__':
 generator.run()
