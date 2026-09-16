
from fastapi import FastAPI, status, HTTPException, Body
from fastapi.responses import JSONResponse

app = FastAPI()

costs_dict = {}
new_id = 1


@app.get("/")
def root():
    return JSONResponse(
        content={"message": "welcome to Cost Manager!"},
        status_code=status.HTTP_202_ACCEPTED
    )


@app.post("/adding_cost/")
def add_cost(
        description: str = Body(),
        amount: float = Body()
):
    global new_id 
    
    new_cost = {
        "id": new_id,
        "description": description,
        "amount": amount
    }
    
    costs_dict[new_id] = new_cost
    new_id += 1

    return JSONResponse(content=new_cost, status_code=status.HTTP_201_CREATED)


@app.get("/cost_names/")
def retriev_costs_list():
    return JSONResponse(content=costs_dict, status_code=status.HTTP_200_OK)


@app.get("/cost_names/{cost_id}")
def fetch_detailed_id(cost_id: int):
    if cost_id in costs_dict:
        return JSONResponse(content=costs_dict[cost_id], status_code=status.HTTP_200_OK)
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Cost not found"
    )


@app.put("/cost_names/{cost_id}/")
def update_detailed_cost(
        cost_id: int,
        cost_description: str = Body(),
        cost_amount: float = Body()
):
    if cost_id in costs_dict:
        costs_dict[cost_id]["description"] = cost_description
        costs_dict[cost_id]["amount"] = cost_amount
        
        return JSONResponse(content=costs_dict[cost_id], status_code=status.HTTP_200_OK)
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Cost not found"
    )


@app.delete("/cost_names/{cost_id}/")
def delete_detailed_cost(cost_id: int):
    if cost_id in costs_dict:
        del costs_dict[cost_id]
        return JSONResponse(
            content={"detail": "Cost record deleted successfully"},
            status_code=status.HTTP_200_OK
        )
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="object not found"
    )