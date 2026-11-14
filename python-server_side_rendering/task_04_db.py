#!/usr/bin/python3
"""Flask app displaying products from JSON, CSV or a SQLite database."""
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(path='products.json'):
    """Return the list of products stored in a JSON file."""
    with open(path, 'r') as f:
        return json.load(f)


def read_csv(path='products.csv'):
    """Return the list of products stored in a CSV file."""
    products = []
    with open(path, 'r', newline='') as f:
        for row in csv.DictReader(f):
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql(path='products.db'):
    """Return the list of products stored in the SQLite Products table."""
    conn = sqlite3.connect(path)
    try:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


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
            item_list = json.load(f).get('items', [])
    except (OSError, ValueError):
        item_list = []
    return render_template('items.html', items=item_list)


@app.route('/products')
def products():
    """Show products from ?source=json|csv|sql, optionally filtered by ?id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json()
        elif source == 'csv':
            data = read_csv()
        elif source == 'sql':
            data = read_sql()
        else:
            return render_template('product_display.html',
                                   error="Wrong source")
    except sqlite3.Error as e:
        return render_template('product_display.html',
                               error="Database error: {}".format(e))
    except (OSError, ValueError, KeyError):
        return render_template('product_display.html',
                               error="Could not read the data file")

    if product_id is not None:
        try:
            wanted = int(product_id)
        except ValueError:
            wanted = None
        data = [p for p in data if int(p.get('id', -1)) == wanted]
        if not data:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
