from models import TaskManager, FeatureTask, BugTask

def populate():
    tm = TaskManager()
    tasks = [
        FeatureTask("Cadastro de usuários", "Implementar CRUD de usuários", priority=4, story_points=5),
        BugTask("Erro login", "Exception no login quando senha vazia", priority=5, severity="high"),
        FeatureTask("Página inicial", "Layout responsivo da home", priority=3, story_points=3),
    ]
    for t in tasks:
        tid = tm.create_task(t)
        print("Criado id", tid)

if __name__ == "__main__":
    populate()
