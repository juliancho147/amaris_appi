from flask import Flask, make_response, jsonify
application = Flask(__name__)
# print a nice greeting.
@application.route("/",methods=["GET"])
def say_hello(username = "World"):
    return make_response(jsonify({"hola":"hola"}))


# run the app.
if __name__ == "__main__":

    application.run()