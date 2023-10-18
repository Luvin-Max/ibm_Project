from flask import *
import sqlite3

conn = sqlite3.connect('database.dp')
print("connection will be connected")

app = Flask(__name__)

#first route
@app.route("/")
@app.route("/TamilLoft")
def index():
    return render_template('index.html')

#second route
@app.route("/project_orders", methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        n = request.form.get('name')
        e = request.form.get('email')
        c = request.form.get('command')
        f = request.form.get('file')
        return render_template('project_orders.html', name=n, email=e, command=c, file=f)

#conn.execute("database commends")
print("table is created")
conn.close()

#condision Execution part
if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
