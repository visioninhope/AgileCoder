from setuptools import setup, find_packages
setup(name='agilecoder',
version='0.1.9',
description='AgileCoder',
url='https://github.com/FSoft-AI4Code/AgileCoder',
author='FSoft-AI4Code',
author_email='support.aic@fpt.com',
license='Apache-2.0',
python_requires=">=3.8",
include_package_data=True,
package_data={"agilecoder": ["CompanyConfig/*/*.json"]},
entry_points={
        'console_scripts': ['agilecoder=agilecoder:main'],
},
install_requires=[
        "openai==0.28.1",
        "tiktoken==0.6.0",
        "markdown==3.5.2",
        "colorama",
        "nltk==3.8.1",
        "flask",
        "tenacity==8.2.3",
        "python-dotenv",
        "codebleu==0.7.0",
        "google-auth",
        "google-auth-oauthlib",
        "google-auth-httplib2",
        "anthropic",
        "pygame",
        "numpy",
        "tree-sitter",
        "tree-sitter-python @ git+https://github.com/tree-sitter/tree-sitter-python.git@master"
      ],
packages=find_packages(),
zip_safe=False)