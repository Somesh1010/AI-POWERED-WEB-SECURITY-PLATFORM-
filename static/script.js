// 🌐 Module 1: ML-Based URL Scanner
async function scanURL() {
    const url = document.getElementById("url-input").value;
    if (!url) return alert("Please enter a valid URL!");

    try {
        const res = await fetch("/scan", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url: url })
        });

        const data = await res.json();

        if (data.error) {
            alert("Error: " + data.error);
            return;
        }

        displayResults(data);
    } catch (err) {
        alert("❌ Request failed: " + err.message);
    }
}

function displayResults(data) {
    const resultsSection = document.getElementById("results");
    resultsSection.classList.remove("hidden");

    const statusElem = document.getElementById("status");
    statusElem.innerText = `Status: ${data.status}`;
    statusElem.style.color = data.status === "Malicious" ? "red" : "green";

    const tableBody = document.querySelector("#feature-results tbody");
    tableBody.innerHTML = "";

    for (const [key, val] of Object.entries(data.features_used)) {
        const row = `<tr><td>${key}</td><td>${val}</td></tr>`;
        tableBody.innerHTML += row;
    }
}

// 📡 Module 2: Real-Time Network Anomaly Detection
async function analyzeTraffic() {
    const output = document.getElementById("traffic-output");
    output.innerHTML = "⏳ Monitoring network traffic...";

    try {
        const res = await fetch("/analyze-traffic");
        const data = await res.json();

        if (data.error) {
            output.innerHTML = `<p style="color:red;">❌ ${data.error}</p>`;
        } else if (data.count > 0) {
            output.innerHTML = `
                <p style="color:red;">⚠️ ${data.count} anomalies detected!</p>
                <pre>${JSON.stringify(data.anomalies, null, 2)}</pre>
            `;
        } else {
            output.innerHTML = `<p style="color:green;">✅ No anomalies detected.</p>`;
        }
    } catch (err) {
        output.innerHTML = `<p style="color:red;">❌ Error: ${err.message}</p>`;
    }
}

// 📁 Module 3: File Malware Scanner
async function scanFile() {
    const fileInput = document.getElementById("file-input");
    const resultDiv = document.getElementById("file-scan-result");
    resultDiv.classList.remove("hidden");
    resultDiv.innerHTML = "⏳ Scanning file...";

    const file = fileInput.files[0];
    if (!file) {
        alert("Please select a file to scan.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const res = await fetch("/scan-file", {
            method: "POST",
            body: formData
        });

        const data = await res.json();

        if (data.status) {
            resultDiv.innerHTML = `
                <p><strong>${data.filename}</strong> → 
                   <span style="color:${data.status === 'Malicious' ? 'red' : 'green'}">
                      ${data.status}
                   </span>
                </p>
                <pre>${JSON.stringify(data.details, null, 2)}</pre>
            `;
        } else {
            resultDiv.innerHTML = `<p style="color:red;">Error: ${data.error}</p>`;
        }
    } catch (err) {
        resultDiv.innerHTML = `<p style="color:red;">❌ Failed to scan: ${err.message}</p>`;
    }
}


