from backend import create_app
from dotenv import load_dotenv
load_dotenv()


app = create_app(debug=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)