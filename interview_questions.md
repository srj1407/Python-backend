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
