from flask import Blueprint, render_template

blog_bp = Blueprint('blog',__name__,url_prefix='/blog',template_folder='templates')

entradas={
        1:'informacion de flask',
        2:'Informacion de python',
        3:'Informacion de c#'   
    }

@blog_bp.route('/entrada/<int:id>')
def entrada(id):
    titulo = entradas.get(id,'Entrada no encontrada')
    return render_template('entrada.html', titulo=titulo)    
