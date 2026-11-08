
from marshmallow import Schema, fields, validate, EXCLUDE


class CustomerSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    customer_id = fields.String(
        required=True,
        validate=validate.Length(min=1, max=5)
    )

    company_name = fields.String(
        required=True,
        validate=validate.Length(min=1, max=100)
    )

    contact_name = fields.String(
        load_default=None,
        allow_none=True
    )

    contact_title = fields.String(
        load_default=None,
        allow_none=True
    )

    address = fields.String(load_default=None, allow_none=True)
    city = fields.String(load_default=None, allow_none=True)
    region = fields.String(load_default=None, allow_none=True)
    postal_code = fields.String(load_default=None, allow_none=True)
    country = fields.String(load_default=None, allow_none=True)
    phone = fields.String(load_default=None, allow_none=True)
    fax = fields.String(load_default=None, allow_none=True)
