import subprocess
import docker


def check_docker_version():
    client = docker.from_env()
    version = client.version()["Version"]
    print(f"Docker version: {version}")


def build_image():
    client = docker.from_env()
    image, _ = client.images.build(
        path="files", dockerfile="Dockerfile", tag="hello-world-image")
    print(f"Image created with ID: {image.id}")


def create_container():
    client = docker.from_env()
    container = client.containers.create(
        image="hello-world-image", command="python app.py", name="hello-world-container", detach=True)
    print(f"Container created with ID: {container.id}")


def start_container():
    client = docker.from_env()
    container = client.containers.get("hello-world-container")
    container.start()
    print("Container started")


def stop_container():
    client = docker.from_env()
    container = client.containers.get("hello-world-container")
    container.stop()
    print("Container stopped")


def remove_container():
    client = docker.from_env()
    container = client.containers.get("hello-world-container")
    container.remove()
    print("Container removed")


if __name__ == "__main__":
    check_docker_version()
    build_image()
    create_container()
    start_container()
    # wait for a while to see the output
    subprocess.run(["sleep", "10"])
    stop_container()
    remove_container()
