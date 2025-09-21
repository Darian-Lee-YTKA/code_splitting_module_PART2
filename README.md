# Python Modules, Packages, and Imports - Learning Module

## Learning Objectives

After completing this module, you will understand:

### 1. **What is a Module?**
- A single `.py` file containing Python code
- Contains functions, classes, and variables
- Can be imported directly: `from module_name import function`

### 2. **What is a Package?**
- A directory containing `__init__.py` and modules
- Allows cleaner imports: `from package_name import function`
  - Say a package contains 100 files. Without a package, you would need to import from each file one by one. Having a package allows you to just import once from the package name

### 3. **What does `__init__.py` do?**
- **Makes a directory a package** - Without it, Python won't recognize the directory as a package
- **Runs initialization code** - Executes when the package is first imported
- **Controls package imports** - Defines what gets imported with `from package import *`
- **Exposes variables** - Can make module variables available at package level

### 5. **Benefits of Packages**
- **Organization**: Related code grouped together
- **Cleaner imports**: One import statement instead of multiple
- **Maintainability**: Easier to manage and update
- **Reusability**: Easy to use in other projects

## Repository Structure

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

## How to Use This Module

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Explore the code**  
   Read through the files to understand how each part works.

3. **Run the example**
   ```bash
   python3 using_package.py
   ```
   > This demonstrates how to use a package instead of importing from separate files.

4. **Compare the approaches**
   - **Without packages**: You'd need to import from 3 separate files
   - **With packages**: You can import everything from one place

5. **Verify completion**  
   Answer a quick quiz question to confirm you successfully ran the code:  
   [Quiz Link]([https://docs.google.com/forms/d/e/1FAIpQLScjxQsGWvdjXWOI23znq1BWv39saW_lV0nxhKch_wlHOkNTeQ/viewform?usp=sharing&ouid=102851559774167624772](https://docs.google.com/forms/d/e/1FAIpQLSdKIJtP58M1xWkUSXqe73a7gJXmpA2pqgUKg_MiPblw5IjPoQ/viewform?usp=header))

## How It Works

1. **`lr_package/__init__.py`** imports from all the modules and exposes key variables
2. **`using_package.py`** demonstrates how to use the package with a simple import
3. **All the original functionality** is preserved but now organized in a package

The package structure makes your code more professional and easier to use!
