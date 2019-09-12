from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


###to run FLASK WEB SERVER:
#execute command to register as env variables. second one refreshes the server live
#export FLASK_APP=flaskblog.py
#export FLASK_DEBUG=1
#flask run
## add name == main and run the file directly =  works better.


app = Flask(__name__)
app.config['SECRET_KEY'] = 'be55d207f7a71bdaf2d529cbb90d4f3a'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Log in unsuccessful', 'danger')
    return render_template('login.html', title='LogIn', form=form)


if __name__ == '__main__':
    app.run(debug=True)