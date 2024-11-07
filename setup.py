from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)-> List[str]:
    '''
    this function will return the list of requirements
    '''

    #  *type 1
    # requirements = []
    # with open(file_path) as file_obj:
    #     for line in file_obj:
    #         stripped_line = line.strip()
    #         if stripped_line and stripped_line != '-e .':
    #          requirements.append(stripped_line)


    #  *type 2
    with open(file_path) as file_obj:
        # Read lines, strip newline characters, and remove any empty lines
        requirements = [line.strip() for line in file_obj if line.strip() != '-e .']


    return requirements

# * type 3
#     h='-e .'
# def get_requirements(file_path:str)-> List[str]:
#     '''
#     this function will return the list of requirements
#     '''

#     req=[]
#     with open(file_path) as file_obj:
#         req=file_obj.readlines()
#         req = [r.replace('\n',' ') for r in req]
#         if h in req:
#             req.remove(h)
#     return req;

setup(
    name="my_project",
    version="0.1.0",
    author="Rabiul Ahsan",
    author_email="rabiulahsan64@gmail.com",
    description="A brief description of the project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_project",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires= get_requirements("requirements.txt"),
    # install_requires=[
    #     "numpy",
    #     "pandas",
    #     "scikit-learn",
    # ],
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
    # entry_points={
    #     "console_scripts": [
    #         "my_command=my_project.module:main_function",
    #     ],
    # },
)
