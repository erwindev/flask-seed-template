import sys
import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import *

app = create_app(os.getenv('ENV_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    test_result = unittest.TextTestRunner(verbosity=2).run(tests)
    sys.exit(len(test_result.failures))


@manager.command
def run_am_i_alive(customer_id, kpi_id):
    """ python application.py run_am_i_alive 123 11 """
    """ just runs a command to verify this application is runnable """
    print("I am alive! customer_id:{} kpi_id:{}".format(customer_id, kpi_id))
    sys.exit(0)

if __name__ == '__main__':
    # import profile
    # profile.run('manager.run()')
    manager.run()
