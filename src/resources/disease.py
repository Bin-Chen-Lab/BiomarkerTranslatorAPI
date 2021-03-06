from flask_restful import Resource
from ..common.query import Query


class Disease(Resource):

    def get(self, curie=None):
        q = Query()
        if not curie:
            q.cursor.execute(
                """select a.curie, a.disease
                   from disease a""")
        else:
            q.cursor.execute(
                """select a.curie, a.disease
                   from disease a
                   where a.curie = %(curie)s""", {'curie': curie})

        return q.cursor.fetchall()
