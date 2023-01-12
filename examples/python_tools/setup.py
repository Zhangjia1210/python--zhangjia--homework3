from setuptools import find_packages, setup

setup(
    name='projectname',
    version='0.0.1',
    install_requires=[
        'requests >= 2.0.0',
        'flask >= 2.0.0; python_version == "3.10"',
    ],
    packages=find_packages(
        where='.',  
        include=['projectname*'], 
        exclude=['tests'],  
    ),
    entry_points={
        'console_scripts': [
            'mul = projectname.mul:main',
        ]
    }
)