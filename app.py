import random
from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def zero():
    return "page 0"

@app.route("/1")
def one():
    return "page 1"


csv=open('occupations.csv').read()
dictionary=dict()
for line in csv.split('\n'):
    if not line == "":
        if line[0] == '"':
            dictionary[line.split('"')[1]] = float(line.split('"')[2].split(',')[1])
        else:
            dictionary[line.split(',')[0]] = float(line.split(',')[1])


def blah():
    rn=random.random()
    rn=rn*99.8
    for k in dictionary:
        if rn<dictionary[k]:
            return k
        rn-=dictionary[k]

#job=blah()



@app.route("/occupations")
def occ():
    job=blah()
    return render_template("occ.html",dictionary=dictionary, job=job)



if __name__=="__main__":
    app.run(debug=True)



