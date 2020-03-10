from app import db
from app.models.tables import Atividade
from datetime import date

a1 = Atividade(nome='Github',tipo='Oficina',data=date(2020,12,10),carga_horaria='100',arquivo='/1/155.pdf',usurio_id=1)
a2 = Atividade(nome='Qualquer',tipo='Indefinido',data=date(2019,5,22),carga_horaria='100',arquivo='/1/172.pdf',usurio_id=1)
a3 = Atividade(nome='Coisa', tipo='Indefinido', data=date(2015,10,9), carga_horaria='80', arquivo='/1/192.pdf', usurio_id=1)

db.session.add(a1)
db.session.add(a2)
db.session.add(a3)

db.session.commit()
