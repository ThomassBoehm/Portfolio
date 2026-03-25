# 🧬 Genetic Algorithm Grade Predictor

This project implements a **Genetic Algorithm (GA)** to solve a common academic optimization problem: calculating the necessary grades for future exams and assignments to achieve a specific target final grade.

The system takes the user's current grades and their desired goal (Meta) as input. It then evolves a population of potential grade scenarios to find the optimal combination of future scores needed to reach that target, minimizing the effort required or balancing the grades realistically.

## 🚀 Key Features

* **Optimization Engine:** Uses a custom Genetic Algorithm to "evolve" solutions, finding the best combination of future grades.
* **Goal-Oriented:** Users define a specific target (e.g., "I want a final grade of 8.0"), and the algorithm works backward to find the path.
* **Clean Architecture:** The project is structured using modular design principles, separating business logic, control flow, and data presentation.
* **Test-Driven:** Includes a comprehensive suite of unit tests for controllers, presenters, use cases, and domain entities to ensure algorithmic accuracy and structural integrity.

## 📂 Project Structure

The project follows a modular architecture to ensure separation of concerns and maintainability, mirrored by a dedicated testing suite.

```text
grades_prediction_project/
├── src/
│   ├── modules/
│   │   └── genetic_algorithm/
│   │       └── app/
│   │           ├── genetic_algorithm_controller.py   # Handles incoming requests
│   │           ├── genetic_algorithm_presenter.py    # Formats data for the view
│   │           ├── genetic_algorithm_usecase.py      # Application specific business rules
│   │           └── genetic_algorithm_viewmodel.py    # Manages UI state/data
│   └── shared/
│       └── domain/
│           ├── genetic_algorithm_solver.py        # Core GA logic (The Solver)
│           └── entities/
│               └── boletim_ga.py                  # Grade & Weight Data Models
└── tests/
    ├── modules/
    │   └── genetic_algorithm/
    │       └── app/
    │           ├── test_genetic_algorithm_controller.py
    │           ├── test_genetic_algorithm_presenter.py
    │           ├── test_genetic_algorithm_usecase.py
    │           └── test_genetic_algorithm_viewmodel.py
    └── shared/
        └── domain/
            └── entities/
                └── test_boletim_ga.py
```

## 🛠 Architecture & Design

This project goes beyond a simple script by implementing structural patterns:

* **Domain (Solver):** The `genetic_algorithm_solver.py` contains the pure mathematical logic of the genetic algorithm (population initialization, selection, crossover, mutation, and fitness calculation). It is independent of the application layer.
* **Data Modeling (Boletim):** The boletim_GA.py is responsible for modeling the academic report card. It defines the structure of subjects, exams, and weights, acting as the ground truth for the fitness function to calculate whether a generated solution meets the student's target.
* **Use Case:** Coordinate the flow of data to and from the solver, applying application-specific rules.
* **Controller & Presenter:** Manage the input/output cycle, ensuring the core logic remains decoupled from how the data is displayed or received.

## 💻 Tech Stack

* **Language:** Python 3.14.2
* **Concepts:** Genetic Algorithms, Evolutionary Computing, Clean Architecture, Object-Oriented Programming (OOP).

---

## ⚠️ Code Disclaimer

The code in this repository represents **only my specific contributions** to the project.

As this was a collaborative development, I have excluded parts of the system that were not written by me (such as the Error Handling classes and Lambda Request integrations) to ensure this portfolio strictly reflects my own work and algorithmic logic. The structure shown focuses on the Genetic Algorithm implementation and its direct architecture.
