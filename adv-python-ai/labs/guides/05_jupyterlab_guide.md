# JupyterLab Guide

## What is JupyterLab?

JupyterLab is the next-generation web-based user interface for Project Jupyter. It's a powerful, flexible, and feature-rich evolution of Jupyter Notebook, offering an IDE-like experience in your browser. JupyterLab allows you to work with notebooks, text editors, terminals, and custom components in a flexible, integrated, and extensible manner.

### Key Features

- **Modern Interface**: Tabbed, multi-panel, drag-and-drop workspace
- **Multiple Document Support**: Work with notebooks, Python files, CSV, JSON, Markdown simultaneously
- **Integrated Terminal**: Full terminal access within the interface
- **Extensible**: Rich ecosystem of extensions
- **Real-time Collaboration**: With extensions like jupyter-collaboration
- **File Browser**: Advanced file management with search and preview
- **Code Console**: Interactive console for quick testing
- **Theme Support**: Customizable themes and appearance
- **Keyboard Shortcuts**: Fully customizable shortcuts
- **Notebook Tools**: Cell tagging, table of contents, debugger
- **Output Views**: Multiple views of the same notebook

### JupyterLab vs Jupyter Notebook

| Feature         | Jupyter Notebook | JupyterLab              |
| --------------- | ---------------- | ----------------------- |
| Interface       | Single document  | Multi-document IDE      |
| Layout          | Fixed            | Flexible, drag-and-drop |
| File Browser    | Basic            | Advanced with preview   |
| Text Editor     | Limited          | Full-featured           |
| Terminal        | Separate window  | Integrated              |
| Extensions      | Limited          | Rich ecosystem          |
| Multiple Files  | New tabs/windows | Side-by-side panels     |
| Themes          | Basic            | Extensive               |
| CSV Viewer      | No               | Yes                     |
| Debugger        | No               | Yes (with extension)    |
| Git Integration | No               | Yes (with extension)    |
| Future          | Maintenance mode | Active development      |

## Installation

### Prerequisites

Before installing JupyterLab, ensure you have Python 3.8 or higher:

```bash
python --version
# or
python3 --version
```

### Installation Methods

#### Method 1: Using pip (Standalone)

**Windows:**

```bash
# Open Command Prompt or PowerShell
python -m pip install jupyterlab

# Or for Python 3 specifically
python3 -m pip install jupyterlab

# Verify installation
jupyter lab --version
```

**macOS/Linux:**

```bash
# Using pip
pip install jupyterlab

# Or with pip3
pip3 install jupyterlab

# Verify installation
jupyter lab --version
```

#### Method 2: Using conda (Recommended)

**All Platforms:**

```bash
# Using conda (recommended for data science)
conda install -c conda-forge jupyterlab

# Or create new environment with JupyterLab
conda create -n jupyterlab-env python=3.11 jupyterlab
conda activate jupyterlab-env

# Verify installation
jupyter lab --version
```

#### Method 3: Using pipx (Isolated Installation)

```bash
# Install pipx first
python -m pip install pipx

# Install JupyterLab with pipx
pipx install jupyterlab

# Verify
jupyter lab --version
```

### Platform-Specific Installation

#### Windows Installation

**Step 1: Install Python**

- Download from [python.org](https://www.python.org/downloads/)
- Or install via Microsoft Store
- Or use Anaconda (recommended for data science)

**Step 2: Install JupyterLab**

```bash
# Using pip
pip install jupyterlab

# Or using conda
conda install -c conda-forge jupyterlab
```

**Step 3: Launch JupyterLab**

```bash
# From Command Prompt or PowerShell
jupyter lab

# Or specify directory
jupyter lab C:\Users\YourName\Projects
```

**Windows Tips:**

- Use Anaconda Prompt for conda installations
- Add Python to PATH during installation
- Use PowerShell for better terminal experience
- Consider Windows Terminal for modern interface

---

#### macOS Installation

**Step 1: Install Python**

```bash
# Check if Python is installed
python3 --version

# Install via Homebrew (if not installed)
brew install python

# Or install Anaconda
brew install --cask anaconda
```

**Step 2: Install JupyterLab**

```bash
# Using pip
pip3 install jupyterlab

# Or using conda
conda install -c conda-forge jupyterlab

# Or using Homebrew
brew install jupyterlab
```

**Step 3: Launch JupyterLab**

```bash
jupyter lab

# Or specify directory
jupyter lab ~/Projects
```

**macOS Tips:**

- Use Homebrew for package management
- Terminal.app or iTerm2 work well
- Consider creating alias in ~/.zshrc or ~/.bash_profile
- Use virtual environments for project isolation

---

#### Linux Installation

**Ubuntu/Debian:**

```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip

# Install JupyterLab
pip3 install jupyterlab

# Or install via conda
conda install -c conda-forge jupyterlab
```

**Fedora/RHEL/CentOS:**

```bash
# Install Python
sudo dnf install python3 python3-pip

# Install JupyterLab
pip3 install jupyterlab
```

**Arch Linux:**

```bash
# Install Python
sudo pacman -S python python-pip

# Install JupyterLab
pip install jupyterlab

# Or from AUR
yay -S jupyterlab
```

**Launch JupyterLab:**

```bash
jupyter lab

# Or specify directory
jupyter lab ~/projects
```

**Linux Tips:**

- Use package manager for Python installation
- Consider using virtual environments
- Add `~/.local/bin` to PATH if needed
- Use systemd for auto-start (optional)

---

## Working with Conda

### Why Use Conda with JupyterLab?

1. **Environment Management**: Isolate project dependencies
2. **Package Management**: Handle complex dependencies automatically
3. **Multiple Python Versions**: Easy switching between versions
4. **Pre-tested Packages**: Curated, compatible package versions
5. **Cross-platform**: Works same on Windows, Mac, Linux

### Setting Up Conda Environments

#### Creating Environments

```bash
# Create environment with specific Python version
conda create -n myproject python=3.11

# Create environment with packages
conda create -n data-science python=3.11 jupyterlab numpy pandas matplotlib

# Create from environment file
conda env create -f environment.yml
```

#### Installing JupyterLab in Environment

```bash
# Activate environment
conda activate myproject

# Install JupyterLab
conda install -c conda-forge jupyterlab

# Install additional packages
conda install numpy pandas scikit-learn matplotlib seaborn

# Or install multiple at once
conda install jupyterlab numpy pandas matplotlib scikit-learn
```

#### Managing Environments

```bash
# List all environments
conda env list

# Activate environment
conda activate myproject

# Deactivate environment
conda deactivate

# Remove environment
conda remove -n myproject --all

# Clone environment
conda create -n newproject --clone myproject

# Export environment
conda env export > environment.yml

# Update environment
conda env update -f environment.yml
```

### Using Conda Environments in JupyterLab

#### Method 1: Install Kernel in Environment

```bash
# Activate your environment
conda activate myproject

# Install ipykernel
conda install ipykernel

# Register kernel with JupyterLab
python -m ipykernel install --user --name=myproject --display-name "Python (myproject)"

# Now launch JupyterLab (from any environment)
jupyter lab
```

The kernel "Python (myproject)" will be available in JupyterLab's kernel selection.

#### Method 2: Launch JupyterLab from Environment

```bash
# Activate environment
conda activate myproject

# Install JupyterLab in this environment
conda install jupyterlab

# Launch JupyterLab
jupyter lab
```

This uses the packages from the activated environment.

#### Method 3: Use nb_conda_kernels (Automatic)

```bash
# Install nb_conda_kernels in base environment
conda install -n base nb_conda_kernels

# Create environments with ipykernel
conda create -n project1 python=3.11 ipykernel
conda create -n project2 python=3.9 ipykernel

# Launch JupyterLab from base
conda activate base
jupyter lab
```

All conda environments with ipykernel will appear automatically!

### Example: Complete Setup

```bash
# 1. Create base environment with JupyterLab
conda create -n jupyter-base python=3.11 jupyterlab nb_conda_kernels
conda activate jupyter-base

# 2. Create project-specific environments
conda create -n ml-project python=3.11 ipykernel numpy pandas scikit-learn
conda create -n dl-project python=3.11 ipykernel tensorflow pytorch

# 3. Launch JupyterLab from base
conda activate jupyter-base
jupyter lab

# Now you can select kernels from any environment!
```

### Conda Environment Best Practices

```bash
# 1. Keep base environment minimal
conda activate base
conda install jupyterlab nb_conda_kernels

# 2. Create separate environment for each project
conda create -n project1 python=3.11 ipykernel
conda create -n project2 python=3.9 ipykernel

# 3. Document dependencies
conda env export > environment.yml

# 4. Use environment.yml for reproducibility
# environment.yml example:
```

```yaml
name: myproject
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - jupyterlab=4.0
  - numpy=1.24
  - pandas=2.0
  - matplotlib=3.7
  - scikit-learn=1.3
  - ipykernel
```

```bash
# Create from file
conda env create -f environment.yml

# 5. Update environments regularly
conda update --all

# 6. Clean up unused packages
conda clean --all
```

## Launching JupyterLab

### Basic Launch

```bash
# Launch in current directory
jupyter lab

# Launch in specific directory
jupyter lab /path/to/project

# Launch on specific port
jupyter lab --port 8889

# Launch without opening browser
jupyter lab --no-browser

# Show JupyterLab URL
jupyter lab --no-browser
# Copy the URL and paste in browser
```

### Advanced Launch Options

```bash
# Specify IP address (for remote access)
jupyter lab --ip=0.0.0.0

# Allow root user (not recommended)
jupyter lab --allow-root

# Set notebook directory
jupyter lab --notebook-dir=/path/to/notebooks

# Enable debug mode
jupyter lab --debug

# Custom config file
jupyter lab --config=/path/to/jupyter_lab_config.py

# List available options
jupyter lab --help
```

### Creating Launch Shortcuts

**Windows (Batch File):**

```batch
@echo off
cd C:\Users\YourName\Projects
jupyter lab
```

**macOS/Linux (Shell Script):**

```bash
#!/bin/bash
cd ~/Projects
jupyter lab
```

Make executable:

```bash
chmod +x launch_jupyter.sh
```

**Alias (macOS/Linux):**

```bash
# Add to ~/.bashrc or ~/.zshrc
alias jlab='cd ~/Projects && jupyter lab'

# Reload
source ~/.bashrc  # or source ~/.zshrc

# Use
jlab
```

## JupyterLab Interface

### Main Components

#### 1. Menu Bar (Top)

- **File**: New, open, save, export, close
- **Edit**: Undo, redo, cut, copy, paste, find
- **View**: Show/hide panels, presentation mode
- **Run**: Execute cells, kernels
- **Kernel**: Interrupt, restart, change kernel
- **Tabs**: Manage open tabs
- **Settings**: Editor settings, theme, keyboard shortcuts
- **Help**: Documentation, keyboard shortcuts, about

#### 2. Left Sidebar

- **File Browser** (📁): Navigate and manage files
- **Running Terminals and Kernels** (⚙️): Active sessions
- **Commands** (🔍): Command palette
- **Notebook Tools** (🔧): Cell metadata, TOC
- **Extension Manager** (🧩): Install/manage extensions
- **Tabs** (📑): Tab manager

#### 3. Main Work Area

- Tabbed interface for notebooks, files, terminals
- Drag-and-drop to arrange panels
- Split views (horizontal/vertical)
- Synchronized scrolling (for notebooks)

#### 4. Status Bar (Bottom)

- Kernel status
- Line/column numbers
- Tab/space settings
- Trusted/Untrusted notebook

### Workspace Layouts

#### Single Panel

```
┌─────────────────────────────────┐
│     Notebook or File            │
│                                 │
│                                 │
└─────────────────────────────────┘
```

#### Split Horizontal

```
┌──────────────┬──────────────────┐
│   Notebook   │   Terminal       │
│              │                  │
│              │                  │
└──────────────┴──────────────────┘
```

#### Split Vertical

```
┌─────────────────────────────────┐
│        Notebook                 │
├─────────────────────────────────┤
│        Output/Console           │
└─────────────────────────────────┘
```

#### Complex Layout

```
┌────────┬────────────┬───────────┐
│ File   │  Notebook  │  CSV      │
│ Browser│            │  Preview  │
├────────┼────────────┼───────────┤
│        │  Terminal  │           │
└────────┴────────────┴───────────┘
```

## Working with Notebooks

### Creating Notebooks

1. **From Launcher:**

   - File → New Launcher (Ctrl+Shift+L)
   - Click "Python 3" under Notebook

2. **From File Browser:**

   - Right-click in file browser
   - New → Notebook

3. **From Menu:**
   - File → New → Notebook
   - Select kernel

### Cell Operations

#### Adding Cells

```
Click "+" in toolbar
Or press A (insert above) or B (insert below) in command mode
```

#### Running Cells

```
Shift+Enter: Run cell, select next
Ctrl+Enter: Run cell, stay on current
Alt+Enter: Run cell, insert below
```

#### Cell Types

```
Code: Python code execution
Markdown: Formatted text
Raw: Plain text (not executed)

Change type: Press M (markdown) or Y (code) in command mode
```

#### Cell Selection

```
Click left margin: Select cell
Shift+Click: Select multiple cells
Shift+Up/Down: Extend selection
```

#### Moving Cells

```
Drag cell by left margin
Or use Ctrl+Shift+Up/Down (move up/down)
Or cut (X) and paste (V)
```

### Keyboard Shortcuts

#### Command Mode (Press Esc)

```
A: Insert cell above
B: Insert cell below
D, D: Delete cell
Z: Undo cell deletion
M: Change to markdown
Y: Change to code
C: Copy cell
X: Cut cell
V: Paste cell below
Shift+V: Paste cell above
Shift+M: Merge cells
Ctrl+Shift+-: Split cell
```

#### Edit Mode (Press Enter)

```
Tab: Code completion or indent
Shift+Tab: Show documentation
Ctrl+]: Indent
Ctrl+[: Dedent
Ctrl+/: Comment/uncomment
Ctrl+D: Delete line
Ctrl+Z: Undo
Ctrl+Shift+Z: Redo
```

#### Both Modes

```
Shift+Enter: Run cell, select next
Ctrl+Enter: Run cell
Alt+Enter: Run cell, insert below
Ctrl+S: Save notebook
Ctrl+Shift+L: New launcher
Ctrl+Shift+C: Command palette
```

### Markdown Features

````markdown
# Headers

## H2

### H3

**Bold text**
_Italic text_
~~Strikethrough~~
`inline code`

- Bullet list
- Another item

1. Numbered list
2. Another item

[Link](https://example.com)
![Image](image.png)

```python
# Code block
print("Hello")
```
````

> Blockquote

---

Horizontal rule

Math: $E = mc^2$

Display math:

$$
\int_{0}^{\infty} e^{-x} dx = 1
$$

````

## Working with Multiple Files

### Opening Files

```bash
# From file browser
Double-click file

# From menu
File → Open from Path
Ctrl+O

# Drag and drop
Drag file into work area
````

### Supported File Types

**Notebooks:**

- `.ipynb` - Jupyter notebooks

**Code Files:**

- `.py` - Python scripts
- `.r`, `.R` - R scripts
- `.jl` - Julia scripts
- `.js` - JavaScript
- `.html`, `.css` - Web files

**Data Files:**

- `.csv` - CSV viewer
- `.json` - JSON viewer
- `.tsv` - TSV viewer
- `.txt` - Text files

**Documents:**

- `.md` - Markdown editor/preview
- `.pdf` - PDF viewer
- `.jpg`, `.png` - Image viewer

### Side-by-Side Editing

```bash
# Method 1: Drag tab to split
Drag notebook tab to side of work area

# Method 2: Right-click menu
Right-click tab → New View for Notebook

# Method 3: File menu
File → New View for Notebook
```

**Use Cases:**

- Compare two notebooks
- View data file while editing code
- Edit Python file while testing in notebook
- View documentation while coding

## Integrated Terminal

### Opening Terminal

```bash
# From launcher
File → New → Terminal

# From menu
File → New Launcher → Terminal

# Shortcut
Ctrl+Shift+L (launcher) then click Terminal

# Multiple terminals
Open multiple terminals in separate tabs
```

### Using Terminal

```bash
# Navigate directories
cd /path/to/project
pwd
ls -la

# Install packages
pip install package-name
conda install package-name

# Run Python scripts
python script.py

# Git operations
git status
git add .
git commit -m "message"
git push

# Check system info
python --version
which python
nvidia-smi  # Check GPU
```

### Terminal Features

- **Multiple terminals**: Open as many as needed
- **Tab completion**: Use Tab for autocomplete
- **Command history**: Use Up/Down arrows
- **Split view**: Place terminal beside notebook
- **Themes**: Inherits JupyterLab theme

## Extensions

### Built-in Extensions

JupyterLab comes with several built-in extensions:

- Notebook
- Text Editor
- Terminal
- File Browser
- Image Viewer
- CSV Viewer
- JSON Viewer
- Markdown Previewer

### Installing Extensions

#### Method 1: Extension Manager (GUI)

```bash
# Enable extension manager
Settings → Extension Manager → Enable

# Search and install extensions
Click puzzle piece icon in left sidebar
Search for extension
Click "Install"
```

#### Method 2: Command Line

```bash
# Install extension
pip install jupyterlab-extension-name

# Or with conda
conda install -c conda-forge jupyterlab-extension-name

# Some extensions require rebuild
jupyter lab build
```

### Popular Extensions

#### 1. Git Extension

```bash
# Install
pip install jupyterlab-git

# Features:
# - Initialize repositories
# - Stage/commit changes
# - Push/pull
# - View diff
# - Branch management
```

#### 2. Variable Inspector

```bash
# Install
pip install lckr-jupyterlab-variableinspector

# Features:
# - View all variables
# - See types and values
# - Inspect DataFrames
# - Monitor memory usage
```

#### 3. Table of Contents

```bash
# Built-in, just enable
# View → Show Table of Contents

# Features:
# - Auto-generate TOC
# - Navigate sections
# - Collapsible headings
```

#### 4. Debugger

```bash
# Install (included in JupyterLab 3.0+)
pip install xeus-python

# Features:
# - Visual debugger
# - Breakpoints
# - Step through code
# - Inspect variables
```

#### 5. Code Formatter

```bash
# Install
pip install jupyterlab-code-formatter
pip install black isort

# Features:
# - Format code with black
# - Sort imports with isort
# - Format on save option
```

#### 6. Plotly Extension

```bash
# Install
pip install jupyterlab-plotly

# Features:
# - Interactive Plotly plots
# - Zoom, pan, hover
# - Export images
```

#### 7. Matplotlib Integration

```bash
# Install
pip install ipympl

# Usage in notebook:
%matplotlib widget
```

#### 8. Real-time Collaboration

```bash
# Install
pip install jupyter-collaboration

# Features:
# - Multiple users editing simultaneously
# - See cursors and selections
# - Chat functionality
```

#### 9. GitHub Integration

```bash
# Install
pip install jupyterlab-github

# Features:
# - Browse GitHub repos
# - Open notebooks from GitHub
# - Save to GitHub
```

#### 10. Spreadsheet Viewer

```bash
# Install
pip install jupyterlab-spreadsheet-editor

# Features:
# - Edit CSV files
# - Formula support
# - Data manipulation
```

### Managing Extensions

```bash
# List installed extensions
jupyter labextension list

# Disable extension
jupyter labextension disable extension-name

# Enable extension
jupyter labextension enable extension-name

# Uninstall extension
pip uninstall jupyterlab-extension-name
# or
jupyter labextension uninstall extension-name

# Update extensions
pip install --upgrade jupyterlab-extension-name
```

## Advanced Features

### Table of Contents

```bash
# Enable TOC
View → Show Table of Contents

# Or click TOC icon in left sidebar

# Features:
# - Auto-generated from markdown headers
# - Click to navigate
# - Collapsible sections
# - Updates in real-time
```

### Cell Tags

```bash
# Show cell tags
View → Show Cell Tags
# Or right sidebar → Property Inspector

# Use tags for:
# - Organization ("setup", "analysis", "viz")
# - Filtering cells
# - Parameterization
# - Export control
```

### Notebook Checkpoints

```bash
# Manual checkpoint
File → Save and Create Checkpoint

# Revert to checkpoint
File → Revert Notebook to Checkpoint

# Checkpoints saved automatically
# Access in .ipynb_checkpoints/ folder
```

### Debugger

```bash
# Enable debugger
View → Show Debugger

# Set breakpoints:
# Click left of line numbers in cell

# Debug controls:
# - Continue (▶️)
# - Step Over (⤵️)
# - Step Into (⤴️)
# - Step Out (⤴️)

# Inspect:
# - Variables
# - Call stack
# - Breakpoints list
```

### Code Console

```bash
# Open console for notebook
Right-click notebook → New Console for Notebook

# Features:
# - Quick code testing
# - Share kernel with notebook
# - Access notebook variables
# - Interactive exploration
```

### File Operations

```bash
# Create new folder
Right-click → New Folder

# Rename
Right-click → Rename

# Delete
Right-click → Delete
# Moves to trash (can recover)

# Download
Right-click → Download

# Copy path
Right-click → Copy Path

# Duplicate
Right-click → Duplicate
```

## Customization

### Settings

```bash
# Access settings
Settings → Settings Editor

# Or Ctrl+,
```

**Key Settings:**

- **Theme**: Light, Dark, JupyterLab Dark
- **Editor**: Font size, line numbers, tabs vs spaces
- **Keyboard Shortcuts**: Customize all shortcuts
- **Notebook**: Auto-save interval, scroll past end
- **Terminal**: Shell, font, theme
- **Extension Manager**: Enable/disable

### Keyboard Shortcuts

```bash
# View shortcuts
Settings → Keyboard Shortcuts

# Or press Ctrl+Shift+H (Help → Keyboard Shortcuts)

# Customize:
# Click on command
# Press keys to assign
# Save
```

### Themes

```bash
# Change theme
Settings → Theme → JupyterLab Dark/Light

# Install theme extensions
pip install jupyterlab-night
pip install theme-darcula

# Select in Settings → Theme
```

### Workspace

```bash
# Save workspace layout
File → Save Workspace

# Restore workspace
File → Open Workspace

# Export workspace
File → Export Workspace

# Reset workspace
View → Reset Workspace Layout
```

## Best Practices

### Project Organization

```
project/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── data.py
│   └── models.py
├── tests/
├── docs/
├── requirements.txt
├── environment.yml
└── README.md
```

### Notebook Best Practices

```python
# 1. Use descriptive names
# 01_data_exploration.ipynb
# 02_feature_engineering.ipynb

# 2. Add header cell with description
"""
# Data Exploration

**Author**: Your Name
**Date**: 2024-01-15
**Description**: Initial exploration of customer data

## Goals:
- Understand data structure
- Identify missing values
- Visualize distributions
"""

# 3. Organize with markdown sections
## Data Loading
## Preprocessing
## Analysis
## Results

# 4. One concept per cell
# Keep cells focused and readable

# 5. Clear all outputs before committing
# Kernel → Restart Kernel and Clear All Outputs

# 6. Use relative paths
data_path = '../data/raw/data.csv'

# 7. Document key decisions
# Explain why certain approaches were chosen

# 8. Test with "Restart & Run All"
# Ensure reproducibility
```

### Environment Management

```bash
# 1. Document dependencies
conda env export > environment.yml

# 2. Include environment.yml in repo

# 3. Add .gitignore
echo ".ipynb_checkpoints" >> .gitignore
echo "__pycache__" >> .gitignore
echo "*.pyc" >> .gitignore

# 4. Use separate environments per project

# 5. Keep environments updated
conda update --all

# 6. Clean up
conda clean --all
```

## Troubleshooting

### Common Issues

#### 1. JupyterLab Won't Start

```bash
# Check if already running
jupyter lab list

# Kill existing instances
jupyter lab stop 8888

# Try different port
jupyter lab --port 8889

# Check Python path
which jupyter

# Reinstall
pip uninstall jupyterlab
pip install jupyterlab
```

#### 2. Kernel Won't Connect

```bash
# Restart kernel
Kernel → Restart Kernel

# Check kernel specs
jupyter kernelspec list

# Remove problematic kernel
jupyter kernelspec remove kernel-name

# Reinstall kernel
python -m ipykernel install --user

# Check for errors
# Look in terminal where JupyterLab is running
```

#### 3. Extensions Not Working

```bash
# Rebuild JupyterLab
jupyter lab build

# Clear cache
jupyter lab clean
jupyter lab build

# Check extension status
jupyter labextension list

# Reinstall extension
pip uninstall extension-name
pip install extension-name
```

#### 4. Conda Environments Not Showing

```bash
# Install ipykernel in environment
conda activate myenv
conda install ipykernel

# Register kernel
python -m ipykernel install --user --name=myenv

# Or use nb_conda_kernels
conda install -n base nb_conda_kernels

# Restart JupyterLab
```

#### 5. File Not Saving

```bash
# Check disk space
df -h

# Check permissions
ls -la

# Try manual save
File → Save Notebook

# Create checkpoint
File → Save and Create Checkpoint

# Export as backup
File → Export Notebook As → Python
```

### Performance Tips

```bash
# 1. Close unused notebooks
# Reduces memory usage

# 2. Clear output regularly
# Edit → Clear All Outputs

# 3. Restart kernel periodically
# Kernel → Restart Kernel

# 4. Use generators for large data
def data_generator():
    for i in range(1000000):
        yield i

# 5. Process in chunks
for chunk in pd.read_csv('large.csv', chunksize=10000):
    process(chunk)

# 6. Disable autosave for large notebooks
# Settings → Notebook → Autosave Documents (uncheck)

# 7. Increase memory limit
# Edit jupyter_lab_config.py:
c.NotebookApp.max_buffer_size = 536870912
```

## Tips and Tricks

### Productivity Tips

```python
# 1. Use command palette
# Ctrl+Shift+C
# Quick access to all commands

# 2. Use code snippets
# Create .jupyterlab/snippets/
# Save frequently used code

# 3. Create cell with title
#@title This is a title cell
# Collapsible section

# 4. Use magic commands
%timeit sum(range(1000))
%%time
# ... cell code ...

# 5. Quick documentation
# Shift+Tab in function
# Or ? after function name
np.array?

# 6. Run shell commands
!pip list
!ls -la

# 7. Use keyboard shortcuts
# Learn and customize

# 8. Split views
# Drag tabs to arrange

# 9. Search in files
# Edit → Find in Files
# Ctrl+Shift+F

# 10. Use table of contents
# Quick navigation
```

### Useful Magic Commands

```python
# Timing
%time
%timeit
%%time
%%timeit

# Debugging
%debug
%pdb

# System
%pwd
%cd
%ls
!command

# Matplotlib
%matplotlib inline
%matplotlib widget

# Load/Save
%load file.py
%%writefile file.py

# Running
%run script.py

# Environment
%env
%pip install package

# History
%history
%recall

# Memory
%who
%whos
%reset
```

## Resources

### Official Documentation

- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
- [Jupyter Project](https://jupyter.org/)
- [JupyterLab GitHub](https://github.com/jupyterlab/jupyterlab)

### Extensions

- [Awesome JupyterLab](https://github.com/mauhai/awesome-jupyterlab)
- [Extension Gallery](https://jupyterlab.readthedocs.io/en/stable/user/extensions.html)

### Tutorials

- [JupyterLab Tutorial](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)
- [Real Python JupyterLab](https://realpython.com/jupyter-notebook-introduction/)

### Community

- [Jupyter Discourse](https://discourse.jupyter.org/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/jupyter-lab)

## Conclusion

JupyterLab is a powerful, modern platform for data science and scientific computing. Its flexible interface, extensive extension ecosystem, and seamless integration with conda make it an excellent choice for:

- **Data Scientists**: Interactive exploration and visualization
- **Researchers**: Reproducible research and documentation
- **Educators**: Creating interactive course materials
- **Developers**: Prototyping and testing Python code

Combined with conda for environment management, JupyterLab provides a complete solution for Python development, especially in AI/ML and data science workflows.

**Key Takeaways:**

- Modern, flexible interface superior to classic Jupyter Notebook
- Excellent conda integration for environment management
- Rich extension ecosystem for customization
- Perfect for exploratory data analysis and visualization
- Active development and community support
- Free and open-source

Start with JupyterLab for your next data science project and experience the difference!
