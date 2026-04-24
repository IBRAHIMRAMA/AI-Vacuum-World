import random

# 1. الوكيل البسيط (الذي يعتمد على رد الفعل اللحظي فقط)
class SimpleReflexAgent:
    def __init__(self, environment):
        self.env = environment
        self.x = 0
        self.y = 0
        self.steps = 0

    def move_randomly(self):
        # يتحرك عشوائياً في الاتجاهات الأربعة
        directions = ['Up', 'Down', 'Left', 'Right']
        move = random.choice(directions)
        
        if move == 'Up' and self.x > 0: self.x -= 1
        elif move == 'Down' and self.x < self.env.size - 1: self.x += 1
        elif move == 'Left' and self.y > 0: self.y -= 1
        elif move == 'Right' and self.y < self.env.size - 1: self.y += 1
        
        self.steps += 1
        return True

    def step(self):
        # القاعدة: لو المربع الحالي متسخ نظف، غير كدة اتحرك عشوائي
        if self.env.grid[self.x][self.y] == "Dirty":
            print(f"🧹 (Reflex) Cleaning cell ({self.x}, {self.y})")
            self.env.grid[self.x][self.y] = "Clean"
            return True
        else:
            return self.move_randomly()


# 2. الوكيل الذكي (الذي يعتمد على الذاكرة والنموذج الداخلي)
class ModelBasedAgent:
    def __init__(self, environment):
        self.env = environment
        self.x = 0
        self.y = 0
        self.steps = 0
        # الذاكرة (النموذج الداخلي للعالم)
        self.memory = [
            ["Unknown" for _ in range(environment.size)]
            for _ in range(environment.size)
        ]

    def update_memory(self):
        self.memory[self.x][self.y] = self.env.grid[self.x][self.y]

    def is_dirty(self):
        return self.env.grid[self.x][self.y] == "Dirty"

    def clean(self):
        print(f"🧹 (Model-Based) Cleaning cell ({self.x}, {self.y})")
        self.env.grid[self.x][self.y] = "Clean"
        self.memory[self.x][self.y] = "Clean"

    def get_targets(self):
        dirty_targets = []
        unknown_targets = []
        for i in range(self.env.size):
            for j in range(self.env.size):
                if self.memory[i][j] == "Dirty":
                    dirty_targets.append((i, j))
                elif self.memory[i][j] == "Unknown":
                    unknown_targets.append((i, j))
        
        if dirty_targets: return dirty_targets
        return unknown_targets

    def find_closest_target(self):
        targets = self.get_targets()
        if not targets: return None
        return min(targets, key=lambda cell: abs(cell[0] - self.x) + abs(cell[1] - self.y))

    def move(self):
        target = self.find_closest_target()
        if target is None: return False
        
        tx, ty = target
        if self.x < tx: self.x += 1
        elif self.x > tx: self.x -= 1
        elif self.y < ty: self.y += 1
        elif self.y > ty: self.y -= 1

        self.steps += 1
        return True

    def step(self):
        self.update_memory()
        if self.is_dirty():
            self.clean()
            return True
        else:
            return self.move()