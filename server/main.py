from flask import Flask
from JDMApi import *
from JDMResponse import *
from BenchmarkEngine import *
app = Flask(__name__)
api = JDMApi()

@app.route('/query/<content>')
def handle_query(content):
    benchmarkEngine = BenchmarkEngine()
    api.submit(content, benchmarkEngine)
    print("Délai de réponse : " + str(benchmarkEngine.duration) + " seconds")
    benchmarkEngine.reset()
    return "ok"
