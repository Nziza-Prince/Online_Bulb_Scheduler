function sendSchedule() {
    const delay = document.getElementById("delay").value;
    const data = { delay };
  
    const ws = new WebSocket("ws://localhost:6789");
    ws.onopen = () => {
      ws.send(JSON.stringify(data));
      alert("Schedule sent!");
    };
  }
  