import logging
from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str

@dataclass
class LogConfig:
    level: int
    format: str

@dataclass
class Config:
    bot: TgBot
    log: LogConfig
    
def get_config():
    env = Env()
    return Config(
        bot=TgBot(token=env('BOT_TOKEN')),
        log=LogConfig(
            level=getattr(logging,env('LOG_LEVEL')),
            format=env('LOG_FORMAT'),
        )
    )