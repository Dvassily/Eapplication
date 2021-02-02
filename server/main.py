from flask import Flask
from JDMApi import *
from JDMResponse import *
from BenchmarkEngine import *
from flask_cors import CORS
from textx import TextXSyntaxError

app = Flask(__name__)
api = JDMApi()
formatter = ResponseFormatter()
CORS(app)

@app.route('/get/<query>')
def handleQuery(query):
    benchmark_engine = BenchmarkEngine()
    apiResponse = api.submit(query, benchmark_engine)
    response = ResponseFormatter().formatQueryResult(apiResponse)
    print("Délai de réponse : " + str(benchmark_engine.duration) + " seconds")
    benchmark_engine.reset()
    return response

@app.route('/parse_query/<query_str>')
def parseQuery(query_str):
    try:
        query = QueryParser(query_str).parse()
        return ResponseFormatter().formatQueryParsingResult(query)
    except TextXSyntaxError as err:
        return ResponseFormatter().formatQueryParsingError(err)



app.run()