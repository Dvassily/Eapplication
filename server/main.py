from flask import Flask
from JDMApi import *
from JDMResponse import *
from BenchmarkEngine import *

app = Flask(__name__)
api = JDMApi()
formatter = ResponseFormatter()

@app.route('/query/<content>')
def handle_query(content):
    benchmarkEngine = BenchmarkEngine()
    response = api.submit(content, benchmarkEngine)
    print("Délai de réponse : " + str(benchmarkEngine.duration) + " seconds")
    benchmarkEngine.reset()
    return response
