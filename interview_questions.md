## Day 1
- What is the difference between `main:app` in the `uvicorn` command?
- Why do we use `--reload` in development but not in production?
- Difference between opening `http://127.0.0.1:8000` vs `http://127.0.0.1:8000/docs`?
- What is ASGI and how is it different from WSGI?
- If your file was named `server.py` and your FastAPI instance was called `api`, how would you run it?

- Git Questions:
  - What does `git init` do?
  - Why is `git add` required before `git commit`?
  - Difference between `git status` and `git log`?

## Day 2

**Q1. Difference between path params and query params in FastAPI?**  
- **Path params** → part of the URL itself (e.g., `/items/42`).  
- **Query params** → after `?` in the URL, used for filters or optional info (e.g., `/items/42?q=apple`).  

---

**Q2. What does Pydantic provide in FastAPI?**  
- Data validation (types, required fields).  
- Automatic error responses if input is invalid.  
- Auto docs generation in `/docs`.  

---

**Q3. What happens if the request body doesn’t match the Pydantic model?**  
- FastAPI automatically rejects it with a **422 Unprocessable Entity** error.  
- Returns JSON details about what was wrong.  

---

**Q4. Blog API Design — Path vs Query Params**  
- Get a specific blog post → Path param (`/posts/{id}`).  
- Filter blog posts by author → Query param (`/posts?author=shashwat`).  

# Day 3 – Interview & System Design

---

**Q1. How do you define optional query parameters in FastAPI?**  
- Use `Optional[type] = None` or provide a default value.  
- Example:  
  ```python
  @app.get("/search/")
  def search(q: Optional[str] = None, limit: int = 10):
      return {"query": q, "limit": limit}

Q2. What are nested request bodies in FastAPI?

You can define Pydantic models inside other models.

Useful for complex data (like User with Address).

FastAPI validates the entire nested JSON automatically.

Q3. What error do you get if nested fields are missing or invalid?

FastAPI returns 422 Unprocessable Entity with detailed validation errors.

Q4. If you are designing a Task Manager API, how would you structure the endpoints?

POST /tasks → Create a task

GET /tasks → Get all tasks (with optional filters like status=completed)

GET /tasks/{id} → Get task by ID

PUT /tasks/{id} → Update task

DELETE /tasks/{id} → Delete task

Users and authentication can be added later for multi-user support.