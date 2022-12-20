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
    info_list = data.search(keyword, 'title')
    return render_template('result.html', info_list=info_list)

@app.route('/download/<id>')
def download(id):
    info = data.get(id)
    if info is None:
        return 'Not Found'
    title = info['title']
    extension = info['extension']
    base_dir = '/Volumes/Data-Resource/R-Book-ZLibrary'
    response = send_from_directory(base_dir, id, as_attachment=True, attachment_filename=title + '.' + extension)
    return response

if __name__ == '__main__':
    app.run()
