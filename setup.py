from setuptools import setup, find_packages

setup(
    name='skicourse_signup',
    version='0.1.1',
    description='Testing',
    author='Alexander Kuermeier',
    author_email='alexander.kuermeier@web.de',
    packages=find_packages(),
    install_requires=[
        'blinker==1.5',
        'build==0.10.0',
        'click==8.1.3',
        'Flask==2.2.2',
        'Flask-Mail==0.9.1',
        'gunicorn==20.1.0',
        'importlib-metadata==6.0.0',
        'itsdangerous==2.1.2',
        'Jinja2==3.1.2',
        'MarkupSafe==2.1.1',
        'numpy==1.24.1',
        'packaging==23.0',
        'pandas==1.5.2',
        'psycopg2-binary==2.9.5',
        'pyproject_hooks==1.0.0',
        'python-dateutil==2.8.2',
        'pytz==2022.7.1',
        'six==1.16.0',
        'tomli==2.0.1',
        'Werkzeug==2.2.2',
        'zipp==3.11.0'
    ]
)