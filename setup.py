# Copyright 2021 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This file is used to build a Python package that can then by used by
Google Cloud Dataflow workers (Apache Beam).

The package is built by running 'python setup.py sdist' in the build.py.
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import pkg_resources
import setuptools

# Configure the required packages and scripts to install.
with open('requirements.txt', encoding='utf-8') as requirements_txt: # pylint: disable=replace-disallowed-function-calls
    # The 'parse_requirements' returns a list of 'Requirement' objects.
    # We need to transform these to strings using the str() function.
    REQUIRED_PACKAGES = [
        str(requirement)  # pylint: disable=replace-disallowed-function-calls
        for requirement in pkg_resources.parse_requirements(requirements_txt)
    ]

setuptools.setup(
    name='oppia-beam-job',
    version='0.0.1',
    description='Oppia Apache Beam package',
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
    include_package_data=True,
)
