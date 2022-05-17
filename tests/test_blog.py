import unittest
from app.models import Blogs,db,User

class BlogModelTest(unittest.TestCase):
    def setUp(self):
        '''
          Test that runs before every other test
        '''
        self.user_oparanya = User(username = "Oparanya", email ="oparanya@gmail.com", password = '1234567')
        self.new_blog = Blogs(title= 'python',blog='A line of code a day keeps peace at bay',user = self.user_oparanya)
        
    def tearDown(self):
        Blogs.query.delete()
        User.query.delete()
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title,'python')
        self.assertEquals(self.new_blog.blog,'A line of code a day keeps peace at bay')
        self.assertEquals(self.new_blog.user,self.user_oparanya)
        
    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blogs.query.all())>0)
        
    def test_get_blog_by_id(self):
    
        self.new_blog.save_blog()
        got_blogs = Blogs.get_blogs(12345)
        self.assertTrue(len(got_blogs) == 1)