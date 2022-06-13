from flask import Flask, request
from flask import render_template

from analysis import analysis
from ssvep import ssvep

app = Flask(__name__)


@app.route('/')
def tv():
    return render_template('tv.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/tvcontrol')
def tvcontrol():
    return render_template('tvcontrol.html')


@app.route('/call')
def call():
    return render_template('call.html')


@app.route('/ssvep')
def ssvep_analysis():
    idx = request.args.get('idx')
    date = request.args.get('date')
    result = ssvep(idx, date)
    # result = [1, '2022-06-10_오후 8_55']
    print('ssvep 결과')
    print(result)
    return {"result": {
        'idx': result[1],
        'date': date,
        'hz': result[0]
    }}


@app.route('/analysis')
def blink_analysis():
    print('데이터 분석!')
    result = analysis()
    # result = [1, '2022-06-10_오후 8_55']
    print(result)
    return {"result": {
        'idx': int(result[0]),
        'date': result[1]
    }}


@app.route('/rest')
def rest():
    idx = request.args.get('idx')
    date = request.args.get('date')

    return render_template('rest.html')


@app.route('/tvon')
def tv_on():
    return render_template('tvon.html')


@app.route('/tvoff')
def tv_off():
    return render_template('tvoff.html')


@app.route('/helper')
def helper():
    return render_template('helper.html')


@app.route('/doctor')
def doctor():
    return render_template('doctor.html')


@app.route('/first')
def first():
    return render_template('test/first.html')


@app.route('/test')
def test():
    return render_template('test/test.html')


@app.route('/test2')
def test2():
    return render_template('test/test2.html')


@app.route('/test3')
def test3():
    return render_template('test/test3.html')


if __name__ == '__main__':
    app.run()
