[![Python application](https://github.com/jermwatt/quick_batch/actions/workflows/python-app.yml/badge.svg)](https://github.com/jermwatt/quick_batch/actions/workflows/python-app.yml)
[![Upload Python Package](https://github.com/jermwatt/quick_batch/actions/workflows/python-publish.yml/badge.svg)](https://github.com/jermwatt/quick_batch/actions/workflows/python-publish.yml)

# quick_batch

`quick_batch` is an ultra-simple command-line tool for large batch python-driven processing and transformation.  It was designed to be fast to deploy, transparent, and portable.  This allows you to scale any `processor` function that needs to be run over a large set of input data, enabling batch/parallel processing of the input with minimal setup and teardown.


- [quick\_batch](#quick_batch)
- [Getting started](#getting-started)
  - [Usage](#usage)
  - [Installation](#installation)
  - [The `processor.py` file](#the-processorpy-file)
- [Why use quick\_batch](#why-use-quick_batch)

# Getting started

All you need to scale batch transformations with `quick_batch` is a

- transformation function(s) in a `processor.py` file
- optionally a `docker` image name or
  - `Dockerfile` containing a container build appropriate to y our processor
  - an optional `requirements.txt` file containing required python modules
    - custom `requirements.txt` require `flask`, `requests`, and `pyyaml`

Document paths to these objects as well as other parameters in a `config.yaml` config file of the form below


```yaml
data:
  input_path: /path/to/your/input/data
  output_path: /path/to/your/output/data
  log_path: /path/to/your/log/file

queue:
  feed_rate: <int - number of examples processed per processor instance>
  order_files: <boolean - whether or not to order input files by size>

processor:
  image_name: <pre-built-image-name>
  dockerfile_path: /path/to/your/Dockerfile
  requirements_path: /path/to/your/requirements.txt
  processor_path: /path/to/your/processor/processor.py
  num_processors: <int - instances of processor to run in parallel>

```

`quick_batch` will point your `processor.py` at the `input_path` defined in this `config.yaml` and process the files listed in it in parallel at a scale given by your choice of `num_processors`.  

Output will be written to the `output_path` specified in the configuration file.

You can see `tests/config_files` for examples of valid configs.


## Usage

With your `config.yaml` defined you can use `quick_batch` at the terminal by typing

```bash
quick_batch /path/to/your/config.yaml
```

## Installation

To install quick_batch, simply use `pip`:

```bash
pip install quick-batch
```

## The `processor.py` file

Create a `processor.py` file with the following basic pattern:

```python
import ...

def processor(todos):
  for file_name in todos.file_paths_to_process:
    # processing code
```

The `todos` object will carry in `feed_rate` number of file names to process in `.file_paths_to_process`.  

Note: the function name `processor` is mandatory.


# Why use quick_batch

quick_batch aims to be

- **dead simple to use:** versus standard cloud service batch transformation services that require significant configuration / service understanding

- **ultra fast setup:** versus setup of heavier orchestration tools like `airflow` or `mlflow`, which may be a hinderance due to time / familiarity / organisational constraints

- **100% portable:** - use quick_batch on any machine, anywhere

- **processor-invariant:** quick_batch works with arbitrary processes, not just machine learning or deep learning tasks.

- **transparent and open source:** quick_batch uses Docker under the hood and only abstracts away the not-so-fun stuff - including instantiation, scaling, and teardown.  you can still monitor your processing using familiar Docker command-line arguments (like `docker service ls`, `docker service logs`, etc.).

