from app import create_app
from app.extensions import db
from app.models import User
from sqlalchemy import inspect

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        if inspect(db.engine).has_table("user") and not User.query.filter_by(username="admin").first():
            usuario = User(username="admin", role="admin")
            usuario.set_password('1234')
            db.session.add(usuario)
            db.session.commit()
    app.run(debug=True, port=5001)
