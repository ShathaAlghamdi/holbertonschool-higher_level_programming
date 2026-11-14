# Python - Server-Side Rendering

Generating HTML on the server with Python: string templating, Flask,
Jinja templates (include, loops, conditions) and data from JSON, CSV and SQLite.

| File | Description |
| ---- | ----------- |
| task_00_intro.py | `generate_invitations(template, attendees)` writes `output_X.txt` files |
| task_01_jinja.py | Flask app with `/`, `/about`, `/contact` and shared header/footer |
| task_02_logic.py | Adds `/items`, rendering `items.json` with Jinja loops and conditions |
| task_03_files.py | `/products?source=json\|csv&id=N` rendered in a table |
| task_04_db.py | Adds `source=sql` reading from `products.db` |
| create_database.py | Creates and fills `products.db` |
| templates/ | Jinja templates |

Run any app with `python3 task_0X_*.py` and open http://localhost:5000
