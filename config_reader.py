from environs import Env

env = Env()
env.read_env()

USERNAME: str = env.str("USERNAME")
PASSWORD: str = env.str("PASSWORD")
HOST: str = env.str("HOST")
PORT: str = env.str("PORT")
DB_NAME: str = env.str("DB_NAME")
