# cloud-expense-tracker
fix: configure docker hub secrets


                 Developer
                     │
                     │ Push Code
                     ▼
                GitHub Repository
                     │
                     │ Triggers
                     ▼
             GitHub Actions (CI/CD)
             ─────────────────────
             • Install Dependencies
             • Run Tests
             • Build Docker Image
             • Push to Docker Hub
                     │
                     ▼
                Docker Hub
                     │
                     │ Pull Image
                     ▼
               AWS EC2 Server
                     │
                     ▼
             Docker Compose
            ┌───────────────┐
            │               │
            ▼               ▼
        Nginx Proxy      Flask App
        (Port 80)        (Port 5000)
            │
            ▼
          Internet
            │
            ▼
        Users Access API
