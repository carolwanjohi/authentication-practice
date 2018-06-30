import unittest
# Import class to be tested
from app.models import User,Role

class TestUser(unittest.TestCase):
    '''
    Test class to test behaviours of the User class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_role = Role(role_name="Teacher")
        self.user_me = User(username="Meme", role=self.new_role)

    def test_instance(self):

        self.assertTrue(self.new_role, Role)

