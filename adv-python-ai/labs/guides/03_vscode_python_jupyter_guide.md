# VS Code Python & Jupyter Guide

## What is Visual Studio Code?

Visual Studio Code (VS Code) is a free, open-source, lightweight code editor developed by Microsoft. It provides excellent support for Python development and Jupyter notebooks through extensions, making it a popular choice for data science and machine learning workflows.

### Key Features

- **Lightweight**: Fast startup and low resource usage
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Extensions**: Rich ecosystem of extensions
- **IntelliSense**: Intelligent code completion
- **Integrated Terminal**: Built-in command line access
- **Git Integration**: Version control built-in
- **Debugging**: Powerful debugging tools
- **Jupyter Support**: Native notebook experience

## Installation

### Windows Installation

#### Step 1: Download VS Code

1. Visit [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Click "Download for Windows"
3. Choose installer type:
   - **User Installer**: Install for current user (recommended)
   - **System Installer**: Install for all users (requires admin)
   - **ZIP Archive**: Portable version

#### Step 2: Install

1. Run the downloaded `.exe` file
2. Accept the license agreement
3. Choose installation location
4. Select additional tasks:
   - ☑️ Create a desktop icon
   - ☑️ Add "Open with Code" action to context menu
   - ☑️ Register Code as an editor for supported file types
   - ☑️ Add to PATH (recommended)
5. Click "Install"
6. Click "Finish" to launch VS Code

#### Step 3: Verify Installation

```bash
# Open Command Prompt or PowerShell
code --version
```

#### Windows-Specific Tips

- Use PowerShell or Git Bash for better terminal experience
- Windows Defender may slow down initial startup
- Use WSL (Windows Subsystem for Linux) for Linux-like environment

### macOS Installation

#### Method 1: Download from Website

1. Visit [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Click "Download for Mac"
3. Choose version:
   - **Intel Chip**: Universal or Intel
   - **Apple Silicon**: Universal or Apple Silicon
4. Open the downloaded `.zip` file
5. Drag Visual Studio Code to Applications folder

#### Method 2: Using Homebrew

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install VS Code
brew install --cask visual-studio-code
```

#### Step 3: Add to PATH (Optional)

1. Open VS Code
2. Press `Cmd + Shift + P`
3. Type "shell command"
4. Select "Shell Command: Install 'code' command in PATH"

#### Step 4: Verify Installation

```bash
code --version
```

#### macOS-Specific Tips

- Grant necessary permissions in System Preferences
- Use `Cmd` instead of `Ctrl` for shortcuts
- Install Xcode Command Line Tools for full functionality

### Linux Installation

#### Ubuntu/Debian

```bash
# Method 1: Using snap
sudo snap install --classic code

# Method 2: Using apt
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg

sudo apt update
sudo apt install code
```

#### Fedora/RHEL/CentOS

```bash
# Add repository
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'

# Install
sudo dnf install code
```

#### Arch Linux

```bash
# Using yay (AUR helper)
yay -S visual-studio-code-bin

# Or using pamac
pamac install visual-studio-code-bin
```

#### Verify Installation

```bash
code --version
```

#### Linux-Specific Tips

- May need to install additional libraries
- Check file permissions for workspace folders
- Use native terminal for best experience

## Installing Python Extension

### Step 1: Open Extensions View

- Press `Ctrl + Shift + X` (Windows/Linux)
- Press `Cmd + Shift + X` (macOS)
- Or click Extensions icon in Activity Bar (left sidebar)

### Step 2: Install Python Extension

1. Search for "Python"
2. Find "Python" by Microsoft (most popular)
3. Click "Install"
4. Wait for installation to complete

### Step 3: Verify Installation

1. Open a `.py` file or create new one
2. Look for Python version in status bar (bottom-right)
3. IntelliSense should work in Python files

### Python Extension Features

- **IntelliSense**: Auto-completion and suggestions
- **Linting**: Code quality checks (pylint, flake8)
- **Formatting**: Code formatting (black, autopep8)
- **Debugging**: Breakpoints and step-through debugging
- **Testing**: Unit test discovery and execution
- **Jupyter Support**: Run Jupyter notebooks
- **Environment Selection**: Switch between Python environments

## Installing Jupyter Extension

### Step 1: Install Jupyter Extension

1. Open Extensions view (`Ctrl/Cmd + Shift + X`)
2. Search for "Jupyter"
3. Find "Jupyter" by Microsoft
4. Click "Install"

### Optional: Install Related Extensions

```
- Jupyter Keymap (Jupyter shortcuts)
- Jupyter Notebook Renderers (Rich output support)
- Jupyter Slide Show (Presentation mode)
```

### Step 2: Verify Installation

1. Create or open a `.ipynb` file
2. Notebook interface should appear
3. Select kernel from top-right

### Jupyter Extension Features

- **Native Notebook Experience**: No browser needed
- **IntelliSense**: Code completion in notebooks
- **Variable Explorer**: Inspect variables
- **Data Viewer**: View DataFrames and arrays
- **Plot Viewer**: Interactive plots
- **Debugging**: Debug notebook cells
- **Export**: Export to various formats

## Setting Up Python Environment

### Selecting Python Interpreter

1. **Open Command Palette**: `Ctrl/Cmd + Shift + P`
2. Type "Python: Select Interpreter"
3. Choose from available interpreters:
   - System Python
   - Anaconda environments
   - Virtual environments
   - pyenv versions

### Creating Virtual Environment

#### Using venv

```bash
# Open integrated terminal (Ctrl/Cmd + `)
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (macOS/Linux)
source myenv/bin/activate
```

#### Using conda

```bash
# Create environment
conda create --name myenv python=3.11

# Activate
conda activate myenv
```

### VS Code will auto-detect environments in:

- `.venv/` folder in workspace
- `env/` folder in workspace
- Conda environments
- pyenv installations

## Configuring Python Settings

### Access Settings

- **UI**: `Ctrl/Cmd + ,`
- **JSON**: `Ctrl/Cmd + Shift + P` → "Preferences: Open Settings (JSON)"

### Recommended Settings

```json
{
  // Python
  "python.defaultInterpreterPath": "python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length", "88"],
  "python.languageServer": "Pylance",

  // Auto-formatting
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },

  // Jupyter
  "jupyter.askForKernelRestart": false,
  "jupyter.widgetScriptSources": ["jsdelivr.com", "unpkg.com"],
  "jupyter.interactiveWindow.textEditor.executeSelection": true,

  // Terminal
  "terminal.integrated.defaultProfile.windows": "PowerShell",
  "terminal.integrated.fontSize": 14,

  // Editor
  "editor.rulers": [88, 120],
  "editor.minimap.enabled": true,
  "files.autoSave": "afterDelay"
}
```

## Working with Python Files

### Creating Python File

1. `Ctrl/Cmd + N` for new file
2. Save as `.py` extension
3. Select Python interpreter if prompted

### Running Python Code

#### Method 1: Run File

- Press `F5` for debug mode
- Press `Ctrl/Cmd + F5` for run without debugging
- Or click ▶️ button in top-right

#### Method 2: Run in Terminal

- Right-click in editor → "Run Python File in Terminal"
- Or use shortcut (configured in keybindings)

#### Method 3: Run Selection

- Select code
- Right-click → "Run Selection/Line in Python Terminal"
- Or use `Shift + Enter`

### Debugging Python

1. Set breakpoints: Click left of line numbers
2. Start debugging: Press `F5`
3. Debug controls:
   - `F5`: Continue
   - `F10`: Step Over
   - `F11`: Step Into
   - `Shift + F11`: Step Out
   - `Shift + F5`: Stop

### Launch Configuration

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python: Debug Tests",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": ["-v"]
    }
  ]
}
```

## Working with Jupyter Notebooks

### Creating Notebook

1. `Ctrl/Cmd + Shift + P`
2. Type "Jupyter: Create New Blank Notebook"
3. Or create file with `.ipynb` extension

### Notebook Interface

#### Cell Types

- **Code Cell**: Execute Python code
- **Markdown Cell**: Write formatted text
- **Raw Cell**: Plain text (not executed)

#### Cell Operations

- `Esc`: Enter command mode
- `Enter`: Enter edit mode
- `A`: Insert cell above
- `B`: Insert cell below
- `DD`: Delete cell
- `M`: Change to Markdown
- `Y`: Change to Code
- `Shift + Enter`: Run cell and select below
- `Ctrl + Enter`: Run cell
- `Alt + Enter`: Run cell and insert below

### Selecting Kernel

1. Click kernel picker (top-right)
2. Choose from:
   - Python environments
   - Conda environments
   - Jupyter servers
   - Remote kernels

### Running Cells

#### Run Single Cell

- Click ▶️ button in cell
- Press `Shift + Enter`

#### Run Multiple Cells

- Select cells (Shift + Click)
- Click "Run All" in toolbar

#### Cell Execution States

- `[ ]`: Not executed
- `[*]`: Currently executing
- `[1]`: Executed (number = execution order)

### Variable Explorer

1. Click "Variables" button in notebook toolbar
2. View all variables in current session
3. Click variable to see details
4. Double-click DataFrame to open Data Viewer

### Data Viewer

- View DataFrames in spreadsheet format
- Sort and filter data
- Search for values
- Export to CSV

### Plot Viewer

- Interactive plots with zoom/pan
- Save plots as images
- Multiple plots in tabs

### Notebook Output

#### Clear Output

- Click "Clear All Outputs" in toolbar
- Or right-click cell → "Clear Cell Outputs"

#### Collapse Output

- Click collapse icon in output area
- Useful for long outputs

#### Export Notebook

- `Ctrl/Cmd + Shift + P`
- "Jupyter: Export to..."
- Choose format: HTML, PDF, Python

## Interactive Python (REPL)

### Python Interactive Window

1. Write Python code in `.py` file
2. Add `# %%` to create cells
3. Click "Run Cell" or press `Shift + Enter`
4. Results appear in Interactive Window

Example:

```python
# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()

# %%
print("Results:", np.mean(y))
```

### Benefits

- Keep code in `.py` files
- Interactive execution like notebooks
- Better for version control
- Easy to convert to scripts

## Keyboard Shortcuts

### Essential Shortcuts

| Action          | Windows/Linux      | macOS             |
| --------------- | ------------------ | ----------------- |
| Command Palette | `Ctrl + Shift + P` | `Cmd + Shift + P` |
| Quick Open      | `Ctrl + P`         | `Cmd + P`         |
| Terminal        | `` Ctrl + ` ``     | `` Cmd + ` ``     |
| Extensions      | `Ctrl + Shift + X` | `Cmd + Shift + X` |
| Settings        | `Ctrl + ,`         | `Cmd + ,`         |
| Run File        | `Ctrl + F5`        | `Cmd + F5`        |
| Debug           | `F5`               | `F5`              |

### Python-Specific

| Action               | Shortcut                                        |
| -------------------- | ----------------------------------------------- |
| Run Selection        | `Shift + Enter`                                 |
| Run File in Terminal | `Ctrl + Alt + N`                                |
| Select Interpreter   | `Ctrl + Shift + P` → Python: Select Interpreter |
| Format Document      | `Shift + Alt + F`                               |

### Notebook Shortcuts

| Action               | Command Mode    | Edit Mode       |
| -------------------- | --------------- | --------------- |
| Run Cell             | `Ctrl + Enter`  | `Ctrl + Enter`  |
| Run and Select Below | `Shift + Enter` | `Shift + Enter` |
| Insert Above         | `A`             | -               |
| Insert Below         | `B`             | -               |
| Delete Cell          | `DD`            | -               |
| To Markdown          | `M`             | -               |
| To Code              | `Y`             | -               |
| Enter Edit Mode      | `Enter`         | -               |
| Enter Command Mode   | -               | `Esc`           |

## Additional Extensions

### Recommended Extensions

#### Code Quality

```
- Pylance (Enhanced IntelliSense)
- Python Docstring Generator
- autoDocstring
- Better Comments
```

#### Formatting & Linting

```
- Black Formatter
- isort (Import sorting)
- Flake8
- mypy (Type checking)
```

#### Productivity

```
- Code Runner (Quick code execution)
- Path Intellisense
- GitLens (Git supercharged)
- Todo Tree (Track TODOs)
```

#### Data Science

```
- Data Wrangler (Data cleaning)
- Rainbow CSV (CSV file viewer)
- Excel Viewer
- Jupyter Notebook Renderers
```

#### Themes & Icons

```
- Material Icon Theme
- One Dark Pro
- Dracula Official
```

### Installing Extensions from Command Line

```bash
# Install extension
code --install-extension ms-python.python

# List installed extensions
code --list-extensions

# Uninstall extension
code --uninstall-extension ms-python.python
```

## Remote Development

### Remote - SSH

1. Install "Remote - SSH" extension
2. `Ctrl/Cmd + Shift + P` → "Remote-SSH: Connect to Host"
3. Enter SSH connection string
4. VS Code opens in remote context

### Remote - Containers

1. Install "Remote - Containers" extension
2. Open project in container
3. Work with isolated environment

### WSL (Windows)

1. Install "Remote - WSL" extension
2. Open WSL terminal
3. Type `code .` to open in WSL context

## Tips and Best Practices

### Python Development

1. **Use virtual environments**: Isolate project dependencies
2. **Enable auto-formatting**: Keep code consistent
3. **Configure linting**: Catch errors early
4. **Use type hints**: Improve code clarity
5. **Write docstrings**: Document functions
6. **Use .gitignore**: Exclude virtual environments

### Jupyter Notebooks

1. **Clear outputs before committing**: Reduce file size
2. **Use descriptive cell markdown**: Document workflow
3. **Keep cells small**: One concept per cell
4. **Restart kernel regularly**: Ensure reproducibility
5. **Export to Python**: For production code
6. **Use keyboard shortcuts**: Increase productivity

### General VS Code

1. **Learn keyboard shortcuts**: Save time
2. **Use Command Palette**: Discover features
3. **Customize settings**: Tailor to workflow
4. **Install relevant extensions**: Enhance functionality
5. **Use integrated terminal**: Stay in context
6. **Configure workspace settings**: Project-specific configs

## Troubleshooting

### Python Extension Issues

#### Python interpreter not found

```bash
# Verify Python installation
python --version

# Add to PATH (Windows)
setx PATH "%PATH%;C:\Python311"

# Manually set in VS Code
Ctrl+Shift+P → Python: Select Interpreter → Enter interpreter path
```

#### IntelliSense not working

1. Reload window: `Ctrl/Cmd + R`
2. Check language server: Settings → Python › Language Server
3. Reinstall Python extension
4. Clear VS Code cache

#### Linting errors

```json
// Disable specific linters
{
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true
}
```

### Jupyter Issues

#### Kernel not starting

1. Reinstall ipykernel: `pip install --upgrade ipykernel`
2. Select different kernel
3. Restart VS Code
4. Check Python environment has ipykernel

#### Slow notebook performance

1. Clear all outputs
2. Restart kernel
3. Reduce plot complexity
4. Use smaller datasets for testing

#### Cannot install packages

```python
# Install in notebook cell
!pip install package-name

# Or use conda
!conda install package-name
```

### General Issues

#### Extension conflicts

- Disable conflicting extensions
- Check extension logs: Help → Toggle Developer Tools

#### High CPU/Memory usage

- Disable unused extensions
- Reduce file watcher scope
- Close unused notebooks

#### Terminal not working

- Change default shell in settings
- Check terminal profiles
- Reset terminal

## Resources

### Official Documentation

- [VS Code Documentation](https://code.visualstudio.com/docs)
- [Python in VS Code](https://code.visualstudio.com/docs/languages/python)
- [Jupyter in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

### Learning Resources

- [VS Code Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)
- [Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Data Science Tutorial](https://code.visualstudio.com/docs/datascience/data-science-tutorial)

### Community

- [VS Code GitHub](https://github.com/microsoft/vscode)
- [Python Extension GitHub](https://github.com/microsoft/vscode-python)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/visual-studio-code)

## Quick Start Checklist

- [ ] Install VS Code
- [ ] Install Python extension
- [ ] Install Jupyter extension
- [ ] Select Python interpreter
- [ ] Create virtual environment
- [ ] Configure settings.json
- [ ] Install additional extensions (optional)
- [ ] Test Python file execution
- [ ] Test Jupyter notebook
- [ ] Customize keyboard shortcuts (optional)
- [ ] Set up version control (Git)

## Conclusion

VS Code provides a powerful, flexible environment for Python development and data science work. With the Python and Jupyter extensions, you get a feature-rich IDE with excellent notebook support, all in a lightweight package. The integrated debugging, IntelliSense, and variable exploration make it an excellent choice for both beginners and experienced developers.
