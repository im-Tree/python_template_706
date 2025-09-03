# Python Template for IDS706  
   
[![Python Template for IDS706](https://github.com/im-Tree/python_template_706/actions/workflows/main.yml/badge.svg)](https://github.com/im-Tree/python_template_706/actions/workflows/main.yml)
   
This repository provides a Python project template for the IDS706 course. It includes tools and configurations for code quality, testing, and continuous integration.  
   
## Features   
   
- **Python 3.11**: The project is configured to use Python 3.11.  
- **Dependency Management**: Dependencies are listed in `requirements.txt`.  
- **Code Formatting**: Ensures consistent code style using `black`.  
- **Code Linting**: Checks code quality using `flake8`.  
- **Testing**: Includes unit tests with `pytest` and test coverage with `pytest-cov`.  
- **GitHub Actions**: Automates linting and testing workflows.  

    

### Prerequisites    

- Python 3.11  
- `pip` (Python package manager)  

### Installation  
  
1. Clone the repository:  
   ```bash  
   git clone <repository-url>  
   cd python_template_706  
   ```
<br>
1. Create and activate a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
<br>
1. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
<br>  

### Usage  
- Run the application: Modify hello.py as needed and use its functions in your project.  

- Run tests:      
 ```bash  
  pytest --cov=hello  
  ```
- Lint the code:  
  ```bash
  flake8 hello.py
  ```
- Format the code:
  ```bash
  black *.py
  ```

### Using Makefile
The `Makefile` provides shortcuts for common tasks:

- Install dependencies:
  ```bash
  make install
  ```

- Format code:
  ```bash
  make format
  ```

- Lint code:
  ```bash
  make lint
  ```

- Run tests:
  ```bash
  make test
  ```

- Clean up:
  ```bash
  make clean
  ```

- Run all tasks:
  ```bash
  make all
  ```

#### GitHub Actions  
The repository includes a GitHub Actions workflow (.github/workflows/main.yml) that:  
   
  1. Checks out the code.
  1. Sets up Python 3.11.
  1. Installs dependencies.
  1. Lints the code using flake8.
  1. Runs tests with pytest and generates a coverage report.