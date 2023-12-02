import json
from mock import Mock

def deserialize_mock(json_data):
    # Create a new Mock object
    mock_obj = Mock()

    # Restore class name (if applicable)
    class_name = json_data.get("class_name")
    if class_name:
        # This assumes the class is present in the global namespace
        mock_obj.__class__ = globals()[class_name]

    # Restore attributes
    attributes = json_data.get("attributes", {})
    for attr, value in attributes.items():
        setattr(mock_obj, attr, value)

    # Restore methods
    methods = json_data.get("methods", [])
    for method in methods:
        # For simplicity, methods are restored as empty functions
        setattr(mock_obj, method, lambda *args, **kwargs: None)

    return mock_obj


def read_mock_object(file):
    # Load serialized data from JSON file
    with open(file, "r") as json_file:
        loaded_data = json.load(json_file)

    # Reconstruct the Mock object
    reconstructed_mock = deserialize_mock(loaded_data)

    return reconstructed_mock


def serialize_mock(mock_obj):
    # Extract the attributes and methods of the mock object
    mock_dict = {
        "class_name": str(mock_obj.__class__),
        "attributes": {attr: getattr(mock_obj, attr) for attr in dir(mock_obj) if not callable(getattr(mock_obj, attr)) and not attr.startswith("__")},
        "methods": [method for method in dir(mock_obj) if callable(getattr(mock_obj, method)) and not method.startswith("__")],
    }
    return mock_dict


def save_mock_object(file, mock_obj):

    # Serialize the mock object using the custom function
    serialized_mock = serialize_mock(mock_obj)

    # Save the serialized data to a JSON file
    with open(file, "w") as json_file:
        json.dump(serialized_mock, json_file, indent=2)
