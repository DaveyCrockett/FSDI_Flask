from flask import Flask     # From the flask module import the Flask class.


app = Flask(__name__)       # Instantiate the Flask class into the app variable.
                            # Variables that contain class instances are called "objects".
@app.route("/")             #this is a decorator.
def index():                # this is a function; in the contexxt of flask it is a "view Function"
    return "<h1>Hello, World!</h1>"     # Return statement; this is returning a string.

# @app.get("/home")
# def home():
#     return "Welcome Home!"

@app.route("/about")
def about_me():
    me = {
        "first_name": "David",
        "last_name": "Paredes",
        "hobbies": "Games",
        "active": True,
        "list": [1,2,3],
        "tuple": (1,2,3) # converts to list or just crashes
    }
    return me

# adding a comment to try to commit change