from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import gas_predict, viz, airbnb_predict, tesla_predict, viz_e

app = FastAPI(
    title='RESFEBER CARTER DS API',
    description='Awesome Data Science Team',
    version='0.1',
    docs_url='/',
)

app.include_router(gas_predict.router)
app.include_router(airbnb_predict.router)
app.include_router(tesla_predict.router)
app.include_router(viz.router)
app.include_router(viz_e.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
