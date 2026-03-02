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

voila = NORTHTool(
    short_description='voilà, a Jupyter extension, in NOMAD NORTH integrated by NOMAD plugin nomad-north-voila.',
    image='ghcr.io/fairmat-nfdi/nomad-north-voila:ANONYMOUS_TAG',
    description="""### **Voilà**:
        [Render Jupyter notebooks as standalone web applications](https://github.com/voila-dashboards/voila)""",
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='https://github.com/FAIRmat-NFDI/nomad-north-voila/blob/main/src/nomad_north_voila/north_tools/voila/voila.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'fairmat@physik.hu-berlin.de', 'name': 'NOMAD Authors'}],
    mount_path='/home/jovyan',
    path_prefix='voila/render',
    privileged=False,
    with_path=True,
    display_name='voilà',
)

north_tool_entry_point = NorthToolEntryPoint(
    id_url_safe='north_tool_voila', north_tool=voila
)
