from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
readme = (this_directory / "README.md").read_text()


setup(
    name='TMKTPostgresql',
    license='Apache 2.0',
    version='',
    python_requires='~=3.10',
    author="Tanguy Ladet",
    maintainer="Tanguy Ladet",
    maintainer_email='sti2dlab.ladettanguy@gmail.com',
    author_email='sti2dlab.ladettanguy@gmail.com',
    packages=find_packages(include=['tmktpostgresql.*']),
    url='https://github.com/ladettanguy/TMKTPostgresql',
    download_url='https://github.com/ladettanguy/TMKTPostgresql.git',
    install_requires=[
        "psycopg2 ~=2.9.6",
    ],
    keywords=[
        'Postgres',
        'ORM',
        'Postgresql',
        "Database",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
    ],
    description="Easyfull postgresql connector.",
    long_description=readme,
    long_description_content_type='text/markdown',
    zip_safe=False,
)
