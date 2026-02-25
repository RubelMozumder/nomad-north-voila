# voila - NORTH tool

This directory contains the configuration and a minimal Dockerfile template for defining a NORTH (NOMAD Remote Tools Hub) tool.

## Quick start

The voila NORTH tool provides a Voilà-based environment defined in `NORTHTool`, a `NorthToolEntryPoint`, and a Dockerfile.

## Building and testing

Build the Docker image locally:

```bash
docker build -f src/nomad_north_voila/north_tools/voila/Dockerfile \
    -t ghcr.io/FAIRmat-NFDI/nomad-north-voila:latest .
```

Test the image (Voila server):

```bash
docker run -p 8888:8888 ghcr.io/FAIRmat-NFDI/nomad-north-voila:latest
```

Access the service at `http://localhost:8888`.

## Documentation

For comprehensive documentation on creating and managing NORTH tools, including detailed about some of the topic e.g.,

- Entry point configuration and `NORTHTool` API
- Docker image structure and best practices
- Dependency management

See the [NOMAD NORTH Tools documentation](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html).
