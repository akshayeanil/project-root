const apiBase = "https://jwrtp0hfb4.execute-api.us-east-1.amazonaws.com"; // Replace with your actual API Gateway base URL

// Notification function
function showNotification(message) {
  const container = document.getElementById("notification-container");
  if (!container) return;

  const notification = document.createElement("div");
  notification.className = "notification";
  notification.textContent = message;

  container.appendChild(notification);

  setTimeout(() => {
    container.removeChild(notification);
  }, 3000);
}

document.getElementById("task-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const title = document.getElementById("task-title").value;
  const taskId = Date.now().toString();

  await fetch(`${apiBase}/tasks`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ taskId, title, status: "pending" }),
  });

  document.getElementById("task-title").value = "";
  loadTasks();

  showNotification("Task created!");
});

async function loadTasks() {
  const res = await fetch(`${apiBase}/tasks`);
  const tasks = await res.json();
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
}

async function deleteTask(id) {
  await fetch(`${apiBase}/tasks/${id}`, { method: "DELETE" });
  loadTasks();
  showNotification("Task deleted!");
}

async function updateTask(id, title, status) {
  const newStatus = status === "pending" ? "completed" : "pending";
  await fetch(`${apiBase}/tasks/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, status: newStatus }),
  });
  loadTasks();
  showNotification("Task updated!");
}

window.onload = loadTasks;
