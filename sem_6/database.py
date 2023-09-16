import databases as db
import sqlalchemy as sqla

DATABASE_URL = "sqlite:///prod_data.db"
database = db.Database(DATABASE_URL)
engine = sqla.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = sqla.MetaData()


users = sqla.Table(
    "users",
    metadata,
    sqla.Column("id", sqla.Integer, primary_key=True),
    sqla.Column("name", sqla.String(50)),
    sqla.Column("surname", sqla.String(50)),
    sqla.Column("email", sqla.String(50)),
    sqla.Column("password", sqla.String(120)),
)

goods = sqla.Table(
    "goods",
    metadata,
    sqla.Column("id", sqla.Integer, primary_key=True),
    sqla.Column("name", sqla.String(50)),
    sqla.Column("description", sqla.String(200)),
    sqla.Column("price", sqla.Float)
)

orders = sqla.Table(
    "orders",
    metadata,
    sqla.Column("id", sqla.Integer, primary_key=True),
    sqla.Column("user_id", sqla.ForeignKey("users.id"), nullable=False),
    sqla.Column("goods_id", sqla.ForeignKey("goods.id"), nullable=False),
    sqla.Column("order_date", sqla.DATE),
    sqla.Column('status', sqla.String(20))
)

metadata.create_all(engine)
