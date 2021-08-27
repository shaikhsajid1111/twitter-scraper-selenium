import setuptools

with open("README.MD", "r") as file:
    long_description = file.read()

requirements = []

for line in open("requirements.txt", 'r', encoding="utf-8").readlines():
  requirements.append(line.replace("\n", ""))

setuptools.setup(
    name="facebook_page_scraper",
    version="0.1.0",
    author="Sajid Shaikh",
    author_email="shaikhsajid3732@gmail.com",
    description="Python package to scrap twitter's front-end easily with selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/shaikhsajid1111/twitter-scraper-selenium",
    keywords="web-scraping selenium social media twitter keyword twitter-profile twitter-keywords automation json csv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP"

    ],
    python_requires=">=3.6",
    install_requires=requirements
)
