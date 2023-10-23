"""
运行在服务器上
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import json

app = FastAPI()

def getPosition():
    x = 7.955
    y = 5.031
    z = 3.141
    return [x, y, z]

def getId():
    return 86767673

# 创建POST请求处理程序
@app.post("/getDronePos")
async def process_data():
    responseData = {"position": getPosition(), "id": getId()}
    jsonResponse = json.dumps(responseData)
    return JSONResponse(content=jsonResponse)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=5000) # 阻塞的
