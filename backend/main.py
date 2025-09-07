from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()

# Test route
@app.get("/")
def read_root():
    return {"message": "Backend is running 🚀"}
