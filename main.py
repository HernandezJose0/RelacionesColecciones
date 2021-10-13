from collections import Counter
from collections import defaultdict

users = [{"id":0, "name":"Hero"},{"id":1, "name":"Dunn"},{"id":2,"name":"Obed"},{"id":3,"name":"Aldo"},{"id":4,"name":"Carlos"},{"id":5,"name":"Sergio"},{"id":6,"name":"Alexis"},{"id":7,"name":"Alberto"},{"id":8,"name":"Joel"},{"id":9,"name":"Rodri"}]
amigos =[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]
for user in users:
    user["amigo"] = []
for i,j in amigos:
    users[i]["amigo"].append(users[j])
    users[j]["amigo"].append(users[i])
def numeroAmigos(user):
    return len(user["amigo"])
conexiones = sum(numeroAmigos(user) for user in users)
print("numero de conexiones " + str(conexiones))
numUsuarios = len(users)
promedioAmigos = conexiones/numUsuarios
print("Promedio de amigos = " + str(promedioAmigos))
amigosPorId = [(user["id"], numeroAmigos(user)) for user in users]
def distintos(usuario,otro):
    return usuario["id"] != otro["id"]
def noAmigo(usuario,otro):
    return all(distintos(amigo,otro) for amigo in usuario["amigo"])
def amigoDeAmigo(usuario):
    return Counter(ac["id"] for amigo in usuario["amigo"] for ac in amigo["amigo"] if distintos(usuario,ac) and noAmigo(usuario,ac))
print(amigoDeAmigo(users[3]))
intereses = [
 (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
 (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
 (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
 (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
 (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
 (3, "statistics"), (3, "regression"), (3, "probability"),
 (4, "machine learning"), (4, "regression"), (4, "decision trees"),
 (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
 (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
 (6, "probability"), (6, "mathematics"), (6, "theory"),
 (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
 (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
 (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
 (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def cientificoGusta(objetivo):
    return [userId for userId, interes in intereses if interes == objetivo]
idPorInteres = defaultdict(list)
for userId, interes in intereses:
    idPorInteres[interes].append(userId)
interesPorId = defaultdict(list)
for userId, interes in intereses:
    interesPorId[userId].append(interes)

def interesComunCon(usuario):
    return Counter(idUsuarioInteresado for interes in interesPorId[usuario["id"]] for idUsuarioInteresado in idPorInteres [interes] if idUsuarioInteresado != usuario["id"])

print(interesComunCon(users[3]))