
tasks = []  # قائمة لتخزين المهام (كل مهمة عبارة عن Dictionary)
def show_taskes():
    if not tasks:
        print("\n📭 قائمة المهام فارغة حالياً!")
        return
    
show_taskes()   