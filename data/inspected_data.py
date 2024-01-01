class InspectedAddressValue():

    INSPECTED_ADDRESS_VALUE = 'город Москва, поселение "Мосрентген", квартал № 8, дом 293, строение 1'

    # Для проверки json объекта в ответе с помощью jsonschema
    INSPECTING_ADDRESS_PATTERN = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "object",
                    "properties": {
                        "default": {"type": "string", "const": "г Москва, п Мосрентген, кв-л 8, д. 293, стр. 1"}
                    },
                    "required": ["default"]
                },
                "_links": {
                    "type": "object",
                    "properties": {
                        "self": {
                            "type": "object",
                            "properties": {
                                "href": {"type": "string", "const": "http://gar.gblinov.ru:18181/v1/Addresses/36173601"},
                                "method": {"type": "string", "const": "Get"}
                            },
                            "required": ["href", "method"]
                        }
                    },
                    "required": ["self"]
                }
            },
            "required": ["name", "_links"]
        }
    }

    NON_EXISTENT_ADDRESS = 'г. Москва, ул. Вайнера'

