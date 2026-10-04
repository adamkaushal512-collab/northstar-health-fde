from pathlib import Path

def test_deployment_artifacts_exist():
    for path in ["Dockerfile",".dockerignore","deploy/docker-compose.yml",
                 "deploy/env/dev.env.example","deploy/env/staging.env.example","deploy/env/prod.env.example"]:
        assert Path(path).exists()

def test_real_env_files_are_not_packaged():
    text=Path(".dockerignore").read_text()
    assert ".env" in text
