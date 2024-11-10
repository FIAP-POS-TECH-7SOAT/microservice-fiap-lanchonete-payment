from marshmallow import Schema, fields, validates, ValidationError

class ProcessPaymentRequestValidator(Schema):
    amount = fields.Float(required=True)
    order_id = fields.Str(required=True)
    customer = fields.Nested(
        {
            "email": fields.Email(required=True),
            "doc_number": fields.Str(required=True, validate=lambda x: len(x) in [11, 14])
        },
        required=True
    )

    @validates("amount")
    def validate_amount(self, value):
        if value <= 0:
            raise ValidationError("Amount must be greater than zero.")
