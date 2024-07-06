document.getElementById("chatForm").addEventListener("submit", async (e) => {
    e.preventDefault();
  
    const promptInput = document.getElementById("promptInput");
    const scriptureSelect = document.getElementById("scriptureSelect");
    const resultsDiv = document.getElementById("results");
  
    const prompt = promptInput.value;
    const model = scriptureSelect.value;
  
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt, model }),
    });
  
    const data = await response.json();
    resultsDiv.innerHTML = data.response;
  });