from .flask_app import app
from .qa import qa
from .user import user
from .dbs import db
from .extensions import loginManager
from .user import User

app.register_blueprint(qa)
app.register_blueprint(user)


def configure_login(app):
    loginManager.login_view = 'qa.index'
    loginManager.refresh_view = 'qa.index'
    loginManager.login_message = None
    loginManager.session_protection = 'basic'
    loginManager.init_app(app)

    @loginManager.user_loader
    def load_user(id):
        return User.query.get(id)
    loginManager.setup_app(app)


configure_login(app)
