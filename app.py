from flask import Flask, render_template, request, abort
import math

app = Flask(__name__)


@app.context_processor
def inject_year():
    from datetime import datetime
    return {'year': datetime.utcnow().year}


@app.route('/')
def index():
    return render_template('index.html', message='Hello from Flask + Jinja2!')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/programming')
def programming():
    return render_template('programming.html')


def _parse_positive_float(value):
    try:
        v = float(value)
        if v <= 0:
            raise ValueError()
        return v
    except Exception:
        raise ValueError('Value must be a positive number')


@app.route('/area/circle', methods=['POST'])
def area_circle():
    radius = request.form.get('radius')
    try:
        r = _parse_positive_float(radius)
    except ValueError:
        abort(400, 'radius must be a positive number')
    area = math.pi * r * r
    return f'Area of circle with radius {r:g} is {area:.4f}'


@app.route('/area/triangle', methods=['POST'])
def area_triangle():
    base = request.form.get('base')
    height = request.form.get('height')
    try:
        b = _parse_positive_float(base)
        h = _parse_positive_float(height)
    except ValueError:
        abort(400, 'base and height must be positive numbers')
    area = 0.5 * b * h
    return f'Area of triangle with base {b:g} and height {h:g} is {area:.4f}'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
