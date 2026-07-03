from kernel.container.container import Container


def test_register():

    container = Container()

    service = object()

    container.singleton(
        "service",
        service,
    )

    assert container.exists("service")


def test_resolve():

    container = Container()

    value = object()

    container.singleton(
        "db",
        value,
    )

    assert container.resolve("db") is value
