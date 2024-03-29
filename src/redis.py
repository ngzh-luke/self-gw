""" Redis related """
# Adapted from https://github.com/zhanymkanov/fastapi_production_template/blob/main/src/redis.py

from datetime import timedelta
from typing import Optional
from redis.asyncio import Redis
from .models import CustomModel
import config

try:
    r = Redis(
        host=config.REDISHOST, port=config.REDISPORT,
        # use your Redis user. More info https://redis.io/docs/management/security/acl/
        username=config.REDISUSER,
        password=config.REDISPASSWORD,  # use your Redis password
        decode_responses=True
    )
except ConnectionError:
    r = Redis(host='localhost', port=6379, decode_responses=True)
except Exception as e:
    print("Redis connection failed")
    exit(code=1)


redisClient: Redis = Redis  # type: ignore


class RedisCustomBase(CustomModel):
    """ Base model for Redis """
    key: bytes | str
    value: bytes | str
    ttl: Optional[int | timedelta] = None


class RedisStrings(RedisCustomBase):
    """ Redis strings data type """
    key: str


class RedisLists(RedisCustomBase):
    """ Redis lists data type """
    key: str
    value: list


class RedisHashes(RedisCustomBase):
    """ Redis hashes data type """
    key: str
    value: dict


async def set(redis_data: RedisStrings | RedisLists | RedisHashes, *, is_transaction: bool = False) -> None:
    async with redisClient.pipeline(transaction=is_transaction) as pipe:
        await pipe.set(redis_data.key, redis_data.value)
        if redis_data.ttl:
            await pipe.expire(redis_data.key, redis_data.ttl)

        await pipe.execute()


async def getByKey(key: str) -> Optional[str]:
    return await redisClient.get(key)


async def deleteByKey(key: str) -> None:
    return await redisClient.delete(key)
