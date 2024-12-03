document.addEventListener('DOMContentLoaded', async () => {
  const button = document.getElementById('myButton');
  button.addEventListener("click", () => {
    fetch('http://127.0.0.1:5000/generate-graph')
      .then(response => response.json())
      .then(data => {
        const main = document.getElementById('graph');
        main.innerHTML = data.graph_html
      })
      .catch(error => {
        console.error("Error:", error);
      });
  });
});

