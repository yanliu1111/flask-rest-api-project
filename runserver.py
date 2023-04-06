from api import create_app
from api.config.config import config_dict

app= create_app(config=config_dict['prodution'])

if __name__ == '__main__':
    app.run()

# working on dev config
# from api import create_app
# app=create_app()
# if __name__ == '__main__':
#     app.run()