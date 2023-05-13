from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()],render_kw={"placeholder":"Digite seu nome de usuário"})
    email = StringField("E-mail", validators=[DataRequired(),Email(message='Endereço de e-mail inválido')], render_kw={"placeholder": "Digite seu e-mail "})
    senha = PasswordField("Senha", validators=[DataRequired(),Length(6,20, message='Sua senha deve ter entre 6 e 20 caracteres')],render_kw={"placeholder": "Digite sua senha"})
    confirmacao = PasswordField("Confirmação da senha", validators=[DataRequired(message='Senha diferente da preenchida anteriormente'), EqualTo('senha')],render_kw={"placeholder": "Confirme sua senha"})
    botao_submit_criar_conta = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('Já existe uma conta associada a esse e-mail. Cadastre-se com outro e-mail ou faça login para continuar')

    def validate_username(self, username):
        user = Usuario.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Já existe uma conta com esse nome de usuário. Escolha outro nome ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email(message='Endereço de e-mail inválido')], render_kw={"placeholder": "Digite seu e-mail "})
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6,20, message='Sua senha deve ter entre 6 e 20 caracteres')], render_kw={"placeholder": "Digite sua senha"})
    botao_submit_login = SubmitField("Fazer Login")
    lembrar_dados = BooleanField("Lembrar")

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()],render_kw={"placeholder": "Digite seu nome de usuário"})
    email = StringField("E-mail", validators=[DataRequired(), Email(message='Endereço de e-mail inválido')],render_kw={"placeholder": "Digite seu e-mail "})
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    curso_excel = BooleanField('Excel Impressionador')
    curso_vba = BooleanField('VBA Impressionador')
    curso_powerbi = BooleanField('Power BI Impressionador')
    curso_python = BooleanField('Python Impressionador')
    curso_sql = BooleanField('SQL Impressionador')
    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse e-mail. Cadastre outro e-mail')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do post', validators=[DataRequired(), Length(2,140)])
    corpo =  TextAreaField('Escreva seu post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')