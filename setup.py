import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_chatfuel_class",
    version="2.1.3",
    author="Peter Dinh",
    license="BSD 3-Clause",
    keywords = "Package for Chatfuel",
    author_email="peterdinh018@gmail.com",
    description=" Python Wrapper for JSON API Chatfuel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=['urllib3'],
    url="https://github.com/peter-dinh/class-chatfuel-python",
    packages=['python_chatfuel_class'],
    classifiers=(
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
