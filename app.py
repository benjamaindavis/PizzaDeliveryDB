from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/signup')
def signup():
    # Placeholder for future signup page
    return "Sign Up Page Coming Soon"

if __name__ == "__main__":
    app.run(debug=True)

