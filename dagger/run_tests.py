# referenced with modifications from:
# https://docs.dagger.io/sdk/python/628797/get-started
"""Run tests for multiple Python versions concurrently."""

import sys

import anyio

import dagger


async def test(versions):

    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        # get reference to the local project
        src = client.host().directory(".")

        async def test_version(version: str):
            python = (
                client.container()
                .from_(f"python:{version}-slim-buster")
                # mount cloned repository into image
                .with_mounted_directory("/demo-github-actions", src)
                # set current working directory for next commands
                .with_workdir("/demo-github-actions")
                # install test dependencies
                .with_exec(["pip", "install", "poetry==1.4"])
                .with_exec(["poetry", "install"])
                # run tests
                .with_exec(["poetry", "run", "python", "-m", "pytest"])
            )

            print(f"Starting tests for Python {version}")

            # execute
            await python.exit_code()

            print(f"Tests for Python {version} succeeded!")

        # when this block exits, all tasks will be awaited (i.e., executed)
        async with anyio.create_task_group() as tg:
            for version in versions:
                tg.start_soon(test_version, version)

    print("All tasks have finished")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        py_versions = sys.argv[1:]
    else:
        py_versions = ["3.10", "3.11"]

    anyio.run(test, py_versions)

