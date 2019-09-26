from flask import Flask
from finalproject import do_everything

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = do_everything()
    return data

if __name__ == '__main__':
    app.run(debug=True)
