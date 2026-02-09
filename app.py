from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)

# Secret key for security
app.config["SECRET_KEY"] = os.urandom(32)

# Enable CSRF protection
csrf = CSRFProtect(app)

@app.route("/")
def hello():
    return "Hello from Docker CI/CD Pipeline with Security!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
