from setuptools import setup

setup(
    name='QualityOfLifeAPI',
    version='0.1.0',
    packages=['api', 'api.endpoints', 'repo', 'domain'],
    package_dir={'': '../quality_of_life'},
    url='https://github.com/MaciejZawierzeniec/Quality_of_life_API',
    license='',
    author='Maciej',
    author_email='mzawierzeniec@gmail.com',
    description='API for the quality_of_life dataset results',
    install_requires=['fastapi~=0.70.1',
                      'pandas~=1.3.5',
                      'geopy~=2.2.0',
                      'OSMPythonTools~=0.3.3',
                      'requests~=2.26.0',
                      ],
)
