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
    users_data: List[dict] = []
    result = await fetch_json_go(USERS_DATA_URL)
    for user1 in result:
        user_for_dict = dict({
            "user_id": user1.get('id'),
            "username": user1.get('username'),
            "name": user1.get('name'),
            "email": user1.get('email'),
            "db_user_id": user1.get('id')
            }
        )
        users_data.append(user_for_dict)

    return users_data


async def fetch_post_data() -> list:
    posts_data: List[dict] = []
    result = await fetch_json_go(POSTS_DATA_URL)
    for post1 in result:
        post_for_dict = dict({
            "user_id": post1.get('userId'),
            "title": post1.get('title'),
            "body": post1.get('body')
            }
        )
        posts_data.append(post_for_dict)

    return posts_data


async def get_userid_from_username(username: String):
    stmt = select(User).where(User.username == username)
    result = await Session.execute(stmt)
    user = result.scalar_one_or_none()
    if user is None:
        return 0
    else:
        return user.id


async def create_many_users(users_data: List[dict]):
    users_list: List[User] = []
    for el in users_data:
        username: String = el.get('username')
        new_us_id: Integer = await get_userid_from_username(username)

        if new_us_id == 0:
            users_list.append(
                User(username=el.get('username'),
                     email=el.get('email'),
                     name=el.get('name')
                     )
            )
    if len(users_list) > 0:
        async with async_session_factory() as db_session:
            async with db_session.begin():
                db_session.add_all(users_list)

    return print('!End create_many_users')


async def create_many_posts(users_data: List[dict], posts_data: List[dict]):
    posts_list: List[Post] = []
    # для каждого словаря (user) из списка users_data
    # по ключу user_id (=id загрузки) определяем username,
    # по ранее загруженной в схему таблице находим по username (уникальный)
    # новое значение ключа ID присвоенное при добавлении записи в таблицу БД

    for us1 in users_data:
        us_id: Integer = us1.get('user_id')
        username: String = us1.get('username')
        new_us_id: Integer = await get_userid_from_username(username)

        if new_us_id > 0:
            for el in posts_data:
                if el.get('user_id') == us_id:
                    posts_list.append(
                        Post(
                             title=el.get('title'),
                             body=el.get('body'),
                             user_id=new_us_id,
                             )
                    )
    if len(posts_list) > 0:
        async with async_session_factory() as db_session:
            async with db_session.begin():
                db_session.add_all(posts_list)

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
    await create_many_posts(users_data, posts_data)


def main():
    # вариант 1: asyncio.run()
    #asyncio.run(async_main())

    # вариант 2 : получаем текущий цикл событий
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())


if __name__ == "__main__":
    main()
