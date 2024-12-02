from fastapi import FastAPI

app = FastAPI()

@app.get("/", description="This is Our First Route!!")
async def root():
    return {"message": "hello world!!"}

@app.post("/")
async def post_req():
    return {"message":"Hi this is from Post Method!!"}

@app.put("/")
async def put_req():
    return {"message" : "Hi this is from Put Method!!"}