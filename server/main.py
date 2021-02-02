from flask import Flask
from flask import request
# from flask_executor import Executor
from concurrent.futures import ThreadPoolExecutor
from JDMApi import *
from JDMResponse import *
from BenchmarkEngine import *
from flask_cors import CORS
from textx import TextXSyntaxError

app = Flask(__name__)
executor = ThreadPoolExecutor()
api = JDMApi()
formatter = ResponseFormatter()
CORS(app)

@app.route('/get/<query>')
def handleQuery(query):
    benchmark_engine = BenchmarkEngine()
    with_cache = not (request.args.get('disable_cache') == 'true')
    api_response = api.submit(query, benchmark_engine, with_cache)
    response = ResponseFormatter().formatQueryResult(api_response)
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
