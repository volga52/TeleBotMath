import ipaddress
import pathlib
from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    # Желательно вместо str использовать SecretStr
    # для конфиденциальных данных, например, токена бота
    bot_container_name: str = 'bot_container_name'
    bot_image_name: str = 'botimage_name'
    bot_name: str
    bot_token: SecretStr
    admins: list
    use_redis: bool

    db_user: str = 'volga52'
    pg_password: SecretStr = 'examplePostgresPass'
    db_pass: SecretStr = 'pg_password'
    db_name: str
    db_host: ipaddress.IPv4Address

    # Вложенный класс с дополнительными указаниями для настроек
    class Config:
        # Имя файла, откуда будут прочитаны данные
        # (относительно текущей рабочей директории)
        # env_file = '.env'
        # env_file = f"{pathlib.Path(__file__).resolve().parent}/.env"
        # env_file = f"{pathlib.Path(__file__).resolve().parent.parent.parent}/.env"
        env_file = ["/etc/secrets/.env",
                    f"{pathlib.Path(__file__).resolve().parent}/.env",
                    f"{pathlib.Path(__file__).resolve().parent.parent}/.env"]
        # print(env_file)
        # Кодировка читаемого файла
        env_file_encoding = 'utf-8'
