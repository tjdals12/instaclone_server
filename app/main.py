from flask import Flask
from models import db
from routes.sample_router import sample_blueprint
import config

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = config.SECREY_KEY
db.init_app(app)

app.register_blueprint(sample_blueprint)

if __name__ == '__main__':
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
