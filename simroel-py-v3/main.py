import os
import subprocess
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from endpoints import router  # import the single router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.post("/run_simulation")
def run_simulation():
    try:
        # Build an absolute path from this file's directory to 'core/simroel.py'
        script_path = os.path.join(
            os.path.dirname(__file__),
            "core",
            "simroel.py"
        )
        
        # Run the script
        # If you need Python 3 specifically, replace "python" with "python3"
        result = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True,
            check=True
        )
        
        return {"stdout": result.stdout, "stderr": result.stderr}
    except subprocess.CalledProcessError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error running simroel.py: {e.stderr}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
