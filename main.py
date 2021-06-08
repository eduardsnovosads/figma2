from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def Klients():
  return render_template("Medicina_Klients.html")

@app.route('/arsti')
def arsti():
  return render_template("arstu_tabula.html")

@app.route('/pieraksti')
def pieraksti():
  return render_template("pierakstu_tabula.html")

@app.route('/tavs_akaunts')
def tavs_akaunts():
  return render_template("tavs_akaunts.html")

@app.route('/Administrators')
def administrators():
  return render_template("Medicina_Administrators.html")

@app.route('/Klients')
def klients():
  return render_template("Medicina_Klients.html")

@app.route('/slimnicas')
def slimnicas():
  return render_template("slimnicas_pievienosana.html")

@app.route('/slimnicu')
def slimnicu():
  return render_template("slimnicu_tabula.html")

@app.route('/arstu')
def arstu():
  return render_template("arsta_pievienosana.html")

app.run(host='0.0.0.0', port=8080)