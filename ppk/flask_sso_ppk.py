from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'secret-key'

# Hardcoded user data for demonstration purposes
users = {
    'john': {'password': 'password123', 'ppk': 'validppkfile'},
    'jane': {'password': 'password456', 'ppk': 'validppkfile'},
}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if ppk file is submitted
        if 'ppk_file' in request.files:
            ppk_file = request.files['ppk_file']
            for username, user in users.items():
                if user['ppk'] == ppk_file.read().decode('utf-8'):
                    session['username'] = username
                    return redirect('/content1')
            return 'Invalid PPK file.'

        # Check if username and password are submitted
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect('/content1')
        return 'Invalid username or password.'

    return render_template('login.html')


@app.route('/content1')
def content1():
    if 'username' not in session:
        return redirect('/login')
    return render_template('content1.html', username=session['username'])


@app.route('/content2')
def content2():
    if 'username' not in session:
        return redirect('/login')
    return render_template('content2.html', username=session['username'])


@app.route('/content3')
def content3():
    if 'username' not in session:
        return redirect('/login')
    return render_template('content3.html', username=session['username'])


if __name__ == '__main__':
    app.run()
