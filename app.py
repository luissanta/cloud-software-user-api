from flask import Flask
from flask_jwt_extended import JWTManager

from config import ProductionConfig
from flask_cors import CORS
from routes import api_routes
from models.database import database


app = Flask(__name__)
app.config.from_object(ProductionConfig)
app_context = app.app_context()
app_context.push()

database.init_app(app)
database.create_all()


cors = CORS(app)
jwt = JWTManager(app)

app.register_blueprint(api_routes, url_prefix='/api')

if __name__ == '__main__':
    app.run()
