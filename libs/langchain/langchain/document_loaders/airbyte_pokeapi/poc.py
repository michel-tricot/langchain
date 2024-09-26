from airbyte_embed_cdk.tools import parse_json
from config import PokeApiConfig

from langchain.document_loaders.airbyte_pokeapi import AirbytePokeApiLoader, AirbytePokeApiContainerLoader


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
    reader = AirbytePokeApiContainerLoader(config=config, stream="pokemon", version="0.1.5-dev.819dd97d48")
    print(reader.load_data())


if __name__ == "__main__":
    main()
