# Jupyter Notebook Guide

## What is Jupyter Notebook?

Jupyter Notebook is an open-source web application that allows you to create and share documents containing live code, equations, visualizations, and narrative text. It's widely used for data science, machine learning, scientific computing, and educational purposes.

## How Jupyter Notebooks Work

### Architecture

- **Notebook Server**: Runs on your local machine or remote server
- **Web Interface**: Browser-based interface for interacting with notebooks
- **Kernel**: Computational engine that executes code (Python, R, Julia, etc.)
- **Cells**: Building blocks that contain code or markdown content

### File Format

- Files have `.ipynb` extension (IPython Notebook)
- Stored as JSON documents containing metadata, code, and outputs
- Can be version controlled with Git

## Installation

### Using pip

```bash
pip install notebook
```

### Using conda

```bash
conda install -c conda-forge notebook
```

### Using JupyterLab (recommended)

```bash
pip install jupyterlab
```

## Launching Jupyter Notebook

### Classic Notebook

```bash
jupyter notebook
```

### JupyterLab

```bash
jupyter lab
```

### From Specific Directory

```bash
cd /path/to/your/project
jupyter notebook
```

## Working with Cells

### Cell Types

1. **Code Cells**: Execute Python code
2. **Markdown Cells**: Format text with Markdown syntax
3. **Raw Cells**: Plain text, not executed or rendered

### Keyboard Shortcuts

#### Command Mode (press `Esc`)

- `A`: Insert cell above
- `B`: Insert cell below
- `D, D`: Delete selected cell
- `M`: Change cell to Markdown
- `Y`: Change cell to Code
- `Z`: Undo cell deletion
- `Shift + Up/Down`: Select multiple cells
- `Shift + M`: Merge selected cells

#### Edit Mode (press `Enter`)

- `Shift + Enter`: Run cell and select below
- `Ctrl + Enter`: Run cell
- `Alt + Enter`: Run cell and insert below
- `Tab`: Code completion or indent
- `Shift + Tab`: Tooltip/documentation

#### Both Modes

- `Shift + Enter`: Execute cell and move to next
- `Ctrl + S`: Save notebook

## Running Code

### Execute a Cell

```python
# Click the cell and press Shift+Enter
print("Hello, World!")
```

### Execute Multiple Cells

- Select multiple cells and press `Shift + Enter`
- Or use menu: Cell → Run All

### Restart Kernel

- Menu: Kernel → Restart
- Clears all variables and outputs
- Useful when debugging or starting fresh

## Markdown Features

### Headers

```markdown
# H1 Header

## H2 Header

### H3 Header
```

### Formatting

```markdown
**bold text**
_italic text_
`inline code`
~~strikethrough~~
```

### Lists

```markdown
- Bullet point
- Another point
  - Nested point

1. Numbered item
2. Another item
```

### Code Blocks

````markdown
```python
def hello():
    print("Hello!")
```
````

### Links and Images

```markdown
[Link text](https://example.com)
![Alt text](image.png)
```

### Math Equations

```markdown
Inline: $E = mc^2$
Display: $$\int_{0}^{\infty} e^{-x} dx$$
```

## Magic Commands

### Cell Magics (start with %%)

```python
%%time
# Measure execution time of entire cell
sum(range(1000000))
```

```python
%%writefile script.py
# Write cell contents to file
print("Hello from file")
```

### Line Magics (start with %)

```python
%timeit sum(range(1000))  # Time a single line
%pwd  # Print working directory
%ls  # List files
%who  # List variables
%matplotlib inline  # Display plots inline
```

### Useful Magic Commands

- `%run script.py`: Execute Python script
- `%load script.py`: Load script into cell
- `%debug`: Enter debugger
- `%pdb`: Enable automatic debugger
- `%history`: Show command history
- `%reset`: Remove all variables

## Best Practices

### Organization

1. **Use descriptive titles**: Start with H1 header
2. **Separate sections**: Use markdown cells for structure
3. **Logical flow**: Arrange cells in execution order
4. **Clear outputs**: Clear outputs before committing

### Code Quality

1. **One concept per cell**: Keep cells focused
2. **Document code**: Add comments and markdown explanations
3. **Import at top**: Keep imports in first code cell
4. **Avoid side effects**: Minimize global state changes

### Reproducibility

1. **Run All**: Test with "Restart Kernel & Run All"
2. **Version control**: Commit `.ipynb` files
3. **Dependencies**: Document required packages
4. **Data paths**: Use relative paths when possible

### Performance

1. **Large outputs**: Clear or suppress when not needed
2. **Memory management**: Delete unused variables with `del`
3. **Profiling**: Use `%%time` and `%prun` for optimization

## Common Workflows

### Data Analysis

```python
# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load data
df = pd.read_csv('data.csv')

# 3. Explore data
df.head()
df.describe()

# 4. Visualize
df.plot()
plt.show()
```

### Machine Learning

```python
# 1. Import and load data
from sklearn.model_selection import train_test_split

# 2. Preprocess
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 3. Train model
model.fit(X_train, y_train)

# 4. Evaluate
score = model.score(X_test, y_test)
```

## Exporting Notebooks

### Command Line

```bash
# Convert to HTML
jupyter nbconvert --to html notebook.ipynb

# Convert to PDF (requires LaTeX)
jupyter nbconvert --to pdf notebook.ipynb

# Convert to Python script
jupyter nbconvert --to script notebook.ipynb
```

### From Interface

- File → Download as → [format]
- Supports: HTML, PDF, Markdown, Python, LaTeX

## Troubleshooting

### Kernel Issues

- **Kernel died**: Restart kernel and run cells again
- **Kernel busy**: Interrupt kernel (Kernel → Interrupt)
- **Wrong kernel**: Change kernel (Kernel → Change Kernel)

### Common Errors

- **Module not found**: Install in correct environment
- **Port already in use**: Specify different port: `jupyter notebook --port 8889`
- **Browser doesn't open**: Copy URL from terminal

## Extensions and Enhancements

### Jupyter Notebook Extensions

```bash
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

Popular extensions:

- **Table of Contents**: Navigation sidebar
- **Code folding**: Collapse code blocks
- **Variable Inspector**: View all variables
- **ExecuteTime**: Show execution timestamps

### JupyterLab Extensions

```bash
jupyter labextension install @extension-name
```

## Tips and Tricks

1. **Suppress output**: End line with semicolon `;`
2. **Display variables**: Just type variable name in last line
3. **Shell commands**: Prefix with `!` (e.g., `!pip install numpy`)
4. **Multiple outputs**: Use `display()` function
5. **Rich media**: Display images, HTML, videos with IPython.display

## Resources

- [Official Documentation](https://jupyter-notebook.readthedocs.io/)
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
- [Jupyter Notebook Tutorial](https://www.datacamp.com/tutorial/tutorial-jupyter-notebook)
- [Gallery of Interesting Notebooks](https://github.com/jupyter/jupyter/wiki)

## VS Code Integration

VS Code has native Jupyter support:

- Open `.ipynb` files directly
- Run cells with keyboard shortcuts
- Variable explorer built-in
- IntelliSense and debugging support
- No need to run separate server
