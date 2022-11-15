from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'page': 'Home', 'Message': 'Successful loaded the homepage', 'Titlestamp': time.time()}

    json_dump = json.dumps(data_set)
    return json_dump



@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))# /user/?user=energy
     
    data_set = {'page': 'Request', 'Message': f'Successful got request{user_query}', 'Titlestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump  



    if __name__=='__main__':
        app.run(port=7777)