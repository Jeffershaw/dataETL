from flask import *
import pandas as pd
from flaskr import utilities
import numpy as np
import json
import schedule

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def show_tables():
    search_keywords = request.form.get('keywords','Trump')
    data_news= utilities.getNewsKeyword(search_keywords)
    df_news = utilities.getSnapshot(data_news)
    df_treands = utilities.getGoogleTrends(search_keywords)
    trendsData = np.squeeze(df_treands.values[1:])
    trendsTime = df_treands.index[1:]

    return render_template('view.html',tables=[df_news.to_html(classes='news'), df_treands.to_html(classes='trends')],
    trendsData =json.dumps(trendsData.tolist()),
    trendsTime = json.dumps(trendsTime.tolist()),
    titles = ['na', 'Top News', 'Google Trends'])

if __name__ == "__main__":
    app.run(debug=True)