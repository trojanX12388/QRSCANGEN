from flask import Blueprint, render_template, session, flash, redirect, url_for
from flask_login import current_user

views = Blueprint('views', __name__)



# MAIN PAGE
@views.route("/", methods=['GET', 'POST'])
def home():
    # CHECKING ACTIVE SESSIONS
    if current_user.__class__.__name__ == "Faculty_Profile":     
        return redirect(url_for('auth.facultyH'))
    
    # IF NO ACTIVE SESSION, REDIRECT TO MAIN PAGE
    else:
        return render_template("Faculty-Login-Page/index.html")

