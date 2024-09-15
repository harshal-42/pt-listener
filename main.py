from fastapi import FastAPI
import time
app = FastAPI()
# Simulate batch processing API
@app.post("/process")
async def process_data():

  # Simulate long-running batch task

  time.sleep(10) # Simulates processing time

  return {"message": "Batch processed"}

