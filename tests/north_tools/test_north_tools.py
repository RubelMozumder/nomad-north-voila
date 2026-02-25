def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from nomad_north_voila.north_tools.voila_north_tool import (
        north_tool_entry_point,
    )

    assert (
        north_tool_entry_point.id_url_safe == 'voila_north_tool'
        or north_tool_entry_point.id_url_safe == 'nomad-north-nomad-north-voila'
    ), 'NORTHtool entry point has incorrect id or id_url_safe'
