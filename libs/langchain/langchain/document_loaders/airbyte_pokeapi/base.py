from airbyte_embed_cdk.integrations.langchain import container_airbyte_langchain_loader, cdk_airbyte_langchain_loader
from source_pokeapi import SourcePokeapi

AirbytePokeApiContainerLoader = container_airbyte_langchain_loader(
    "airbyte/source-pokeapi",
    "0.1.5-dev.819dd97d48")

AirbytePokeApiLoader = cdk_airbyte_langchain_loader(SourcePokeapi)
