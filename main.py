from flask import Flask, send_from_directory, request, render_template
from api import Data

app = Flask(__name__)

data = Data()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    res = data.search(keyword, 'title')
    return ''.join([str(r) for r in res])



if __name__ == '__main__':
    app.run()
