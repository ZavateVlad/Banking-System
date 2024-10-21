
# Python Learning Path Project

This repository is designed to guide participants through learning Python fundamentals, working with FastAPI for API development, integrating databases, and using advanced frameworks like PySpark and Pandas. The project is structured into various phases, each with clear goals and tasks.

## Table of Contents

- [Phase 1: Python Basics](#phase-1-python-basics-pr1)
- [Phase 2: FastAPI Basics](#phase-2-fastapi-basics-pr2)
- [Phase 3: PostgreSQL Integration with SQLAlchemy](#phase-3-postgresql-integration-with-sqlalchemy-pr3)
- [Phase 4: Replacing SQLAlchemy with Raw SQL](#phase-4-replacing-sqlalchemy-with-raw-sql-queries-pr4)
- [Phase 5: Pandas](#phase-5-pandas-pr5)
- [Phase 6: PySpark Introduction](#phase-6-pyspark-pr6)
- [Phase 7: Unit Testing with Pytest](#phase-7-unit-testing-with-pytest-pr7)
- [Phase 8: Integration Testing with SQLite & PostgreSQL](#phase-8-integration-testing-with-sqlite-postgresql-pr8)
- [Phase 9: Dockerizing the Application](#phase-9-dockerizing-the-application-pr9)
- [Phase 10: Final Project Submission](#phase-10-final-project-submission-pr10)
  
---
## Phase 0: Setup - Week 1

- **Python download**: https://www.python.org/downloads/ - Choose version 3.9+
- **Pycharm download**: https://www.jetbrains.com/products/compare/?product=pycharm&product=pycharm-ce - Choose community edition or
- **VS Code download**: https://code.visualstudio.com/download
- **Git CLI**: https://git-scm.com/downloads
- Tasks:
  - Clone this repository
  - Create a new repository within https://github.ibm.com/ and grant write access to:
    - Andrei-Terecoasa
    - andrei-rizea
    - Vlad-Nicolae-Dumitrescu 

## Phase 1: Python Basics (PR1) - Week 1

**Goal**:  Strengthen knowledge of Python fundamentals.

- **Documentation**: Refer to [Learning Python (O'Reilly)](https://learning.oreilly.com/library/view/learning-python-5th/9781449355722/) and [Python Bootcamp](https://ibm-learning.udemy.com/course/complete-python-bootcamp/).

**Tasks**:
- Core Python skills: Functions, loops, OOP, data structures, exceptions.
- Virtual environments: [Python venv](https://docs.python.org/3/library/venv.html), [pyenv](https://github.com/pyenv/pyenv).
  
**Checkpoint**: Submit basic Python scripts demonstrating classes, functions, and system simulation.
   - `exercises/base_exercises.py`
   - `exercises/oop_ex.py`

---

## Phase 2: FastAPI Basics (PR2) - Week 2

**Goal**: Introduce REST API concepts using FastAPI.

- **Documentation**: [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/).

**Tasks**:
- Set up FastAPI with basic routes.
- Implement CRUD operations using [Pydantic models](https://pydantic-docs.helpmanual.io/).
  
**Checkpoint**: Build a minimal API with core CRUD functionality.
- endpoint to retrive all the items from a list
- endpoint to retrieve an item from a static list
- endpoint to create an item in a list
- endpoint to delete an item from a list
- endpoint to update an item in a list
- you can leverage the data from `app/datasets/students.json` for those operations

---

## Phase 3: PostgreSQL Integration with SQLAlchemy (PR3) - Week 3

**Goal**: Integrate PostgreSQL with the application using SQLAlchemy.

- **Documentation**: [SQLAlchemy Docs](https://docs.sqlalchemy.org/en/20/), [Docker PostgreSQL](https://hub.docker.com/_/postgres).

**Tasks**:
- Setup PostgreSQL in Docker.
- Define models for core entities using SQLAlchemy.
- Implement CRUD operations.

**Checkpoint**: Working API with PostgreSQL and SQLAlchemy integration.
- the API endpoints should facilitate CRUD operations against tables which respect the same structure as the files:
    - `datasets/Restaurant - Foods.csv`
    - `datasets/Restaurant - Customers.csv`
    - `datasets/Restaurant - Week 1 Sales.csv`
    - `datasets/Restaurant - Week 1 Satisfaction.csv`
---

## Phase 4: Replacing SQLAlchemy with Raw SQL Queries (PR4) - Week 4

**Goal**: Replace SQLAlchemy with raw SQL queries for database interaction.

- **Documentation**: [asyncpg](https://pypi.org/project/asyncpg/), [psycopg](https://pypi.org/project/psycopg/).

**Tasks**:
- Replace ORM operations with raw SQL queries using asyncpg or psycopg.
  
**Checkpoint**: Fully functional API using raw SQL queries.

---

## Phase 5: Pandas (PR5) - Week 5

**Goal**: Learn data manipulation using Pandas.

- **Documentation**: [Pandas Docs](https://pandas.pydata.org/docs/).

**Tasks**:
- Work with Pandas for data manipulation and visualization.
- Read, manipulate, and export data from DataFrames.
  - Starting from `datasets/Restaurant*` csv files:
    - `datasets/Restaurant - Foods.csv` - check if the data is consistent and take necessary actions
    - `datasets/Restaurant - Customers.csv` - check if the data is consistent and take necessary actions
    - `datasets/Restaurant - Week 1 Sales.csv` - check if the data is consistent and take necessary actions
    - `datasets/Restaurant - Week 1 Satisfaction.csv` - check if the data is consistent and take necessary actions
    - `datasets/Restaurant - Week 2 Sales.csv` - check if the data is consistent and take necessary actions
      extract the following:
      - most popular foods based on a Job Category
      - correlation between most popular foods and satisfaction for week 1
      - correlation between most popular foods and sales for week 1 & week 2
      create endpoints in the exposed API to:
      - be able to upload each of the files mentioned above into the database after the cleaninng/preparation has been done
      - support different load types: delta, truncate, etc

**Checkpoint**: Submit scripts demonstrating Pandas-based data analysis.

---

## Phase 6: PySpark (PR6) - Week 6

**Goal**: Understand parallel processing using PySpark.

- **Documentation**: [Installing PySpark](https://medium.com/@deepaksrawat1906/a-step-by-step-guide-to-installing-pyspark-on-windows-3589f0139a30), [PySpark Examples](https://sparkbyexamples.com/pyspark-tutorial/).

**Tasks**:
- Install and run Spark in local mode.
- Read and process data using Spark DataFrames.
- Perform transformations and actions on data - same exercises as done for Pandas
  
**Checkpoint**: Submit PySpark scripts for data manipulation.

---

## Phase 7: Unit Testing with Pytest (PR7) - Week 7

**Goal**: Write unit tests using pytest.

- **Documentation**: [Pytest Docs](https://docs.pytest.org/en/stable/).

**Tasks**:
- Write unit tests for API endpoints and mock database operations.
  
**Checkpoint**: Unit tests covering all key API endpoints.

---

## Phase 8: Integration Testing with SQLite & PostgreSQL (PR8) - Week 7

**Goal**: Set up integration tests using SQLite and PostgreSQL.

- **Documentation**: [Pytest Docs](https://docs.pytest.org/en/stable/).

**Tasks**:
- Write integration tests for both SQLite and PostgreSQL in Docker.
  
**Checkpoint**: Integration tests that work with both databases.

---

## Phase 9: Dockerizing the Application (PR9) - Week 8

**Goal**: Containerize the full application using Docker.

- **Documentation**: [Dockerfile Reference](https://docs.docker.com/reference/dockerfile/), [Dockerize Python Apps](https://www.docker.com/blog/how-to-dockerize-your-python-applications/).

**Tasks**:
- Write a Dockerfile and set up docker-compose to manage FastAPI and PostgreSQL.

**Checkpoint**: A fully containerized app with seamless Docker setup.

---

## Phase 10: Final Project Submission (PR10) - Week 8 & 9

**Goal**: Submit the final project for review.

**Tasks**:
- Ensure all features are implemented.
- Finalize code, write documentation, and optimize Docker setup.

---

## Resources

- [Python Virtual Environments](https://docs.python.org/3/library/venv.html)
- [Python Dependency Management: Poetry](https://python-poetry.org/docs/)
- [Spark Introduction](https://sparkbyexamples.com/pyspark-tutorial/)
- [Python Docs](https://docs.python.org/3/)
- [Python concurrency](https://realpython.com/python-concurrency/)
- [Intro to threading](https://realpython.com/intro-to-python-threading/)
  [AsyncIO](https://realpython.com/async-io-python/)
