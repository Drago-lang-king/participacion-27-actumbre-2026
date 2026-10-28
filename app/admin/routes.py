from flask import Blueprint, render_template

admin_bp = Blueprint('admin',__name__,url_prefix='/panel',template_folder='templates')

@admin_bp.route('/')
def listar_panel():
    return render_template('mostrar_panel.html')