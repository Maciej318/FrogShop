from setuptools import setup

# Pakiet Frog
setup(
    name="Frog",
    version="0.0.1",
    packages=["Frog"],
    description="Frog package for customers and products",
    include_package_data=True,
    url="https://github.com/Maciej318/FrogShop.git",
    author="Maciej318 , stanislawchociej , lybsoon",
    license="MIT",
    zip_safe= True,
    install_requires=["pandas", "openpyxl","pillow"],
)