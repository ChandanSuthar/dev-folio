from flask import Flask,render_template,url_for,request
import mysql.connector as mc


app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'userdata'
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/section1')
def section1():
    return render_template('section1.html')
@app.route('/section2')
def section2():
    return render_template('section2.html')
@app.route('/section3')
def section3():
    return render_template('section3.html')

@app.route('/query')
def query():
    return render_template('query.html')

@app.route('/user_query',methods=['GET','POST'])
def user_query():
    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        query = request.form['query']
     # Save the data to the database
        conn = mc.connect(**db_config)
        cur = conn.cursor()
        insert_query = """
        INSERT INTO userecord (name, email, query)
        VALUES (%s, %s, %s)
        """
        cur.execute(insert_query, (name, email, query))
        conn.commit()
        cur.close()
        conn.close()

        user_data = [name, email, query]
        return render_template('query.html', user_data=user_data)
    return "Please submit the form."
        

if __name__ == "__main__":
    app.run(debug=True) #if facing error :- host="0.0.0.0"