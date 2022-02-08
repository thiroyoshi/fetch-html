from setuptools import setup

setup(
    install_requires=["requests", "beautifulsoup4"],
    entry_points={
        "console_scripts": [
            "fetch = app:main"
        ]
    }
)