from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class Company(BaseModel, db.Model):
    """Model for the company table"""
    __tablename__ = 'Company'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    IDCompany = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.VARCHAR)

    #full_models = db.relationship("FullModel", backref="Company", uselist=False)


class Model(BaseModel, db.Model):
    """Model for the model table"""
    __tablename__ = 'Model'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    IDModel = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.VARCHAR)


class Version(BaseModel, db.Model):
    """Model for the version table"""
    __tablename__ = 'Version'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    IDVersion = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.VARCHAR)


class FullModel(BaseModel, db.Model):
    """Model for the version table"""
    __tablename__ = 'FullModel'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    IDFullModel = db.Column(db.Integer, primary_key=True)
    IDCompany = db.Column(db.Integer, db.ForeignKey('Company.IDCompany'))
    Company = db.relationship("Company", uselist=False)
    IDModel = db.Column(db.Integer, db.ForeignKey('Model.IDModel'))
    Model = db.relationship("Model", uselist=False)
    IDVersion = db.Column(db.Integer, db.ForeignKey('Version.IDVersion'))
    Version = db.relationship("Version", uselist=False)
    IDLabel = db.Column(db.Integer)


def delete_data(app):
    with app.app_context():
        full_models = FullModel.query.filter_by()
        for it in full_models:
            db.session.delete(it)
        companies = Company.query.filter_by()
        for it in companies:
            db.session.delete(it)
        models = Model.query.filter_by()
        for it in models:
            db.session.delete(it)
        versions = Version.query.filter_by()
        for it in versions:
            db.session.delete(it)
        db.session.commit()


def create_data(app):
    company_bmw = Company(Name='BMW')
    company_audi = Company(Name='Audi')
    companies = [company_bmw, company_audi]
    model_118d = Model(Name='118d')
    model_316d = Model(Name='316d')
    model_318 = Model(Name='318')
    model_320d = Model(Name='320d')
    model_325 = Model(Name='325')
    model_520d = Model(Name='520d')
    model_x1 = Model(Name='x1')
    model_x3 = Model(Name='x3')
    model_x5 = Model(Name='x5')
    models = [model_118d, model_316d, model_318, model_320d, model_325, model_520d, model_x1,
              model_x3, model_x5]
    version_caravan = Version(Name='caravan')
    version_saloon = Version(Name='saloon')
    version_sedan = Version(Name='sedan')
    version_suv = Version(Name='suv')
    versions = [version_caravan, version_saloon, version_sedan, version_suv]
    full_models = [FullModel(Company=company_bmw, Model=model_118d, Version=version_saloon, IDLabel=0),
                   FullModel(Company=company_bmw, Model=model_316d, Version=version_caravan, IDLabel=1),
                   FullModel(Company=company_bmw, Model=model_316d, Version=version_sedan,  IDLabel=2),
                   FullModel(Company=company_bmw, Model=model_318, Version=version_caravan, IDLabel=3),
                   FullModel(Company=company_bmw, Model=model_318, Version=version_sedan, IDLabel=4),
                   FullModel(Company=company_bmw, Model=model_320d, Version=version_caravan, IDLabel=5),
                   FullModel(Company=company_bmw, Model=model_320d, Version=version_sedan, IDLabel=6),
                   FullModel(Company=company_bmw, Model=model_325, Version=version_sedan, IDLabel=7),
                   FullModel(Company=company_bmw, Model=model_520d, Version=version_caravan, IDLabel=8),
                   FullModel(Company=company_bmw, Model=model_520d, Version=version_sedan, IDLabel=9),
                   FullModel(Company=company_bmw, Model=model_x1, Version=version_suv, IDLabel=10),
                   FullModel(Company=company_bmw, Model=model_x3, Version=version_suv, IDLabel=11),
                   FullModel(Company=company_bmw, Model=model_x5, Version=version_suv, IDLabel=12)
                   ]
    with app.app_context():
        for it in companies:
            db.session.add(it)
        for it in models:
            db.session.add(it)
        for it in versions:
            db.session.add(it)
        for it in full_models:
            db.session.add(it)
        db.session.commit()
