import os

from apps import create_app

if __name__ == '__main__':
    app = create_app()
    app.config.from_object('settings.{}'.format(os.getenv('FLASK_ENV', 'development')))
    app.run(use_reloader=False)
