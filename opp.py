from flask import Flask, request, redirect

app = Flask(__name__)

urls = {}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form["url"]

        code = str(len(urls) + 1)
        urls[code] = url

        return "Short URL: http://127.0.0.1:5000/" + code

    return '''
    <form method="POST">
    Long URL: <input name="url">
    <button>Shorten</button>
    </form>
    '''

@app.route("/<code>")
def open_url(code):
    if code in urls:
        return redirect(urls[code])

    return "URL Not Found"

app.run(debug=True)