'''


from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands."""
    def test_wait_for_db_ready(self,patched_check):
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_once_with(database='default')'''
        
from unittest.mock import patch
from django.core.management import call_command
from django.test import SimpleTestCase


class CommandTests(SimpleTestCase):
    """Test wait_for_db command."""

    @patch('django.db.utils.ConnectionHandler.__getitem__')
    def test_wait_for_db_ready(self, mock_getitem):
        """Test waiting for db when db is available."""
        mock_getitem.return_value = True
        call_command('wait_for_db')
        mock_getitem.assert_called_with('default')