from flask import render_template, redirect, url_for, flash, request, send_file, send_from_directory
from app import app
from app.models import User, Book, Loan
from app.forms import ChooseForm, LoginForm, BorrowForm, ReturnForm
from flask_login import current_user, login_user, logout_user, login_required, fresh_login_required
import sqlalchemy as sa
from app import db
from urllib.parse import urlsplit
import datetime


@app.route("/")
def home():
    return render_template('home.html', title="Home")


@app.route("/account")
@login_required
def account():
    form=ReturnForm()
    list_loans=current_user.loans
    return render_template('account.html', title="Account", list_loans=list_loans, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('generic_form.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/all_books', methods=['GET', 'POST'])
def all_books():
    form=BorrowForm()
    list_books=Book.query.all()
    return render_template('all_books.html', title="All Books", list_books=list_books, form=form)

@app.route('/book_details/<int:book_id>', methods=['GET', 'POST'])
def book_details(book_id):
    book=db.session.get(Book, book_id)
    #invalid book_id
    if book is None:
        flash('Book not found', 'danger')
        return redirect(url_for('all_books'))
    return render_template('book_info.html', title='Book information', book=book)


@app.route('/borrow_book', methods=['GET', 'POST'])
def borrow_book():
    form=BorrowForm()
    if form.validate_on_submit():
        book=db.session.get(Book,int(form.choice.data))
        loan=Loan(date_loaned=datetime.datetime.now(),book_id=book.id)
        current_user.loans.append(loan)

        # handle multiple users borrowing
        try:
            db.session.commit()
        except sa.exc.IntegrityError as err:
            flash('Error: someone else just borrowed this book', 'danger')
            app.logger.warning(f'IntegrityError: {err=}')
            db.session.rollback()
        flash(f'Book borrowed successfully', 'success')
    return redirect(url_for('account'))

@app.route('/return_book', methods=['GET', 'POST'])
def return_book():
    form=ReturnForm()
    if form.validate_on_submit():
        book_id=form.choice1.data
        user_id=form.choice2.data
        loan=db.session.get(Loan,(book_id,user_id))
        db.session.delete(loan)
        db.session.commit()
        flash(f'Book returned successfully', 'success')
    return redirect(url_for('account'))



# Error handlers
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# Error handler for 403 Forbidden
@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html', title='Error'), 403

# Handler for 404 Not Found
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', title='Error'), 404

@app.errorhandler(413)
def error_413(error):
    return render_template('errors/413.html', title='Error'), 413

# 500 Internal Server Error
@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html', title='Error'), 500