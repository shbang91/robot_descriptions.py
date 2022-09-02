#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Simple Humanoid description.
"""

from os import path as _path

from ._cache import clone_to_cache as _clone_to_cache

PATH: str = _clone_to_cache("simple_humanoid_description")

MESHES_PATH: str = ""

URDF_PATH: str = _path.join(PATH, "urdf", "simple_humanoid.urdf")

URDF_PATH_CLASSICAL: str = _path.join(
    PATH, "urdf", "simple_humanoid_classical.urdf"
)