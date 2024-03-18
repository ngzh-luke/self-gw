# GW by LukeCreated

Personal Project: `GW` is a Python based web app powered by FastAPI to redirect to any given URL.

## About

- Expected live application link: [gw.lukecreated.com](https://gw.lukecreated.com)

- Developer: **Kittipich "Luke" Aiumbhornsin**

- Development Status: **Initial Development**

- License information: **LICENSE** [go to file](LICENSE)

- Development history: **CHANGELOG.md** [go to file](CHANGELOG.md)

Current Status: **Initial Development**

Current Version: **0.1.4**

Updated: **March 18, 2024**

## Instructions of running locally

1. change working directory on terminal using `cd` command to where the project will be saved

2. at the desire directory, clone the repo by run command:
`git clone https://github.com/ngzh-luke/self-gw.git`

3. if already cloned, update the local repository by run command:
`git pull`

4. create virtual environment by run command:
`python -m venv venv`

5. check to see that the virtual is at the virtual environment is created by run command: `which pip`

6. activate virtual environment (macOS) by run command:
`source venv/bin/activate`
activate virtual environment (Windows) by run command: `venv\Scripts\activate`

7. install project dependencies by run command:
`pip install -r requirements/base.txt`

8. run command to start the application:
`uvicorn main:app --reload`

9. check out the running application on browser by navigate to: `127.0.0.1:8000`

10. impressed by the cool application!

---

### TODO for developer

- complete auth
- complete root
- complete redirector
- others

### Resources

- <https://github.com/zhanymkanov/fastapi-best-practices>
- <https://github.com/zhanymkanov/fastapi_production_template>
