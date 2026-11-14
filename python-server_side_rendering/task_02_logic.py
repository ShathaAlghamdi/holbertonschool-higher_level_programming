#!/usr/bin/python3
"""Flask app that renders a list of items read from a JSON file."""
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Read items.json and pass the list to the template."""
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
        item_list = data.get('items', [])
    except (OSError, ValueError):
        item_list = []
    return render_template('items.html', items=item_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
