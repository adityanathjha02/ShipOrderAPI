from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "Server is running", "status": "healthy", "port": os.getenv("PORT")}

@app.get("/env")
def check_env():
    return {
        "MONGODB_URI": bool(os.getenv("MONGODB_URI")),
        "DB_NAME": os.getenv("DB_NAME"),
        "PORT": os.getenv("PORT")
    }

@app.get("/test-import")
def test_import():
    try:
        from models import Product, Order
        return {"models_import": "success"}
    except Exception as e:
        return {"models_import": "failed", "error": str(e)}

# DO NOT import at module level yet

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8000))
    print(f"=== Starting server on port {port} ===")
    uvicorn.run(app, host="0.0.0.0", port=port)