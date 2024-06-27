from setuptools import setup, find_packages

setup(
    name='file_organizer_tool',
    version='0.1.0',
    description='A simple tool to organize files in directories based on their extensions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Albert Mwasisoba',
    author_email='almwassy@gmail.com',
    url='https://github.com/albizzy/file_organizer',  # Update with your actual URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'file-organizer-tool=file_organizer_tool.organizer:main',
        ],
    },
)
