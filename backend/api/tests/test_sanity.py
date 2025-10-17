from django.test import TestCase

class TestSanity(TestCase):
    def test_math(self):
        assert 1 + 1 == 2