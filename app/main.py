from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="Calculator"
)


api_router = APIRouter()


@api_router.get("/calc", status_code=200)
def calculator(x:float, y:float, op:str) -> float:
    if op == 'plus':
        return x+y
    elif op == 'mult':
        return x*y


app.include_router(api_router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")