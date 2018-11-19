from flask import url_for, redirect, flash, render_template
from flask_login import current_user, login_user, logout_user, login_required

from resumebuilder import app, db, bcrypt
from resumebuilder.forms import RegistrationForm, LoginForm, ExperienceForm
from resumebuilder.models import User, Experience, Tag


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash("Your account has been created successfully", 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check login information', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/ExperienceRegistration', methods=['GET', 'POST'])
@login_required
def registerExperience():
    form = ExperienceForm()

    if form.validate_on_submit():
        experience = Experience(proposition1=form.proposition1.data, proposition2=form.proposition2.data, proposition3=
        form.proposition3.data, date=form.date.data, role=form.role.data, host=form.host.data, user_id=current_user.id)
        db.session.add(experience)

        experience_tags = form.tags.data.split()
        tags_qs = Tag.query.all()
        db_tags = [tag.name for tag in tags_qs]
        for tag in experience_tags:
            if tag not in db_tags:
                temp_Tag = Tag(name=tag)
                db.session.add(temp_Tag)
            else:
                temp_Tag = list(filter(lambda x: x.name == tag, tags_qs))[0]
            experience.tags.append(temp_Tag)

        db.session.commit()
        flash("Your experience has been registered successfully", 'success')
        return redirect(url_for('index'))

    return render_template('register_experiences.html', title='Register Experience', form=form)
