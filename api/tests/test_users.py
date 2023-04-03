import unittest

from werkzeug.security import generate_password_hash

from ..import create_app

from ..config.config import config_dict
from ..utils.db import db
from ..models.users import User

class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app=create_app(config=config_dict['testing'])
        self.appctx=self.app.app_context()
        self.appctx.push()
        self.client=self.app.test_client()
        db.create_all()
 
    def tearDown(self): #tearDown is a method that runs after every test
        db.drop_all()
        self.appctx.pop()
        self.app=None
        self.client=None

    def test_user_registration(self):

        data={
            "username":"testuser",
            "email":"testuser@test.com",
            "password":"password"
        }

        response=self.client.post('/auth/signup',json=data)

        user=User.query.filter_by(email="testuser@test.com").first()

        assert user.username == "testuser"

        assert response.status_code == 201
    
    def test_user_login(self):
        data={
            "email":"testuser@test.com",
            "password":"password"
        }
        response=self.client.post('/auth/login',json=data)
        assert response.status_code == 400