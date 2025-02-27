from uuid import UUID

import pytest
from dateutil import parser

from kiota_serialization_json.json_serialization_writer import JsonSerializationWriter

from ..helpers import OfficeLocation, User, User2


@pytest.fixture
def user_1():
    user = User()
    user.updated_at = parser.parse("2022-01-27T12:59:45.596117")
    user.is_active = True
    user.id = UUID("8f841f30-e6e3-439a-a812-ebd369559c36")
    return user


@pytest.fixture
def user_2():
    user = User2()
    user.age = 32
    user.display_name = "John Doe"
    return user


def test_write_str_value():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_str_value("displayName", "Adele Vance")
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"displayName": "Adele Vance"}'


def test_write_string_value_no_key():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_str_value(None, "Adele Vance")
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '"Adele Vance"'


def test_write_bool_value():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_bool_value("isActive", True)
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"isActive": true}'


def test_write_int_value():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_int_value("timestamp", 28192199291929192)
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"timestamp": 28192199291929192}'


def test_write_float_value():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_float_value("gpa", 3.2)
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"gpa": 3.2}'


def test_write_uuid_value():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_uuid_value("id", UUID("8f841f30-e6e3-439a-a812-ebd369559c36"))
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"id": "8f841f30-e6e3-439a-a812-ebd369559c36"}'


def test_write_datetime_value():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_datetime_value(
        "updatedAt", parser.parse('2022-01-27T12:59:45.596117')
    )
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"updatedAt": "2022-01-27T12:59:45.596117"}'


def test_write_timedelta_value():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_timedelta_value(
        "diff",
        parser.parse('2022-01-27T12:59:45.596117') - parser.parse('2022-01-27T10:59:45.596117')
    )
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"diff": "2:00:00"}'


def test_write_date_value():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_date_value("birthday", parser.parse("2000-09-04").date())
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"birthday": "2000-09-04"}'


def test_write_time_value():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_time_value(
        "time",
        parser.parse('2022-01-27T12:59:45.596117').time()
    )
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"time": "12:59:45.596117"}'


def test_write_collection_of_primitive_values():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_collection_of_primitive_values(
        "businessPhones", ["+1 412 555 0109", 1]
    )
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"businessPhones": ["+1 412 555 0109", 1]}'


def test_write_collection_of_object_values(user_1, user_2):
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_collection_of_object_values("users", [user_1, user_2])
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"users": [{"id": "8f841f30-e6e3-439a-a812-ebd369559c36", '\
        '"updated_at": "2022-01-27T12:59:45.596117", "is_active": true}, '\
        '{"display_name": "John Doe", "age": 32}]}'


def test_write_collection_of_enum_values():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_collection_of_enum_values(
        "officeLocation", [OfficeLocation.Dunhill, OfficeLocation.Oval]
    )
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"officeLocation": ["dunhill", "oval"]}'


def test_write_object_value(user_1):
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_object_value("user1", user_1)
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"user1": {"id": "8f841f30-e6e3-439a-a812-ebd369559c36", '\
        '"updated_at": "2022-01-27T12:59:45.596117", "is_active": true}}'


def test_write_enum_value():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_enum_value("officeLocation", OfficeLocation.Dunhill)
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"officeLocation": "dunhill"}'


def test_write_null_value():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_null_value("mobilePhone")
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"mobilePhone": null}'


def test_write_additional_data_value():
    json_serialization_writer = JsonSerializationWriter()
    json_serialization_writer.write_additional_data_value(
        {
            "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity",
            "businessPhones": ["+1 205 555 0108"],
        }
    )
    content = json_serialization_writer.get_serialized_content()
    content_string = content.decode('utf-8')
    assert content_string == '{"@odata.context": '\
        '"https://graph.microsoft.com/v1.0/$metadata#users/$entity", '\
            '"businessPhones": ["+1 205 555 0108"]}'
