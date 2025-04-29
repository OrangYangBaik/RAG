# RAG Recommendation System (Meals & Drinks)

This is my first project about Retrieval-Augmented Generation (RAG)!  
The project is a simple recommendation system for meals and drinks.

## About

- This project uses RAG techniques to recommend meals and drinks based on user queries.
- **Note:** This is my first implementation, so it may not be fully optimized yet.

## LLM and Embedding Models

For this project, I am using **LM Studio** to serve local models:

- **Language Model (LLM):** DeepSeek 7B (Q4 quantized version)
- **Embedding Model:** Nomic Embed Text v1.5

The base URLs for both the LLM and the embedding model for my experiment are pointed to my localhost.

## Getting Started

If you want to run the project, follow these steps:

1. **Set up your environment variables:**
   - Navigate to the `backend/` folder.
   - Create or update the `.env` file.
   - Insert your base URLs for the LLM and embedding model.  
     (Both should point to your locally running LM Studio endpoints.)

2. **Run the project using Docker Compose:**
   ```bash
   docker-compose up --build
