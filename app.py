from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    names = ['Alice', 'Bob', 'Charlie']
    return render_template('names.html', names=names)
app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def login_register():
    if request.method == 'POST':
        random = "Something"
        login = request.form.get('login', '')
        password = request.form.get('password', '')

        with open('text.txt') as file:
            lines = file.readlines()

        login_found = False
        for line in lines:
            line = line.strip()
            parts = line.split(",")
            rlogin = parts[0]
            rpassword = parts[1]

            if rlogin == login and rpassword == password:
                login_found = True
                return render_template('index.html')

        if login == '' or password == '':
            return "Invalid login or password. Please try again."

        if login_found:
            return "Username already exists. Please choose a different username."

        new_login = request.form.get('new_login', '')
        new_password = request.form.get('new_password', '')
        confirm_new_password = request.form.get('confirm_new_password', '')

        if new_login == '' or new_password == '':
            return "Invalid username or password. Please try again."

        if new_password != confirm_new_password:
            return "Passwords do not match. Please try again."

        with open('text.txt', 'a') as file:
            file.write('\n' + new_login + "," + new_password)
        return "Registration successful! Please login."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)