from flask import Flask
import flask





def create_app():
 app = Flask(__name__)
 app.config["SECRET_KEY"] = "JHHGUIF HUHUH HHUF UH"
 


 from .views import views
 

 app.register_blueprint(views, url_prefix="/")
 return app


print(print(flask.__version__))
