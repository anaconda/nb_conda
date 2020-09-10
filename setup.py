import setuptools
import versioneer

setuptools.setup(
    name="nb_conda",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url="https://github.com/Anaconda-Platform/nb_conda",
    author="Continuum Analytics",
    description="Manage your conda environments from the Jupyter Notebook",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False
)
