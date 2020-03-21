from flask import *
import pandas as pd
from flaskr import utilities

app = Flask(__name__)

@app.route("/tables")
def show_tables():
    data = utilities.getNewsKeyword('Trump')
    return render_template('view.html',tables=[data.to_html(classes='female')],
    titles = ['na', 'Female surfers', 'Male surfers'])

if __name__ == "__main__":
    app.run(debug=True)