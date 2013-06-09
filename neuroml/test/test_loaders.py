"""
Unit tests for loaders

"""

import neuroml
from neuroml import loaders
import os

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class TestNeuroMLLoader(unittest.TestCase):
    def test_load_neuroml(self):
        path =  neuroml.__path__
        test_file_path=os.path.join(path,'Purk2M9s.nml')
        doc = loaders.NeuroMLLoader.load(test_file_path)
        self.assertEqual(doc.id,'Purk2M9s')
