import inspect

def pytest_collection_modifyitems(config, items):
    for item in items:
        doc = inspect.getdoc(item.obj)
        if not doc:
            continue

        first_line = doc.strip().splitlines()[0].strip()

        item._nodeid = f"{item.nodeid}  —  {first_line}"
