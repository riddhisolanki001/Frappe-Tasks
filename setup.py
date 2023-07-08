from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_tasks/__init__.py
from frappe_tasks import __version__ as version

setup(
	name="frappe_tasks",
	version=version,
	description="customizations",
	author="riddhi",
	author_email="riddhi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
