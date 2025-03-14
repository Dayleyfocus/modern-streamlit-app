from setuptools import setup, find_packages

setup(
    name="modern-streamlit-app",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.31.0",
        "pandas>=2.1.3",
        "plotly>=5.18.0",
        "pillow>=10.1.0",
        "streamlit-extras>=0.3.5",
        "streamlit-option-menu>=0.3.6",
        "hydralit-components>=1.0.10",
    ],
) 