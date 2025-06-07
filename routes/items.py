from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Item
from db import engine

router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session

# CREATE
@router.post("/", response_model=Item)
def create_item(item: Item, session: Session = Depends(get_session)):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

# READ ALL
@router.get("/", response_model=list[Item])
def read_items(session: Session = Depends(get_session)):
    return session.exec(select(Item)).all()

# READ ONE
@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# UPDATE
@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item, session: Session = Depends(get_session)):
    db_item = session.get(Item, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = updated_item.name
    db_item.price = updated_item.price
    db_item.in_stock = updated_item.in_stock
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

# DELETE
@router.delete("/{item_id}")
def delete_item(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
    return {"message": f"Item {item_id} deleted successfully"}
