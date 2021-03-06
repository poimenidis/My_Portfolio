from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return  render_template('portfolio.html')

@app.route("/Google_Play")
def Google_Play():
    return  render_template('Google_Play.html')

@app.route("/Resume")
def Resume():
    return  render_template('Resume.html')

@app.route("/Form")
def Form():
    return  render_template('Form.html')

if __name__ == '__main__':
    app.run(debug= True, host="127.0.0.1", port=80)