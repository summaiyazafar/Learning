# Simple flask class sy wsgi application bnana:
from flask import Flask
app=Flask(__name__)
@app.route('/')
def Hello_World():
    return "Hello World!"
if __name__=="__main__":
    app.run(debug=True)

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
<script>alert("bad")</script>
