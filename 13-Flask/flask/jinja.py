##Building URL Dynamically
##Variable Rule
#Jinja 2 Template Engine
'''
{{ }} expressions to print output in html
{%..%} conditions, for loops
{#..#} this is for comments
'''


from flask import Flask,render_template,request,redirect,url_for
'''
It creates an instance of the Flask class,
which will be your WSGI(web server Gateqay interface) application
'''
app=Flask(__name__) ##WSGI application

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask Course<h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':  
        name=request.form['name']
        return f'Hello {name} !'
    return render_template('getresult.html')

##Variable Rule
# ✅ Success route
@app.route('/success/<int:score>')
def success(score):
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL !!"

    exp = {'score': score, "res": res}  # This is a dictionary
    return render_template('result1.html', results=exp)

# ✅ Fail route (should match success route structure)
@app.route('/fail/<int:score>')
def fail(score):
    res = "FAIL !!"
    exp = {'score': score, "res": res}
    return render_template('result1.html', results=exp)

# ✅ Route to handle form submission
@app.route('/getresults', methods=['POST', 'GET'])
def get_result():
    if request.method == 'POST':
        # Get data from form
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        data_science = float(request.form['datascience'])

        # Calculate average score
        total_score = (science + maths + data_science) / 3

        # ✅ Smart routing: redirect based on score
        if total_score >= 50:
            return redirect(url_for('success', score=int(total_score)))## basically this means '/success/85' -> if marks = 85
        else:
            return redirect(url_for('fail', score=int(total_score)))

    
    return render_template("getresult.html")  # fallback if GET method is called


if __name__=="__main__":
    app.run(debug=True)