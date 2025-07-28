const apiBase = "https://jwrtp0hfb4.execute-api.us-east-1.amazonaws.com"; // Replace with your actual API Gateway base URL

document.getElementById("task-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const title = document.getElementById("task-title").value;
  const taskId = Date.now().toString();

  try {
    const res = await fetch(`${apiBase}/tasks`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ taskId, title, status: "pending" }),
    });
    if (!res.ok) throw new Error(`Failed to create task: ${res.status}`);
    console.log("Task created successfully");
    document.getElementById("task-title").value = "";
    await loadTasks();  // Wait to finish loading tasks before continuing
  } catch (err) {
    console.error("Error creating task:", err);
  }
});

async function loadTasks() {
  console.log("Loading tasks...");
  try {
    const res = await fetch(`${apiBase}/tasks`);
    if (!res.ok) throw new Error(`Failed to fetch tasks: ${res.status}`);
    const tasks = await res.json();
    console.log("Tasks loaded:", tasks);
    const list = document.getElementById("task-list");
    list.innerHTML = "";

    tasks.forEach((task) => {
      const li = document.createElement("li");
      li.innerHTML = `
        ${task.title} 
        <span>
          <button onclick="deleteTask('${task.taskId}')">🗑️</button>
          <button onclick="updateTask('${task.taskId}', '${task.title}', '${task.status}')">✅</button>
        </span>
      `;
      list.appendChild(li);
    });
  } catch (err) {
    console.error("Error loading tasks:", err);
  }
}

async function deleteTask(id) {
  try {
    const res = await fetch(`${apiBase}/tasks/${id}`, { method: "DELETE" });
    if (!res.ok) throw new Error(`Failed to delete task: ${res.status}`);
    console.log(`Task ${id} deleted`);
    await loadTasks();
  } catch (err) {
    console.error("Error deleting task:", err);
  }
}

async function updateTask(id, title, status) {
  const newStatus = status === "pending" ? "completed" : "pending";
  try {
    const res = await fetch(`${apiBase}/tasks/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, status: newStatus }),
    });
    if (!res.ok) throw new Error(`Failed to update task: ${res.status}`);
    console.log(`Task ${id} updated`);
    await loadTasks();
  } catch (err) {
    console.error("Error updating task:", err);
  }
}

window.onload = loadTasks;
