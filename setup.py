from setuptools import setup
setup(
      name='Raid',
      version='0.1',
      description="Simple HTTP's requests generator",
      author='Jose Vidal',
      author_email='javidgon[at]gmail.com',
      url='https://github.com/javidgon/raid',
      packages=['raid'],
      license='BSD',
      long_description=open('README.md').read(),
      install_requires=["requests","unittest2"],
      scripts=['raid/raid.py', 'raid/worker.py', 'raid/utils.py',
               'raid/run_tests.py'],
)
