from models import TaskManager, BugTask, FeatureTask

def print_menu():
    print("\n=== Task Manager ===")
    print("1. Listar tarefas")
    print("2. Criar tarefa (feature)")
    print("3. Criar bug")
    print("4. Atualizar status")
    print("5. Excluir tarefa")
    print("0. Sair")

def main():
    manager = TaskManager()
    while True:
        print_menu()
        choice = input("Escolha uma opção: ").strip()
        if choice == "1":
            tasks = manager.list_tasks()
            if not tasks:
                print("Nenhuma tarefa encontrada.")
            else:
                for t in tasks:
                    print(f"[{t['id']}] ({t['type']}) {t['title']} - status: {t['status']} - prioridade: {t['priority']}")
        elif choice == "2":
            title = input("Título da feature: ").strip()
            desc = input("Descrição: ").strip()
            pts = input("Story points (int, padrão 3): ").strip() or "3"
            priority = int(input("Prioridade (1-5, 5=maior): ").strip() or "1")
            ft = FeatureTask(title, desc, priority=int(priority), story_points=int(pts))
            tid = manager.create_task(ft)
            print(f"Feature criada com id {tid}")
        elif choice == "3":
            title = input("Título do bug: ").strip()
            desc = input("Descrição: ").strip()
            sev = input("Severidade (low/medium/high, padrão medium): ").strip() or "medium"
            priority = int(input("Prioridade (1-5, 5=maior): ").strip() or "2")
            bt = BugTask(title, desc, priority=int(priority), severity=sev)
            tid = manager.create_task(bt)
            print(f"Bug criado com id {tid}")
        elif choice == "4":
            tid = int(input("ID da tarefa: ").strip())
            new_status = input("Novo status (todo/in_progress/done): ").strip()
            try:
                manager.set_status(tid, new_status)
                print("Status atualizado.")
            except Exception as e:
                print("Erro ao atualizar status:", e)
        elif choice == "5":
            tid = int(input("ID da tarefa a excluir: ").strip())
            manager.delete(tid)
            print("Tarefa excluída (se o id existia).")
        elif choice == "0":
            print("Encerrando.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
