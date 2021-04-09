from os import remove, system,  walk, path
from io import IOBase, FileIO
import unittest

from ..source.rnd import rnd


class baseTest(unittest.TestCase):
    def setUp(self):
        self.path_artifact = 'code/source/artifact/'
        self.file_template_name = 'test.test'
        self.path_template = 'code/source/template/'
        self.result_path = self.path_template+self.file_template_name
        with open(self.result_path, 'w+') as file:
            file.write('Hello {{world}}')
            file.close()
        self.testrnd = rnd(self.file_template_name)
        self.vars = self.testrnd.cast_variable({'world': 'Neryungri'})
        self.template = self.testrnd.cast_template(self.file_template_name)
        self.file_result_name = 'test.result'

    def tearDown(self):
        remove(self.result_path)
        files = next(walk(self.testrnd._pathOut))
        if self.file_result_name in files[2]:
            remove(path.join(self.testrnd._pathOut, self.file_result_name))

    def test_render_file(self):
        try:
            self.testrnd.cast_file(self.file_result_name, self.vars, self.template)
            files = next(walk(self.testrnd._pathOut))
            if self.file_result_name in files[2]:
                self.assertTrue('OK')
            else:
                error_mess = f'test_render_file tro-lo-lo: not find result file {self.file_result_name}'
                self.assertFalse(error_mess)
        except Exception as err:
            error_mess = f'test_render_file tro-lo-lo ERROR: {err}'
            self.assertFalse(error_mess)

    def test_render(self):
        try:
            result_test = self.testrnd._go_render(self.vars, self.template)
            if result_test == 'Hello Neryungri':
                self.assertTrue('OK')
            else:
                error_mess = f"test_render tro-lo-lo: {result_test}"
                self.assertFalse(error_mess)
        except Exception as err:
            error_mess = f"test_render tro-lo-lo ERROR: {err}"
            self.assertFalse(error_mess)


if __name__ == '__main__':
    unittest.main()
