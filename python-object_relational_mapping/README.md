# Python - Object Relational Mapping

## My Local Setup Notes

Quick reference for running this project locally using Docker, MySQL, and Python.

---

## 1. Open the Docker Environment

Check available containers:

```bash
docker ps -a
```

Start the Ubuntu container:

```bash
docker start -ai <container_name>
```

If the container is already running:

```bash
docker exec -it <container_name> bash
```

The project files should be available inside:

```text
/workspace
```

---

## 2. Go to the Project

Inside Docker:

```bash
cd /workspace
```

Then enter the project directory if needed:

```bash
cd python-object_relational_mapping
```

---

## 3. Start MySQL

Every time the Docker container is restarted, MySQL may need to be started again:

```bash
service mysql start
```

Check its status:

```bash
service mysql status
```

If the output shows a MySQL server version and uptime, the server is running.

---

## 4. Connect to MySQL

```bash
mysql -uroot -p
```

Enter the root password when prompted.

Useful MySQL commands:

```sql
SHOW DATABASES;
```

Select a database:

```sql
USE hbtn_0e_0_usa;
```

Show its tables:

```sql
SHOW TABLES;
```

Display the states:

```sql
SELECT * FROM states;
```

Exit MySQL:

```sql
exit;
```

---

## 5. Create the Exercise Database Locally

The Holberton checker prepares its own database.

For local testing, I need to create the database myself using the SQL file supplied in the task.

From the Linux terminal, not from inside `mysql>`:

```bash
mysql -uroot -p < 0-select_states.sql
```

Another equivalent command:

```bash
cat 0-select_states.sql | mysql -uroot -p
```

Then verify:

```bash
mysql -uroot -p
```

Inside MySQL:

```sql
SHOW DATABASES;
USE hbtn_0e_0_usa;
SHOW TABLES;
SELECT * FROM states;
```

---

## 6. Required Python Packages

If `pip3` is missing:

```bash
apt-get update
apt-get install -y python3-pip
```

Required MySQL development packages:

```bash
apt-get install -y python3-dev
apt-get install -y libmysqlclient-dev
apt-get install -y zlib1g-dev
```

Install MySQLdb through `mysqlclient`:

```bash
pip3 install mysqlclient==2.0.3
```

Verify:

```bash
python3 -c "import MySQLdb; print('MySQLdb OK')"
```

For later ORM tasks:

```bash
pip3 install SQLAlchemy==1.4.22
```

---

## 7. Run the Python Tasks

General format:

```bash
python3 <script.py> <mysql_username> <mysql_password> <database_name>
```

Example:

```bash
python3 0-select_states.py root root hbtn_0e_0_usa
```

Task 1:

```bash
python3 1-filter_states.py root root hbtn_0e_0_usa
```

Expected format:

```text
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
```

---

## 8. How Python Connects to MySQL

Basic connection:

```python
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=username,
    passwd=password,
    db=database
)
```

Create a cursor:

```python
cursor = db.cursor()
```

Run SQL:

```python
cursor.execute(
    "SELECT * FROM states ORDER BY states.id ASC"
)
```

Get all results:

```python
rows = cursor.fetchall()
```

Print them:

```python
for row in rows:
    print(row)
```

Close the connection:

```python
cursor.close()
db.close()
```

---

## 9. Command-Line Arguments

For:

```bash
python3 0-select_states.py root root hbtn_0e_0_usa
```

Python receives:

```text
sys.argv[0] = 0-select_states.py
sys.argv[1] = root
sys.argv[2] = root
sys.argv[3] = hbtn_0e_0_usa
```

So:

```python
user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
```

---

## 10. Important: Terminal vs MySQL

Linux commands are written here:

```text
root@container:/workspace#
```

Examples:

```bash
python3 0-select_states.py root root hbtn_0e_0_usa
service mysql start
mysql -uroot -p
```

SQL commands are written only when the prompt is:

```text
mysql>
```

Examples:

```sql
SHOW DATABASES;
USE hbtn_0e_0_usa;
SELECT * FROM states;
exit;
```

Do **not** run this inside `mysql>`:

```bash
python3 0-select_states.py ...
```

Exit MySQL first.

---

## 11. Common Errors

### Can't connect to local MySQL server

Example:

```text
Can't connect to local MySQL server through socket
```

Fix:

```bash
service mysql start
```

---

### Unknown database

Example:

```text
Unknown database 'hbtn_0e_0_usa'
```

For local testing, create it:

```bash
mysql -uroot -p < 0-select_states.sql
```

The Holberton checker normally prepares its own test database.

---

### pip3: command not found

Fix:

```bash
apt-get update
apt-get install -y python3-pip
```

---

### MySQLdb not found

Fix:

```bash
pip3 install mysqlclient==2.0.3
```

Check:

```bash
python3 -c "import MySQLdb"
```

---

## 12. Before Running the Checker

Make files executable:

```bash
chmod +x 0-select_states.py
chmod +x 1-filter_states.py
```

Check style:

```bash
pycodestyle 0-select_states.py
pycodestyle 1-filter_states.py
```

Make sure the README is not empty.

Check Git:

```bash
git status
```

Then:

```bash
git add .
git commit -m "Object relational mapping tasks"
git push
```

---

## Quick Restart Checklist

When coming back to the project later:

```text
1. Open Docker
2. cd /workspace/python-object_relational_mapping
3. service mysql start
4. Verify MySQLdb is installed
5. Create the local test database if needed
6. Run the Python script with username/password/database arguments
```

Quick commands:

```bash
service mysql start

python3 -c "import MySQLdb; print('MySQLdb OK')"

mysql -uroot -p < 0-select_states.sql

python3 0-select_states.py root root hbtn_0e_0_usa
``` 