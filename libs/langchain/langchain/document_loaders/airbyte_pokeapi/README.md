# Airbyte Pokeapi Loader

The Airbyte Pokeapi Loader allows you to access different Pokeapi objects.

## Usage

```python
from airbyte_embed_cdk.tools import parse_json

from langchain.document_loaders.airbyte_pokeapi import AirbytePokeApiLoader, AirbytePokeApiContainerLoader, PokeApiConfig


def main():
    config = parse_json('{ "pokemon_name": "ditto" }')

    # using package
    reader = AirbytePokeApiLoader(config=config, stream="pokemon")
    print(reader.load_data())

    # using package & config object
    config = PokeApiConfig(pokemon_name="ditto")
    reader = AirbytePokeApiLoader(config=config, stream="pokemon")
    print(reader.load_data())

    # show all available streams
    print(reader.available_streams())

    # using image
    reader = AirbytePokeApiContainerLoader(config=config, stream="pokemon")
    print(reader.load_data())

    # using image & config object
    config = PokeApiConfig(pokemon_name="ditto")
    reader = AirbytePokeApiContainerLoader(config=config, stream="pokemon")
    print(reader.load_data())

    # use specific image version
    reader = AirbytePokeApiContainerLoader(config=config, version="0.1.5-dev.819dd97d48")
    print(reader.load_data('pokemon'))

main()
```

## Field notes

Right now I can't get it to work because of the pydantic deps conflict.

```shell
# Generate config object
(
    rm -rf .genenv && virtualenv .genenv && . .genenv/bin/activate
    pip install datamodel-code-generator==0.17.1
    docker run --rm -it airbyte/source-pokeapi:0.1.5-dev.819dd97d48 spec | jq '.spec.connectionSpecification' > spec.json
    datamodel-codegen --input spec.json --input-file-type jsonschema --disable-timestamp --allow-extra-fields --class-name PokeApiConfig --output config.py
)
```
