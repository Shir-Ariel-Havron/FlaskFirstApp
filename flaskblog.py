from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bba2894ae248caf20c394f74a58914c2'


posts = [
    {
        'author': 'me',
        'title': 'first post',
        'content': 'asdfasdfasdf',
        'date_posted': 'April 1, 2020'
    },
    {
        'author': 'me',
        'title': 'second post',
        'content': 'asdfasdfasdfasdfasdfasdfasdfasdf',
        'date_posted': 'April 2, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'pass':
            flash('You logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Log in unsuccessful.', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
