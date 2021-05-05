from flask import Blueprint
from flask_restful import Api, Resource
from .schemas import *
from .models import Energy
from flask_jwt import jwt_required
from app.extension.ext import cache

api_v1_0_bp = Blueprint('energy', __name__)

api = Api(api_v1_0_bp)

powerschema = PowerSchema(many=True)
energyeschema_month = EnergySchema(many=False)
statuseschema = ActualStatus(many=False)
reactiveschema = ReactiveSchema(many=False)


class power_time_series(Resource):
    @cache.memoize(timeout=50)
    def get(self,init_date,final_date):
        energy=Energy.filter_date_query(init_date,final_date,Energy.power)
        return powerschema.jsonify(energy)

class daily_power(Resource):
    @cache.memoize(timeout=50)
    def get(self,init_date,final_date):
        daily_energy=Energy.filter_date_query_daily(init_date,final_date,
                                                    Energy.power)
        return powerschema.jsonify(daily_energy)

class month_energy(Resource):
    @cache.memoize(timeout=50)
    def get(self):
        month_energy = Energy.get_actual_month(Energy.energy)
        return energyeschema_month.jsonify(month_energy)

class month_reactive(Resource):
    @cache.memoize(timeout=50)
    def get(self):
        month_energy = Energy.get_actual_month(Energy.reactive_energy)
        return reactiveschema.jsonify(month_energy)

class actual_estatus(Resource):
    @cache.memoize(timeout=50)
    @jwt_required()
    def get(self):
        status= Energy.get_status()
        return statuseschema.jsonify(status)

api.add_resource(actual_estatus, '/api/actual-status',
                 endpoint='actual-status')
api.add_resource(power_time_series,'/api/power-timeseries/'
                                   '<init_date>/<final_date>',
                 endpoint='power-series')
api.add_resource(daily_power,'/api/daily-power/<init_date>/<final_date>',
                 endpoint='daily-power')
api.add_resource(month_energy, '/api/actual-energy-month',
                 endpoint='power-month')
api.add_resource(month_reactive, '/api/actual-reactive-month',
                 endpoint='power-reactive-month')