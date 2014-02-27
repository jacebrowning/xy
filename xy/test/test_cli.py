#!/usr/bin/env python

"""Integration tests for the doorstop.cli package."""

import unittest
from unittest.mock import patch, Mock

import os
import tempfile
import shutil

from xy.cli import main


from xy.test import ENV, REASON


@unittest.skipUnless(os.getenv(ENV), REASON)  # pylint: disable=R0904
class TestMain(unittest.TestCase):  # pylint: disable=R0904

    """Integration tests for the 'xy' command."""

    def setUp(self):
        """Run setup for each test method."""
        self.cwd = os.getcwd()
        self.temp = tempfile.mkdtemp()

    def tearDown(self):
        """Run teardown for each test method."""
        os.chdir(self.cwd)
        shutil.rmtree(self.temp)

    def test_no_args(self):
        """Verify 'xy' requires arguments."""
        self.assertRaises(SystemExit, main, [])

    @patch('xy.cli._run', Mock(return_value=False))
    def test_exit(self):
        """Verify 'xy' treats False as an error ."""
        self.assertRaises(SystemExit, main, [])

    @patch('xy.cli._run', Mock(side_effect=KeyboardInterrupt))
    def test_interrupt(self):
        """Verify 'xy' treats KeyboardInterrupt as an error."""
        self.assertRaises(SystemExit, main, [])


@unittest.skipUnless(os.getenv(ENV), REASON)  # pylint: disable=R0904
class TestNew(unittest.TestCase):  # pylint: disable=R0904

    """Integration tests for creating new files with 'xy'."""

    def setUp(self):
        """Run setup for each test method."""
        self.cwd = os.getcwd()
        self.temp = tempfile.mkdtemp()

    def tearDown(self):
        """Run teardown for each test method."""
        os.chdir(self.cwd)
        shutil.rmtree(self.temp)

    def test_new_document(self):
        """Verify 'xy' can create a new document."""
        self.assertIs(None, main(['new.docxy', '--no-open']))
        # TODO: compare output with expected

    def test_new_spreadsheet(self):
        """Verify 'xy' can create a new spreadsheet."""
        self.assertIs(None, main(['new.xlsxy', '--no-open']))
        # TODO: compare output with expected

    # TODO: add test for creating an ambiguous file 'new.xy'

    # TODO: add mock decorator to force an error
    def test_new_no_save(self):
        """Verify 'xy' doesn't create a file on error."""
        self.assertIs(None, main(['new.xlsxy', '--no-open']))
        # TODO: verify no file created

    def test_bad_format(self):
        """Verify 'xy' shows an error on unknown formats."""
        # TODO: copy sample.docx
        self.assertRaises(SystemExit, main, ['sample.docx'])


@unittest.skipUnless(os.getenv(ENV), REASON)  # pylint: disable=R0904
class TestConvert(unittest.TestCase):  # pylint: disable=R0904

    """Integration tests for converting files with 'xy'."""

    def setUp(self):
        """Run setup for each test method."""
        self.cwd = os.getcwd()
        self.temp = tempfile.mkdtemp()

    def tearDown(self):
        """Run teardown for each test method."""
        os.chdir(self.cwd)
        shutil.rmtree(self.temp)

    def test_convert_document(self):
        """Verify 'xy' can convert a document."""
        # TODO: copy input
        self.assertIs(None, main(['--convert', 'sample.docx',
                                  '--no-open']))
        # TODO: compare output with expected
        # TODO: verify the input is renamed

    def test_convert_spreadsheet(self):
        """Verify 'xy' can convert a spreadsheet."""
        # TODO: copy input
        self.assertIs(None, main(['--convert', 'sample.xlsx',
                                  '--no-open']))
        # TODO: compare output with expected
        # TODO: verify the input is renamed

    def test_convert_custom_output(self):
        """Verify 'xy' can convert a document to a specific output."""
        # TODO: copy input
        self.assertIs(None, main(['--convert', 'sample.docx',
                                  '--out', 'sample.xy',
                                  '--no-open']))
        # TODO: compare output with expected
        # TODO: verify the input is renamed


@unittest.skipUnless(os.getenv(ENV), REASON)  # pylint: disable=R0904
@patch('xy.cli._run', Mock(return_value=True))  # pylint: disable=R0904
class TestLogging(unittest.TestCase):  # pylint: disable=R0904

    """Integration tests for setting the 'xy' logging level."""

    def test_verbose_1(self):
        """Verify verbose level 1 can be set."""
        self.assertIs(None, main(['-v']))

    def test_verbose_2(self):
        """Verify verbose level 2 can be set."""
        self.assertIs(None, main(['-vv']))

    def test_verbose_3(self):
        """Verify verbose level 3 can be set."""
        self.assertIs(None, main(['-vvv']))
