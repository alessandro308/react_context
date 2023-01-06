from react_context import get_context, use_context
from unittest import TestCase

class UseContextTest(TestCase):

    def test_simple_context(self):
        def nested_function():
            return get_context('something')
        import inspect
        print('frame_id_original', id(inspect.stack()[0].frame))
        with use_context(something=123):
            value = nested_function()
            self.assertEqual(123, value)
        value = nested_function()
        self.assertEqual(None, value)
    
    def test_missing_value(self):
        def nested_function():
            return get_context('something')
            
        with use_context(value=123):
            value = nested_function()
            self.assertEqual(None, value)
            self.assertEqual(123, get_context('value'))
        value = nested_function()
        self.assertEqual(None, value)

    def test_deep_nested(self):
        def nested_1_function():
            return get_context('something')
        
        def nested_2_function():
            return nested_1_function()
        
        def nested_3_function():
            return nested_2_function()
            
        with use_context(something=123):
            value = nested_3_function()
            self.assertEqual(123, value)
        value = nested_3_function()
        self.assertEqual(None, value)
    
    def test_double_context(self):
        def nested_1_function():
            return get_context('something')
            
        with use_context(something=456):
            with use_context(something=123):
                value = nested_1_function()
                self.assertEqual(123, value)
            value = nested_1_function()
            self.assertEqual(456, value)
        value = nested_1_function()
        self.assertEqual(None, value)
        