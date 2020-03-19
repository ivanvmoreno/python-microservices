import json

# Base event class
class EventBase:
    def serialize(self):
        return json.dumps(self.__dict__)

    @classmethod
    def deserialize(cls, body):
        # Call child class constructor, passing JSON keys as keyword args
        return cls.__call__(**json.loads(body.decode('ascii')))
