from flask import Flask
import src.database.db as db

from src import env
from src.routes.blog import blog_bp
from src.routes.hipnoterapija import hipnoterapija_bp
from src.routes.index import index_bp
from src.routes.jasnovidnost import jasnovidnost_bp
from src.routes.medijstvo import medijstvo_bp
from src.routes.omeni import omeni_bp
from src.routes.regresija import regresija_bp
from src.routes.samohipnoza import samohipnoza_bp

app = Flask(__name__)

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
