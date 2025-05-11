
import { useState, useEffect } from "react";
import axios from "axios";

export default function App() {
  const [status, setStatus] = useState("Idle");
  const [lastCommand, setLastCommand] = useState("");
  const [logs, setLogs] = useState([]);

  const sendCommand = async (cmd) => {
    setLastCommand(cmd);
    setStatus("Executing: " + cmd);
    await axios.post("/api/updateStatus", { task: cmd, battery: 90 });
    setTimeout(() => setStatus("Idle"), 3000);
  };

  const fetchLogs = async () => {
    const response = await axios.get("/api/actionLogs");
    setLogs(response.data);
  };

  useEffect(() => { fetchLogs(); }, []);

  return (
    <div className="flex flex-col items-center p-6">
      <h1 className="text-3xl font-bold mb-4">📦 Pickasso HMI Dashboard</h1>
      <p className="text-xl mb-2">Status: {status}</p>
      <button onClick={() => sendCommand("Collect Trash")} className="bg-green-500 text-white p-2 m-2 rounded">Collect Trash</button>
      <button onClick={() => sendCommand("Navigate to Bin")} className="bg-blue-500 text-white p-2 m-2 rounded">Navigate to Bin</button>
      <button onClick={() => sendCommand("Emergency Stop")} className="bg-red-500 text-white p-2 m-2 rounded">Emergency Stop</button>
      <p className="mt-4 text-gray-600">Last Command: {lastCommand}</p>
      <h2 className="text-2xl mt-6">Action Logs</h2>
      <ul>{logs.map((log, idx) => <li key={idx}>{log.action} - {log.reason}</li>)}</ul>
    </div>
  );
}
