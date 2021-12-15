import cdindex
import datetime

pyvertices = [{"name": "0Z", "time": datetime.datetime(1992, 1, 1)},
              {"name": "1Z", "time": datetime.datetime(1992, 1, 1)},
              {"name": "2Z", "time": datetime.datetime(1993, 1, 1)},
              {"name": "3Z", "time": datetime.datetime(1993, 1, 1)},
              {"name": "4Z", "time": datetime.datetime(1995, 1, 1)},
              {"name": "5Z", "time": datetime.datetime(1997, 1, 1)},
              {"name": "6Z", "time": datetime.datetime(1998, 1, 1)},
              {"name": "7Z", "time": datetime.datetime(1999, 1, 1)},
              {"name": "8Z", "time": datetime.datetime(1999, 1, 1)},
              {"name": "9Z", "time": datetime.datetime(1998, 1, 1)},
              {"name": "10Z", "time": datetime.datetime(1997, 1, 1)}]
pyedges = [{"source": "4Z", "target": "2Z"},
           {"source": "4Z", "target": "0Z"},
           {"source": "4Z", "target": "1Z"},
           {"source": "4Z", "target": "3Z"},
           {"source": "5Z", "target": "2Z"},
           {"source": "6Z", "target": "2Z"},
           {"source": "6Z", "target": "4Z"},
           {"source": "7Z", "target": "4Z"},
           {"source": "8Z", "target": "4Z"},
           {"source": "9Z", "target": "4Z"},
           {"source": "9Z", "target": "1Z"},
           {"source": "9Z", "target": "3Z"},
           {"source": "10Z", "target": "4Z"}]
graph = cdindex.Graph()
for vertex in pyvertices:
    graph.add_vertex(vertex["name"], cdindex.timestamp_from_datetime(vertex["time"]))
for edge in pyedges:
    graph.add_edge(edge["source"], edge["target"])
print(graph.cdindex("4Z", int(datetime.timedelta(days=1825).total_seconds())))
print(graph.mcdindex("4Z", int(datetime.timedelta(days=1825).total_seconds())))
