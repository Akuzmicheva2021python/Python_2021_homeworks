"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
from typing import List
from sqlalchemy import select

from jsonplaceholder_requests import *
from models import *


async def fetch_users_data() -> list:
    users_data: List[User] = []
    result = await fetch_json_go(USERS_DATA_URL)
    for el in result:
        us1 = User(
                username=el.get('username'),
                email=el.get('email'),
                name=el.get('name')
                )
        us1.id = el.get('id')
        users_data.append(us1)

    return users_data


async def fetch_post_data() -> list:
    posts_data: List[Post] = []
    result = await fetch_json_go(POSTS_DATA_URL)
    for el in result:
        posts_data.append(
            Post(
                title=el.get('title'),
                body=el.get('body'),
                user_id=el.get('userId')
            )
        )

    return posts_data


# async def get_userid_from_username(username: String):
#     stmt = select(User).where(User.username == username)
#     result = await Session.execute(stmt)
#     user = result.scalar_one_or_none()
#     if user is None:
#         return 0
#     else:
#         return user.id


async def create_many_users(users_data: List[User]):
    if len(users_data) > 0:
        async with async_session_factory() as db_session:
            async with db_session.begin():
                db_session.add_all(users_data)

    return print('!End create_many_users')


async def create_many_posts(posts_data: List[Post]):

    if len(posts_data) > 0:
        async with async_session_factory() as db_session:
            async with db_session.begin():
                db_session.add_all(posts_data)

    return print('!End create_many_posts')


async def async_create():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await engine.dispose()


async def async_main():
    await async_create()
    users_data, posts_data = await asyncio.gather(fetch_users_data(), fetch_post_data())
    await create_many_users(users_data)
    await create_many_posts(posts_data)


def main():
    # вариант 1: asyncio.run()
    #asyncio.run(async_main())

    # вариант 2 : получаем текущий цикл событий
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())


if __name__ == "__main__":
    main()
