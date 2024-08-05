# commentshow 
<p>This project follows a feature driven development design and is powered by fastapi and mongodb as database</p>

## To set up poetry
### only if poetry is not installed
```
pip install poetry
```
### to make the virtual enviroments be created in the project folder
```
poetry config virtualenvs.in-project true
```

## Install dependecies and run app
### 1. install poetry (all dependencies)
```
poetry install
```

### 2. to run fastapi
```
fastapi dev main.py
```

### to add dependency
```
poetry add [name]
```

### to remove dependency
```
poetry remove [name]
```

