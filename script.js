async function sendMessage() {
  const input = document.getElementById("user-input");
  const msg = input.value.trim();
  if (!msg) return;

  addMessage(msg, "user");
  input.value = "";

  addMessage("Typing...", "bot");

  const res = await fetch("http://localhost:3000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg })
  });

  const data = await res.json();
  chatBox.lastChild.remove();
  addMessage(data.reply, "bot");
}
