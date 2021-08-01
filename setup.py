from setuptools import find_packages, setup
import togglefield

setup_requires = [
    "wheel",
]

def read_file(path: str):
    with open(path, "r") as file:
        return file.read()

setup(
    name="togglefield",
    version=togglefield.__version__,
    url=togglefield.__url__,
    description=togglefield.__doc__,
    author=togglefield.__author__,
    author_email=togglefield.__email__,
    license=togglefield.__license__,
    platforms="any",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    packages=find_packages(),
    package_data={'':['*.html', '*.js', '*.css']},
    include_package_data=True,
    install_requires=read_file("requirements.txt").splitlines(),
)