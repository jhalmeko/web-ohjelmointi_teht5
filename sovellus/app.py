from dotenv import load_dotenv
from flask import Flask
import controllers.users


app = Flask(__name__)


app.add_url_rule('/api/users', view_func=controllers.users.get_all_users())


if __name__ == '__main__':
    load_dotenv()
    app.run()
