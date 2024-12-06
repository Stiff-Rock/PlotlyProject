document.addEventListener('DOMContentLoaded', async () => {
  const button = document.getElementById('myButton');
  const file_chooser = document.getElementById('file_chooser');
  let file;

  file_chooser.addEventListener("change",(e)=>{
    const files = e.target.files;
      if (files.length > 0) {
        file = files[0];
      }
  });

  button.addEventListener("click", () => {
    const formData = new FormData();
    formData.append('file', file);

    fetch('http://127.0.0.1:5000/generate-graph',{
      method: 'POST',
      body: formData
    })
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
            <link rel="stylesheet" href="../static/css/graph.css">
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
