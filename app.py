from flask import Flask, render_template, request, redirect
from baekjoon import getAlgorithmTag
from algospot import getAlgorithmName


# app = Flask("AlgorithmSearch")
app = Flask(__name__)

db = {}


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/baekjoon")
def baekjoon():
    print("2")
    Algorithm__tag = request.args.get("Algorithm__baekjoon")
    if Algorithm__tag:
        Algorithm__tag = Algorithm__tag.lower()
        # Tag=getAlgorithmTag(Algorithm__tag)
        existingTag = db.get(Algorithm__tag)
        if existingTag:
            problems = existingTag
        else:
            problems = getAlgorithmTag(Algorithm__tag)
            db[Algorithm__tag] = problems
    else:
        return redirect("/")
    return render_template("baekjoon.html", searchingBy=Algorithm__tag, resultsNumber=len(problems), problems=problems)


@app.route("/algospot")
def algospot():
    # print("3")
    Algorithm__tag = request.args.get("Algorithm__algospot")
    if Algorithm__tag:
        Algorithm__tag = Algorithm__tag.lower()
        # Tag=getAlgorithmTag(Algorithm__tag)
        existingTag = db.get(Algorithm__tag)
        if existingTag:
            problems = existingTag
        else:
            problems = getAlgorithmName(Algorithm__tag)
            db[Algorithm__tag] = problems
    else:
        return redirect("/")
    return render_template("algospot.html", searchingBy=Algorithm__tag, resultsNumber=len(problems), problems=problems)


if __name__ == "__main__":
    print("1")
    app.run()
    # app.run(host='0.0.0.0', port="5000", debug=True)

# app.run(host='0.0.0.0', debug=True)


# app.run(debug=True)
# app.run(host='0.0.0.0')
# app.run()
