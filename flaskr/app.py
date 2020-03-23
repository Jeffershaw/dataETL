import pandas as pd
from flaskr import utilities
import numpy as np
import json
from flask_bootstrap import Bootstrap
import schedule
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

app = Flask(__name__)
Bootstrap(app)

@app.route("/",methods=['GET','POST'])
def show_tables():
    search_keywords = request.form.get('keywords','Rate')
    df_trends = utilities.getGoogleTrends(search_keywords)
    trends_snapshot = utilities.showSnapshot(df_trends)
    try:
        data_news= utilities.getNewsKeyword(search_keywords)
        df_news = utilities.getSnapshot(data_news)
        return render_template('view.html',tables=[df_news.to_html(classes='news'), trends_snapshot.to_html(classes='trends')],
        titles = ['na', 'Top News', 'Google Trends'])
    except:
        return redirect(url_for('show_tables'))

#Another potential way:
#     except Exception as e:
#         return str(e)


@app.route("/trends",methods=['GET','POST'])
def show_trends():
    search_keywords = request.form.get('keywords','Trump')
    df_trends = utilities.getGoogleTrends(search_keywords)
    trendsData = np.squeeze(df_trends.values[1:])
    trendsTime = df_trends.index[1:]
    return render_template('view.html', trendsData =json.dumps(trendsData.tolist()),
    trendsTime = json.dumps(trendsTime.tolist()))


# cron = Scheduler(daemon=True)
# # Explicitly kick off the background thread
# cron.start()

# @cron.interval_schedule(hours=1)
# def job_function():
#     # Do your work here


# # Shutdown your cron thread if the web process is stopped
# atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == "__main__":
    print(__name__)
    schedule.every(1).day.at("23:55").do(job)
    t = Thread(target=run_schedule)
    t.start()
    print "Start time: " + str(start_time)
    app.run(debug=True, host='0.0.0.0', port=5000)