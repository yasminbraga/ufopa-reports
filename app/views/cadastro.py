from flask import Blueprint, render_template, session, request, flash, redirect, url_for
from app.models.models import Usuario, db

cadastro_bp = Blueprint('cadastro',
                    __name__,
                    url_prefix='/cadastro')


@cadastro_bp.route('/', methods=["GET", "POST"])
def new_cadastro():
    if request.method == "POST":
        
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirma_senha = request.form.get('confirma_senha')

        user_exists = db.session.query(Usuario).filter_by(email=email).first() 
        usuario = Usuario(nome=nome, email=email, senha=senha)

        if user_exists:
            flash('Email já cadastrado, tente outro!', 'danger')
        elif senha != confirma_senha:
            flash('Senhas não conferem, tente novamente!', 'danger')
        else:
            db.session.add(usuario)
            db.session.commit()

            flash('Usuário cadastrado, faça login para continuar!', 'success')
            return redirect(url_for('login.index_login'))
            
        return render_template('cadastro/index.html', show_navigation=True, usuario=usuario or Usuario())
    return render_template('cadastro/index.html', show_navigation=True)
