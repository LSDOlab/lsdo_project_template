from setuptools import setup, find_packages

setup(
    name='lsdo_project_template',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pytest',
        'myst-nb',
        'sphinx_rtd_theme',
        # 'sphinx-collections',
        'sphinx-collections @ git+https://github.com/anugrahjo/sphinx-collections.git'
#         'scipy',
#         'pint',
#         'sphinx-rtd-theme',
#         'sphinx-code-include',
#         'jupyter-sphinx',
#         'numpydoc',
    ],
)
