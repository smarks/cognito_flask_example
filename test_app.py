import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app


class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_index_route(self):
        """Test the home page route"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Cognito Auth Demo', response.data)
        self.assertIn(b'Sign In', response.data)
        self.assertIn(b'Sign Up', response.data)
    
    def test_signup_route(self):
        """Test the signup page route"""
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sign Up', response.data)
        self.assertIn(b'AWS Cognito', response.data)
    
    def test_signin_route(self):
        """Test the signin page route"""
        response = self.app.get('/signin')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sign In', response.data)
        self.assertIn(b'AWS Cognito', response.data)
    
    def test_test_route(self):
        """Test the test route"""
        response = self.app.get('/test')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Simplified app is working!', response.data)
    
    def test_nonexistent_route(self):
        """Test a non-existent route returns 404"""
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
    
    def test_navigation_links(self):
        """Test that navigation links are present on all pages"""
        routes = ['/', '/signin', '/signup']
        for route in routes:
            response = self.app.get(route)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'href="/"', response.data)
            self.assertIn(b'href="/signin"', response.data)
            self.assertIn(b'href="/signup"', response.data)


if __name__ == '__main__':
    unittest.main()