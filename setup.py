from setuptools import find_packages, setup
from typing import List

e = "-e ."
def get_requirements(file_path: str) -> List[str]:
    '''
    Returns the list of requirements
    '''
    reqs = []
    with open(file_path) as f:
        reqs = f.readlines()
        reqs = [r.replace("\n", "") for r in reqs]
        if e in reqs: reqs.remove(e)
    return reqs

setup(
    name = 'MLProj', 
    version = '0.0.1',
    author = 'Gopal',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
