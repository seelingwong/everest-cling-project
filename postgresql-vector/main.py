from database import semantic_search, hybrid_search, aws_semantic_search

results = hybrid_search("running shoe")
results2 = semantic_search("running shoe")
results3 = aws_semantic_search("running shoe")

for r in results:
    print(f"{r.name}: {r.description}")
print("-----------------")
for r in results2:
    print(f"{r.name}:{r.score}:{r.description}")
print("-----------------")
for r in results3:
    print(f"{r.name}:{r.score}:{r.description}")
