from invoke import task


def __runall__(c, msg, cmds):
    print(f"###\n###\n###\n### {msg}\n###")
    [c.run(cmd) for cmd in cmds]  # pylint: disable=expression-not-assigned


@task
def build(c):
    __runall__(
        c,
        "Build",
        [
            "rm -rf build",
            "west build --board nrf52840dk_nrf52840",
        ],
    )
    c.run("rm -rf build")
