async function loadIncidents() {
    try {
        const res = await fetch('/api/v1/dashboard/incidents/recent');
        const data = await res.json();
        const feed = document.getElementById('incidentFeed');
        feed.innerHTML = data.map(inc => `
            <div class="incident-card">
                <div><strong>${inc.incident_type}</strong> - ${new Date(inc.occurred_at).toLocaleString()}</div>
                <div>${inc.summary || 'No summary'}</div>
                <div>Status: ${inc.status}</div>
            </div>
        `).join('');
    } catch(e) { console.error(e); }
}
loadIncidents();