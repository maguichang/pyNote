# -*- coding:utf-8 -*-
# @Time :2019/11/7 16:31
# Author :MaGuichang

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="pyApp",
    version="0.0.1",
    author="maguichang",
    author_email="maguichang@unicloud.com",
    description="python 完整项目结构示例",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)