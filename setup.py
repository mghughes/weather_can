from setuptools import setup

setup(
    name='weather_can',
    version='0.1.0',
    description='Retrieve Canadian weather forecasts.',
    url='',
    author='Matthieu Hughes',
    author_email='matthieuhughes.1@gmail.com',
    license='MIT',
    packages=['weather_can'],
    install_requires=[
        'fiona',
        'numpy',
        'requests',
        'scipy'
    ],
    zip_safe=False
)
