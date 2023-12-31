### **Check out Client Side Application: [hsalen-app](https://github.com/danilojezernik/hsalen-app) (TypeScript, Angular, Angular Material, Bootstrap,...).**
# Server Side Application with Flask and PyMongo

For error free Heroku upload use: `pip freeze > requirements.txt`
Check for build log in case of errors and repair accordingly!

# Hypnosis Studio Alen 
Backend for Hypnosis Studio Alen.

## Table of Contents
* [About](#about)
* [Getting Started](#getting-started)
* [Deploy](#deploy)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## About
Provide a brief description of what your project does, its features, and its purpose.

## Getting Started

### Prerequisites
List any prerequisites or requirements needed to use or set up your project.

* Python (version)
* MongoDB (version)

### Installation
Provide step-by-step instructions on how to install and set up your project.

Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

Install dependencies using pip (or any package manager you use).
```bash
pip install -r requirements.txt
```

Configure environment variables (if needed).

```bash
cp .env.example .env
```
Modify the `.env` file to include necessary configurations.

### Running the Application
Explain how to run the application, including any necessary commands.

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Deploy
Before deploy on heroqu use:

```bash
pip freeze > requirements.txt
```


## Usage
Explain how to use your project, including API endpoints, functionalities, and examples.

## Contributing
Explain how others can contribute to your project and the guidelines for contributing.

1. Fork the project.
2. Create a new branch (`git checkout -b feature/yourfeature`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature/yourfeature`).
5. Open a pull request.

## License
Indicate the license under which your project is released.