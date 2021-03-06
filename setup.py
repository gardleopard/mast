from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime
from subprocess import check_output, CalledProcessError

from setuptools import setup, find_packages
from warnings import warn


def version():
    date_string = datetime.now().strftime("1.%Y%m%d.%H%M%S")
    try:
        git_sha = check_output(["git", "describe", "--always", "--dirty=dirty", "--match=NOTHING"]).strip().decode()
        return "{}+{}".format(date_string, git_sha)
    except CalledProcessError as e:
        warn("Error calling git: {}".format(e))
    return date_string

GEN_REQ = [
    "Flask==0.12.4",
    "flask-talisman==0.5.1",
    "flask-bootstrap==3.3.7.1",
    "PyYAML==3.12",
    "requests==2.13.0",
    "six==1.10.0",
    "ipaddress==1.0.18",
    "k8s==0.10.0",
    "prometheus_client == 0.3.1",
]

CODE_QUALITY_REQ = [
    "prospector",
]

CI_REQ = [
    "tox==2.7.0",
    "tox-travis==0.8",
]

TEST_REQ = [
    'mock==2.0.0',
    'pytest-sugar==0.8.0',
    'pytest==3.0.7',
    "pytest-cov==2.4.0",
    "pytest-html==1.14.2",
]

setup(
    name="fiaas-mast",
    url="https://github.com/fiaas/mast",
    maintainer="fiaas",
    maintainer_email="fiaas@googlegroups.com",
    version=version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=GEN_REQ,
    extras_require={
        "dev": ['yapf==0.16.1'] + TEST_REQ + CODE_QUALITY_REQ + CI_REQ,
        "ci": CI_REQ,
        "codacy": ["codacy-coverage"]
    },
    setup_requires=['setuptools>=17.1', 'pytest-runner', 'wheel'],
    entry_points={"console_scripts": ['fiaas-mast=fiaas_mast.__main__:main']},
)
