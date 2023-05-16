import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-priority-queue",
    version="1.0.0",
    author="Alonso Benavente Fortes",
    author_email="alonsobenavente@gmail.com",
    description="A simple priority queue library and GUI application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abenaventefortes/simple_priority_queue.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "PyQt5==5.15.9",
    ],
    entry_points={
        "console_scripts": [
            "simple_priority_queue=simple_priority_queue.__main__:main",
            "simple_priority_queue_cli=simple_priority_queue.cli:main_cli",
            "simple_priority_queue_gui=simple_priority_queue.gui:main_gui"
        ]
    }
)
