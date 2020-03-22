from flask import *
import pandas as pd
from flaskr import utilities

app = Flask(__name__)

@app.route("/")
def show_tables():
    df_news= utilities.getNewsKeyword('Trump')
    df_treands = utilities.getGoogleTrends('Trump')

    return render_template('view.html',tables=[df_news.to_html(classes='news'), df_treands.to_html(classes='trends')],
    titles = ['na', 'Top News', 'Google Trends'])

if __name__ == "__main__":
    app.run(debug=True)