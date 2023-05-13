from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario
from comunidadeimpressionadora.routes import login
from flask_bcrypt import Bcrypt
##################### criar database
# with app.app_context():
#         database.create_all()



########## CHECAR SE TEM USUARIO

with app.app_context():
        usuarios = Usuario.query.all()
        print(usuarios)
        usuario1= usuarios[0]
        usuario2 = usuarios[1]
        print(usuario1.email, usuario1.username)
        print('-'*20)
        print(usuario2.email, usuario2.username)



############# deletar database
# with app.app_context():
#        database.drop_all()