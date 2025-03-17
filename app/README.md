# Demo Flask App

The Demo app does absolutely nothing

## Getting started

- Create a virtual environment (make sure you have virtualenv installed and setup)

    ```
    virtualenv venv
    ```

- Activate the Virtual environment

    ```
    source venv/bin/activat
    ```

- Install requirements

    ```
    pip install -r requirements.txt
    ```

- Starting the application

    ```
    python server.py
    ```

## Running tests

We are using pytest for tests
```
python -m unittest test_server.py
```

## DOCKER 

- Build and tag a docker image; replace `demo-app` with whatever you want to name the image. 

    ```
    docker build -t demo-app .
    ```

- Run the container
    ```
    docker run -p 5000:5000 demo-app
    ```

- Push the image to a repository
    ```
    ```
