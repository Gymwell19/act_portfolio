from flask import Flask, render_template, request, abort, jsonify
import math
from .linked_list import LinkedList
from .infix_postfix import infix_to_postfix

app = Flask(__name__)

# Global store for the linked list demo
linked_list_store = LinkedList()


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


@app.route('/programming/circle')
def programming_circle():
    # Render a dedicated page for the circle area exercise
    return render_template('programming_circle.html')


@app.route('/programming/triangle')
def programming_triangle():
    # Render a dedicated page for the triangle area exercise
    return render_template('programming_triangle.html')


@app.route('/programming/linkedlist')
def programming_linkedlist():
    return render_template('programming_linkedlist.html')


@app.route('/api/linkedlist', methods=['GET'])
def get_linked_list():
    return jsonify(linked_list_store.to_list())


@app.route('/api/linkedlist/add', methods=['POST'])
def add_linked_list():
    data = request.json.get('data')
    if data:
        linked_list_store.append(data)
    return jsonify(linked_list_store.to_list())


@app.route('/api/linkedlist/remove-beginning', methods=['POST'])
def remove_beginning():
    removed = linked_list_store.remove_beginning()
    return jsonify({'removed': removed, 'list': linked_list_store.to_list()})


@app.route('/api/linkedlist/remove-end', methods=['POST'])
def remove_end():
    removed = linked_list_store.remove_at_end()
    return jsonify({'removed': removed, 'list': linked_list_store.to_list()})


@app.route('/api/linkedlist/remove-at', methods=['POST'])
def remove_at():
    data = request.json.get('data')
    removed = linked_list_store.remove_at(data)
    return jsonify({'removed': removed, 'list': linked_list_store.to_list()})


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


@app.route('/programming/infix')
def programming_infix():
    return render_template('programming_infix.html')


@app.route('/api/infix-to-postfix', methods=['POST'])
def api_infix_to_postfix():
    data = request.json.get('expression')
    if not data:
        return jsonify({'postfix': ''})
    try:
        postfix = infix_to_postfix(data)
        return jsonify({'postfix': postfix})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
