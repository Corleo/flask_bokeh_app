from flask import Flask, render_template
from bokeh.embed import autoload_server

app = Flask(__name__)


@app.route('/home')
@app.route('/index', alias=True)
@app.route('/', alias=True)
def index():
    return render_template('index.html')


@app.route('/slider')
def slider():
    script = autoload_server(model=None, app_path="/_sliders")
    return render_template('bokeh.html', bokeh_script=script)


@app.route('/fourier')
def fourier():
    script = autoload_server(model=None, app_path="/_fourier")
    return render_template('bokeh.html', bokeh_script=script)


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
