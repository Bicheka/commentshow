# Comment_show
## Sharing honest thoughts about shows and movies
<p>Commentshow is meant to be a hub to share comments about shows</p>

## Stack
<p>This project follows a feature driven development design</p>
<p>Powered by FastApi as backend framework and MongoDB as database</p>

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

