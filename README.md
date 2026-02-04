# fintech-data-platform
An evolving fintech data platform designed to explore scalable data modeling, reliable pipelines, observability, and AI-assisted data operations.

**Why this project exists**

Modern data platforms are not just about moving data from point A to point B. They require careful consideration of data modeling, correctness, rerunnability, monitoring, and long-term maintainability.

**This project exists to:**
1. Practice designing clear and scalable data models
2. Implement reliable ingestion patterns that are safe to rerun
3. Understand incremental processing and data evolution
4. Build observability into data pipelines from the start
5. Explore practical, responsible ways to apply AI in data operations

_All data and scenarios in this repository are synthetic and created solely for learning and experimentation._

## Project scope and evolution

This repository is intentionally built in incremental stages. Each stage focuses on a specific aspect of building and operating data platforms.

- **v1**: Core data modeling and repeatable ingestion using Postgres
- **v2**: Incremental processing using watermarks and backfill strategies
- **v3**: Observability and data quality checks
- **v4**: Performance optimization and query tuning
- **v5**: AI-assisted analysis for data operations

The goal is to evolve the platform gradually, mirroring how real-world data systems grow over time rather than being designed all at once.

## High-level architecture

At a high level, the platform follows a layered architecture:

1. **Source layer**  
   Synthetic fintech data generated as CSV files to simulate upstream systems.

2. **Raw layer**  
   Raw tables in Postgres that store ingested data with minimal transformation.

3. **Curated layer**  
   Modeled tables (dimensions and facts) designed for analytics and reporting.

4. **Metadata and operations layer**  
   Tables and logs used to track pipeline runs, data quality, and system health (added in later versions).

## Run locally

### Prerequisites
- Docker Desktop
- Python 3.10+

### Setup
```bash
docker compose up -d
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env




