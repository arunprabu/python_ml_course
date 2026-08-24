# PyCharm Guide

## What is PyCharm?

PyCharm is a powerful Integrated Development Environment (IDE) specifically designed for Python development by JetBrains. It provides intelligent code assistance, debugging tools, testing support, and integration with popular frameworks and databases.

### Key Features

- **Intelligent Code Editor**: Smart code completion and syntax highlighting
- **Powerful Debugger**: Visual debugger with breakpoints and watches
- **Testing Support**: Integrated unittest, pytest, and doctest
- **Version Control**: Git, GitHub, Mercurial, SVN integration
- **Database Tools**: Query console and schema navigation
- **Web Development**: Django, Flask, FastAPI support
- **Scientific Tools**: Jupyter, NumPy, Matplotlib integration
- **Refactoring**: Safe rename, extract method, and more

## PyCharm Editions

### Professional Edition

- **Price**: Paid (subscription-based)
- **Features**: All features including web frameworks, databases, remote development
- **Best for**: Professional developers, web development, data science
- **Free for**: Students, teachers, open-source projects

### Community Edition

- **Price**: Free and open-source
- **Features**: Core Python development features
- **Best for**: Beginners, pure Python projects, learning
- **Limitations**: No web framework support, no database tools, no remote development

### Comparison

| Feature                        | Community | Professional |
| ------------------------------ | --------- | ------------ |
| Python Development             | ✓         | ✓            |
| Debugging & Testing            | ✓         | ✓            |
| Version Control                | ✓         | ✓            |
| Web Frameworks (Django, Flask) | ✗         | ✓            |
| Database Tools                 | ✗         | ✓            |
| Remote Development             | ✗         | ✓            |
| Scientific Tools               | ✗         | ✓            |
| Jupyter Notebooks              | ✗         | ✓            |
| JavaScript/HTML/CSS            | ✗         | ✓            |

## Installation

### Windows Installation

#### Step 1: Download PyCharm

1. Visit [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)
2. Choose your edition:
   - **Professional**: Full-featured (30-day free trial)
   - **Community**: Free and open-source
3. Click "Download" for Windows

#### Step 2: Install PyCharm

1. Run the downloaded `.exe` file
2. Click "Next" in the installer
3. Choose installation location (default: `C:\Program Files\JetBrains\PyCharm`)
4. Select installation options:
   - ☑️ **64-bit launcher** (recommended)
   - ☑️ **Add "Open Folder as Project"** to context menu
   - ☑️ **Add launchers dir to PATH**
   - ☑️ **.py file association** (optional)
5. Click "Install"
6. Choose "Reboot now" or "Reboot later"
7. Launch PyCharm

#### Step 3: First Launch Configuration

1. Import settings (or start fresh)
2. Choose UI theme (Light or Darcula)
3. Install featured plugins (optional)
4. Start using PyCharm

#### Step 4: Verify Installation

```bash
# Check PyCharm from command line (if added to PATH)
pycharm --version
```

#### Windows-Specific Tips

- Increase heap size for large projects: Help → Edit Custom VM Options
- Use Windows Defender exclusion for PyCharm directory
- Configure Windows Terminal integration

### macOS Installation

#### Step 1: Download PyCharm

1. Visit [https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)
2. Choose edition (Professional or Community)
3. Select appropriate version:
   - **Apple Silicon**: For M1/M2/M3 Macs
   - **Intel**: For Intel-based Macs
4. Download `.dmg` file

#### Step 2: Install PyCharm

1. Open the downloaded `.dmg` file
2. Drag PyCharm icon to Applications folder
3. Wait for copy to complete
4. Eject the disk image

#### Step 3: Launch PyCharm

1. Open Applications folder
2. Double-click PyCharm
3. If security warning appears:
   - Right-click PyCharm → Open
   - Or: System Preferences → Security & Privacy → Open Anyway

#### Step 4: Command Line Launcher

1. Open PyCharm
2. Go to Tools → Create Command-line Launcher
3. Use default path: `/usr/local/bin/pycharm`
4. Now you can use `pycharm` command in terminal

#### Alternative: Using Homebrew

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install PyCharm Community
brew install --cask pycharm-ce

# Or install PyCharm Professional
brew install --cask pycharm
```

#### macOS-Specific Tips

- Grant necessary permissions in System Preferences
- Use `Cmd` instead of `Ctrl` for shortcuts
- Install Xcode Command Line Tools for full functionality
- Configure Terminal integration

### Linux Installation

#### Ubuntu/Debian

**Method 1: Using Snap (Recommended)**

```bash
# Install PyCharm Community
sudo snap install pycharm-community --classic

# Or install PyCharm Professional
sudo snap install pycharm-professional --classic

# Launch PyCharm
pycharm-community
# or
pycharm-professional
```

**Method 2: Using Toolbox App**

```bash
# Download Toolbox
wget https://download.jetbrains.com/toolbox/jetbrains-toolbox-latest.tar.gz

# Extract
sudo tar -xzf jetbrains-toolbox-*.tar.gz -C /opt

# Run Toolbox
/opt/jetbrains-toolbox-*/jetbrains-toolbox

# Use GUI to install PyCharm
```

**Method 3: Manual Installation**

```bash
# Download from website
wget https://download.jetbrains.com/python/pycharm-community-2024.1.tar.gz

# Extract
sudo tar -xzf pycharm-*.tar.gz -C /opt/

# Create symlink
sudo ln -s /opt/pycharm-*/bin/pycharm.sh /usr/local/bin/pycharm

# Launch
pycharm
```

#### Fedora/RHEL/CentOS

```bash
# Using snap
sudo dnf install snapd
sudo snap install pycharm-community --classic

# Or download tarball and install manually (same as Ubuntu method 3)
```

#### Arch Linux

```bash
# Using yay
yay -S pycharm-community-edition

# Or Professional
yay -S pycharm-professional
```

#### Create Desktop Entry

```bash
# PyCharm usually creates this automatically
# Manual creation if needed:
cat > ~/.local/share/applications/pycharm.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=PyCharm
Icon=/opt/pycharm-community/bin/pycharm.svg
Exec="/opt/pycharm-community/bin/pycharm.sh" %f
Comment=Python IDE
Categories=Development;IDE;
Terminal=false
StartupWMClass=jetbrains-pycharm
EOF
```

#### Linux-Specific Tips

- Install required dependencies: `sudo apt install libfuse2`
- Increase inotify watches: `sudo sysctl fs.inotify.max_user_watches=524288`
- Configure font rendering for better appearance
- Use native file chooser

## Creating Your First Python Project

### Method 1: New Project

#### Step 1: Create New Project

1. Launch PyCharm
2. Click "New Project" on welcome screen
3. Or: File → New Project

#### Step 2: Configure Project Settings

1. **Location**: Choose project directory

   ```
   /Users/username/PycharmProjects/my_first_project
   ```

2. **Python Interpreter**: Choose environment type

   - **New Virtual Environment**

     - Location: `<project_dir>/venv`
     - Base interpreter: Select Python version
     - Inherit packages: Unchecked (recommended)

   - **Previously Configured Interpreter**

     - Select existing Python/conda environment

   - **Conda Environment**
     - Create new conda environment
     - Specify Python version

3. **Create main.py**: ☑️ Check to create welcome script

4. Click "Create"

#### Step 3: Project Structure

```
my_first_project/
├── venv/                 # Virtual environment
├── main.py              # Main Python file
└── .idea/               # PyCharm settings (don't commit to Git)
```

### Method 2: Open Existing Project

1. Click "Open" on welcome screen
2. Navigate to project directory
3. Click "OK"
4. Configure interpreter if prompted

### Method 3: Clone from Version Control

1. Click "Get from VCS" on welcome screen
2. Enter repository URL
3. Choose directory
4. Click "Clone"
5. Configure interpreter

## PyCharm Interface Overview

### Main Components

#### 1. Project Tool Window (Left)

- **Project view**: File structure
- **Structure view**: File contents outline
- **Favorites**: Bookmarked files
- **Scratches**: Temporary files

#### 2. Editor (Center)

- Code editor with tabs
- Split view support
- Breadcrumbs navigation
- Gutter with line numbers

#### 3. Tool Windows (Bottom/Sides)

- **Terminal**: Integrated terminal
- **Python Console**: Interactive Python
- **TODO**: Track TODO comments
- **Version Control**: Git integration
- **Run**: Program output
- **Debug**: Debugging tools
- **Problems**: Code issues

#### 4. Navigation Bar (Top)

- File path
- Quick navigation
- Run configurations

#### 5. Status Bar (Bottom)

- Line/column number
- File encoding
- Line endings
- VCS branch
- Python interpreter

## Writing Python Code

### Creating Python File

1. Right-click project folder
2. New → Python File
3. Enter file name (without .py)
4. Press Enter

### Code Features

#### Intelligent Code Completion

```python
# Start typing and press Ctrl+Space
import num[Ctrl+Space]  # Suggests numpy
```

#### Quick Documentation

```python
# Place cursor on function and press Ctrl+Q (Windows/Linux) or F1 (Mac)
print()  # Shows print() documentation
```

#### Parameter Info

```python
# Place cursor in function call and press Ctrl+P
print([Ctrl+P])  # Shows parameters
```

#### Code Generation

```python
# Press Alt+Insert for generate menu
class MyClass:
    # Alt+Insert → Constructor, Methods, etc.
```

### Running Python Code

#### Method 1: Run File

- Right-click in editor → Run 'filename'
- Or press `Shift+F10` (Windows/Linux) or `Ctrl+R` (Mac)
- Or click ▶️ in gutter next to `if __name__ == "__main__"`

#### Method 2: Run Configuration

1. Edit Configurations (top-right)
2. Click "+"
3. Choose Python
4. Configure:
   - Script path
   - Parameters
   - Environment variables
   - Working directory
5. Click OK
6. Run with `Shift+F10`

#### Method 3: Python Console

1. Tools → Python Console
2. Type code interactively
3. Press Enter to execute

### Code Examples

#### Basic Script (main.py)

```python
def greet(name):
    """Print a greeting message."""
    return f"Hello, {name}!"

def main():
    """Main function."""
    message = greet("World")
    print(message)

    # Get user input
    user_name = input("Enter your name: ")
    print(greet(user_name))

if __name__ == "__main__":
    main()
```

#### Running the Script

```bash
# Output:
Hello, World!
Enter your name: Alice
Hello, Alice!
```

## Debugging in PyCharm

### Setting Breakpoints

1. Click left gutter next to line number
2. Red dot appears
3. Or: Click line and press `Ctrl+F8`

### Starting Debug Session

1. Right-click file → Debug 'filename'
2. Or press `Shift+F9` (Windows/Linux) or `Ctrl+D` (Mac)
3. Or click debug icon (🐛) in toolbar

### Debug Controls

| Action              | Windows/Linux | Mac       |
| ------------------- | ------------- | --------- |
| Step Over           | F8            | F8        |
| Step Into           | F7            | F7        |
| Step Out            | Shift+F8      | Shift+F8  |
| Resume              | F9            | Cmd+Alt+R |
| Stop                | Ctrl+F2       | Cmd+F2    |
| Evaluate Expression | Alt+F8        | Alt+F8    |

### Debug Windows

#### Variables

- View all variables in scope
- Expand objects to see attributes
- Right-click to set value

#### Watches

- Add expressions to monitor
- Right-click variable → Add to Watches

#### Console

- Execute code during debugging
- Inspect values interactively

#### Frames

- View call stack
- Navigate between function calls

### Example Debug Session

```python
def calculate_average(numbers):
    """Calculate average of numbers."""
    total = sum(numbers)  # Set breakpoint here
    count = len(numbers)
    average = total / count
    return average

# Debug this
numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print(f"Average: {result}")
```

## Package Management

### Installing Packages

#### Method 1: Using PyCharm UI

1. File → Settings → Project → Python Interpreter
2. Click "+" button
3. Search for package (e.g., "numpy")
4. Click "Install Package"
5. Wait for installation

#### Method 2: Using Terminal

```bash
# Activate virtual environment (if not auto-activated)
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install package
pip install numpy pandas matplotlib

# Install specific version
pip install numpy==1.24.3

# Install from requirements.txt
pip install -r requirements.txt
```

#### Method 3: Using requirements.txt

1. Create requirements.txt

```
numpy==1.24.3
pandas==2.0.0
matplotlib==3.7.1
```

2. Install all:

```bash
pip install -r requirements.txt
```

### Managing Packages

#### View Installed Packages

- File → Settings → Project → Python Interpreter
- Shows all packages with versions

#### Update Package

- Select package
- Click upgrade icon (⬆️)

#### Uninstall Package

- Select package
- Click remove icon (-)

## Version Control (Git)

### Initialize Git Repository

1. VCS → Enable Version Control Integration
2. Choose "Git"
3. Click OK

### Basic Git Operations

#### Commit Changes

1. Right-click project → Git → Commit
2. Or press `Ctrl+K` (Windows/Linux) or `Cmd+K` (Mac)
3. Write commit message
4. Click "Commit" or "Commit and Push"

#### Push to Remote

1. VCS → Git → Push
2. Or press `Ctrl+Shift+K` (Windows/Linux) or `Cmd+Shift+K` (Mac)

#### Pull from Remote

1. VCS → Git → Pull
2. Or press `Ctrl+T` (Windows/Linux) or `Cmd+T` (Mac)

#### View History

1. Right-click file → Git → Show History
2. Or: Git tool window → Log tab

#### Create Branch

1. Git → Branches → New Branch
2. Enter branch name
3. Click Create

### GitHub Integration

1. File → Settings → Version Control → GitHub
2. Add GitHub account
3. Clone repositories
4. Create pull requests
5. Review code

## Working with Virtual Environments

### Creating Virtual Environment

#### During Project Creation

- Choose "New environment using virtualenv"
- Specify location and base interpreter

#### For Existing Project

1. File → Settings → Project → Python Interpreter
2. Click gear icon → Add
3. Choose "Virtual Environment"
4. Select "New environment"
5. Choose base interpreter
6. Click OK

### Activating Virtual Environment

PyCharm automatically activates the project's virtual environment in:

- Terminal tool window
- Python Console
- Run configurations

### Switching Interpreters

1. Bottom-right corner (status bar)
2. Click Python interpreter
3. Select different interpreter
4. Or: Add new interpreter

## Code Quality Tools

### PEP 8 Compliance

PyCharm automatically checks PEP 8:

- Yellow/gray underlines indicate warnings
- Red underlines indicate errors
- Hover for details

#### Configure Inspections

1. File → Settings → Editor → Inspections
2. Expand Python
3. Enable/disable specific checks
4. Adjust severity levels

### Code Reformatting

```python
# Select code and press Ctrl+Alt+L (Windows/Linux) or Cmd+Alt+L (Mac)

# Before
def example(x,y,z):
    return x+y+z

# After (formatted)
def example(x, y, z):
    return x + y + z
```

### Code Analysis

1. Code → Inspect Code
2. Choose scope
3. Click OK
4. Review issues in inspection window

### TODO Comments

```python
# TODO: Implement error handling
# FIXME: Bug in calculation
# NOTE: This is a temporary solution

# View all TODOs in TODO tool window
```

## Testing

### Creating Tests

#### Method 1: Generate Test

1. Right-click class/function
2. Go To → Test
3. Create New Test
4. Choose test framework (unittest, pytest)
5. Select methods to test

#### Method 2: Manual Creation

```python
# test_calculator.py
import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)

if __name__ == '__main__':
    unittest.main()
```

### Running Tests

1. Right-click test file → Run 'Unittests in test\_...'
2. Or click ▶️ next to test class/method
3. Or press `Ctrl+Shift+F10`

### Test Results

- Green: Passed
- Red: Failed
- Yellow: Skipped
- View detailed output in Run tool window
- Click test to see failure details

### Test Coverage

1. Right-click test file → More Run/Debug → Run with Coverage
2. View coverage report
3. See highlighted lines in editor (green = covered, red = not covered)

## Refactoring

### Rename

1. Select symbol
2. Press `Shift+F6`
3. Enter new name
4. Preview changes
5. Click Refactor

### Extract Method

```python
# Select code block
# Press Ctrl+Alt+M (Windows/Linux) or Cmd+Alt+M (Mac)

# Before
result = x * 2 + y * 3

# After
def calculate_result(x, y):
    return x * 2 + y * 3

result = calculate_result(x, y)
```

### Extract Variable

1. Select expression
2. Press `Ctrl+Alt+V` (Windows/Linux) or `Cmd+Alt+V` (Mac)
3. Enter variable name

### Move

1. Select function/class
2. Press `F6`
3. Choose destination module

### Other Refactorings

- **Inline**: `Ctrl+Alt+N`
- **Change Signature**: `Ctrl+F6`
- **Pull Members Up**: Available in context menu
- **Push Members Down**: Available in context menu

## Productivity Tips

### Keyboard Shortcuts

#### Essential Shortcuts

| Action            | Windows/Linux     | Mac               |
| ----------------- | ----------------- | ----------------- |
| Search Everywhere | Double Shift      | Double Shift      |
| Find Action       | Ctrl+Shift+A      | Cmd+Shift+A       |
| Recent Files      | Ctrl+E            | Cmd+E             |
| Go to Class       | Ctrl+N            | Cmd+O             |
| Go to File        | Ctrl+Shift+N      | Cmd+Shift+O       |
| Go to Symbol      | Ctrl+Alt+Shift+N  | Cmd+Alt+O         |
| Go to Declaration | Ctrl+B            | Cmd+B             |
| Find Usages       | Alt+F7            | Alt+F7            |
| Rename            | Shift+F6          | Shift+F6          |
| Comment/Uncomment | Ctrl+/            | Cmd+/             |
| Duplicate Line    | Ctrl+D            | Cmd+D             |
| Delete Line       | Ctrl+Y            | Cmd+Backspace     |
| Move Line Up/Down | Alt+Shift+Up/Down | Alt+Shift+Up/Down |
| Optimize Imports  | Ctrl+Alt+O        | Ctrl+Alt+O        |

### Live Templates

```python
# Type abbreviation and press Tab

main<Tab>
# Expands to:
if __name__ == '__main__':


iter<Tab>
# Expands to:
for item in iterable:

```

#### Create Custom Template

1. File → Settings → Editor → Live Templates
2. Click "+"
3. Add abbreviation and template text
4. Define context (Python)

### Multiple Cursors

1. Hold `Alt` and click to add cursor
2. Or: `Alt+J` to select next occurrence
3. `Alt+Shift+J` to unselect
4. `Ctrl+Alt+Shift+J` to select all occurrences

### Quick Documentation

- `Ctrl+Q` (Windows/Linux) or `F1` (Mac)
- Shows documentation popup
- Works on functions, classes, modules

### Structure View

- `Alt+7` to open Structure tool window
- Shows file outline
- Click to jump to definition

## Plugins and Customization

### Installing Plugins

1. File → Settings → Plugins
2. Search for plugin
3. Click "Install"
4. Restart PyCharm

### Popular Plugins

#### General

- **IdeaVim**: Vim emulation
- **CodeGlance**: Minimap
- **Rainbow Brackets**: Colorful brackets
- **Key Promoter X**: Learn shortcuts

#### Python-Specific

- **Python Security**: Security checks
- **Requirements**: requirements.txt support
- **Markdown**: Enhanced markdown editing

#### Appearance

- **Material Theme UI**: Modern themes
- **Atom Material Icons**: Icon pack
- **Nyan Progress Bar**: Fun progress bar

### Customizing Theme

1. File → Settings → Appearance & Behavior → Appearance
2. Choose theme (Light, Darcula, High Contrast)
3. Customize colors: Editor → Color Scheme

### Customizing Keymap

1. File → Settings → Keymap
2. Search for action
3. Right-click → Add Keyboard Shortcut
4. Or choose predefined keymap (VS Code, Eclipse, etc.)

## Professional Edition Features

### Jupyter Notebook Support

1. Open `.ipynb` file
2. Edit cells inline
3. Run cells with `Shift+Enter`
4. View variables and plots

### Django Support

1. Create Django project
2. Automatic settings configuration
3. Template debugging
4. Database tools

### Database Tools

1. Database tool window
2. Connect to databases
3. Query console
4. Schema navigation
5. Data editing

### Remote Development

1. File → Settings → Build, Execution, Deployment → Deployment
2. Add server (SSH, FTP, etc.)
3. Upload/download files
4. Remote interpreter

### Scientific Tools

1. Create Scientific project
2. NumPy, SciPy, Matplotlib support
3. Array viewer
4. Interactive plots

## Troubleshooting

### PyCharm Won't Start

```bash
# Check logs
# Windows: %USERPROFILE%\.PyCharm2024.1\system\log
# macOS: ~/Library/Logs/JetBrains/PyCharm2024.1
# Linux: ~/.cache/JetBrains/PyCharm2024.1/log

# Increase heap size
# Help → Edit Custom VM Options
-Xms256m
-Xmx2048m
```

### Python Interpreter Issues

1. File → Settings → Project → Python Interpreter
2. Click gear icon → Show All
3. Remove invalid interpreters
4. Add correct interpreter

### Performance Issues

1. Exclude large directories from indexing
   - Right-click folder → Mark Directory as → Excluded
2. Disable unnecessary plugins
3. Increase heap size
4. Disable language injections for large files

### Import Errors

1. File → Invalidate Caches
2. Restart PyCharm
3. Check interpreter has package installed
4. Mark directory as Sources Root

## Tips and Best Practices

### Project Organization

1. Use virtual environments for each project
2. Keep requirements.txt updated
3. Use .gitignore for Python projects
4. Mark directories appropriately (Sources Root, Test Sources)

### Code Quality

1. Enable PEP 8 inspections
2. Use type hints
3. Write docstrings
4. Run code inspections regularly

### Productivity

1. Learn keyboard shortcuts
2. Use live templates
3. Customize your workflow
4. Use TODO comments for tracking tasks

### Version Control

1. Commit frequently with meaningful messages
2. Review changes before committing
3. Use feature branches
4. Keep .idea folder in .gitignore

## Resources

### Official Resources

- [PyCharm Documentation](https://www.jetbrains.com/pycharm/learn/)
- [PyCharm Guide](https://www.jetbrains.com/pycharm/guide/)
- [PyCharm Blog](https://blog.jetbrains.com/pycharm/)
- [PyCharm YouTube Channel](https://www.youtube.com/c/PyCharmIDE)

### Learning Resources

- [PyCharm for Productive Python Development](https://realpython.com/pycharm-guide/)
- [Getting Started with PyCharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)
- [PyCharm Tips and Tricks](https://www.jetbrains.com/pycharm/guide/tips/)

### Community

- [PyCharm Issue Tracker](https://youtrack.jetbrains.com/issues/PY)
- [PyCharm Forum](https://intellij-support.jetbrains.com/hc/en-us/community/topics/200366979-PyCharm)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/pycharm)

## Quick Start Checklist

- [ ] Download and install PyCharm
- [ ] Complete first launch setup
- [ ] Create first Python project
- [ ] Configure Python interpreter
- [ ] Write and run "Hello, World!" program
- [ ] Set up version control
- [ ] Install necessary packages
- [ ] Explore keyboard shortcuts
- [ ] Try debugging with breakpoints
- [ ] Customize settings to your preference
- [ ] Install useful plugins

## Conclusion

PyCharm is a comprehensive IDE that significantly enhances Python development productivity. Whether you choose the free Community Edition for pure Python development or the Professional Edition for web and data science work, PyCharm provides powerful tools for writing, debugging, testing, and deploying Python applications. Its intelligent code assistance, robust debugging capabilities, and seamless integration with various tools make it an excellent choice for both beginners and experienced Python developers.
