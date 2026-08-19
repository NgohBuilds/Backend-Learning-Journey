# Personal Expenses Tracker

A command-line application built with Python to record, manage, and analyze personal expenses.

This project is the **second project** of my Backend Learning Journey. It builds upon the foundations developed in the first project while introducing more complex data manipulation, validation, date handling, aggregation, and modular application design.

---

## Project Overview

The Personal Expenses Tracker allows users to manage their expenses directly from the terminal.
[Project Overview](./expenses_tracker_final.png)

The application stores expense data in a JSON file, making the data persistent between application sessions.

Each expense contains:

- A unique ID
- An amount
- A category
- An optional description
- The date and time of creation

The project was developed incrementally, starting with a functional implementation and followed by a dedicated code review and refactoring phase.

---

## Features

### Expense Management

- Add a new expense
- Update an existing expense
- Delete an expense
- Search for an expense by ID

### Expense Visualization

- View all expenses
- View expenses from a specific category
- View the total amount of all expenses
- View total expenses grouped by category
- View detailed information about a specific expense

### Data Validation

- Validate menu options
- Validate expense amounts
- Prevent invalid or non-positive amounts
- Validate category selections
- Validate expense IDs before performing operations

### Data Persistence

Expense data is stored in a JSON file and automatically loaded when the application starts.

---

## Technologies

- *Python 3*
- *JSON* — data persistence
- *pathlib* — file path management
- *uuid* — unique expense ID generation
- *datetime* — automatic date and time generation
- *collections.defaultdict* — expense aggregation by category

No external Python packages are required.

---

## Project Structure

```text
personal_expenses_tracker/
│
├── .gitignore
├── README.md
├── expenses.json
├── expenses_tracker_final.png
│
├── main.py
├── menu.py
├── expenses.py
└── utils.py

```

### Module Roles

- **main.py**: Responsible for the main application loop and controlling the lifecycle of the CLI application.
- **menu.py**: Handles user interaction, menu navigation, input collection, and calls the appropriate expense operations.
- **expenses.py**: Contains the main expense management operations (Adding, searching, displaying, updating, deleting expenses, and calculating totals).
- **utils.py**: Contains reusable helper functions (Input/amount validation, loading/saving JSON, category display, calculations).
- **expenses.json**: JSON file used for persistent local storage of expense data.

---

## Data Model

Expenses are stored as a list of dictionaries in JSON format.

Example:

```json
{
    "id": "cd0d23b170b047f1adacaaa6e8f7265d",
    "amount": 7500,
    "category": "Shopping",
    "description": "New clothes",
    "date": "2026/08/13 at 21:36:28"
}

```

| Field | Description |
| --- | --- |
| `id` | Unique identifier generated with UUID |
| `amount` | Expense amount |
| `category` | Expense category |
| `description` | Optional description |
| `date` | Date and time when the expense was created |

---

## Available Categories

The application currently supports the following categories:

- Food
- Transport
- Housing
- Health
- Education
- Shopping
- Other

Categories are selected from a predefined menu to ensure consistent data.

---

## Application Menu

The application provides the following main options:

1. Add a new expense
2. View expenses
3. Update an expense
4. Delete an expense
5. Search an expense
6. Exit

The expense visualization menu also provides options for:

- Viewing all expenses
- Viewing expenses by category
- Calculating total expenses
- Calculating total expenses by category

---

## Getting Started

### Prerequisites

Make sure Python 3 is installed on your system. Check your Python version with:

```bash
python --version

```

### Installation & Run

1.**Clone the Repository**

```bash
git clone [https://github.com/NgohBuilds/Backend-Learning-Journey.git](https://github.com/NgohBuilds/Backend-Learning-Journey.git)

```

2.**Navigate to the Project**

```bash
cd Backend-Learning-Journey/Project/personal_expenses_tracker

```

3.**Run the Application**

```bash
python main.py

```

No external Python packages are required.

---

## Concepts Practiced

This project allowed me to practice and reinforce:

- Functions and modular programming
- Lists and dictionaries
- CRUD operations
- JSON file handling & File persistence
- Exception handling & Input validation
- UUID generation
- Date and time manipulation
- `pathlib` & `defaultdict`
- List comprehensions & Generator expressions
- CLI application design & State management
- Separation of responsibilities & Code refactoring

---

## Development Process

The project was developed in two main stages:

1. **Functional Implementation**
The primary objective was to implement all required features and ensure functionality (handling user input, validating data, persisting expenses in JSON).
2. **Code Review & Refactoring**
After completing the functional version, the code was refactored to remove recursive menu calls, introduce a persistent main loop, improve module responsibilities, and handle edge cases.

---

## What I Learned

This project helped me move beyond basic CRUD operations and work with realistic application logic. I learned how to design CLI applications, structure JSON data, validate user input, and improve code maintainability through refactoring.

---

## Future Improvements

- Search expenses by category or description
- Filter expenses by date range
- Generate monthly and yearly expense reports
- Add automated tests
- Replace JSON storage with a relational database (SQL/PostgreSQL)
- Build a REST API with FastAPI
- Add a web frontend

---

## Backend Learning Journey

This project is part of my repository documenting progression toward full-stack development:

`Python` ➔ `Application Design` ➔ `Data Persistence` ➔ `SQL / PostgreSQL` ➔ `FastAPI` ➔ `REST APIs` ➔ `React` ➔ `Full-Stack Applications`

- Author: __**Gabriel Ngoh** (M.sc. student focused on building backend development skills)
- Repository:__ [Backend Learning Journey](https://github.com/NgohBuilds/Backend-Learning-Journey)
