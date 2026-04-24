import tkinter as tk
import random
from environment import VacuumEnvironment
from agent import ModelBasedAgent, SimpleReflexAgent

class VacuumGUI:
    def __init__(self, root, env_size=5):
        self.root = root
        self.root.title("AI Vacuum Cleaner - Comparison Mode")
        self.root.configure(bg="#2c3e50")

        self.env = VacuumEnvironment(env_size)
    
        self.agent = ModelBasedAgent(self.env)
        self.agent_type = "Model-Based"

        self.cell_size = 80
        self.is_running = False

        self.canvas = tk.Canvas(root, width=env_size*self.cell_size, height=env_size*self.cell_size, bg="#ecf0f1", highlightthickness=0)
        self.canvas.pack(pady=20, padx=20)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self.info = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#2c3e50", fg="white")
        self.info.pack(pady=5)

        btn_frame = tk.Frame(root, bg="#2c3e50")
        btn_frame.pack(pady=10)

        self.toggle_btn = tk.Button(
            btn_frame, 
            text=f"Switch to Simple Reflex", 
            command=self.toggle_agent,
            bg="#3498db", fg="white", font=("Arial", 10, "bold"), padx=10
        )
        self.toggle_btn.pack(side=tk.LEFT, padx=10)

        self.re_button = tk.Button(
            btn_frame, text="Random Dust 🎲", command=self.reactivate_dirt,
            bg="#e67e22", fg="white", font=("Arial", 10, "bold"), padx=10
        )
        self.re_button.pack(side=tk.LEFT, padx=10)

        self.update_gui()

    def toggle_agent(self):
        if self.agent_type == "Model-Based":
            self.agent = SimpleReflexAgent(self.env)
            self.agent_type = "Simple Reflex"
            self.toggle_btn.config(text="Switch to Model-Based", bg="#2ecc71")
        else:
            self.agent = ModelBasedAgent(self.env)
            self.agent_type = "Model-Based"
            self.toggle_btn.config(text="Switch to Simple Reflex", bg="#3498db")
        
        print(f"🔄 Switched to: {self.agent_type}")
        self.update_info()

    def draw_grid(self):
        self.canvas.delete("all")
        for r in range(self.env.size):
            for c in range(self.env.size):
                x1, y1 = c * self.cell_size, r * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                color = "#7f8c8d" if self.env.grid[r][c] == "Dirty" else "#ffffff"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#bdc3c7")

                if self.agent.x == r and self.agent.y == c:
                    self.canvas.create_oval(x1+15, y1+15, x2-15, y2-15, fill="#34495e", outline="#2c3e50", width=2)
                    self.canvas.create_rectangle(x1+30, y1+55, x2-30, y2-15, fill="#2ecc71", outline="#27ae60")
                    self.canvas.create_text(x1+self.cell_size/2, y1+self.cell_size/2-5, text="VAC", fill="white", font=("Arial", 8, "bold"))

    def update_gui(self):
        running = self.agent.step()
        self.draw_grid()
        self.update_info()
        if running:
            self.is_running = True
            delay = 200 if self.agent_type == "Simple Reflex" else 400
            self.root.after(delay, self.update_gui)
        else:
            self.is_running = False

    def update_info(self):
        self.info.config(text=f"Mode: {self.agent_type} | Steps: {self.agent.steps}")

    def on_canvas_click(self, event):
        c, r = event.x // self.cell_size, event.y // self.cell_size
        if 0 <= r < self.env.size and 0 <= c < self.env.size:
            self.env.grid[r][c] = "Dirty"
            if self.agent_type == "Model-Based":
                self.agent.memory[r][c] = "Dirty"
            if not self.is_running: self.update_gui()

    def reactivate_dirt(self):
        for r in range(self.env.size):
            for c in range(self.env.size):
                if random.random() < 0.2 and not (self.agent.x == r and self.agent.y == c):
                    self.env.grid[r][c] = "Dirty"
                    if self.agent_type == "Model-Based": self.agent.memory[r][c] = "Dirty"
        if not self.is_running: self.update_gui()

if __name__ == "__main__":
    root = tk.Tk()
    app = VacuumGUI(root, env_size=5)
    root.mainloop()