from setuptools import setup, find_packages

setup(
    name='fast_glcm',
    description='fast grey-level co-occurrence matrix calculations',
    author='lafa',
    author_email='lfa027@uit.no',
    packages=find_packages(),
    python_requires='>=3.8',
    use_scm_version=[],
    setup_requires=[
        'numpy',
        'matplotlib'
    ],
    install_requires=[]
)
