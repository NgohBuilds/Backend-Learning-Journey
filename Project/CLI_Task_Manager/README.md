# CLI Task Manager -

A command-line Task Manager built with Python as part of my **Backend Learning Journey**. This project focuses on applying core Python concepts through a complete CRUD application while progressively improving software design, code organization, and maintainability.

![Application Preview](preview.png)

> **Project Status:** ✅ Completed

---

## About the Project

This project was built to move beyond small Python exercises and experience what it's like to develop a complete application from start to finish.

Rather than only implementing features, I focused on designing a clean project structure, handling file persistence, refactoring working code, and improving the application's architecture throughout development.

The goal was not only to make the application work, but also to write code that is modular, reusable, and easy to maintain.

---

## Features

* ✅ Create a new task
* ✅ View all tasks
* ✅ Update an existing task
* ✅ Delete a task
* ✅ Mark tasks as completed
* ✅ Mark completed tasks as pending
* ✅ Filter tasks by status
* ✅ Automatic task persistence using JSON
* ✅ Automatic unique ID generation with UUID

---

## Technologies Used

* Python 3
* JSON
* pathlib
* uuid

---

## Project Structure

```text
CLI_Task_Manager/
│
├── README.md
├── preview.jpg
├── Readme Files/
│   └── app_design.md
│
└── src/
    ├── main.py
    ├── menu.py
    ├── tasks.py
    ├── utils.py
    └── tasks.json
```

---

## What I Practiced

During this project I practiced:

* Modular programming
* Function decomposition
* CRUD operations
* JSON file persistence
* File handling
* Error handling
* Custom exceptions
* UUID generation
* Path management with `pathlib`
* Code refactoring
* Separation of responsibilities
* Building a CLI application

---

## Development Process

Rather than building the application all at once, I followed an incremental development process.

1. Designed the application's architecture.
2. Implemented one feature at a time.
3. Tested each feature before continuing.
4. Refactored duplicated and unnecessary code.
5. Improved the project structure.
6. Documented the final application.

Following this workflow helped me understand the importance of writing maintainable code instead of simply writing code that works.

## Lessons Learned

This project taught me how to:

* Design an application before writing code
* Organize a Python project into multiple modules
* Persist application data using JSON
* Build reusable helper functions
* Refactor working code into a cleaner architecture
* Handle invalid user input gracefully
* Work with file paths using `pathlib`
* Improve code quality without changing application behavior

---

## Future Improvements

Possible future enhancements include:

* Task priorities
* Due dates
* Categories
* Keyword search
* Unit testing
* Object-Oriented implementation
* SQLite database
* Graphical User Interface (GUI)

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/NgohBuilds/Backend-Learning-Journey.git
```

Navigate to the project folder:

```bash
cd Backend-Learning-Journey/Project/CLI_Task_Manager
```

Run the application:

```bash
python src/main.py
```

---

## Repository

This project is part of my larger repository:

**Backend Learning Journey**
👉[Repository](https://github.com/NgohBuilds/Backend-Learning-Journey)

This repository documents my progression as I learn backend development by building increasingly challenging projects.

---

## Author

**Gabriel Ngoh**
I'm currently learning backend development by building real-world projects and continuously improving my software engineering practices.

Feel free to explore the repository and follow my learning journey!
