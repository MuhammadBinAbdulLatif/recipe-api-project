"""
Django command for the database to be available
"""

from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycog2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django Command to wait for the database"""
    def handle(self, *args, **options):
        """Entrypoint for the command"""
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                # check if database is available
                self.check(databases=['default'])
                db_up = True
            except (Psycog2Error, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
