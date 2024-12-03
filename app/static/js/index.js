document.addEventListener('DOMContentLoaded', async () => {
  const button = document.getElementById('myButton');
  button.addEventListener("click", () => {
    fetch('http://127.0.0.1:5000/generate-graph')
      .then(response => response.json())
      .then(data => {
        const iframe = document.getElementById('graphIframe');

        const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;

        iframeDocument.open();
        iframeDocument.write(`
          <!DOCTYPE html>
          <html lang="en">
          <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Graph</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
          </head>
          <body>
            <main id="graph">${data.graph_html}</main>
          </body>
          </html>
        `);
        iframeDocument.close();

        iframe.onload = () => {
          const iframeHeight = iframe.contentWindow.document.documentElement.scrollHeight;
          iframe.style.height = `${iframeHeight}px`;
        };
      })
      .catch(error => {
        console.error("Error:", error);
      });
  });
});
