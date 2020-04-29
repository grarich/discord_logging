import setuptools  

with open("README.md", "r", encoding="utf-8") as fh:  
    long_description = fh.read()  

setuptools.setup(  
    name="discord_logging",  
    version="1.0",  
    author="grarich",  
    author_email="grarich123+github@gmail.com",  
    description="Transfer logs acquired by logging module to discord with webhook!",  
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    url="https://github.com/grarich123/discord_logging",  
    packages=setuptools.find_packages(),  
    classifiers=[  
        "Programming Language :: Python :: 3.8",  
        "License :: OSI Approved :: MIT License",  
        "Operating System :: OS Independent",  
    ],  
)  
