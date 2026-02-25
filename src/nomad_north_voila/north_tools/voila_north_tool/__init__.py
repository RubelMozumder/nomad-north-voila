from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

voila_north_tool = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-voila.',
    image='ghcr.io/FAIRmat-NFDI/nomad-north-voila:latest',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-voila.',
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
    id_url_safe='voila_north_tool', north_tool=voila_north_tool
)
