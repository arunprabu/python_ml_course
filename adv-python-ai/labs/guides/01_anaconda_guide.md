# Anaconda Guide

## What is Anaconda?

Anaconda is a free, open-source distribution of Python and R for scientific computing, data science, and machine learning. It simplifies package management and deployment, and includes over 1,500 pre-installed packages.

### Key Benefits

- **Package Management**: Easy installation and management of Python packages
- **Environment Management**: Create isolated environments for different projects
- **Pre-installed Libraries**: Comes with popular data science libraries
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Conda Package Manager**: Handles dependencies automatically
- **Anaconda Navigator**: GUI for managing environments and packages

## Anaconda vs Miniconda

| Feature  | Anaconda                    | Miniconda                       |
| -------- | --------------------------- | ------------------------------- |
| Size     | ~3 GB                       | ~400 MB                         |
| Packages | 1,500+ pre-installed        | Only conda and Python           |
| Best for | Beginners, full setup       | Advanced users, minimal install |
| GUI      | Anaconda Navigator included | Not included                    |

## Installation

### Windows Installation

#### Step 1: Download

1. Visit [https://www.anaconda.com/download](https://www.anaconda.com/download)
2. Download the Windows installer (64-bit or 32-bit)
3. Choose Python 3.x version (recommended)

#### Step 2: Install

1. Run the downloaded `.exe` file
2. Click "Next" and accept the license agreement
3. Choose installation type:
   - **Just Me**: Installs for current user (recommended)
   - **All Users**: Requires admin privileges
4. Choose installation location (default: `C:\Users\<username>\anaconda3`)
5. Advanced options:
   - ☑️ **Add Anaconda to PATH** (not recommended by installer, but useful)
   - ☑️ **Register Anaconda as default Python**
6. Click "Install" and wait for completion
7. Click "Finish"

#### Step 3: Verify Installation

```bash
# Open Anaconda Prompt (from Start Menu)
conda --version
python --version
```

#### Common Issues on Windows

- **PATH not set**: Use Anaconda Prompt instead of CMD
- **Permission errors**: Run as Administrator
- **Slow installation**: Disable antivirus temporarily

### macOS Installation

#### Step 1: Download

1. Visit [https://www.anaconda.com/download](https://www.anaconda.com/download)
2. Download the macOS installer (Intel or Apple Silicon)
3. Choose `.pkg` installer for GUI or `.sh` for command line

#### Step 2: Install (GUI Method)

1. Double-click the downloaded `.pkg` file
2. Follow the installation wizard
3. Accept the license agreement
4. Choose installation location (default: `/Users/<username>/anaconda3`)
5. Click "Install"
6. Complete installation

#### Step 3: Install (Command Line Method)

```bash
# Navigate to Downloads
cd ~/Downloads

# Make installer executable
chmod +x Anaconda3-*-MacOSX-*.sh

# Run installer
bash Anaconda3-*-MacOSX-*.sh

# Follow prompts:
# - Press Enter to review license
# - Type 'yes' to accept
# - Press Enter for default location
# - Type 'yes' to initialize conda
```

#### Step 4: Activate Installation

```bash
# Close and reopen terminal, or run:
source ~/.bash_profile  # For bash
source ~/.zshrc         # For zsh (macOS Catalina+)
```

#### Step 5: Verify Installation

```bash
conda --version
python --version
which python  # Should show anaconda path
```

#### Common Issues on macOS

- **Command not found**: Restart terminal or run `source` command
- **Apple Silicon (M1/M2)**: Use Rosetta 2 for older packages
- **Permission denied**: Use `sudo` for system-wide installation

### Linux Installation

#### Step 1: Download

```bash
# Navigate to home directory
cd ~

# Download installer (replace URL with latest version)
wget https://repo.anaconda.com/archive/Anaconda3-<VERSION>-Linux-x86_64.sh

# Or use curl
curl -O https://repo.anaconda.com/archive/Anaconda3-<VERSION>-Linux-x86_64.sh
```

#### Step 2: Verify Download (Optional)

```bash
# Check SHA-256 hash
sha256sum Anaconda3-<VERSION>-Linux-x86_64.sh
```

#### Step 3: Install

```bash
# Make installer executable
chmod +x Anaconda3-<VERSION>-Linux-x86_64.sh

# Run installer
bash Anaconda3-<VERSION>-Linux-x86_64.sh

# Follow prompts:
# - Press Enter to review license
# - Press 'q' to finish reading
# - Type 'yes' to accept
# - Press Enter for default location (/home/<username>/anaconda3)
# - Type 'yes' to initialize conda
```

#### Step 4: Activate Installation

```bash
# Close and reopen terminal, or run:
source ~/.bashrc
```

#### Step 5: Verify Installation

```bash
conda --version
python --version
which conda
```

#### Common Issues on Linux

- **Missing dependencies**: Install `libgl1-mesa-glx libegl1-mesa libxrandr2`
- **PATH issues**: Manually add to `.bashrc` or `.zshrc`
- **SSH sessions**: Initialize conda in shell config file

## Basic Conda Commands

### Package Management

```bash
# List installed packages
conda list

# Search for a package
conda search numpy

# Install a package
conda install numpy

# Install specific version
conda install numpy=1.24.3

# Install multiple packages
conda install numpy pandas matplotlib

# Update a package
conda update numpy

# Update all packages
conda update --all

# Remove a package
conda remove numpy

# Clean up (remove unused packages and cache)
conda clean --all
```

### Environment Management

```bash
# List all environments
conda env list
conda info --envs

# Create new environment
conda create --name myenv

# Create environment with specific Python version
conda create --name myenv python=3.13

# Create environment with packages
conda create --name myenv python=3.13 numpy pandas

# Activate environment
conda activate myenv

# Deactivate current environment
conda deactivate

# Remove environment
conda remove --name myenv --all

# Clone environment
conda create --name newenv --clone myenv

# Export environment
conda env export > environment.yml

# Create environment from file
conda env create -f environment.yml
```

### Information Commands

```bash
# Check conda version
conda --version

# Display conda configuration
conda config --show

# Show environment information
conda info

# List packages in specific environment
conda list -n myenv
```

### Update Commands

```bash
# Update conda itself
conda update conda

# Update Anaconda distribution
conda update anaconda

# Update all packages in current environment
conda update --all
```

## Anaconda Navigator

### Launching Navigator

**Windows**: Start Menu → Anaconda Navigator  
**macOS/Linux**: Type `anaconda-navigator` in terminal

### Navigator Features

1. **Home**: Launch applications (Jupyter, Spyder, VS Code, etc.)
2. **Environments**: Create and manage conda environments
3. **Learning**: Access tutorials and documentation
4. **Community**: Connect with Anaconda community

### Common Tasks in Navigator

#### Create Environment

1. Click "Environments" tab
2. Click "Create" button at bottom
3. Enter environment name
4. Select Python version
5. Click "Create"

#### Install Packages

1. Select environment
2. Change dropdown from "Installed" to "Not installed" or "All"
3. Search for package
4. Check box next to package
5. Click "Apply"

#### Launch Jupyter Notebook

1. Go to "Home" tab
2. Select environment from dropdown
3. Click "Launch" under Jupyter Notebook

## Working with Environments

### Why Use Environments?

- **Isolation**: Keep project dependencies separate
- **Reproducibility**: Share exact package versions
- **Compatibility**: Avoid package conflicts
- **Testing**: Test code with different Python versions

### Best Practices

```bash
# Create environment for each project
conda create --name project1 python=3.13
conda create --name project2 python=3.9

# Always specify Python version
conda create --name myenv python=3.13

# Install packages after creating environment
conda activate myenv
conda install numpy pandas scikit-learn

# Keep base environment clean
# Don't install packages in base environment
```

### Environment File (environment.yml)

```yaml
name: myproject
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.13
  - numpy=1.24
  - pandas=2.0
  - matplotlib
  - scikit-learn
  - pip
  - pip:
      - some-pip-only-package
```

Usage:

```bash
# Create environment from file
conda env create -f environment.yml

# Update existing environment
conda env update -f environment.yml
```

## Channels and Configuration

### What are Channels?

Channels are repositories where conda looks for packages. Default channels are maintained by Anaconda.

### Popular Channels

- **defaults**: Official Anaconda repository
- **conda-forge**: Community-driven repository (largest)
- **bioconda**: Bioinformatics packages
- **pytorch**: PyTorch and related packages

### Managing Channels

```bash
# Add channel
conda config --add channels conda-forge

# Set channel priority
conda config --set channel_priority strict

# List channels
conda config --show channels

# Remove channel
conda config --remove channels conda-forge

# Search package in specific channel
conda search -c conda-forge package-name
```

## Using Pip with Conda

### When to Use Pip

- Package not available in conda
- Specific pip-only package needed
- Installing from GitHub or local files

### Best Practices

```bash
# Always use pip within conda environment
conda activate myenv

# Install pip packages
pip install package-name

# Install from requirements.txt
pip install -r requirements.txt

# List pip packages
pip list

# Export pip packages
pip freeze > requirements.txt
```

### Combined Approach

```bash
# 1. Create conda environment
conda create --name myenv python=3.13

# 2. Install conda packages first
conda activate myenv
conda install numpy pandas matplotlib

# 3. Install pip packages last
pip install some-pip-only-package
```

## Common Workflows

### Data Science Setup

```bash
# Create environment
conda create --name ds_project python=3.13

# Activate environment
conda activate ds_project

# Install core packages
conda install numpy pandas matplotlib seaborn scikit-learn jupyter

# Install additional packages
conda install plotly statsmodels

# Launch Jupyter
jupyter notebook
```

### Machine Learning Setup

```bash
# Create environment
conda create --name ml_project python=3.13

# Activate environment
conda activate ml_project

# Install ML packages
conda install numpy pandas scikit-learn jupyter
conda install -c pytorch pytorch torchvision

# Install TensorFlow
pip install tensorflow

# Launch Jupyter
jupyter notebook
```

### Web Development Setup

```bash
# Create environment
conda create --name web_project python=3.13

# Activate environment
conda activate web_project

# Install web frameworks
conda install flask
pip install django fastapi
```

## Troubleshooting

### Common Issues and Solutions

#### 1. Conda command not found

```bash
# Windows: Use Anaconda Prompt
# macOS/Linux: Add to PATH
export PATH="/Users/<username>/anaconda3/bin:$PATH"
```

#### 2. Environment activation not working

```bash
# Initialize conda for your shell
conda init bash  # or zsh, fish, etc.

# Restart terminal
```

#### 3. Slow package resolution

```bash
# Use mamba (faster conda alternative)
conda install -c conda-forge mamba

# Use mamba instead of conda
mamba install numpy pandas
```

#### 4. Package conflicts

```bash
# Remove problematic packages
conda remove package-name

# Create fresh environment
conda create --name newenv python=3.13

# Install packages one by one
conda install numpy
conda install pandas
```

#### 5. Disk space issues

```bash
# Clean up
conda clean --all

# Remove unused packages
conda clean --packages

# Remove cached tarballs
conda clean --tarballs
```

### Getting Help

```bash
# General help
conda --help

# Command-specific help
conda install --help
conda create --help

# Check conda info
conda info
```

## Advanced Features

### Conda-Pack

Create portable environments:

```bash
# Install conda-pack
conda install -c conda-forge conda-pack

# Pack environment
conda pack -n myenv -o myenv.tar.gz

# Unpack on another machine
mkdir -p myenv
tar -xzf myenv.tar.gz -C myenv
source myenv/bin/activate
```

### Conda-Build

Create custom packages:

```bash
# Install conda-build
conda install conda-build

# Build package
conda build recipe/

# Install local package
conda install --use-local package-name
```

### Multiple Python Versions

```bash
# Install different Python versions
conda create --name py39 python=3.9
conda create --name py311 python=3.11
conda create --name py313 python=3.13

# Switch between versions
conda activate py39
conda activate py313
```

## Tips and Best Practices

1. **Keep base environment minimal**: Don't install packages in base
2. **Use environment.yml files**: For reproducibility
3. **Specify versions**: Pin important package versions
4. **Regular updates**: Keep conda and packages updated
5. **Clean regularly**: Use `conda clean --all` periodically
6. **Use conda-forge**: Often has more up-to-date packages
7. **Document environments**: Export and save environment files
8. **Separate environments**: One per project or purpose
9. **Activate before installing**: Always activate environment first
10. **Use mamba for speed**: Install mamba for faster operations

## Resources

- [Anaconda Documentation](https://docs.anaconda.com/)
- [Conda Documentation](https://docs.conda.io/)
- [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
- [Conda-Forge](https://conda-forge.org/)
- [Anaconda Package Repository](https://anaconda.org/)
- [Anaconda Community Forum](https://community.anaconda.cloud/)

## Quick Reference

### Essential Commands

```bash
# Environment
conda create --name myenv python=3.13
conda activate myenv
conda deactivate
conda env list

# Packages
conda install package-name
conda update package-name
conda remove package-name
conda list

# Maintenance
conda update conda
conda clean --all
conda info
```

### Environment File Template

```yaml
name: myproject
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.13
  - numpy
  - pandas
  - jupyter
```
