# Polls the DomJudge server and checks for new submissions

import threading
import mysql.connector

import config

# Global lock; protects all global vars
lock = threading.Lock()

# Database connection
db = None

def init_db():
    global db
    with lock:
        db = mysql.connector.connect(autocommit=True, **config.dbconfig)

def poll_domjudge():
    with lock:
        cursor = db.cursor()
        cursor.execute("""
                select submission.teamid, submission.probid
                from judging, submission
                where judging.submitid = submission.submitid
                and judging.endtime is not null
                and (NOW() - judging.endtime) < 10
                and judging.result = "accepted"
                order by judging.endtime desc
                limit 1""")
        results = list(cursor)
        cursor.close()
        return results[0] if len(results) > 0 else None

def eye():
    result = poll_domjudge()
    if result is not None:
        print "Moving the light to team %s for solving problem %s" % result
    else:
        print "Moving the light to neutral position"

def periodically(fun, period):
    def run_the_fun():
        fun()
        threading.Timer(period, run_the_fun).start()

    run_the_fun()


init_db()
periodically(eye, 2.0)
