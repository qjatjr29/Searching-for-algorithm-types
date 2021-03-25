from flask import Flask, render_template, request, redirect
from baekjoon import getAlgorithmTag
from algospot import getAlgorithmName
from group import getGroupName


# app = Flask("AlgorithmSearch")
app = Flask(__name__)

BJdb = {}
Algodb = {}
Groupdb = {}


@app.route("/")
def homepage():
    return render_template("index.html")


# @app.route("/home")
# def redirecting():
#     return render_template("index.html")


@app.route("/Search_Baekjoon")
def SearchBJ():
    # return render_template("site.html")
    return render_template("Search_Baekjoon.html")


@app.route("/Search_Algospot")
def SearchAlgo():
    return render_template("Search_Algospot.html")


@app.route("/Group")
def SearchGroup():
    return render_template("Search_Group.html")


@app.route("/baekjoon")
def baekjoon():
    print("hi")
    Algorithm__tag = request.args.get("Algorithm__baekjoon")
    if Algorithm__tag:
        Algorithm__tag = Algorithm__tag.lower()
        # Tag=getAlgorithmTag(Algorithm__tag)
        existingTag = BJdb.get(Algorithm__tag)
        print(existingTag)
        if existingTag:
            problems = existingTag
        else:
            problems = getAlgorithmTag(Algorithm__tag)
            BJdb[Algorithm__tag] = problems
    else:
        return redirect("/")
    return render_template("baekjoon.html",
                           searchingBy=Algorithm__tag, resultsNumber=len(
                               problems),
                           problems=problems)


@app.route("/algospot")
def algospot():
    Algorithm__tag = request.args.get("Algorithm__algospot")
    if Algorithm__tag:
        Algorithm__tag = Algorithm__tag.lower()
        # Tag=getAlgorithmTag(Algorithm__tag)
        existingTag = Algodb.get(Algorithm__tag)
        print(existingTag)
        if existingTag:
            problems = existingTag
        else:
            problems = getAlgorithmName(Algorithm__tag)
            Algodb[Algorithm__tag] = problems
    else:
        return redirect("/")
    return render_template("algospot.html", searchingBy=Algorithm__tag,
                           resultsNumber=len(problems), problems=problems)


@app.route("/group_result")
def group():
    Group_name = request.args.get("Baekjoon_group")
    if Group_name:
        Group_name = Group_name.lower()
        # Tag=getAlgorithmTag(Algorithm__tag)
        existingGroup = Groupdb.get(Group_name)
        print(existingGroup)
        if existingGroup:
            groups = existingGroup
        else:
            groups = getGroupName(Group_name)
            Groupdb[Group_name] = groups
            print("됐어")
    else:
        return redirect("/")
    return render_template("group.html", searchingBy=Group_name,
                           resultsNumber=len(groups), groups=groups)


if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0', port="5000", debug=True)

# app.run(host='0.0.0.0', debug=True)


# app.run(debug=True)
# app.run(host='0.0.0.0')
# app.run()
