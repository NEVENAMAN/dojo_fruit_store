from flask import Flask,render_template,request
app = Flask(__name__)
# ------------------------------------------------------------
@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    total = int(request.form['strawberry'])+ int(request.form['raspberry']) + int(request.form['apple'])
    return render_template("checkout.html",strawberrynum=request.form['strawberry'],
    raspberryNum=request.form['raspberry'],appleNum=request.form['apple'],
    name=request.form['first_name'],lastName=request.form['last_name'],
    id=request.form['student_id'] , sum=total)

@app.route('/fruits')         
def fruits():
    fruit = ['apple.png','blackberry.png','raspberry.png','strawberry.png']
    return render_template("fruits.html",fruitName=fruit)

# ------------------------------------------------------------
if __name__=="__main__":   
    app.run(debug=True)  