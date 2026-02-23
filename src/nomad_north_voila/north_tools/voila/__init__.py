# Copyright 2026 NOMAD Authors
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

from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

voila_tool = NORTHTool(
    short_description='Voila application server in NOMAD NORTH for NOMAD plugin nomad-north-voila.',
    image='ghcr.io/FAIRmat-NFDI/nomad-north-voila:latest',
    description='Voila application server in NOMAD NORTH for NOMAD plugin nomad-north-voila.',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'fairmat@physik.hu-berlin.de', 'name': 'NOMAD Authors'}],
    mount_path='/home/jovyan',
    path_prefix='voila/render',
    privileged=False,
    with_path=True,
    display_name='voila',
)

north_tool_entry_point = NorthToolEntryPoint(
    id_url_safe='north_tool_voila', north_tool=voila_tool
)
