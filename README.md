1. Project Overview

This project aims to develop an autonomous intelligent agent that simulates a smart vacuum cleaner operating in a structured environment. The goal is to design and compare different AI agent architectures to solve the Vacuum World problem efficiently.

2. Objectives
Design and implement different types of intelligent agents.
Compare agent performance based on efficiency and decision-making.
Analyze the impact of memory on agent behavior.
3. PEAS Description
Performance Measure:
Cleanliness percentage
Number of actions (energy efficiency)
Time taken
Redundant movements
Environment:
A 2D grid-based environment (e.g., 5x5)
Each cell can be Clean or Dirty
Initially static, with possible extension to dynamic dirt generation
Actuators:
Move (Left, Right, Up, Down)
Suck dirt
Stay Idle
Sensors:
Location Sensor
Dirt Sensor
4. Environment Characteristics (ODESA Analysis)

The vacuum environment can be formally described using the ODESA framework as follows:

Observable (O): Fully Observable
The agent has complete visibility of the environment. It can perceive the entire grid and knows the exact locations of all dirty and clean cells.
Deterministic (D): Deterministic
The environment is fully predictable. Each action taken by the agent leads to a guaranteed outcome. For example, the "Suck" action will always clean the current cell.
Episodic (E): Sequential (Non-Episodic)
The environment is sequential, meaning each action affects future states. The agent’s movement changes its position, which influences subsequent decisions.
Static (S): Static
The environment does not change unless the agent acts. No new dirt appears during execution, and nothing changes while the agent is making decisions.
Agents (A): Single-Agent
The system includes only one intelligent agent (the vacuum cleaner) operating independently.
5. Technical Approach
Programming Language: Python 3.x
Architecture: Object-Oriented Programming (OOP)
Components:
VacuumEnvironment class
VacuumAgent class
Visualization:
Phase 1: Console-based simulation
Phase 2: GUI using Tkinter or Pygame
Randomization:
Random dirt generation using Python’s random module
6. Agent Types
Simple Reflex Agent:
Acts based only on current perception
Rule: If Dirty → Suck
Model-Based Agent:
Maintains internal memory
Avoids revisiting clean cells unnecessarily
7. Evaluation Metrics
Total steps taken
Energy consumption
Cleaning efficiency
Number of repeated actions
8. Expected Results

The Model-Based Agent is expected to outperform the Simple Reflex Agent in terms of efficiency and reduced redundant actions
