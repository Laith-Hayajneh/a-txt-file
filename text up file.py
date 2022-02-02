from flask import Flask, render_template, request
from split import a
import time
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def cal():
    start_time = time.time()
    r = []
    similar = None
    difference = None
    path_file1 =None
    path_file2 =None
    if request.method == 'POST':
        if not request.form['file1'] and not request.form['file2'] \
                and not request.form['split_at']:
            r = 'please fil the form'
        else:
            try:
                path_file1 = request.form['file1']
                path_file2 = request.form['file2']
                split_at = request.form['split_at']
                result1 = a.similar(path_file1, path_file2, split_at)
                r = result1
                similar = (r[0] / r[1]) * 100
                len_difference = r[1] - r[0]
                difference = (len_difference / r[1]) * 100

            except BaseException as error:
                r = 'error : {}'.format(error)
    end_time = time.time()
    time_run = end_time - start_time
    return render_template('up file.html', result=r, similar=similar, difference=difference, time_run=time_run, path_file1=path_file1, path_file2=path_file2)
@app.route('/flowchart')
def flowchart():
    return render_template('flowchart.html')
if __name__ == "__main__":
    app.run(debug=True)