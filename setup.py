from setuptools import find_packages, setup

setup(
    name="trial",
    author="ueki-ssr",
    author_email="",
    package_dir={"": "src"},
    install_requires=[
        "scikit-learn~=1.0.1",
        "pandas~=1.3.4",
        "sktime~=0.8.1",
    ],
    packages=find_packages(where="src"),
    python_requires=">=3.8,<4.0",
    setup_requires=["setuptools_scm"],
    use_scm_version={"version_scheme": "python-simplified-semver"},
)