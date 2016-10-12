import unittest
from phpunitkit.tests.test_case import ViewTestCase
from phpunitkit.plugin import find_php_classes
from phpunitkit.plugin import contains_phpunit_test_case

class ViewHelpersTest(ViewTestCase):

    def test_find_php_classes_returns_array_of_classes_in_view(self):
        self.set_view_content('<?php\nclass x {}\nclass y {}')
        self.assertEquals(['x', 'y'], find_php_classes(self.view))

    def test_find_php_classes_returns_empty_array_when_view_is_empty(self):
        self.set_view_content('')
        self.assertEquals([], find_php_classes(self.view))

    def test_contains_phpunit_test_case_returns_true_when_view_has_test_case(self):
        self.set_view_content("<?php\nclass ExampleTest {}")
        self.assertTrue(contains_phpunit_test_case(self.view))

    def test_contains_phpunit_test_case_returns_false_when_view_has_no_test_case_classes(self):
        self.set_view_content('<?php\nclass x {}\nclass y {}')
        self.assertFalse(contains_phpunit_test_case(self.view))

    def test_contains_phpunit_test_case_returns_false_when_view_is_empty(self):
        self.set_view_content('')
        self.assertFalse(contains_phpunit_test_case(self.view))
