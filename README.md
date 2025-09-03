[![main](https://github.com/liturgical-app/calendar-api/actions/workflows/main.yaml/badge.svg)](https://github.com/liturgical-app/calendar-api/actions/workflows/main.yaml)
<a><img src="./src/resources/coverage/coverage.svg"></a>

# Calendar Api
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-2a3035?logo=python&logoColor=ffdd54"></a>
<a href="https://github.com/features/actions"><img src="https://img.shields.io/badge/github%20actions-%232a3035.svg?logo=githubactions&logoColor=skyblue"></a>
<a href="https://render.com/"><img src="https://img.shields.io/badge/Render-%232a3035.svg?logo=render&logoColor=green"></a>

#### [api.liturgical.uk/\<yyyy-mm-dd>](https://api.liturgical.uk/2024-12-10)

<img alt="Calendar Example" width=480 src="https://github.com/liturgical-app/calendar-api/assets/34093915/0c7a3250-c68f-4e68-9463-9f40e7a3e9f7">

## Explanation
- 🗓 Get Liturgical information for a given date
- ℹ️ [More info?](https://pypi.org/project/liturgical-calendar/) 

## Run Locally
- 🔧 `pip install -r src/app/requirements.txt`
- 🚀 `gunicorn src.app.app:app`

## Pull image

```console
docker pull ghcr.io/liturgical-app/calendar-api:latest
```

- Stable releases are built as image tags, e.g. `1.0.0`
- The `latest` tag points to the latest stable release
- The `edge` tag is built from the latest commit to `main`
