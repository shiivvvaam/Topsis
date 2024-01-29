
import setuptools

setuptools.setup(
    name="Topsis_Shivam_102116113",
    version="1.0.0",
    author="Shivam Dhiman",
    author_email="shivam4968@gmail.com",
    description="It Calculates Topsis Score and Rank",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/shiivvvaam/Topsis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["Topsis_Shivam_102116113"],
    include_package_data=True,
    install_requires='pandas',
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Shivam_102116113.topsis:main",
        ]
    },
)
