import unittest
from app.models import User,db;

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username = "Oparanya", email ="oparanya@gmail.com", bio = "Freaky", profile_pic_path = "static/photos", password = '1234567')
        

    def tearDown(self):
        User.query.delete()
 
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('1234567'))

    def test_save_user(self):
        self.new_user.save_user()
        self.assertTrue(len(User.query.all())>0)

    def test_check_instance_variables(self):
        self.assertEquals(self.new_user.username, 'Oparanya')
        self.assertEquals(self.new_user.email, 'Oparanya@gmail.com')
        self.assertEquals(self.new_user.bio, 'freaky')
        self.assertEquals(self.new_user.profile_pic_path, 'static/photos')
        self.assertTrue(self.new_user.verify_password('12345'))


    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password 
            
if __name__ == '__main':
    unittest.main()            