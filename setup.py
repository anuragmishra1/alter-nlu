from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
import subprocess


def post_install():
    print("> Downloading Spacy English Model")
    subprocess.run("python -m spacy download en", shell=True)
    print("==========Download Finished!==========")


class custom_install(install):
    def run(self):
        print('In Custom_Install')
        install.do_egg_install(self)
        self.execute(post_install, [], msg='Running post_install Task!')


class custom_develop(develop):
    def run(self):
        develop.do_egg_install(self)
        self.execute(post_install, [], msg='Running post_install Task!')


setup(
    name='ALTER NLU',
    version='1.0.0',
    packages=[],
    url='',
    license='',
    author='Kontiki AI',
    author_email='',
    include_package_data=True,
    zip_safe=True,
    package_data = {
        # Include any *.conf files found in the 'conf' subdirectory
        # for the package
    },
    cmdclass={'install': custom_install, 'develop': custom_develop},
    install_requires=[
        'pandas==0.23.4',
        'spacy==2.1.3',
        'numpy==1.15.4',
        'jsonschema==2.6.0',
        'flashtext==2.7',
        'Flask==0.12.4',
        'nltk==3.3',
        'scikit_learn==0.20.1',
        'tensorflow==1.12.0',
        'fuzzywuzzy==0.17.0',
        'python-Levenshtein==0.12.0'
        ],
    description=''
)
