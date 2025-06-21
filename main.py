from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.product_route import router as product_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health-check")
def health_check():
    return {"message": "Backend is running"}

app.include_router(product_router)