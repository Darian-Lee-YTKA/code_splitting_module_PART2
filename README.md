# Instructions

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Explore the code**  
   Read through the files to understand how each part works.

3. **Run the program**
   ```bash
   python eval.py
   ```
   > Note: `eval.py` imports functions from other modules.

4. **Learn about Python modules and packages**
   ```bash
   python demo_imports.py
   ```
   > This demonstrates modules, packages, and different import patterns.

5. **Verify completion**  
   Answer a quick quiz question to confirm you successfully ran the code:  
   [Quiz Link](https://docs.google.com/forms/d/e/1FAIpQLScjxQsGWvdjXWOI23znq1BWv39saW_lV0nxhKch_wlHOkNTeQ/viewform?usp=sharing&ouid=102851559774167624772)

## What You'll Learn

This repository demonstrates:

### 1. **Modules vs Packages**
- **Module**: A single `.py` file (like `data_preprocessing.py`)
- **Package**: A directory with `__init__.py` (like `ml_package/`)

### 2. **What `__init__.py` Does**
- Makes a directory into a Python package
- Runs code when the package is first imported
- Without it, Python won't recognize the directory as a package

### 3. **Import Patterns**
- **Absolute imports**: `from data_preprocessing import X_train`
- **Package imports**: `from ml_package.data_preprocessing import X_train`
- **Relative imports**: `from .data_preprocessing import X_train` (within package)

### 4. **File Structure**
```
code_splitting_module_PART2/
├── data_preprocessing.py    # Original module
├── model.py                 # Original module
├── eval.py                  # Original module
├── demo_imports.py          # Demonstration script
└── ml_package/              # Package (directory with __init__.py)
    ├── __init__.py          # Makes this a package
    ├── data_preprocessing.py # Same code, in package
    ├── model.py             # Same code, in package
    └── eval.py              # Same code, in package
```

Both structures work the same way - the package structure just organizes your code better!
