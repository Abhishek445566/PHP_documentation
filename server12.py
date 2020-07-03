from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
  def php_tutorial():
    return render_template("php_tutorial.html")
    

