
# Skillora-FastAPI

## How to Run

1. How to Run FastAPI Application localy.

```Shell
   uv run fastapi dev --app app.main
```

2. What is UV lock?

```Shell
uv lock
```
* Scope: It only touches the lockfile.
* Environment impact: It does not install, upgrade, or remove any packages in your active virtual environment.
* When to use: Use it when you want to explicitly refresh or generate the lockfile without altering your local machine's installed packages



3. What is UV sync?
```Shell
uv sync
```

* **Scope:** **It updates the actual environment (the** `.venv` **folder).**
* **Exact syncing:** **By default, it removes any extra packages installed in your environment that are no longer listed in the lockfile.**
* **When to use:** **Use it when setting up a project for the first time, cloning a repository, or ensuring your environment matches your team's locked dependencies.**
