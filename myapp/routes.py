from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/post/<int:post_id>')
def view_post(post_id):
    # Logic to fetch and display a specific post
    return f"Viewing post #{post_id}"

@bp.route('/admin')
def admin():
    # Logic to display an admin panel
    return "Admin Panel"

