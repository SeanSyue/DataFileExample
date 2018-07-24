from setuptools import setup

setup(
    name="Show",
    version="0.1",
    packages=['src'],
    entry_points={
        "console_scripts": [
            'show = src.show_content:run'
        ]
    },
    package_data={
        'src': ['file.txt']
    }
)
