class Base(object):
    def from_csv(self, headers, values):
        for header, value in zip(headers, values):
            if hasattr(self, header):
                value = self.validate_value(value)
                setattr(self, header, value)

    def validate_value(self, value):
        if value == 'True':
            value = True
        if value == 'False':
            value = False

        return value
