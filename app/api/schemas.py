from app.extension.ext import ma

class PowerSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("date", "power")

class EnergySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("energy","date")

class ReactiveSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("reactive_energy","date")

class ActualStatus(ma.Schema):
    class Meta:
        fields = ('voltage','intensity','power_factor','reactive_power',
                  'power')

