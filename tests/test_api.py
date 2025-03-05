import pytest
from httpx import AsyncClient, ASGITransport


from less.lesson2 import app

@pytest.mark.asyncio
async def test_get_books():
    async with AsyncClient(transport=ASGITransport(app=app)) as ac:
        res = await ac.get('/books')
        print(res)















#def func(num: int):
#    return 1 / num
#
#
#
#def test_func():
#    assert func(1) == 1
#    assert func(2) == 0.5
#
#
#
#
# pytest -v команда для теста, pytest сам найдет тесты 