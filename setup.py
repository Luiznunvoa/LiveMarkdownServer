from setuptools import setup, find_packages

setup(
    name="live-markdown-server",
    version="1.0.0",
    description="A simple live Markdown preview server",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Luiz Gabriel",
    author_email="luizgpinheiro0905@gmail.com",
    url="https://github.com/Luiznunvoa/LiveMarkdownServer",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "markdown",
    ],
    entry_points={
        "console_scripts": [
            "live-markdown=live_markdown_server.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

