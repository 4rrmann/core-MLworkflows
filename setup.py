from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
#this function will return the list of requirements
def get_requirements(file_path:str) -> List[str]:
    requirements=[]

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
name='end2end mlProject',
version='0.0.1',
author='4rrmann',
author_email='kunzairen@gmail.com',
packages=find_packages(),
install_requirements=get_requirements('requirements.txt')

)