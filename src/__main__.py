from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, JWTManager

from src import env
from src.database import db
from src.routes.blog import blog_bp
from src.routes.hipnoterapija import hipnoterapija_bp
from src.routes.index import index_bp
from src.routes.jasnovidnost import jasnovidnost_bp
from src.routes.medijstvo import medijstvo_bp
from src.routes.omeni import omeni_bp
from src.routes.regresija import regresija_bp
from src.routes.samohipnoza import samohipnoza_bp

app = Flask(__name__)
CORS(app)

app.secret_key = env.SECRET_KEY
jwt = JWTManager(app)

app.register_blueprint(index_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(hipnoterapija_bp)
app.register_blueprint(omeni_bp)
app.register_blueprint(regresija_bp)
app.register_blueprint(jasnovidnost_bp)
app.register_blueprint(samohipnoza_bp)
app.register_blueprint(medijstvo_bp)

if __name__ == '__main__':
    db.drop()
    db.seed()
    app.run(host='0.0.0.0', port=env.PORT, debug=True)
