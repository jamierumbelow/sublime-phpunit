from unittest import TestCase

from sublime import find_resources
from sublime import active_window


class ViewTestCase(TestCase):

    def setUp(self):
        self.view = active_window().create_output_panel(
            'phpunit_test_view',
            unlisted=True
        )
        self.view.set_scratch(True)
        self.view.settings().set('auto_indent', False)
        self.view.settings().set('indent_to_bracket', False)
        self.view.settings().set('tab_size', 4)
        self.view.settings().set('trim_automatic_white_space', False)
        self.view.settings().set('smart_indent', True)
        self.view.settings().set('tab_size', 4)
        self.view.settings().set('translate_tabs_to_spaces', True)
        self.view.set_syntax_file(find_resources('PHP.sublime-syntax')[0])

    def tearDown(self):
        if self.view:
            self.view.close()

    def fixture(self, text):
        self.view.run_command('phpunit_test_setup_fixture', {'text': text})
