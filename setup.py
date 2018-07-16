import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_chatfuel_class",
    version="2.1.1",
    author="Peter Dinh",
    author_email="peterdinh018@gmail.com",
    description=" Python Wrapper for JSON API Chatfuel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=['urllib3'],
    url="https://github.com/peter-dinh/class-chatfuel-python",
    packages=['python_chatfuel_class'],
    classifiers=(
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
