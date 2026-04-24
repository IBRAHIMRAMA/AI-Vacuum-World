from environment import VacuumEnvironment
from agent import ModelBasedAgent

# 🧱 إنشاء البيئة
env = VacuumEnvironment(5)

# 🤖 إنشاء الـ Agent
agent = ModelBasedAgent(env)

print("Initial Grid:")
env.display()

print("\n--- Simulation Start ---")

# 🔁 تشغيل لحد ما يخلص أو لحد حد أقصى
for _ in range(100):
    alive = agent.step()
    if not alive:
        break

print("\n--- Final Grid ---")
env.display()

print(f"\nTotal Steps: {agent.steps}")