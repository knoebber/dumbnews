from setuptools import setup, find_packages

setup(
    name='dumbnews',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
