![FastAPI icon](https://camo.githubusercontent.com/580b7032c938b3cbf4f2547383a8d43d86aba159622747f1993b0e45c04f0665/68747470733a2f2f666173746170692e7469616e676f6c6f2e636f6d2f696d672f6c6f676f2d6d617267696e2f6c6f676f2d7465616c2e706e67)

# Sending Form - FastAPI Backend

This is a [FastAPI](https://fastapi.tiangolo.com/) project built using [FastAPI](https://github.com/tiangolo/fastapi), which provides fast development and high performance.

## Getting Started

First, start the development server:
    
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

Open [http://localhost:8000](http://localhost:3000) in your browser to view the result. There you will be able to see the main page of the site. P.s. links on the main page lead to the production server

You can start editing the code in the project files. The server will automatically reboot when the changes are saved.

## Running in Docker

First, build the image:

```bash
docker-compose build
```

Then, start the container:

```bash
docker-compose up
```

Open [http://localhost:8000](http://localhost:3000) in your browser to view the result. There you will be able to see the main page of the site.

## API documentation

FastAPI provides automatically generated documentation for your API. You can open [http://localhost:8000/docs](http://localhost:8000/docs) to see the available API paths and their parameters.

## Learn More

For more information about FastAPI, visit the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/) - learn about FastAPI features and API.
- [FastAPI User Guide](https://fastapi.tiangolo.com/tutorial/) - an interactive FastAPI tutorial.
- [FastAPI GitHub Repository](https://github.com/tiangolo/fastapi) - your feedback and contributions are welcome!

## Deployment

A quick way to deploy your FastAPI application is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out the [FastAPI deployment documentation](https://fastapi.tiangolo.com/deployment) for more details.