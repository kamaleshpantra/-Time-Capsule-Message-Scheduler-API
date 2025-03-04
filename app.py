from flask import Flask
from models import init_db
from routes import routes
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv('details.env')

app = Flask(__name__)

# Initialize the database
init_db()

# Register the routes blueprint
app.register_blueprint(routes)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)