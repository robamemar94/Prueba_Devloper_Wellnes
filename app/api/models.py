
from sqlalchemy import extract, func
from .utils import parse_time
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask
from app.config.default import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Energy(db.Model):
    __tablename__ = 'energia'

    date = db.Column(db.DateTime, primary_key=True)
    energy = db.Column(db.Float, primary_key=False)
    reactive_energy = db.Column(db.Float, primary_key=False)
    power = db.Column(db.Float, primary_key=False)
    maximeter = db.Column(db.Float, primary_key=False)
    reactive_power = db.Column(db.Float, primary_key=False)
    voltage = db.Column(db.Float, primary_key=False)
    intensity = db.Column(db.Float, primary_key=False)
    power_factor = db.Column(db.Float, primary_key=False)

    @staticmethod
    def filter_date_query(init_date, final_date, column):
        """ Función para obtener los registros en le intervalo marcado

        :param init_date: Fecha inicial del intervalo
        :param final_date: Fecha final del intervalo
        :param Column: Columna con la variable que queremos obtener"""

        init_date = parse_time(init_date)
        final_date = parse_time(final_date)
        energy = db.session.query(Energy.date, column). \
            filter(Energy.date <= final_date).filter(
            Energy.date >= init_date).all()
        return energy

    @staticmethod
    def filter_date_query_daily(init_date,final_date,column):
        """ Función para obtener el valor diario de una variable en el
        periodo de tiempo indicado

        :param init_date: Fecha inicial del intervalo
        :param final_date: Fecha final del intervalo
        :param Column: Columna con la variable que queremos obtener"""

        init_date = parse_time(init_date)
        final_date = parse_time(final_date)

        daily_energy=db.session.query(Energy.date,func.sum(column).label(
            column.key)).group_by(extract('day', Energy.date)).filter\
            (Energy.date < final_date).filter(
            Energy.date > init_date).all()
        return daily_energy

    @staticmethod
    def get_actual_month(column):
        """ Función para obtener el acumulado del mes en
        curso, a partir de la última hora registrada

        :param Column: Columna con la variable que queremos obtener"""

        date = db.session.query(extract('month',Energy.date)).order_by(
            Energy.date.desc()).first()[0]

        month_energy = db.session.query(Energy.date, func.sum(column).label(
            str(column.key)
            )).filter(extract('month', Energy.date==date)).first()
        return month_energy

    @staticmethod
    def get_status():
        """Función para obtener el estado del elemento en su último registro"""

        date = db.session.query(Energy.date).order_by(
            Energy.date.desc()).first()[0]
        actual_status = db.session.query(Energy).filter(
            Energy.date==date).first()
        return actual_status