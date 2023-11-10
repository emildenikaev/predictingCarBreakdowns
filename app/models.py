from .database import Base

from sqlalchemy import String, Date, Integer, Column, DECIMAL
from clickhouse_sqlalchemy import engines


class Cabin(Base):
    __tablename__ = 'cabin'

    DAT_S = Column('DAT_S', Date, primary_key=True)
    SAK = Column('SAK', String)
    FLT_NUM = Column('FLT_NUM', Integer)
    DEP_DATE = Column('DEP_DATE', Date)
    LGNUM = Column('LGNUM', Integer)
    SEG_ORIG = Column('SEG_ORIG', String)
    SEG_DEST = Column('SEG_DEST', String)
    TT_DEP = Column('TT_DEP', Integer)
    TT_ARR = Column('TT_ARR', Integer)
    SSC = Column('SSC', String)
    CAP = Column('CAP', String)
    UAL = Column('UAL', String)
    SAL = Column('SAL', String)
    EQUIP = Column('EQUIP', String)
    DTD = Column('DTD', Integer)

    __table_args__ = (
        engines.Memory(),
    )


class BookingClass(Base):
    __tablename__ = 'class'

    SDAT_S = Column('SDAT_S', Date, primary_key=True)
    SAK = Column("SAK", String)
    FLT_NUM = Column("FLT_NUM", String)
    DD = Column("DD", Date)
    SEG_NUM = Column("SEG_NUM", String)
    SORG = Column("SORG", String)
    SDST = Column("SDST", String)
    SSCL1 = Column("SSCL1", String)
    SEG_CLASS_CODE = Column("SEG_CLASS_CODE", String)
    NBCL = Column("NBCL", String)
    FCLCLD = Column("FCLCLD", String)
    PASS_BK = Column("PASS_BK", String)
    SA = Column("SA", String)
    AU = Column("AU", String)
    PASS_DEP = Column("PASS_DEP", String)
    NS = Column("NS", String)
    DTD = Column("DTD", Integer)

    __table_args__ = (
        engines.Memory(),
    )


class BookingBronIncrement(Base):
    __tablename__ = 'class_bron_increment'

    SDAT_S = Column('SDAT_S', Date, primary_key=True)
    DTD = Column('DTD', Integer)
    FLT_NUM = Column('FLT_NUM', Integer)
    DD = Column('DD', Date)
    SEG_CLASS_CODE = Column('SEG_CLASS_CODE', String)
    PASS_BK = Column('PASS_BK', Integer)
    PASS_BK_prev = Column('PASS_BK_prev', Integer)
    Increment_day = Column('Increment_day', Integer)

    __table_args__ = (
        engines.Memory(),
    )


class ClassBronSeason(Base):
    __tablename__ = 'class_bron_season'

    SDAT_S = Column('SDAT_S', Date, primary_key=True)
    FLT_NUM = Column('FLT_NUM', Integer)
    SEG_CLASS_CODE = Column('SEG_CLASS_CODE', String)
    Increment_day = Column('Increment_day', Integer)

    __table_args__ = (
        engines.Memory(),
    )


class RaspScoreAll(Base):
    __tablename__ = 'rasp_score_all2'

    FLT_NUM = Column('FLT_NUM', Integer)
    EQUIP = Column('EQUIP', String)
    DD = Column('DD', Date, primary_key=True)
    DTD = Column('DTD', Integer)
    SDAT_S = Column('SDAT_S', Date)
    SEG_CLASS_CODE = Column('SEG_CLASS_CODE', String)
    PASS_BK = Column('PASS_BK', Integer)

    __table_args__ = (
        engines.Memory(),
    )


class SeasonMosSochi(Base):
    __tablename__ = 'Season_Mos_sochi'

    Season_name = Column('Season_name', String)
    Direction = Column('Direction', String)
    date_season = Column('date_season', Date, primary_key=True)
    Height = Column('Height', DECIMAL)

    __table_args__ = (
        engines.Memory(),
    )


class Season(Base):
    __tablename__ = 'season'

    date_season = Column('date_season', Date, primary_key=True)
    Season_name = Column('Season_name', String)
    Direction = Column('Direction', String)
    Height = Column('Height', DECIMAL)

    __table_args__ = (
        engines.Memory(),
    )


class RASPScenario(Base):
    __tablename__ = 'RASP20_score_scenario'

    FLT_NUM = Column('FLT_NUM', Integer)
    SORG = Column("SORG", String)
    SDST = Column("SDST", String)
    EQUIP = Column('EQUIP', String)
    DD = Column('DD', Date)
    SDAT_S = Column('SDAT_S', Date, primary_key=True)
    Pred_C_cabin = Column('Pred_C_cabin', Integer)
    Pred_Y_cabin = Column('Pred_Y_cabin', Integer)

    __table_args__ = (
        engines.Memory(),
    )


class RaspAllClass(Base):
    __tablename__ = 'rasp_score_all_noclass'

    SDAT_S = Column('SDAT_S', Date, primary_key=True)
    DTD = Column('DTD', Integer)
    FLT_NUM = Column('FLT_NUM', Integer)
    DD = Column('DD', Date)
    PASS_BK = Column('PASS_BK', Integer)

    __table_args__ = (
        engines.Memory(),
    )
