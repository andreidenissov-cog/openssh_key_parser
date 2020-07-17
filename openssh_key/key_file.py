from openssh_key.pascal_style_byte_stream import (
    PascalStyleFormatInstruction,
    PascalStyleByteStream
)
from openssh_key.key_params import (
    create_public_key_params,
    create_private_key_params
)


class Key():
    @staticmethod
    def header_format_instructions_dict():
        return {
            'key_type': PascalStyleFormatInstruction.STRING
        }

    @staticmethod
    def footer_format_instructions_dict():
        return {}

    def __init__(self, key_byte_stream: PascalStyleByteStream, public_or_private):
        if public_or_private not in ['public', 'private']:
            raise ValueError()

        self.bytes = key_byte_stream.getvalue()

        self.header = key_byte_stream.read_from_format_instructions_dict(
            self.header_format_instructions_dict()
        )

        if public_or_private == 'public':
            params_class = create_public_key_params(self.header['key_type'])
            self.params = params_class(key_byte_stream.read_from_format_instructions_dict(
                create_public_key_params(
                    self.header['key_type']
                ).public_format_instructions_dict()
            ))
        elif public_or_private == 'private':
            params_class = create_private_key_params(self.header['key_type'])
            self.params = params_class(key_byte_stream.read_from_format_instructions_dict(
                create_private_key_params(
                    self.header['key_type']
                ).private_format_instructions_dict()
            ))

        self.footer = key_byte_stream.read_from_format_instructions_dict(
            self.footer_format_instructions_dict()
        )


class PublicKey(Key):
    def __init__(self, key_byte_stream):
        super().__init__(key_byte_stream, 'public')


class PrivateKey(Key):
    @staticmethod
    def footer_format_instructions_dict():
        return {
            'comment': PascalStyleFormatInstruction.STRING
        }

    def __init__(self, key_byte_stream):
        super().__init__(key_byte_stream, 'private')
