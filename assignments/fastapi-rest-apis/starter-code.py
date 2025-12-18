from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="FastAPI - Starter API")


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class Item(ItemBase):
    id: int


# In-memory storage
items: List[Item] = []
_next_id = 1


@app.get("/items", response_model=List[Item])
def list_items():
    return items


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemBase):
    global _next_id
    new_item = Item(id=_next_id, **item.dict())
    _next_id += 1
    items.append(new_item)
    return new_item


def _get_item_or_404(item_id: int) -> Item:
    for it in items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    return _get_item_or_404(item_id)


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemBase):
    existing = _get_item_or_404(item_id)
    existing.name = item.name
    existing.description = item.description
    existing.price = item.price
    return existing


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    existing = _get_item_or_404(item_id)
    items.remove(existing)
    return None


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
