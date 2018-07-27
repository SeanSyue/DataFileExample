from setuptools import setup

setup(
    name='test-import-module',
    version='0.1.0',
    author='seansyue',

    packages=['', 'src'],
    package_data={
        "src": ['rice_menu.txt', 'noodle_menu.txt', 'menu_gui.ui']
    },
    entry_points={
        "console_scripts": ['foo = src.import_demo:run']
    },
)
