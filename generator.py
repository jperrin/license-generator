import os
import json
import glob
from flask import Flask
from flask import render_template
import markovify

generator = Flask(__name__)
@generator.route('/')
def home():
    return render_template('index.html')

@generator.route('/build')
def build():
#    return render_template('index.html')
    titles = []
    licensepath = "spdx-license-data/json/details"
    licensefiles = glob.glob(licensepath + '/*.json')

    for licensefile in licensefiles:
        with open(licensefile, 'r') as f:
            json_file = json.load(f)
            titles.append(json_file['name'])

    modelname = markovify.NewlineText(titles)
    return modelname.make_sentence()




if __name__ == '__main__':
    generator.run()
