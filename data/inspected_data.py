class InspectedAddressValue():

    INSPECTED_ADDRESS_VALUE = 'город Москва, поселение "Мосрентген", квартал № 8, дом 293, строение 1'

    NON_EXISTENT_ADDRESS = 'г. Москва, ул. Вайнера'

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

    INSPECTING_ID_PATTERN = {
        "type": "object",
        "properties": {
            "kind": {"type": "string"},
            "id": {"type": "integer"},
            "isActive": {"type": "boolean"},
            "name": {
                "type": "object",
                "properties": {
                    "default": {"type": "string"},
                    "formatted": {
                        "type": "object",
                        "properties": {
                            "administrative": {"type": "string"},
                            "municipal": {"type": "string"}
                        },
                        "required": ["administrative", "municipal"]
                    }
                },
                "required": ["default", "formatted"]
            },
            "ru:attributes": {
                "type": "object",
                "properties": {
                    "FiasId": {"type": "string"},
                    "IFNSFL": {"type": "string"},
                    "IFNSUL": {"type": "string"},
                    "OKATO": {"type": "string"},
                    "OKTMO": {"type": "string"},
                    "KLADR": {"type": "string"},
                    "LastChangeId": {"type": "string"},
                    "REGIONCODE": {"type": "string"}
                },
                "required": ["FiasId", "IFNSFL", "IFNSUL", "OKATO", "OKTMO", "KLADR", "LastChangeId", "REGIONCODE"]
            },
            "_embedded": {
                "type": "object",
                "properties": {
                    "elements": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "kind": {"type": "string"},
                                "name": {
                                    "type": "object",
                                    "properties": {
                                        "default": {"type": "string"},
                                        "official": {"type": ["string", "null"]},
                                        "structured": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "value": {"type": "string"},
                                                    "type": {
                                                        "type": "object",
                                                        "properties": {
                                                            "name": {"type": ["string", "null"]},
                                                            "shortName": {"type": ["string", "null"]}
                                                        },
                                                        "required": ["name", "shortName"]
                                                    }
                                                },
                                                "required": ["value", "type"]
                                            }
                                        }
                                    },
                                    "required": ["default"]
                                },
                                "_links": {
                                    "type": ["object", "null"],
                                    "properties": {
                                        "self": {
                                            "type": ["object", "null"],
                                            "properties":{
                                                "href":{"type":"string"},
                                                "method":{"type":"string"}
                                            }
                                        }
                                    }
                                },
                                "_embedded":{
                                    "$ref":"#/properties/_embedded"
                                }
                            },
                            "required":["kind","name"]
                        }
                    }
                }
            },
            "_links": {
                "$ref": "#/properties/_embedded/properties/elements/items/properties/_links"
            }
        },
        "$schema": "http://json-schema.org/draft-07/schema#"
    }




