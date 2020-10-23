from flask import Flask
from JDMApi import *
from JDMResponse import *
from BenchmarkEngine import *
from flask_cors import CORS

app = Flask(__name__)
api = JDMApi()
formatter = ResponseFormatter()
CORS(app)

@app.route('/query/<content>')
def handle_query(content):
    benchmarkEngine = BenchmarkEngine()
    response = api.submit(content, benchmarkEngine)
    print("Délai de réponse : " + str(benchmarkEngine.duration) + " seconds")
    benchmarkEngine.reset()
    return response
