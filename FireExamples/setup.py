from setuptools import setup

setup(
    name="Show",
    version="0.1",
    packages=[''],
    entry_points={
        "console_scripts": [
            'show = show_content:run_cli'
        ]
    }
)
