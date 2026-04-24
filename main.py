from environment import VacuumEnvironment
from agent import ModelBasedAgent

env = VacuumEnvironment(5)

agent = ModelBasedAgent(env)

print("Initial Grid:")
env.display()

print("\n--- Simulation Start ---")

for _ in range(100):
    alive = agent.step()
    if not alive:
        break

print("\n--- Final Grid ---")
env.display()

print(f"\nTotal Steps: {agent.steps}")