from fastapi import FastAPI, Depends, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime
import models, schemas
from database import engine, get_db

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Setup templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# ─── Helper ───────────────────────────────────────────
def generate_ticket_id(db: Session):
    count = db.query(models.Ticket).count()
    return f"TKT-{str(count + 1).zfill(3)}"


# ─── PAGE ROUTES (HTML) ────────────────────────────────

@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    tickets = db.query(models.Ticket).order_by(models.Ticket.created_at.desc()).all()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "tickets": tickets
    })

@app.get("/create", response_class=HTMLResponse)
def create_page(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.get("/ticket/{ticket_id}", response_class=HTMLResponse)
def ticket_detail(request: Request, ticket_id: str, db: Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter(models.Ticket.ticket_id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return templates.TemplateResponse("ticket_detail.html", {
        "request": request,
        "ticket": ticket
    })


# ─── API ROUTES (JSON) ─────────────────────────────────

@app.post("/api/tickets")
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    ticket_id = generate_ticket_id(db)
    new_ticket = models.Ticket(
        ticket_id=ticket_id,
        customer_name=ticket.customer_name,
        customer_email=ticket.customer_email,
        subject=ticket.subject,
        description=ticket.description,
        status="Open"
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return {"ticket_id": new_ticket.ticket_id, "created_at": new_ticket.created_at}

@app.get("/api/tickets")
def get_tickets(status: str = None, search: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Ticket)
    if status:
        query = query.filter(models.Ticket.status == status)
    if search:
        query = query.filter(
            models.Ticket.customer_name.contains(search) |
            models.Ticket.customer_email.contains(search) |
            models.Ticket.subject.contains(search) |
            models.Ticket.ticket_id.contains(search)
        )
    return query.order_by(models.Ticket.created_at.desc()).all()

@app.get("/api/tickets/{ticket_id}")
def get_ticket(ticket_id: str, db: Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter(models.Ticket.ticket_id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@app.put("/api/tickets/{ticket_id}")
def update_ticket(ticket_id: str, update: schemas.TicketUpdate, db: Session = Depends(get_db)):
    ticket = db.query(models.Ticket).filter(models.Ticket.ticket_id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    if update.status:
        ticket.status = update.status
    if update.note_text:
        note = models.Note(ticket_id=ticket_id, note_text=update.note_text)
        db.add(note)
    ticket.updated_at = datetime.utcnow()
    db.commit()
    return {"success": True, "updated_at": ticket.updated_at}


# ─── FORM ROUTES (from HTML forms) ────────────────────

@app.post("/create")
def create_ticket_form(
    request: Request,
    customer_name: str = Form(...),
    customer_email: str = Form(...),
    subject: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db)
):
    ticket_id = generate_ticket_id(db)
    new_ticket = models.Ticket(
        ticket_id=ticket_id,
        customer_name=customer_name,
        customer_email=customer_email,
        subject=subject,
        description=description,
        status="Open"
    )
    db.add(new_ticket)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/ticket/{ticket_id}/update")
def update_ticket_form(
    ticket_id: str,
    status: str = Form(...),
    note_text: str = Form(""),
    db: Session = Depends(get_db)
):
    ticket = db.query(models.Ticket).filter(models.Ticket.ticket_id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    ticket.status = status
    if note_text.strip():
        note = models.Note(ticket_id=ticket_id, note_text=note_text)
        db.add(note)
    ticket.updated_at = datetime.utcnow()
    db.commit()
    return RedirectResponse(url=f"/ticket/{ticket_id}", status_code=303)