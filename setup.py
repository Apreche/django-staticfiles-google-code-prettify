from setuptools import setup, find_packages

version = '1.0'

setup(name='django-staticfiles-google-code-prettify',
        version=version,
        description="Google Code Prettify staticfiles for django",
        long_description=open("README.md", "r").read(),
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Web Environment",
            "Framework :: Django",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Topic :: Internet :: WWW/HTTP",
            ],
        keywords='',
        author='Scott Rubin',
        author_email='apreche@frontrowcrew.com',
        url='http://github.com/apreche/django-staticfiles-google-code-prettify',
        license='Apache 2.0',
        packages=find_packages(),
        install_requires = [],
        include_package_data=True,
        zip_safe=False,
    )

