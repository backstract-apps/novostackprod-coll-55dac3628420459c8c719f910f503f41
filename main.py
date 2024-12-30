from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - novostackprod-coll-55dac3628420459c8c719f910f503f41',debug=False,docs_url='/reverent-benz-bc5bd420c51911efb2e60242ac12000572/docs',openapi_url='/reverent-benz-bc5bd420c51911efb2e60242ac12000572/openapi.json')

app.include_router(router, prefix='/reverent-benz-bc5bd420c51911efb2e60242ac12000572/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()