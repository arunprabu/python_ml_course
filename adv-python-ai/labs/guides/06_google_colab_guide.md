# Google Colab Guide

## What is Google Colab?

Google Colaboratory (Colab) is a free, cloud-based Jupyter notebook environment that runs entirely in the cloud and provides free access to computing resources including GPUs and TPUs. It requires no setup and runs entirely in your browser, making it ideal for machine learning, data analysis, and education.

### Key Features

- **Free GPU/TPU Access**: NVIDIA Tesla T4 GPU and Google TPU at no cost
- **Zero Setup**: No installation required, runs in browser
- **Cloud-Based**: Access from anywhere with internet
- **Google Drive Integration**: Save and load files seamlessly
- **Pre-installed Libraries**: TensorFlow, PyTorch, pandas, NumPy, and more
- **Real-time Collaboration**: Work with others like Google Docs
- **Easy Sharing**: Share notebooks via link
- **GitHub Integration**: Import/export from GitHub repositories
- **Form Controls**: Interactive widgets for parameters

## Getting Started

### Accessing Google Colab

#### Method 1: Direct Access

1. Visit [https://colab.research.google.com](https://colab.research.google.com)
2. Sign in with your Google account
3. Start using immediately

#### Method 2: From Google Drive

1. Open Google Drive
2. Right-click → More → Google Colaboratory
3. If not available, install Colab from Google Workspace Marketplace

#### Method 3: From GitHub

1. Go to Colab homepage
2. Click "GitHub" tab
3. Enter repository URL
4. Select notebook to open

### Creating Your First Notebook

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Click "New Notebook" or File → New Notebook
3. Notebook opens with default name "Untitled0.ipynb"
4. Rename: Click title and enter new name
5. Notebook auto-saves to Google Drive in "Colab Notebooks" folder

## Google Colab Interface

### Main Components

#### 1. Menu Bar (Top)

- **File**: New, open, save, download options
- **Edit**: Cut, copy, paste, find/replace
- **View**: Show/hide sections, table of contents
- **Insert**: Add code/text cells
- **Runtime**: Manage runtime, change runtime type
- **Tools**: Settings, keyboard shortcuts, diff
- **Help**: Documentation, tutorials, shortcuts

#### 2. Toolbar

- **+ Code**: Add code cell
- **+ Text**: Add text (markdown) cell
- **Files** 📁: File browser
- **RAM/Disk** 💾: Resource usage
- **Connect**: Connect to runtime

#### 3. Code Cells

```python
# Execute Python code here
print("Hello, Colab!")
```

#### 4. Text Cells

```markdown
# Write formatted text in Markdown

**Bold**, _italic_, `code`, [links](url)
```

#### 5. Left Sidebar

- **Table of Contents**: Navigate document
- **Find and Replace**: Search in notebook
- **Files**: Browse files and upload
- **Code Snippets**: Ready-made code examples
- **Secrets**: Store API keys securely

#### 6. Right Sidebar (when cell selected)

- **Comments**: Add/view comments
- **Variables**: Inspect variable values
- **Code**: View generated code

## Working with Cells

### Cell Types

#### Code Cells

Execute Python code:

```python
# Code cell example
import numpy as np
x = np.array([1, 2, 3, 4, 5])
print(f"Mean: {x.mean()}")
```

#### Text Cells

Write formatted documentation:

````markdown
## Section Title

This is a **text cell** with _markdown_ formatting.

- Bullet point 1
- Bullet point 2

```python
# You can include code blocks
print("example")
```
````

````

### Adding Cells

**Using Buttons:**
- Click "+ Code" or "+ Text" in toolbar
- Or hover over cell, click "+ Code" or "+ Text"

**Using Keyboard Shortcuts:**
- `Ctrl/Cmd + M B`: Insert code cell below
- `Ctrl/Cmd + M A`: Insert code cell above

### Running Cells

**Run Single Cell:**
- Click ▶️ play button on left of cell
- Or press `Shift + Enter` (run and move to next)
- Or press `Ctrl/Cmd + Enter` (run and stay)

**Run Multiple Cells:**
- Runtime → Run all
- Runtime → Run before
- Runtime → Run after
- Runtime → Run selection

**Keyboard Shortcuts:**
- `Shift + Enter`: Run cell, select below
- `Ctrl/Cmd + Enter`: Run cell
- `Alt + Enter`: Run cell, insert below

### Cell Operations

**Delete Cell:**
- Click trash icon 🗑️
- Or select cell and press `Ctrl/Cmd + M D`

**Move Cell:**
- Drag cell up/down using ⋮⋮ handle
- Or `Ctrl/Cmd + M K` (move up)
- Or `Ctrl/Cmd + M J` (move down)

**Copy/Cut/Paste:**
- Select cell and use Edit menu
- Or keyboard shortcuts

**Convert Cell Type:**
- `Ctrl/Cmd + M Y`: Convert to code
- `Ctrl/Cmd + M M`: Convert to markdown

## GPU and TPU Access

### Enabling GPU

1. **Change Runtime Type:**
   - Runtime → Change runtime type
   - Hardware accelerator → GPU
   - GPU type → T4 (free tier)
   - Click "Save"

2. **Verify GPU Access:**
```python
import tensorflow as tf
print("GPU Available:", tf.config.list_physical_devices('GPU'))

# Or check with torch
import torch
print("GPU Available:", torch.cuda.is_available())
print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")
````

3. **Check GPU Details:**

```python
# Using nvidia-smi command
!nvidia-smi
```

### Enabling TPU

1. **Change Runtime Type:**

   - Runtime → Change runtime type
   - Hardware accelerator → TPU
   - Click "Save"

2. **Configure TPU for TensorFlow:**

```python
import tensorflow as tf

# Connect to TPU
tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
print(f'Running on TPU: {tpu.master()}')

tf.config.experimental_connect_to_cluster(tpu)
tf.tpu.experimental.initialize_tpu_system(tpu)

# Create TPU strategy
strategy = tf.distribute.TPUStrategy(tpu)

print(f"Number of accelerators: {strategy.num_replicas_in_sync}")
```

### GPU/TPU Limitations

**Free Tier Limits:**

- **Session Duration**: 12 hours maximum
- **Idle Timeout**: 90 minutes of inactivity
- **GPU Availability**: Not guaranteed, subject to availability
- **RAM**: 12-13 GB (can vary)
- **Disk**: ~78 GB temporary storage
- **No Background Execution**: Session ends when browser closes

**Colab Pro ($10/month):**

- Longer runtimes (up to 24 hours)
- More RAM (up to 25 GB)
- Faster GPUs (V100, A100 priority access)
- Background execution

**Colab Pro+ ($50/month):**

- Even longer runtimes
- More RAM (up to 50 GB)
- Priority access to best GPUs
- Faster execution

## Google Drive Integration

### Mounting Google Drive

```python
from google.colab import drive
drive.mount('/content/drive')
```

**Access Files:**

```python
# Navigate to your Drive
import os
os.chdir('/content/drive/MyDrive')

# List files
!ls

# Read file
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/data.csv')

# Save file
df.to_csv('/content/drive/MyDrive/results.csv', index=False)
```

### File Paths

**Drive Root:**

```python
'/content/drive/MyDrive/'  # Your Google Drive root
```

**Colab Notebooks:**

```python
'/content/drive/MyDrive/Colab Notebooks/'  # Default notebook location
```

**Access Shared Drives:**

```python
'/content/drive/Shareddrives/TeamDrive/'
```

## File Management

### Uploading Files

**Method 1: File Browser**

1. Click 📁 Files icon in left sidebar
2. Click upload icon ⬆️
3. Select files to upload
4. Files go to `/content/` directory

**Method 2: Code**

```python
from google.colab import files
uploaded = files.upload()

# Access uploaded file
for filename in uploaded.keys():
    print(f'Uploaded: {filename} ({len(uploaded[filename])} bytes)')
```

### Downloading Files

**Method 1: File Browser**

1. Right-click file in file browser
2. Click "Download"

**Method 2: Code**

```python
from google.colab import files
files.download('results.csv')
```

**Download Multiple Files:**

```python
# Zip files first
!zip -r results.zip /content/results/

# Download zip
from google.colab import files
files.download('results.zip')
```

### Working with Files

**Check Current Directory:**

```python
!pwd
```

**List Files:**

```python
!ls -la
```

**Create Directory:**

```python
!mkdir mydata
```

**Copy Files:**

```python
!cp source.txt destination.txt
```

**Remove Files:**

```python
!rm filename.txt
!rm -rf directory/
```

## Installing Packages

### Using pip

```python
# Install package
!pip install transformers

# Install specific version
!pip install numpy==1.24.3

# Install from GitHub
!pip install git+https://github.com/user/repo.git

# Install quietly (suppress output)
!pip install -q opencv-python

# Upgrade package
!pip install --upgrade tensorflow
```

### Using apt-get (System Packages)

```python
# Update package list
!apt-get update

# Install system package
!apt-get install -y graphviz

# Example: Install ffmpeg
!apt-get install -y ffmpeg
```

### Checking Installed Packages

```python
# List installed packages
!pip list

# Show specific package info
!pip show numpy

# Check package version
import numpy as np
print(np.__version__)
```

## Data Loading Methods

### From URL

```python
import pandas as pd

# Load CSV from URL
url = 'https://example.com/data.csv'
df = pd.read_csv(url)

# Download file from URL
!wget https://example.com/dataset.zip
!unzip dataset.zip
```

### From Google Drive

```python
from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/data.csv')
```

### From Kaggle

```python
# Install Kaggle
!pip install -q kaggle

# Upload kaggle.json (API credentials)
from google.colab import files
files.upload()  # Select kaggle.json

# Setup Kaggle
!mkdir ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# Download dataset
!kaggle datasets download -d username/dataset-name
!unzip dataset-name.zip
```

### From GitHub

```python
# Clone repository
!git clone https://github.com/username/repository.git

# Navigate to repo
%cd repository

# Pull latest changes
!git pull
```

### Upload from Local

```python
from google.colab import files
uploaded = files.upload()

# Use uploaded file
import pandas as pd
import io
df = pd.read_csv(io.BytesIO(uploaded['data.csv']))
```

## Magic Commands

### Colab-Specific Magic Commands

```python
# Time execution of a line
%time result = sum(range(1000000))

# Time average execution (multiple runs)
%timeit sum(range(1000000))

# Time entire cell
%%time
x = []
for i in range(1000000):
    x.append(i)

# Write cell contents to file
%%writefile script.py
def hello():
    print("Hello from file")

# Execute Python file
%run script.py

# Load external file into cell
%load script.py

# Show current working directory
%pwd

# Change directory
%cd /content/drive/MyDrive/

# List files
%ls

# Display matplotlib plots inline
%matplotlib inline

# Enable interactive plots
%matplotlib notebook

# Show environment variables
%env

# Set environment variable
%env API_KEY=your_key_here

# Show history
%history

# Who - list variables
%who

# Who with types
%whos

# Reset namespace (delete all variables)
%reset
```

### Shell Commands

```python
# Any shell command with !
!python --version
!pip freeze
!ls -la
!df -h  # Disk usage
!free -h  # Memory usage
!nvidia-smi  # GPU info
!cat file.txt  # Display file contents
!head -n 5 data.csv  # Show first 5 lines
!tail -n 5 data.csv  # Show last 5 lines
!wc -l file.txt  # Count lines
!grep "pattern" file.txt  # Search in file
```

## Widgets and Forms

### Creating Interactive Forms

```python
#@title Configuration { run: "auto" }

# Slider
learning_rate = 0.001 #@param {type:"slider", min:0.0001, max:0.1, step:0.0001}

# Number input
epochs = 10 #@param {type:"number"}

# Text input
model_name = "my_model" #@param {type:"string"}

# Dropdown
optimizer = "Adam" #@param ["Adam", "SGD", "RMSprop"]

# Boolean
use_augmentation = True #@param {type:"boolean"}

# Date
start_date = "2024-01-01" #@param {type:"date"}

print(f"Learning Rate: {learning_rate}")
print(f"Epochs: {epochs}")
print(f"Model: {model_name}")
print(f"Optimizer: {optimizer}")
print(f"Augmentation: {use_augmentation}")
```

### Using ipywidgets

```python
import ipywidgets as widgets
from IPython.display import display

# Slider
slider = widgets.IntSlider(value=50, min=0, max=100, description='Value:')
display(slider)

# Button
button = widgets.Button(description='Click Me!')
output = widgets.Output()

def on_button_click(b):
    with output:
        print("Button clicked!")

button.on_click(on_button_click)
display(button, output)

# Dropdown
dropdown = widgets.Dropdown(
    options=['Option 1', 'Option 2', 'Option 3'],
    value='Option 1',
    description='Select:'
)
display(dropdown)
```

## Collaboration Features

### Real-time Collaboration

1. **Share Notebook:**

   - Click "Share" button (top-right)
   - Add collaborators' email addresses
   - Set permissions (Viewer, Commenter, Editor)
   - Copy shareable link

2. **Comment on Cells:**

   - Select cell
   - Click comment icon 💬 in right sidebar
   - Add comment
   - Tag collaborators with @email

3. **View Collaborators:**
   - See who's currently viewing (top-right)
   - See cursor positions of editors

### Version History

1. **View History:**

   - File → Revision History
   - See all saved versions
   - Compare versions
   - Restore previous versions

2. **Save Checkpoint:**
   - File → Save and checkpoint
   - Create named checkpoint

## Best Practices

### Resource Management

```python
# 1. Check RAM usage
!free -h

# 2. Check disk usage
!df -h

# 3. Monitor GPU memory
!nvidia-smi

# 4. Clear output to save memory
from IPython.display import clear_output
clear_output()

# 5. Delete large variables when done
import gc
del large_variable
gc.collect()

# 6. Use generators for large datasets
def data_generator():
    for i in range(1000000):
        yield i

# 7. Process data in chunks
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    process(chunk)
```

### Avoiding Session Timeouts

```python
# 1. Save progress frequently to Drive
import pickle

# Save model
with open('/content/drive/MyDrive/model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Load model
with open('/content/drive/MyDrive/model.pkl', 'rb') as f:
    model = pickle.load(f)

# 2. Use checkpoints during training
# TensorFlow
callbacks = [
    tf.keras.callbacks.ModelCheckpoint(
        '/content/drive/MyDrive/checkpoints/model_{epoch}.h5',
        save_freq='epoch'
    )
]

# PyTorch
if epoch % 5 == 0:
    torch.save(model.state_dict(),
               f'/content/drive/MyDrive/checkpoint_{epoch}.pth')

# 3. Keep browser tab active
# 4. Use Colab Pro for longer sessions
```

### Code Organization

```python
# 1. Use sections with markdown headers
"""
# Data Loading
Load and preprocess data
"""

# 2. Add table of contents
# View → Table of contents

# 3. Use descriptive cell titles
#@title Load and Preprocess Data

# 4. Add comments
# Clear, descriptive comments help collaboration

# 5. Modular code
def load_data():
    """Load data from Drive"""
    pass

def preprocess():
    """Preprocess data"""
    pass

def train_model():
    """Train model"""
    pass

# 6. One task per cell
# Keep cells focused and reusable
```

### Security Best Practices

```python
# 1. Use Secrets for API keys
from google.colab import userdata
api_key = userdata.get('API_KEY')

# 2. Don't hardcode credentials
# ❌ Bad
api_key = "sk-12345..."

# ✅ Good
api_key = userdata.get('API_KEY')

# 3. Clear sensitive output
from IPython.display import clear_output
# ... code that shows sensitive info ...
clear_output()

# 4. Don't commit notebooks with secrets to public repos
```

## Common Workflows

### Machine Learning Training

```python
# Complete ML workflow
#@title Setup
!pip install -q tensorflow

from google.colab import drive
drive.mount('/content/drive')

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Enable GPU
print("GPU:", tf.config.list_physical_devices('GPU'))

#@title Load Data
df = pd.read_csv('/content/drive/MyDrive/data.csv')
print(df.shape)
df.head()

#@title Preprocess
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#@title Build Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#@title Train
checkpoint_path = '/content/drive/MyDrive/checkpoints/model_{epoch}.h5'
callbacks = [
    tf.keras.callbacks.ModelCheckpoint(checkpoint_path, save_freq='epoch'),
    tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
]

history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=50,
    batch_size=32,
    callbacks=callbacks
)

#@title Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {test_acc:.4f}')

#@title Visualize
plt.plot(history.history['accuracy'], label='train')
plt.plot(history.history['val_accuracy'], label='val')
plt.legend()
plt.show()

#@title Save Final Model
model.save('/content/drive/MyDrive/final_model.h5')
```

### Data Analysis

```python
#@title Setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

#@title Load Data
df = pd.read_csv('/content/drive/MyDrive/data.csv')

#@title Explore
print(df.shape)
print(df.info())
df.describe()

#@title Clean
# Handle missing values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

#@title Analyze
# Group by analysis
summary = df.groupby('category').agg({
    'value': ['mean', 'std', 'count']
})
print(summary)

#@title Visualize
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

df['value'].hist(ax=axes[0, 0])
axes[0, 0].set_title('Distribution')

df.boxplot(column='value', by='category', ax=axes[0, 1])

sns.heatmap(df.corr(), annot=True, ax=axes[1, 0])

df.plot(x='date', y='value', ax=axes[1, 1])

plt.tight_layout()
plt.show()

#@title Export Results
df.to_csv('/content/drive/MyDrive/cleaned_data.csv', index=False)
```

## Keyboard Shortcuts

### Cell Operations

```
Ctrl/Cmd + M B: Insert cell below
Ctrl/Cmd + M A: Insert cell above
Ctrl/Cmd + M D: Delete cell
Ctrl/Cmd + M Z: Undo cell deletion
Ctrl/Cmd + M Y: Convert to code cell
Ctrl/Cmd + M M: Convert to text cell
```

### Running Cells

```
Shift + Enter: Run cell, select below
Ctrl/Cmd + Enter: Run cell
Alt + Enter: Run cell, insert below
Ctrl/Cmd + F9: Run all cells
Ctrl/Cmd + Shift + F9: Run all above
```

### Editing

```
Ctrl/Cmd + S: Save
Ctrl/Cmd + /: Comment/uncomment
Tab: Indent or autocomplete
Shift + Tab: Show documentation
Ctrl/Cmd + ]: Indent
Ctrl/Cmd + [: Dedent
Ctrl/Cmd + Z: Undo
Ctrl/Cmd + Y: Redo
```

### Navigation

```
Ctrl/Cmd + Alt + N: Focus next cell
Ctrl/Cmd + Alt + P: Focus previous cell
Ctrl/Cmd + M H: Show keyboard shortcuts
Ctrl/Cmd + F: Find
Ctrl/Cmd + H: Find and replace
```

## Troubleshooting

### Common Issues

#### 1. Session Disconnected

```python
# Reconnect
# Click "Reconnect" button
# Or Runtime → Restart runtime

# Check if reconnected
print("Connected!")
```

#### 2. Out of Memory

```python
# Clear variables
%reset

# Or delete specific variables
del large_variable
import gc
gc.collect()

# Use smaller batch sizes
batch_size = 16  # Instead of 32

# Process data in chunks
```

#### 3. Package Import Errors

```python
# Reinstall package
!pip uninstall -y package_name
!pip install package_name

# Or install specific version
!pip install package_name==version
```

#### 4. GPU Not Available

```python
# Check runtime type
# Runtime → Change runtime type → GPU

# Verify GPU
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))

# Restart runtime if needed
```

#### 5. Files Not Found

```python
# Check current directory
!pwd

# List files
!ls

# Mount Drive if accessing Drive files
from google.colab import drive
drive.mount('/content/drive')
```

## Tips and Tricks

### Productivity Tips

```python
# 1. Use code snippets
# Click </> icon in left sidebar
# Browse and insert ready-made code

# 2. Use scratch cells
# Click "Scratch code cell" in Insert menu
# Temporary cells that aren't saved

# 3. Link to specific cells
# Right-click cell → Copy cell link
# Share links to specific parts of notebook

# 4. Use table of contents
# View → Table of contents
# Click headers to navigate

# 5. Hide code cells
# Double-click on output to hide code
# Or use #@title directive

# 6. Use forms for parameters
learning_rate = 0.01 #@param {type:"slider", min:0.001, max:0.1}

# 7. Search through notebooks
# Ctrl/Cmd + Shift + H
# Search across all your notebooks

# 8. Use keyboard shortcuts
# Ctrl/Cmd + M H to see all shortcuts
```

### Advanced Features

```python
# 1. Connect to local runtime
# Use your own machine's GPU
# Tools → Settings → Manage local runtimes

# 2. Use TensorBoard
%load_ext tensorboard
%tensorboard --logdir logs

# 3. Create notebook badges
# Add badge to GitHub README
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/user/repo/blob/main/notebook.ipynb)

# 4. Schedule notebook execution
# Not built-in, but can use:
# - GitHub Actions
# - Cloud Functions
# - Papermill

# 5. Export to GitHub
# File → Save a copy in GitHub
# Commit directly to repository
```

## Resources

### Official Resources

- [Google Colab Homepage](https://colab.research.google.com)
- [Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Colab Welcome Notebook](https://colab.research.google.com/notebooks/intro.ipynb)
- [Colab Features Overview](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)

### Tutorials

- [TensorFlow with Colab](https://www.tensorflow.org/tutorials)
- [PyTorch with Colab](https://pytorch.org/tutorials/)
- [Kaggle with Colab](https://www.kaggle.com/discussions)
- [Fast.ai with Colab](https://course.fast.ai/)

### Community

- [r/GoogleColab](https://www.reddit.com/r/GoogleColab/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/google-colaboratory)

## Comparison: Free vs Pro vs Pro+

| Feature              | Free     | Pro ($10/mo)   | Pro+ ($50/mo)         |
| -------------------- | -------- | -------------- | --------------------- |
| Session Length       | 12 hours | 24 hours       | 24 hours              |
| Idle Timeout         | 90 min   | 24 hours       | 24 hours              |
| RAM                  | 12-13 GB | Up to 25 GB    | Up to 50 GB           |
| GPU                  | T4       | T4, P100, V100 | V100, A100 (priority) |
| Background Execution | No       | Yes            | Yes                   |
| Priority Access      | No       | Yes            | Highest priority      |
| Compute Units        | Limited  | More           | Most                  |

## Conclusion

Google Colab is an excellent platform for:

- Learning machine learning and data science
- Prototyping ML models
- Running experiments with free GPU/TPU
- Collaborating on notebooks
- Teaching and creating tutorials
- Quick data analysis without setup

It's particularly valuable for students, researchers, and anyone who needs computational resources without investing in expensive hardware. While it has limitations (session timeouts, no persistent storage), proper workflow management and use of Google Drive integration makes it a powerful tool for AI development.
