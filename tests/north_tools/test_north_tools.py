def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from nomad_north_voila.north_tools.voila import (
        north_tool_entry_point,
    )

    assert (
        north_tool_entry_point.id_url_safe == 'north_tool_voila'
        or north_tool_entry_point.id == 'nomad-north-voila'
    ), 'NORTHtool entry point has incorrect id or id_url_safe'
