import setuptools

setuptools.setup(
    name='mac-slideshow',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/slideshow']
)
