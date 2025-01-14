from setuptools import setup, find_packages


setup(
    name="django-channels-utils",
    version="0.2.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        "django-channels"
    ],
    entry_points={
        "console_sripts": [
            
        ]
    },
    author="setsudo",
    author_email="sergiusz.cudo@outlook.com",
    description="This is a package to improve django-channels functionality",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cds88/django-channels-utils",
    classifiers =[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">3.6",
    
    
    
)