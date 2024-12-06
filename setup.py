from setuptools import setup, find_packages

setup(
    name='python-ds-tools',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'wxPython',
        'keyboard',
        'pandas',
        'Pillow',
        'pyautogui',
        'screeninfo'
    ],
    entry_points={
        'console_scripts': [
            'color-picker=src.tools.color_picker:create_color_picker',
            'icon-creator=src.tools.icon_creator:DnDFrame',
            'excel-cleaner=src.tools.excel_cleaner:clean_excel_file'
        ]
    },
    author='Chris Whitaker',
    author_email='your.email@example.com',
    description='A collection of tools for data science tasks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AutonomousBoxer/python-ds-tools',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
