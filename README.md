# Instructions

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Explore the code**  
   Read through the files to understand how each part works.

3. **Run the original program**
   ```bash
   python3 using_package.py
   ```
   > Note: This demonstrates how to use a package instead of importing from separate files.

4. **Learn about Python modules and packages**
   This repository demonstrates:
   - **Modules**: Single `.py` files (like `data_preprocessing.py`)
   - **Packages**: Directories with `__init__.py` (like `lr_package/`)
   - **What `__init__.py` does**: Makes directories into packages and controls imports
   - **Import patterns**: How to import from packages vs individual modules

5. **Verify completion**  
   Answer a quick quiz question to confirm you successfully ran the code:  
   [Quiz Link](https://docs.google.com/forms/d/e/1FAIpQLScjxQsGWvdjXWOI23znq1BWv39saW_lV0nxhKch_wlHOkNTeQ/viewform?usp=sharing&ouid=102851559774167624772)

## What You'll Learn

### 1. **Modules vs Packages**
- **Module**: A single `.py` file containing Python code
- **Package**: A directory containing `__init__.py` and modules

### 2. **What `__init__.py` Does**
- Makes a directory into a Python package
- Runs code when the package is first imported
- Controls what gets imported with `from package import *`
- Without it, Python won't recognize the directory as a package

### 3. **Import Patterns**
- **Original approach**: Import from separate files
  ```python
  from data_preprocessing import X_train, y_train
  from model import lr_model
  from eval import mse, r2
  ```
- **Package approach**: Import everything from one package
  ```python
  from lr_package import lr_model, mse, r2
  ```

### 4. **File Structure**
```
code_splitting_module_PART2/
├── using_package.py          # Example of using the package
├── requirements.txt          # Dependencies
└── lr_package/              # Package (directory with __init__.py)
    ├── __init__.py          # Makes this a package + exposes variables
    ├── data_preprocessing.py # Data loading and preprocessing
    ├── model.py             # Model training
    └── eval.py              # Model evaluation
```

### 5. **Key Benefits of Packages**
- **Organization**: Related code grouped together
- **Cleaner imports**: One import statement instead of multiple
- **Maintainability**: Easier to manage and update
- **Reusability**: Easy to use in other projects

## How It Works

1. **`lr_package/__init__.py`** imports from all the modules and exposes key variables
2. **`using_package.py`** demonstrates how to use the package with a simple import
3. **All the original functionality** is preserved but now organized in a package

The package structure makes your code more professional and easier to use!
