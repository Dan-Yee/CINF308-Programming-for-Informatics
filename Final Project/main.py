import flask                                                # import the Flask module

App = flask.Flask(__name__)                                 # create the new Flask application using the Flask constructor

@App.route("/hello")                                        # create the decorator that defines the route "/hello"
def home():                                                 # the function that is executed when this route is visited in a browser
    return flask.render_template("hello.html")              # render the HTML file "hello.html" onto the browser when this route is visited

@App.route("/world")
def world():
    return flask.render_template("world.html")

App.run()                                                   # Run the application. You can view this page at "localhost:5000" in your browser