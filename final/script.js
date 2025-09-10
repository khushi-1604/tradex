let stockData = [];

document.getElementById("csvFile").addEventListener("change", function (e) {
  const reader = new FileReader();
  reader.onload = function () {
    stockData = reader.result.trim().split("\n").map(row => {
      const [date, open, high, low, close, volume] = row.split(",");
      return {
        date: new Date(date.trim()),
        close: parseFloat(close)
      };
    }).sort((a, b) => a.date - b.date);
    alert("CSV loaded!");
  };
  reader.readAsText(e.target.files[0]);
});

function movingAverage(data, period, idx) {
  if (idx < period - 1) return null;
  let sum = 0;
  for (let i = idx - period + 1; i <= idx; i++) {
    sum += data[i].close;
  }
  return sum / period;
}

let chart;
function runSimulation() {
  const start = new Date(document.getElementById("startDate").value);
  const end = new Date(document.getElementById("endDate").value);
  const filtered = stockData.filter(d => d.date >= start && d.date <= end);

  let labels = [], closes = [], ma20s = [], ma30s = [], buys = [], sells = [], log = [];
  let principal = 100000;
  let holding = false, qty = 0, buyPrice = 0;

  for (let i = 0; i < filtered.length; i++) {
    const d = filtered[i];
    const dateStr = d.date.toISOString().split("T")[0];
    const ma20 = movingAverage(filtered, 20, i);
    const ma30 = movingAverage(filtered, 30, i);

    if (ma20 === null || ma30 === null) continue;

    labels.push(dateStr);
    closes.push(d.close);
    ma20s.push(ma20);
    ma30s.push(ma30);

    let action = "-", invest = "-", gainLoss = "-";

    if (!holding && ma20 > ma30) {
      qty = Math.floor(principal / d.close);
      invest = qty * d.close;
      buyPrice = d.close;
      principal -= invest;
      holding = true;
      action = "BUY";
      buys.push({ x: dateStr, y: d.close });

      log.push({ date: dateStr, close: d.close, ma20, ma30, action, qty, invest, gainLoss, principal });
    }

    if (holding && ma20 < ma30) {
      const sell = qty * d.close;
      const pl = sell - (qty * buyPrice);
      principal += sell;
      action = "SELL";
      gainLoss = pl.toFixed(2);
      invest = (qty * buyPrice).toFixed(2);
      sells.push({ x: dateStr, y: d.close });

      log.push({ date: dateStr, close: d.close, ma20, ma30, action, qty, invest, gainLoss, principal });
      holding = false;
      qty = 0;
    }
  }

  // Final sell if holding
  if (holding) {
    const last = filtered[filtered.length - 1];
    const dateStr = last.date.toISOString().split("T")[0];
    const sell = qty * last.close;
    const pl = sell - (qty * buyPrice);
    principal += sell;

    log.push({
      date: dateStr,
      close: last.close,
      ma20: movingAverage(filtered, 20, filtered.length - 1),
      ma30: movingAverage(filtered, 30, filtered.length - 1),
      action: "SELL",
      qty,
      invest: (qty * buyPrice).toFixed(2),
      gainLoss: pl.toFixed(2),
      principal
    });

    sells.push({ x: dateStr, y: last.close });
  }

  renderLog(log);
  renderChart(labels, closes, ma20s, ma30s, buys, sells);
}

function renderLog(log) {
  const tbody = document.querySelector("#transactionTable tbody");
  tbody.innerHTML = "";
  log.forEach(row => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${row.date}</td>
      <td>${row.close.toFixed(2)}</td>
      <td>${row.ma20.toFixed(2)}</td>
      <td>${row.ma30.toFixed(2)}</td>
      <td>${row.action}</td>
      <td>${row.qty || "-"}</td>
      <td>${row.invest}</td>
      <td>${row.gainLoss}</td>
      <td>${row.principal.toFixed(2)}</td>
    `;
    tbody.appendChild(tr);
  });
}

function renderChart(labels, closes, ma20, ma30, buys, sells) {
  const ctx = document.getElementById("priceChart").getContext("2d");
  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: "line",
    data: {
      labels,
      datasets: [
        {
          label: "Close Price", data: closes, borderColor: "blue", fill: false
        },
        {
          label: "MA20", data: ma20, borderColor: "green", fill: false
        },
        {
          label: "MA30", data: ma30, borderColor: "red", fill: false
        },
        {
          label: "Buy", data: buys, type: "scatter", backgroundColor: "green", pointRadius: 5
        },
        {
          label: "Sell", data: sells, type: "scatter", backgroundColor: "red", pointRadius: 5
        }
      ]
    },
    options: {
      responsive: true,
      plugins: { legend: { position: "top" } },
      scales: {
        x: {
          ticks: { maxTicksLimit: 20, autoSkip: true }
        }
      }
    }
  });
}