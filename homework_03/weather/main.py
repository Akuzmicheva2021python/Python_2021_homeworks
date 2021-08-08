from typing import Optional

import uvicorn
from fastapi import FastAPI, Path

import work_runner as work_runner
from models import MyException, Config, Index

app = FastAPI(title='Bank of Russia information',
              description='My application running on FastAPI + uvicorn',
              version='0.0.1')


@app.get("/ping/", status_code=200)
def get_default(name: Optional[str] = None):
    if name:
        return {"message": f"Hi, "+name+" !"}
    return {"message": "pong"}


@app.get("/{index}", status_code=200)
async def get_result(index: Index = Path(..., title="The name of the Index"),
                     dt_start: str = '26.07.2021',
                     dt_finish: str = '02.08.2021'):
    config1 = Config(index=index)

    try:
        result = await work_runner.run(config1, dt_start, dt_finish)
        return result

    except Exception as e:
        raise MyException(e)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
