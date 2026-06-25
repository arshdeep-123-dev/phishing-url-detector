async function checkURL() {

    const url = document.getElementById("urlInput").value;

    const result = document.getElementById("result");

     // Show scanning animation
    result.innerHTML = `
        <h3 class="scanner">
            Scanning URL...
        </h3>
    `;

    // Wait 2 seconds
    await new Promise(resolve =>
        setTimeout(resolve, 2000)
    );

    // Send request
    const response = await fetch("/check", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            url: url
        })
    });

    const data = await response.json();

    let reasons = "";

    data.reasons.forEach(reason => {
        reasons += `<li>${reason}</li>`;
    });

    const meter = `
        <div class="risk-container">
            <div class="risk-bar">
                <div class="risk-fill"
                    style="width:${data.score}%">
                </div>
            </div>

            <p>Risk Score: ${data.score}%</p>
        </div>
    `;

    if (data.status === "Safe") {
        result.innerHTML =
            meter +
            `<h2 class="safe">✅ SAFE</h2>
             <ul>${reasons}</ul>`;
    }
    else {
        result.innerHTML =
            meter +
            `<h2 class="suspicious">⚠️ SUSPICIOUS</h2>
             <ul>${reasons}</ul>`;
    }

    loadHistory();
}

async function loadHistory() {

    const response = await fetch("/history");

    const history = await response.json();

    let safeCount = 0;
    let suspiciousCount = 0;
    let totalRisk = 0;

    history.forEach(item => {

        totalRisk += item.score;

        if(item.status === "Safe"){
            safeCount++;
        }else{
            suspiciousCount++;
        }
    });

    document.getElementById("totalScans").innerText =
        history.length;

    document.getElementById("safeUrls").innerText =
        safeCount;

    document.getElementById("suspiciousUrls").innerText =
        suspiciousCount;

    document.getElementById("avgRisk").innerText =
        history.length
            ? Math.round(totalRisk/history.length)+"%"
            : "0%";

    const tbody =
        document.querySelector("#historyTable tbody");

    tbody.innerHTML = "";

    history.forEach(item => {

        tbody.innerHTML += `
            <tr>
                <td>${item.url}</td>
                <td>${item.status}</td>
                <td>${item.score}%</td>
            </tr>
        `;
    });
}

// Load history when page opens
window.onload = loadHistory;



//SAfe links
// https://www.google.com
// https://github.com
// https://www.microsoft.com
//Suspicious links
// http://secure-bank-login.xyz
// http://paypal-login@fake-site.com
// http://verify-account-update-free-money.com 