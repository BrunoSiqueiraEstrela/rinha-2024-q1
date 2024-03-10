import os
from pathlib import Path
from typing import Optional, Final

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


def get_env_file_path() -> Optional[str]:
    return [
        *Path().absolute().glob("**/*.env"),
    ]


if len(get_env_file_path()) == 0:
    raise Exception("ENV_DIR não encontrado")

primeiro_em_fila = get_env_file_path()[0]
ENV_DIR = primeiro_em_fila


DIR_ENV: Path = Path(ENV_DIR)
# / ".env"

if ENV_DIR is None:
    raise Exception("ENV_DIR não encontrado")

print(f"Carregando env do diretorio: {DIR_ENV}")
x = get_env_file_path()


class GerenciadorENV(BaseSettings):
    _instance = None

    model_config = SettingsConfigDict(env_file=get_env_file_path()[0])

    # BANCO DE DADOS
    DB_CONNECTION: Final[str] = Field(env="DB_CONNECTION")
    DB_HOST: Final[str] = Field(env="DB_HOST")
    DB_PORT: Final[str] = Field(env="DB_PORT")
    DB_USER: Final[str] = Field(env="DB_USER")
    DB_PASSWORD: Final[str] = Field(env="DB_PASSWORD")
    DB_DATABASE: Final[str] = Field(env="DB_DATABASE")

    # VIRTUAIS
    @property
    def DB_STRING_CONNECTION(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"

    @property
    def RAIZ_PROJETO_PATH(self):
        return Path(self.RAIZ_PROJETO)

    def print(self):
        print("-" * 95)
        for key, value in self.dict().items():
            print(f" - ENV: {key}: {value}")
        print("-" * 95)

    def forcar_envs_no_ambiente(self, print_env: bool = False):
        if print_env:
            print("ENVs: FORÇANDO - INICIO")
            self.print()
            print("ENVs: FORÇANDO - FIM")

        for key, value in self.dict().items():
            if value is not None:
                os.environ[key] = str(value)


env = GerenciadorENV()
