from setuptools import setup, find_namespace_packages

setup(
    name='QualityOfLifeAPI',
    version='0.2.1',
    packages=find_namespace_packages(include=['quality_of_life', 'quality_of_life.*'],
                                     exclude=['quality_of_life.quality_of_life.*']),
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
                      'uvicorn~=0.16.0'
                      ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'quality_of_life = quality_of_life.main:main',
        ],
    },
)
