from react_context import get_context, create_context, debug_context
from unittest import TestCase
import pytest
import asyncio
from aiounittest import AsyncTestCase

class UseContextTest(TestCase):

    def test_simple_context(self):
        def nested_function():
            return get_context('something')
        with create_context(something=123):
            value = nested_function()
            self.assertEqual(123, value)
        value = nested_function()
        self.assertEqual(None, value)
    
    def test_missing_value(self):
        def nested_function():
            return get_context('something')
            
        with create_context(value=123):
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
            
        with create_context(something=123):
            value = nested_3_function()
            self.assertEqual(123, value)
        value = nested_3_function()
        self.assertEqual(None, value)
    
    def test_default_context(self):
        def nested_1_function():
            return get_context('something', 'default_value')
            
        with create_context(something=456):
            value = nested_1_function()
            self.assertEqual(456, value)
        value = nested_1_function()
        self.assertEqual('default_value', value)

class DebugContextTest(TestCase):

    @pytest.fixture(autouse=True)
    def capfd(self, capfd):
        self.capfd = capfd

    def test_deep_nested(self):
        
        def nested_1_function():
            return debug_context('something')
        
        def nested_2_function():
            return nested_1_function()
        
        def nested_3_function():
            return nested_2_function()
            
        with create_context(something=123):
            value = nested_3_function()
            
        value = nested_3_function()

        out, err = self.capfd.readouterr()
        self.assertRegex(
            out,
            r"- test_deep_nested <- Found context value defined here"
        )
