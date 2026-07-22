<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
  <title>SamWeb Store • Admin Panel</title>
  <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Exo+2:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --orange: #FF8C42; --orange-light: #FFB366; --orange-glow: rgba(255,140,66,0.35); --orange-dim: rgba(255,160,66,0.12);
      --black: #0a0a0a; --dark: #111111; --card: #161616; --card2: #1c1c1c; --border: rgba(255,140,66,0.22);
      --text: #f0f0f0; --text-dim: #999; --glass: rgba(255,255,255,0.04);
    }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: 'Exo 2', sans-serif; background: var(--black); color: var(--text); min-height: 100vh; }
    .hidden { display: none !important; }
    .btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 10px 20px; border: none; border-radius: 8px; font-family: 'Exo 2', sans-serif; font-weight: 600; font-size: 14px; cursor: pointer; transition: all .25s ease; }
    .btn-primary { background: linear-gradient(135deg, var(--orange), var(--orange-light)); color: #000; box-shadow: 0 0 12px var(--orange-glow); }
    .btn-primary:hover { transform: translateY(-2px); }
    .btn-outline { background: transparent; color: var(--orange); border: 1.5px solid var(--orange); }
    .btn-outline:hover { background: var(--orange-dim); }
    .btn-danger { background: rgba(255,60,60,0.12); color: #ff6b6b; border: 1px solid rgba(255,60,60,0.3); }
    .btn-danger:hover { background: rgba(255,60,60,0.22); }
    .btn-warning { background: rgba(255,200,50,0.15); color: #ffc832; border: 1px solid rgba(255,200,50,0.35); }
    .btn-warning:hover { background: rgba(255,200,50,0.25); }
    .btn-success { background: rgba(34,197,94,0.15); color: #22c55e; border: 1px solid rgba(34,197,94,0.35); }
    .btn-success:hover { background: rgba(34,197,94,0.25); }
    .btn-sm { padding: 6px 12px; font-size: 12px; }
    .btn-xs { padding: 4px 10px; font-size: 11px; border-radius: 6px; }
    .input-group { display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px; }
    .input-group label { font-size: 13px; color: var(--text-dim); font-weight: 500; }
    .input-group input, .input-group select, .input-group textarea {
      background: var(--card2); border: 1.5px solid var(--border); color: var(--text);
      padding: 12px 14px; border-radius: 8px; font-family: 'Exo 2', sans-serif; font-size: 14px;
      outline: none; width: 100%;
    }
    .input-group input::placeholder, .input-group textarea::placeholder { color: #555; }
    .input-group input:focus, .input-group select:focus, .input-group textarea:focus { border-color: var(--orange); }
    #toast { position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%) translateY(80px); background: var(--card); border: 1px solid var(--border); color: var(--text); padding: 12px 24px; border-radius: 99px; font-size: 14px; z-index: 9999; transition: all .3s ease; white-space: nowrap; pointer-events: none; }
    #toast.show { transform: translateX(-50%) translateY(0); }
    #toast.success { border-color: #4ade80; color: #4ade80; }
    #toast.error { border-color: #f87171; color: #f87171; }
    .header { position: sticky; top: 0; z-index: 100; background: rgba(10,10,10,0.85); backdrop-filter: blur(16px); border-bottom: 1px solid var(--border); padding: 0 20px; height: 60px; display: flex; align-items: center; justify-content: space-between; }
    .header-logo { display: flex; align-items: center; gap: 10px; font-family: 'Rajdhani', sans-serif; font-size: 20px; font-weight: 700; color: var(--orange); }
    .admin-container { max-width: 1200px; margin: 0 auto; padding: 20px 16px 60px; }
    .admin-header { background: linear-gradient(135deg, rgba(255,140,66,0.15), rgba(255,140,66,0.05)); border: 1px solid var(--border); border-radius: 12px; padding: 20px; margin-bottom: 20px; }
    .admin-stats { display: flex; gap: 12px; margin-top: 12px; flex-wrap: wrap; }
    .stat-card { background: var(--card2); border-radius: 8px; padding: 12px 20px; text-align: center; min-width: 100px; flex: 1; }
    .stat-number { font-size: 24px; font-weight: 700; color: var(--orange); }
    .stat-label { font-size: 11px; color: var(--text-dim); }
    .admin-tabs { display: flex; gap: 6px; margin-bottom: 20px; flex-wrap: wrap; background: var(--card); padding: 6px; border-radius: 10px; border: 1px solid var(--border); }
    .admin-tab { padding: 8px 16px; background: transparent; border: none; color: var(--text-dim); border-radius: 8px; cursor: pointer; font-size: 13px; font-weight: 500; transition: all .2s; font-family: 'Exo 2', sans-serif; }
    .admin-tab.active { background: var(--orange); color: #000; }
    .admin-panel { display: none; }
    .admin-panel.active { display: block; }
    .dashboard-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    @media(max-width:768px){ .dashboard-grid { grid-template-columns: 1fr; } }
    .dash-card { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 16px; }
    .dash-card-title { font-weight: 700; font-size: 14px; margin-bottom: 12px; display: flex; align-items: center; justify-content: space-between; color: var(--orange); flex-wrap: wrap; gap: 8px; }
    .visitor-list, .activity-list { display: flex; flex-direction: column; gap: 8px; max-height: 350px; overflow-y: auto; }
    .visitor-item, .activity-item { display: flex; align-items: center; justify-content: space-between; padding: 10px 12px; background: var(--card2); border-radius: 8px; border: 1px solid rgba(255,255,255,0.05); font-size: 13px; cursor: pointer; transition: all .2s; }
    .visitor-item:hover { background: var(--orange-dim); border-color: var(--orange); }
    .visitor-info, .activity-info { display: flex; align-items: center; gap: 8px; flex: 1; min-width: 0; flex-wrap: wrap; }
    .visitor-name { font-weight: 600; font-size: 13px; }
    .visitor-detail { color: var(--text-dim); font-size: 11px; }
    .visitor-time { font-size: 10px; color: var(--text-dim); white-space: nowrap; }
    .badge { padding: 2px 8px; border-radius: 10px; font-size: 10px; font-weight: 600; }
    .badge.user { background: var(--orange-dim); color: var(--orange); }
    .badge.guest { background: #333; color: #aaa; }
    .overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.85); backdrop-filter: blur(8px); z-index: 500; display: flex; align-items: center; justify-content: center; padding: 20px; }
    .overlay.hidden { display: none !important; }
    .modal { background: var(--card); border: 1px solid var(--border); border-radius: 16px; padding: 28px; width: 100%; max-width: 650px; max-height: 90vh; overflow-y: auto; box-shadow: 0 4px 32px rgba(0,0,0,0.8); }
    .modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 10px; }
    .modal-title { font-family: 'Rajdhani', sans-serif; font-size: 20px; font-weight: 700; color: var(--orange); }
    .modal-close-btn { background: var(--glass); border: 1px solid rgba(255,255,255,0.08); color: var(--text-dim); width: 32px; height: 32px; border-radius: 50%; cursor: pointer; font-size: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
    .detail-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 13px; }
    .detail-label { color: var(--text-dim); min-width: 120px; }
    .detail-value { font-weight: 500; text-align: right; word-break: break-all; }
    .history-timeline { position: relative; padding-left: 20px; }
    .history-timeline::before { content: ''; position: absolute; left: 6px; top: 0; bottom: 0; width: 2px; background: var(--border); }
    .history-item { position: relative; padding: 10px 0 10px 20px; border-bottom: 1px solid rgba(255,255,255,0.03); }
    .history-item::before { content: ''; position: absolute; left: -17px; top: 16px; width: 8px; height: 8px; border-radius: 50%; background: var(--orange); }
    .history-time { font-size: 11px; color: var(--orange); font-weight: 600; margin-bottom: 4px; }
    .history-details { display: flex; flex-wrap: wrap; gap: 6px; }
    .history-badge { font-size: 9px; padding: 2px 6px; border-radius: 4px; background: var(--card2); color: var(--text-dim); border: 1px solid rgba(255,255,255,0.05); }
    .confirm-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.9); z-index: 9999; display: flex; align-items: center; justify-content: center; padding: 20px; }
    .confirm-overlay.hidden { display: none !important; }
    .confirm-box { background: var(--card); border: 1px solid var(--border); border-radius: 16px; padding: 28px; max-width: 400px; width: 90%; text-align: center; }
    .spinner { width: 32px; height: 32px; border: 3px solid var(--border); border-top-color: var(--orange); border-radius: 50%; animation: spin .8s linear infinite; margin: 20px auto; }
    @keyframes spin { to { transform: rotate(360deg); } }
    .login-container { display: flex; align-items: center; justify-content: center; min-height: 100vh; padding: 20px; }
    .login-box { background: var(--card); border: 1px solid var(--border); border-radius: 20px; padding: 32px; width: 100%; max-width: 380px; }
    .login-logo { text-align: center; margin-bottom: 24px; font-family: 'Rajdhani', sans-serif; font-size: 24px; font-weight: 700; color: var(--orange); }
    ::-webkit-scrollbar { width: 4px; } ::-webkit-scrollbar-track { background: var(--dark); } ::-webkit-scrollbar-thumb { background: var(--orange); border-radius: 4px; }
    .apk-link-display { background: var(--card2); border: 1px solid var(--border); border-radius: 8px; padding: 10px 14px; font-size: 12px; color: var(--orange); word-break: break-all; margin-top: 8px; }
    
    /* Firebase Config Styles */
    .firebase-status-card { background: linear-gradient(135deg, rgba(34,197,94,0.1), rgba(34,197,94,0.05)); border: 1px solid rgba(34,197,94,0.3); border-radius: 12px; padding: 20px; margin-bottom: 20px; }
    .firebase-status-card.not-connected { background: linear-gradient(135deg, rgba(255,140,66,0.1), rgba(255,140,66,0.05)); border-color: var(--border); }
    .firebase-status-header { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; }
    .firebase-status-icon { font-size: 24px; }
    .firebase-status-title { font-weight: 700; font-size: 16px; }
    .firebase-connected-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(34,197,94,0.2); color: #4ade80; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 600; }
    .firebase-info-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 16px; }
    .firebase-info-item { background: var(--card2); border-radius: 8px; padding: 12px; }
    .firebase-info-label { font-size: 11px; color: var(--text-dim); margin-bottom: 4px; text-transform: uppercase; }
    .firebase-info-value { font-weight: 600; font-size: 13px; color: var(--text); word-break: break-all; }
    .upload-zone { border: 2px dashed var(--border); border-radius: 12px; padding: 30px; text-align: center; cursor: pointer; transition: all .3s; background: var(--card2); }
    .upload-zone:hover { border-color: var(--orange); background: var(--orange-dim); }
    .upload-zone.has-file { border-color: #4ade80; background: rgba(34,197,94,0.1); }
    .upload-zone-icon { font-size: 40px; margin-bottom: 10px; }
    .upload-zone-text { font-size: 14px; color: var(--text-dim); }
    .upload-zone-text strong { color: var(--orange); }
    .file-input { display: none; }
    
    /* Remote Config Styles */
    .remote-config-section { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 20px; margin-bottom: 20px; }
    .remote-config-header { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px; }
    .remote-config-title { font-weight: 700; font-size: 16px; color: var(--orange); }
    .param-list { display: flex; flex-direction: column; gap: 10px; max-height: 400px; overflow-y: auto; }
    .param-item { background: var(--card2); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 14px; display: flex; flex-direction: column; gap: 10px; transition: all .2s; }
    .param-item:hover { border-color: var(--orange); }
    .param-item-header { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; }
    .param-key { font-weight: 700; font-size: 14px; color: var(--orange); font-family: monospace; }
    .param-type-badge { font-size: 10px; padding: 2px 8px; border-radius: 10px; background: var(--orange-dim); color: var(--orange); font-weight: 600; text-transform: uppercase; }
    .param-value-display { background: var(--dark); border-radius: 6px; padding: 8px 12px; font-family: monospace; font-size: 13px; word-break: break-all; max-height: 100px; overflow-y: auto; }
    .param-actions { display: flex; gap: 6px; flex-wrap: wrap; }
    .param-edit-row { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
    .param-edit-row.full-width { grid-template-columns: 1fr; }
    
    /* Add/Edit Parameter Modal */
    .param-form { display: flex; flex-direction: column; gap: 14px; }
    .param-form .input-group { margin-bottom: 0; }
    
    /* Empty state */
    .empty-state { text-align: center; padding: 40px 20px; color: var(--text-dim); }
    .empty-state-icon { font-size: 48px; margin-bottom: 12px; opacity: 0.5; }
    .empty-state-text { font-size: 14px; }
    
    /* Date badges */
    .date-badge { display: inline-flex; align-items: center; gap: 4px; font-size: 11px; color: var(--text-dim); background: var(--card2); padding: 4px 8px; border-radius: 6px; }
    
    /* File preview */
    .file-preview { background: var(--card2); border-radius: 8px; padding: 12px; margin-top: 12px; font-size: 12px; max-height: 150px; overflow-y: auto; }
    .file-preview pre { margin: 0; white-space: pre-wrap; word-break: break-all; font-family: monospace; color: var(--text-dim); }
    
    /* Remote Config in Edit App */
    .app-remote-config-section { background: var(--card2); border: 1px solid var(--border); border-radius: 12px; padding: 16px; margin-top: 16px; }
    .app-remote-config-title { font-weight: 700; font-size: 14px; color: var(--orange); margin-bottom: 12px; display: flex; align-items: center; gap: 8px; }
    
    /* Type selector */
    .type-selector { display: flex; gap: 8px; flex-wrap: wrap; }
    .type-option { padding: 6px 14px; border-radius: 6px; font-size: 12px; cursor: pointer; border: 1px solid var(--border); background: var(--card2); color: var(--text-dim); transition: all .2s; }
    .type-option:hover { border-color: var(--orange); }
    .type-option.selected { background: var(--orange); color: #000; border-color: var(--orange); font-weight: 600; }
    
    /* Toggle switch */
    .toggle-switch { position: relative; width: 44px; height: 24px; }
    .toggle-switch input { opacity: 0; width: 0; height: 0; }
    .toggle-slider { position: absolute; cursor: pointer; inset: 0; background: var(--card2); border: 1px solid var(--border); border-radius: 24px; transition: .3s; }
    .toggle-slider::before { content: ''; position: absolute; height: 18px; width: 18px; left: 2px; bottom: 2px; background: var(--text-dim); border-radius: 50%; transition: .3s; }
    .toggle-switch input:checked + .toggle-slider { background: rgba(34,197,94,0.3); border-color: #4ade80; }
    .toggle-switch input:checked + .toggle-slider::before { transform: translateX(20px); background: #4ade80; }
    
    /* JSON Viewer */
    .json-viewer { background: var(--dark); border-radius: 8px; padding: 12px; font-family: monospace; font-size: 11px; max-height: 200px; overflow-y: auto; white-space: pre-wrap; word-break: break-all; color: var(--text-dim); }
  </style>
</head>
<body>

<div id="toast"></div>

<!-- CONFIRMATION DIALOG -->
<div class="confirm-overlay hidden" id="confirmOverlay">
  <div class="confirm-box">
    <div style="font-size:40px;margin-bottom:10px;">⚠️</div>
    <div style="font-weight:700;font-size:16px;margin-bottom:6px;" id="confirmTitle">Confirm</div>
    <div style="color:var(--text-dim);font-size:13px;" id="confirmMsg">Are you sure?</div>
    <div style="display:flex;gap:10px;margin-top:20px;justify-content:center;">
      <button class="btn btn-outline btn-sm" id="btnConfirmCancel">Cancel</button>
      <button class="btn btn-danger btn-sm" id="confirmYesBtn">Yes, Delete</button>
    </div>
  </div>
</div>

<!-- LOGIN -->
<div id="loginPage" class="login-container">
  <div class="login-box">
    <div class="login-logo">⚙️ SamWeb Admin</div>
    <div class="input-group">
      <label>Username / Email</label>
      <input type="text" id="adminUser" placeholder="Enter username or email">
    </div>
    <div class="input-group">
      <label>Password</label>
      <input type="password" id="adminPass" placeholder="Enter password">
    </div>
    <button class="btn btn-primary" style="width:100%;" id="btnLogin">🔐 Login</button>
  </div>
</div>

<!-- DASHBOARD -->
<div id="adminDashboard" style="display:none;">
  <header class="header">
    <div class="header-logo">⚙️ SamWeb Admin</div>
    <button class="btn btn-outline btn-sm" id="btnLogout">🚪 Logout</button>
  </header>
  <div class="admin-container">
    <div class="admin-header">
      <div style="font-family:'Rajdhani',sans-serif;font-size:20px;font-weight:700;">Dashboard</div>
      <div class="admin-stats">
        <div class="stat-card"><div class="stat-number" id="totalUsers">0</div><div class="stat-label">Users</div></div>
        <div class="stat-card"><div class="stat-number" id="totalApps">0</div><div class="stat-label">Apps</div></div>
        <div class="stat-card"><div class="stat-number" id="totalReports">0</div><div class="stat-label">Reports</div></div>
        <div class="stat-card"><div class="stat-number" id="totalVisitors">0</div><div class="stat-label">Visitors</div></div>
      </div>
    </div>

    <div class="admin-tabs" id="adminTabs">
      <button class="admin-tab active" data-panel="dashboard">📊 Dashboard</button>
      <button class="admin-tab" data-panel="addApp">➕ Add App</button>
      <button class="admin-tab" data-panel="appsList">📋 Apps</button>
      <button class="admin-tab" data-panel="usersList">👥 Users</button>
      <button class="admin-tab" data-panel="reportsPanel">📊 Reports</button>
      <button class="admin-tab" data-panel="settings">⚙️ Settings</button>
    </div>

    <div class="admin-panel active" id="dashboard">
      <div class="dashboard-grid">
        <div class="dash-card">
          <div class="dash-card-title">
            <span>👥 Visitors (Click to view)</span>
            <button class="btn btn-warning btn-xs" id="btnClearAllVisitors">🗑 Clear All</button>
          </div>
          <div class="visitor-list" id="visitorListContainer"><div class="spinner"></div></div>
        </div>
        <div class="dash-card">
          <div class="dash-card-title">
            <span>📋 Activity Log</span>
            <button class="btn btn-warning btn-xs" id="btnClearAllActivity">🗑 Clear All</button>
          </div>
          <div class="activity-list" id="activityLogContainer"><div class="spinner"></div></div>
        </div>
      </div>
    </div>

    <div class="admin-panel" id="addApp">
      <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:18px;">
        <div style="font-weight:700;font-size:16px;margin-bottom:14px;">➕ Add App</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
          <div class="input-group" style="margin-bottom:10px;"><label>Name *</label><input id="aName" placeholder="App name"></div>
          <div class="input-group" style="margin-bottom:10px;"><label>Category</label>
            <select id="aCategory">
              <option>Social</option><option>Games</option><option>Tools</option>
              <option>Entertainment</option><option>Other</option>
            </select>
          </div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
          <div class="input-group" style="margin-bottom:10px;"><label>Icon (Emoji)</label><input id="aIcon" value="📱" placeholder="📱"></div>
          <div class="input-group" style="margin-bottom:10px;"><label>Image URL</label><input id="aImageUrl" placeholder="https://example.com/image.png"></div>
        </div>
        <div class="input-group" style="margin-bottom:10px;"><label>Download Link</label><input id="aLink" placeholder="https://play.google.com/..."></div>
        <div class="input-group" style="margin-bottom:10px;"><label>Description *</label><textarea id="aDesc" rows="2" placeholder="Describe the app..."></textarea></div>
        <div style="font-size:12px;color:var(--text-dim);margin-bottom:8px;font-weight:600;">📸 App Screenshots (optional)</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
          <div class="input-group" style="margin-bottom:8px;"><label>Screenshot 1</label><input id="aScreen1" placeholder="https://..."></div>
          <div class="input-group" style="margin-bottom:8px;"><label>Screenshot 2</label><input id="aScreen2" placeholder="https://..."></div>
          <div class="input-group" style="margin-bottom:8px;"><label>Screenshot 3</label><input id="aScreen3" placeholder="https://..."></div>
          <div class="input-group" style="margin-bottom:8px;"><label>Screenshot 4</label><input id="aScreen4" placeholder="https://..."></div>
          <div class="input-group" style="margin-bottom:8px;"><label>Screenshot 5</label><input id="aScreen5" placeholder="https://..."></div>
        </div>
        <button class="btn btn-primary btn-sm" id="btnAddApp">➕ Add App</button>
      </div>
    </div>

    <div class="admin-panel" id="appsList">
      <div style="font-weight:700;font-size:18px;margin-bottom:16px;">📋 Apps</div>
      <div id="adminAppsList"><div class="spinner"></div></div>
    </div>

    <div class="admin-panel" id="usersList">
      <div style="font-weight:700;font-size:18px;margin-bottom:16px;">👥 Users</div>
      <div id="adminUsersList"><div class="spinner"></div></div>
    </div>

    <div class="admin-panel" id="reportsPanel">
      <div style="font-weight:700;font-size:18px;margin-bottom:16px;">📊 Reports</div>
      <div id="adminReportsList"><div class="spinner"></div></div>
    </div>

    <div class="admin-panel" id="settings">
      <!-- Firebase Config Section -->
      <div class="firebase-status-card not-connected" id="firebaseStatusCard">
        <div class="firebase-status-header">
          <span class="firebase-status-icon">🔥</span>
          <span class="firebase-status-title">Firebase Configuration</span>
        </div>
        <div id="firebaseStatusContent">
          <div class="spinner" style="margin:10px auto;"></div>
        </div>
      </div>

      <!-- Remote Config Section -->
      <div class="remote-config-section" id="remoteConfigSection">
        <div class="remote-config-header">
          <div class="remote-config-title">🔧 Remote Config Parameters</div>
          <button class="btn btn-primary btn-sm" id="btnAddRemoteParam">➕ Add Parameter</button>
        </div>
        <div class="param-list" id="remoteConfigList">
          <div class="spinner"></div>
        </div>
      </div>

      <!-- Admin Credentials Section -->
      <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:24px;margin-bottom:20px;">
        <div style="font-weight:700;font-size:18px;margin-bottom:16px;">🔐 Admin Credentials</div>
        <div class="input-group"><label>Current Password</label><input type="password" id="currentAdminPass" placeholder="Enter current password"></div>
        <div class="input-group"><label>New Username</label><input id="newAdminUser" placeholder="Leave blank to keep current"></div>
        <div class="input-group"><label>New Password</label><input type="password" id="newAdminPass" placeholder="Leave blank to keep current"></div>
        <button class="btn btn-primary" id="btnUpdateAdmin">Update Credentials</button>
      </div>

      <!-- Website Settings Section -->
      <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:24px;margin-bottom:20px;">
        <div style="font-weight:700;font-size:18px;margin-bottom:16px;">🌐 Website Settings</div>
        <div class="input-group"><label>Website Name</label><input id="websiteNameInput" value="SamWeb Store" placeholder="SamWeb Store"></div>
        <div class="input-group">
          <label>Website Logo Image URL</label>
          <input id="logoUrlInput" placeholder="https://example.com/logo.png" type="url">
          <div id="logoPreviewWrap" style="display:none;margin-top:8px;"><img id="logoPreview" style="max-width:72px;max-height:72px;border-radius:12px;border:1px solid var(--border);" src="" alt="Logo Preview"></div>
        </div>
        <button class="btn btn-primary" id="btnSaveSettings">💾 Save Settings</button>
      </div>

      <!-- APK Download Link Section -->
      <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:24px;">
        <div style="font-weight:700;font-size:18px;margin-bottom:6px;color:var(--orange);">📦 APK Download Link</div>
        <div style="color:var(--text-dim);font-size:13px;margin-bottom:16px;">এই link টা user website এর side menu তে "Download APK" button এ click করলে খুলবে।</div>
        <div class="input-group">
          <label>APK Download URL</label>
          <input id="apkLinkInput" placeholder="https://example.com/app.apk" type="url">
        </div>
        <div id="currentApkLinkDisplay" style="display:none;">
          <div style="font-size:12px;color:var(--text-dim);margin-bottom:4px;">Current Link:</div>
          <div class="apk-link-display" id="currentApkLinkText"></div>
        </div>
        <div style="display:flex;gap:10px;margin-top:12px;flex-wrap:wrap;">
          <button class="btn btn-success" id="btnSaveApkLink">💾 Save APK Link</button>
          <button class="btn btn-danger btn-sm" id="btnRemoveApkLink">🗑 Remove Link</button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- EDIT APP MODAL -->
<div class="overlay hidden" id="editAppOverlay">
  <div class="modal" style="max-width:750px;">
    <div class="modal-header">
      <span class="modal-title">✏️ Edit App</span>
      <button class="modal-close-btn" data-close="editAppOverlay">✕</button>
    </div>
    <div id="editAppContent"></div>
  </div>
</div>

<!-- VISITOR DETAIL MODAL -->
<div class="overlay hidden" id="visitorDetailOverlay">
  <div class="modal" style="max-width:700px;">
    <div class="modal-header">
      <span class="modal-title">👤 Visitor Details</span>
      <div style="display:flex;gap:6px;flex-wrap:wrap;">
        <button class="btn btn-warning btn-xs" id="btnClearHistory">🗑 Clear History</button>
        <button class="btn btn-danger btn-xs" id="btnDeleteVisitor">❌ Delete</button>
        <button class="modal-close-btn" data-close="visitorDetailOverlay">✕</button>
      </div>
    </div>
    <div id="visitorDetailContent"><div class="spinner"></div></div>
  </div>
</div>

<!-- ADD/EDIT REMOTE PARAM MODAL -->
<div class="overlay hidden" id="paramModalOverlay">
  <div class="modal" style="max-width:500px;">
    <div class="modal-header">
      <span class="modal-title" id="paramModalTitle">➕ Add Parameter</span>
      <button class="modal-close-btn" data-close="paramModalOverlay">✕</button>
    </div>
    <div id="paramModalContent">
      <div class="param-form">
        <div class="input-group">
          <label>Parameter Key *</label>
          <input id="paramKeyInput" placeholder="e.g., maintenance_mode">
        </div>
        <div class="input-group">
          <label>Value *</label>
          <input id="paramValueInput" placeholder="Enter value">
        </div>
        <div class="input-group">
          <label>Data Type *</label>
          <div class="type-selector" id="typeSelector">
            <div class="type-option selected" data-type="string">String</div>
            <div class="type-option" data-type="number">Number</div>
            <div class="type-option" data-type="boolean">Boolean</div>
            <div class="type-option" data-type="json">JSON</div>
          </div>
        </div>
        <div style="display:flex;gap:10px;margin-top:10px;">
          <button class="btn btn-primary" id="btnSaveParam" style="flex:1;">💾 Save Parameter</button>
          <button class="btn btn-outline" data-close="paramModalOverlay">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- CONFIRM REPLACE FILE MODAL -->
<div class="overlay hidden" id="replaceFileOverlay">
  <div class="modal" style="max-width:450px;">
    <div class="modal-header">
      <span class="modal-title">🔄 Replace google-services.json</span>
      <button class="modal-close-btn" data-close="replaceFileOverlay">✕</button>
    </div>
    <div style="text-align:center;">
      <div style="font-size:48px;margin-bottom:12px;">⚠️</div>
      <p style="color:var(--text-dim);font-size:14px;margin-bottom:20px;">
        This will replace the existing <strong style="color:var(--orange);">google-services.json</strong> file.
        Your Remote Config parameters will be preserved.
      </p>
      <div style="display:flex;gap:10px;justify-content:center;">
        <button class="btn btn-outline" data-close="replaceFileOverlay">Cancel</button>
        <button class="btn btn-warning" id="btnConfirmReplace">✅ Continue</button>
      </div>
    </div>
  </div>
</div>

<script type="module">
import{initializeApp}from"https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import{getDatabase,ref,push,set,get,remove,update}from"https://www.gstatic.com/firebasejs/10.12.0/firebase-database.js";
const firebaseConfig={
  apiKey:"AIzaSyDo4VtvFjkHK_qPKw_8OvjWB3DF93m0_vE",
  authDomain:"samva-app-store.firebaseapp.com",
  databaseURL:"https://samva-app-store-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId:"samva-app-store",
  storageBucket:"samva-app-store.firebasestorage.app",
  messagingSenderId:"42570449631",
  appId:"1:42570449631:web:0c81be27dc888a97db9f6a"
};
const app=initializeApp(firebaseConfig);
const db=getDatabase(app);
window._db=db;window._ref=ref;window._push=push;window._set=set;window._get=get;window._remove=remove;window._update=update;
window.dispatchEvent(new Event('firebaseReady'));
</script>

<script>
// ============ STATE ============
let firebaseReady = false, currentAdminKey = null, allVisitorsData = [], currentVisitorKey = null;
let confirmCallback = null;

// Firebase Config State
let firebaseConfigData = null;
let selectedParamType = 'string';
let editingParamKey = null;

// ============ HELPERS ============
function toast(m, t = 'info') {
  const e = document.getElementById('toast');
  if (!e) return;
  e.textContent = m; e.className = 'show ' + t;
  clearTimeout(e._timeout);
  e._timeout = setTimeout(() => { if (e) e.className = ''; }, 2800);
}
function esc(s) {
  if (s === null || s === undefined) return '';
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
function formatNum(n) {
  n = Number(n) || 0;
  if (n >= 1e6) return (n / 1e6).toFixed(1) + 'M';
  if (n >= 1e3) return (n / 1e3).toFixed(1) + 'K';
  return String(n);
}
function formatDate(timestamp) {
  if (!timestamp) return 'N/A';
  return new Date(timestamp).toLocaleString('en-US', {
    year: 'numeric', month: 'short', day: 'numeric',
    hour: '2-digit', minute: '2-digit'
  });
}
function escapeJson(str) {
  return str.replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

// ============ CONFIRM DIALOG ============
function showConfirm(title, msg, cb) {
  document.getElementById('confirmTitle').textContent = title;
  document.getElementById('confirmMsg').textContent = msg;
  confirmCallback = cb;
  document.getElementById('confirmOverlay').classList.remove('hidden');
}
function closeConfirm() {
  document.getElementById('confirmOverlay').classList.add('hidden');
  confirmCallback = null;
}
function executeConfirm() {
  if (confirmCallback) {
    const cb = confirmCallback;
    confirmCallback = null;
    closeConfirm();
    cb();
  }
}

// ============ MODAL ============
function closeModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.add('hidden');
}

// ============ FIREBASE CONFIG STORAGE ============

// Load Firebase Config from Database
async function loadFirebaseConfig() {
  const content = document.getElementById('firebaseStatusContent');
  const card = document.getElementById('firebaseStatusCard');
  
  if (!content) return;
  
  try {
    const snap = await window._get(window._ref(window._db, 'settings/firebaseConfig'));
    
    if (snap.exists()) {
      firebaseConfigData = snap.val();
      
      card.classList.remove('not-connected');
      card.style.background = 'linear-gradient(135deg, rgba(34,197,94,0.1), rgba(34,197,94,0.05))';
      card.style.borderColor = 'rgba(34,197,94,0.3)';
      
      const uploadedAt = firebaseConfigData.uploadedAt ? formatDate(firebaseConfigData.uploadedAt) : 'N/A';
      const lastModified = firebaseConfigData.lastModified ? formatDate(firebaseConfigData.lastModified) : uploadedAt;
      
      content.innerHTML = `
        <div style="margin-bottom:16px;">
          <span class="firebase-connected-badge">✔ Firebase Connected</span>
        </div>
        
        <div class="firebase-info-grid">
          <div class="firebase-info-item">
            <div class="firebase-info-label">Project ID</div>
            <div class="firebase-info-value">${esc(firebaseConfigData.projectId || 'N/A')}</div>
          </div>
          <div class="firebase-info-item">
            <div class="firebase-info-label">Package Name</div>
            <div class="firebase-info-value">${esc(firebaseConfigData.packageName || 'N/A')}</div>
          </div>
          <div class="firebase-info-item">
            <div class="firebase-info-label">Project Number</div>
            <div class="firebase-info-value">${esc(firebaseConfigData.projectNumber || 'N/A')}</div>
          </div>
          <div class="firebase-info-item">
            <div class="firebase-info-label">Storage Bucket</div>
            <div class="firebase-info-value">${esc(firebaseConfigData.storageBucket || 'N/A')}</div>
          </div>
          <div class="firebase-info-item">
            <div class="firebase-info-label">API Key</div>
            <div class="firebase-info-value" style="font-size:11px;">${esc(firebaseConfigData.apiKey ? firebaseConfigData.apiKey.substring(0, 20) + '...' : 'N/A')}</div>
          </div>
          <div class="firebase-info-item">
            <div class="firebase-info-label">Mobile SDK App ID</div>
            <div class="firebase-info-value">${esc(firebaseConfigData.mobileSdkAppId || 'N/A')}</div>
          </div>
        </div>
        
        <div style="display:flex;gap:12px;margin-top:16px;flex-wrap:wrap;">
          <div class="date-badge">📅 Uploaded: ${uploadedAt}</div>
          <div class="date-badge">✏️ Modified: ${lastModified}</div>
        </div>
        
        <div style="display:flex;gap:10px;margin-top:16px;flex-wrap:wrap;">
          <button class="btn btn-warning btn-sm" id="btnReplaceGoogleJson">🔄 Replace google-services.json</button>
          <button class="btn btn-outline btn-sm" id="btnViewGoogleJson">👁 View JSON</button>
        </div>
        
        <div class="file-preview hidden" id="googleJsonPreview" style="margin-top:12px;">
          <pre id="googleJsonPreviewContent"></pre>
        </div>
      `;
      
      // Attach event listeners
      setTimeout(() => {
        const replaceBtn = document.getElementById('btnReplaceGoogleJson');
        const viewBtn = document.getElementById('btnViewGoogleJson');
        
        if (replaceBtn) replaceBtn.addEventListener('click', showReplaceFileModal);
        if (viewBtn) viewBtn.addEventListener('click', toggleJsonPreview);
      }, 100);
      
    } else {
      firebaseConfigData = null;
      card.classList.add('not-connected');
      content.innerHTML = `
        <div style="text-align:center;padding:20px 0;">
          <div style="font-size:48px;margin-bottom:12px;">📄</div>
          <div style="color:var(--text-dim);font-size:14px;margin-bottom:16px;">No google-services.json uploaded yet</div>
          <div class="upload-zone" id="uploadZone">
            <div class="upload-zone-icon">📤</div>
            <div class="upload-zone-text">
              <strong>Click to upload</strong> google-services.json<br>
              <span style="font-size:11px;">or drag and drop JSON file</span>
            </div>
          </div>
          <input type="file" class="file-input" id="googleJsonFileInput" accept=".json">
        </div>
      `;
      
      setTimeout(() => {
        const uploadZone = document.getElementById('uploadZone');
        const fileInput = document.getElementById('googleJsonFileInput');
        
        if (uploadZone) {
          uploadZone.addEventListener('click', () => fileInput?.click());
        }
        if (fileInput) {
          fileInput.addEventListener('change', handleGoogleJsonUpload);
        }
      }, 100);
    }
  } catch (e) {
    console.error('Error loading Firebase config:', e);
    content.innerHTML = '<div style="color:#f87171;padding:10px;text-align:center;">Error loading Firebase config</div>';
  }
}

// Handle google-services.json Upload
async function handleGoogleJsonUpload(event) {
  const file = event.target.files?.[0];
  if (!file) return;
  
  if (!file.name.endsWith('.json')) {
    toast('Please upload a valid JSON file', 'error');
    return;
  }
  
  try {
    const text = await file.text();
    let jsonData;
    
    try {
      jsonData = JSON.parse(text);
    } catch (parseError) {
      toast('Invalid JSON format', 'error');
      return;
    }
    
    // Extract Firebase config from google-services.json
    const projectInfo = extractFirebaseConfig(jsonData);
    
    if (!projectInfo) {
      toast('Invalid google-services.json structure', 'error');
      return;
    }
    
    // Save to Firebase Database
    const configData = {
      uploaded: true,
      uploadedAt: Date.now(),
      lastModified: Date.now(),
      projectId: projectInfo.project_id,
      projectNumber: projectInfo.project_number,
      packageName: projectInfo.package_name,
      storageBucket: projectInfo.storage_bucket,
      apiKey: projectInfo.api_key?.[0]?.current_key || '',
      mobileSdkAppId: projectInfo.client?.[0]?.client_info?.mobilesdk_app_id || '',
      googleServicesJson: text
    };
    
    await window._set(window._ref(window._db, 'settings/firebaseConfig'), configData);
    
    toast('✅ google-services.json uploaded successfully!', 'success');
    await logActivity('📄 Uploaded google-services.json', projectInfo.project_id);
    
    // Reload the display
    loadFirebaseConfig();
    loadRemoteConfig();
    
  } catch (e) {
    console.error('Upload error:', e);
    toast('Error uploading file: ' + e.message, 'error');
  }
}

// Extract Firebase config from google-services.json
function extractFirebaseConfig(json) {
  if (!json) return null;
  
  // Standard google-services.json structure
  if (json.project_info) {
    return {
      project_id: json.project_info.project_id,
      project_number: json.project_info.project_number,
      package_name: json.client?.[0]?.client_info?.android_client_info?.package_name || '',
      storage_bucket: json.project_info.storage_bucket,
      api_key: json.client?.[0]?.api_key,
      client: json.client
    };
  }
  
  // Alternative structure (sometimes found in older files)
  if (json.projectId) {
    return {
      project_id: json.projectId,
      project_number: json.projectNumber || '',
      package_name: json.package_name || json.client?.[0]?.client_info?.android_client_info?.package_name || '',
      storage_bucket: json.storageBucket || '',
      api_key: json.apiKey ? [{ current_key: json.apiKey }] : [],
      client: json.client || []
    };
  }
  
  return null;
}

// Show Replace File Modal
function showReplaceFileModal() {
  document.getElementById('replaceFileOverlay').classList.remove('hidden');
}

// Handle Replace File
async function handleReplaceGoogleJson() {
  closeModal('replaceFileOverlay');
  
  // Trigger file input click
  const fileInput = document.getElementById('googleJsonFileInput') || document.createElement('input');
  fileInput.type = 'file';
  fileInput.accept = '.json';
  fileInput.id = 'googleJsonFileInputReplace';
  
  fileInput.addEventListener('change', async (event) => {
    const file = event.target.files?.[0];
    if (!file) return;
    
    try {
      const text = await file.text();
      let jsonData;
      
      try {
        jsonData = JSON.parse(text);
      } catch (parseError) {
        toast('Invalid JSON format', 'error');
        return;
      }
      
      const projectInfo = extractFirebaseConfig(jsonData);
      
      if (!projectInfo) {
        toast('Invalid google-services.json structure', 'error');
        return;
      }
      
      // Preserve existing Remote Config parameters
      const existingConfig = firebaseConfigData || {};
      const existingRemoteConfig = existingConfig.remoteConfig || {};
      
      // Update Firebase config (keep existing Remote Config)
      const configData = {
        uploaded: true,
        uploadedAt: existingConfig.uploadedAt || Date.now(),
        lastModified: Date.now(),
        projectId: projectInfo.project_id,
        projectNumber: projectInfo.project_number,
        packageName: projectInfo.package_name,
        storageBucket: projectInfo.storage_bucket,
        apiKey: projectInfo.api_key?.[0]?.current_key || '',
        mobileSdkAppId: projectInfo.client?.[0]?.client_info?.mobilesdk_app_id || '',
        googleServicesJson: text,
        remoteConfig: existingRemoteConfig
      };
      
      await window._set(window._ref(window._db, 'settings/firebaseConfig'), configData);
      
      toast('✅ google-services.json replaced successfully!', 'success');
      await logActivity('🔄 Replaced google-services.json', projectInfo.project_id);
      
      loadFirebaseConfig();
      
    } catch (e) {
      console.error('Replace error:', e);
      toast('Error replacing file: ' + e.message, 'error');
    }
  });
  
  fileInput.click();
}

// Toggle JSON Preview
function toggleJsonPreview() {
  const preview = document.getElementById('googleJsonPreview');
  const content = document.getElementById('googleJsonPreviewContent');
  
  if (!preview || !firebaseConfigData?.googleServicesJson) return;
  
  if (preview.classList.contains('hidden')) {
    content.textContent = JSON.stringify(JSON.parse(firebaseConfigData.googleServicesJson), null, 2);
    preview.classList.remove('hidden');
  } else {
    preview.classList.add('hidden');
  }
}

// ============ REMOTE CONFIG STORAGE ============

// Load Remote Config Parameters
async function loadRemoteConfig() {
  const list = document.getElementById('remoteConfigList');
  if (!list) return;
  
  list.innerHTML = '<div class="spinner"></div>';
  
  try {
    const snap = await window._get(window._ref(window._db, 'settings/firebaseConfig/remoteConfig'));
    
    if (!snap.exists() || Object.keys(snap.val() || {}).length === 0) {
      list.innerHTML = `
        <div class="empty-state">
          <div class="empty-state-icon">🔧</div>
          <div class="empty-state-text">No Remote Config parameters yet.<br>Click "Add Parameter" to create one.</div>
        </div>
      `;
      return;
    }
    
    const params = snap.val();
    let html = '';
    
    // Sort by key
    const sortedKeys = Object.keys(params).sort();
    
    sortedKeys.forEach(key => {
      const param = params[key];
      const type = param.type || 'string';
      let valueDisplay = param.value;
      
      if (type === 'boolean') {
        valueDisplay = param.value === true || param.value === 'true' ? '✅ true' : '❌ false';
      } else if (type === 'json') {
        try {
          valueDisplay = JSON.stringify(typeof param.value === 'string' ? JSON.parse(param.value) : param.value, null, 2);
        } catch {
          valueDisplay = param.value;
        }
      }
      
      html += `
        <div class="param-item" data-key="${esc(key)}">
          <div class="param-item-header">
            <span class="param-key">${esc(key)}</span>
            <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
              <span class="param-type-badge">${type}</span>
              <div class="param-actions">
                <button class="btn btn-outline btn-xs" onclick="editRemoteParam('${esc(key)}')">✏️ Edit</button>
                <button class="btn btn-danger btn-xs" onclick="deleteRemoteParam('${esc(key)}')">🗑 Delete</button>
              </div>
            </div>
          </div>
          <div class="param-value-display">${type === 'json' ? '<pre style="margin:0;white-space:pre-wrap;">' + esc(valueDisplay) + '</pre>' : esc(valueDisplay)}</div>
        </div>
      `;
    });
    
    list.innerHTML = html;
    
  } catch (e) {
    console.error('Error loading Remote Config:', e);
    list.innerHTML = '<div style="color:#f87171;padding:10px;">Error loading parameters</div>';
  }
}

// Show Add Parameter Modal
function showAddParamModal() {
  editingParamKey = null;
  selectedParamType = 'string';
  
  document.getElementById('paramModalTitle').textContent = '➕ Add Parameter';
  document.getElementById('paramKeyInput').value = '';
  document.getElementById('paramValueInput').value = '';
  
  // Reset type selector
  document.querySelectorAll('.type-option').forEach(opt => {
    opt.classList.toggle('selected', opt.dataset.type === 'string');
  });
  
  document.getElementById('paramModalOverlay').classList.remove('hidden');
}

// Edit Parameter
function editRemoteParam(key) {
  editingParamKey = key;
  
  // Get current value from loaded config
  window._get(window._ref(window._db, `settings/firebaseConfig/remoteConfig/${key}`)).then(snap => {
    if (!snap.exists()) {
      toast('Parameter not found', 'error');
      return;
    }
    
    const param = snap.val();
    selectedParamType = param.type || 'string';
    
    document.getElementById('paramModalTitle').textContent = '✏️ Edit Parameter';
    document.getElementById('paramKeyInput').value = key;
    document.getElementById('paramKeyInput').readOnly = true; // Can't change key in edit mode
    document.getElementById('paramKeyInput').style.opacity = '0.5';
    
    let displayValue = param.value;
    if (selectedParamType === 'boolean') {
      displayValue = param.value === true || param.value === 'true' ? 'true' : 'false';
    } else if (selectedParamType === 'json') {
      try {
        displayValue = typeof param.value === 'string' ? param.value : JSON.stringify(param.value, null, 2);
      } catch {
        displayValue = param.value || '';
      }
    }
    
    document.getElementById('paramValueInput').value = displayValue;
    
    // Update type selector
    document.querySelectorAll('.type-option').forEach(opt => {
      opt.classList.toggle('selected', opt.dataset.type === selectedParamType);
    });
    
    document.getElementById('paramModalOverlay').classList.remove('hidden');
  });
}

// Save Parameter
async function saveRemoteParam() {
  const keyInput = document.getElementById('paramKeyInput');
  const valueInput = document.getElementById('paramValueInput');
  
  let key = keyInput.value.trim();
  let value = valueInput.value.trim();
  
  if (!key) {
    toast('Parameter key is required', 'error');
    return;
  }
  
  // Validate key format
  if (!/^[a-zA-Z_][a-zA-Z0-9_]*$/.test(key)) {
    toast('Key must start with letter/underscore and contain only alphanumeric/underscore', 'error');
    return;
  }
  
  if (editingParamKey) {
    // Editing existing param - can't change key
    key = editingParamKey;
  } else {
    // Check if key already exists
    try {
      const existing = await window._get(window._ref(window._db, `settings/firebaseConfig/remoteConfig/${key}`));
      if (existing.exists()) {
        toast('Parameter with this key already exists', 'error');
        return;
      }
    } catch (e) {}
  }
  
  // Parse value based on type
  let parsedValue;
  switch (selectedParamType) {
    case 'number':
      parsedValue = Number(value);
      if (isNaN(parsedValue)) {
        toast('Please enter a valid number', 'error');
        return;
      }
      break;
    case 'boolean':
      parsedValue = value === 'true' || value === '1' || value.toLowerCase() === 'yes';
      break;
    case 'json':
      try {
        parsedValue = JSON.parse(value);
      } catch {
        toast('Please enter valid JSON', 'error');
        return;
      }
      break;
    default:
      parsedValue = value;
  }
  
  try {
    const paramData = {
      value: parsedValue,
      type: selectedParamType,
      updatedAt: Date.now()
    };
    
    if (!editingParamKey) {
      paramData.createdAt = Date.now();
    }
    
    // Get existing remote config
    const remoteSnap = await window._get(window._ref(window._db, 'settings/firebaseConfig/remoteConfig'));
    const existingParams = remoteSnap.exists() ? { ...remoteSnap.val() } : {};
    
    existingParams[key] = paramData;
    
    // Update Firebase
    await window._update(window._ref(window._db, 'settings/firebaseConfig'), {
      remoteConfig: existingParams,
      lastModified: Date.now()
    });
    
    toast(editingParamKey ? '✅ Parameter updated!' : '✅ Parameter added!', 'success');
    await logActivity(editingParamKey ? '✏️ Updated Remote Config' : '➕ Added Remote Config', `${key} (${selectedParamType})`);
    
    closeModal('paramModalOverlay');
    loadRemoteConfig();
    
    // Reset key input for next add
    keyInput.readOnly = false;
    keyInput.style.opacity = '1';
    editingParamKey = null;
    
  } catch (e) {
    console.error('Save param error:', e);
    toast('Error saving parameter: ' + e.message, 'error');
  }
}

// Delete Parameter
async function deleteRemoteParam(key) {
  showConfirm('🗑 Delete Parameter?', `Delete parameter "${key}"? This cannot be undone.`, async () => {
    try {
      const remoteSnap = await window._get(window._ref(window._db, 'settings/firebaseConfig/remoteConfig'));
      
      if (remoteSnap.exists()) {
        const params = { ...remoteSnap.val() };
        delete params[key];
        
        await window._update(window._ref(window._db, 'settings/firebaseConfig'), {
          remoteConfig: params,
          lastModified: Date.now()
        });
      }
      
      toast('✅ Parameter deleted!', 'success');
      await logActivity('🗑 Deleted Remote Config', key);
      loadRemoteConfig();
      
    } catch (e) {
      console.error('Delete param error:', e);
      toast('Error deleting parameter: ' + e.message, 'error');
    }
  });
}

// Type Selector Handler
document.addEventListener('click', (e) => {
  const typeOpt = e.target.closest('.type-option');
  if (typeOpt) {
    selectedParamType = typeOpt.dataset.type;
    document.querySelectorAll('.type-option').forEach(opt => {
      opt.classList.toggle('selected', opt === typeOpt);
    });
  }
});

// ============ ACTIVITY LOG ============
async function logActivity(action, detail = '') {
  if (!firebaseReady || !currentAdminKey) return;
  try {
    const newRef = window._push(window._ref(window._db, 'adminActivity'));
    await window._set(newRef, {
      action, detail, timestamp: Date.now(), adminKey: currentAdminKey
    });
    loadActivity();
  } catch (e) { console.error('Activity log error:', e); }
}

// ============ EVENT DELEGATION ============
document.addEventListener('click', function (e) {
  const target = e.target;
  const id = target.id;

  if (id === 'btnConfirmCancel' || target.closest('#btnConfirmCancel')) { closeConfirm(); return; }
  if (id === 'confirmYesBtn' || target.closest('#confirmYesBtn')) { executeConfirm(); return; }
  if (id === 'btnConfirmReplace' || target.closest('#btnConfirmReplace')) { handleReplaceGoogleJson(); return; }

  const closeBtn = target.closest('[data-close]');
  if (closeBtn) {
    closeModal(closeBtn.getAttribute('data-close'));
    // Reset edit mode state when closing param modal
    if (closeBtn.getAttribute('data-close') === 'paramModalOverlay') {
      const keyInput = document.getElementById('paramKeyInput');
      if (keyInput) {
        keyInput.readOnly = false;
        keyInput.style.opacity = '1';
      }
      editingParamKey = null;
    }
    return;
  }

  if (target.classList.contains('overlay')) { 
    const overlayId = target.id;
    if (overlayId === 'paramModalOverlay') {
      const keyInput = document.getElementById('paramKeyInput');
      if (keyInput) {
        keyInput.readOnly = false;
        keyInput.style.opacity = '1';
      }
      editingParamKey = null;
    }
    closeModal(overlayId); 
    return; 
  }

  const tab = target.closest('.admin-tab');
  if (tab) {
    const panelId = tab.getAttribute('data-panel');
    if (panelId) showPanel(panelId);
    return;
  }

  const visitorItem = target.closest('.visitor-item');
  if (visitorItem) {
    const vk = visitorItem.getAttribute('data-visitor-key');
    if (vk) showVisitorDetail(vk);
    return;
  }

  if (id === 'btnClearHistory' || target.closest('#btnClearHistory')) {
    if (!currentVisitorKey) { toast('No visitor selected', 'error'); return; }
    showConfirm('Clear History?', 'Delete all visit history entries for this visitor?', async () => {
      try {
        await window._remove(window._ref(window._db, `visitors/${currentVisitorKey}/visitHistory`));
        toast('✅ History cleared!', 'success');
        await logActivity('🗑 Cleared Visitor History');
        showVisitorDetail(currentVisitorKey);
        loadVisitors();
        updateStats();
      } catch (e) { toast('Error: ' + e.message, 'error'); }
    });
    return;
  }

  if (id === 'btnDeleteVisitor' || target.closest('#btnDeleteVisitor')) {
    if (!currentVisitorKey) { toast('No visitor selected', 'error'); return; }
    showConfirm('Delete Visitor?', 'Permanently delete this visitor and all their data?', async () => {
      try {
        const oldKey = currentVisitorKey;
        await window._remove(window._ref(window._db, `visitors/${oldKey}`));
        toast('✅ Visitor deleted!', 'success');
        currentVisitorKey = null;
        closeModal('visitorDetailOverlay');
        await logActivity('🗑 Deleted Visitor', oldKey.substring(0, 12) + '...');
        loadVisitors();
        updateStats();
      } catch (e) { toast('Error: ' + e.message, 'error'); }
    });
    return;
  }

  if (id === 'btnClearAllVisitors' || target.closest('#btnClearAllVisitors')) {
    if (!firebaseReady) { toast('Not connected to server', 'error'); return; }
    showConfirm('Delete ALL Visitors?', 'This will permanently delete ALL visitor data!', async () => {
      try {
        await window._remove(window._ref(window._db, 'visitors'));
        toast('✅ All visitors deleted!', 'success');
        allVisitorsData = [];
        document.getElementById('totalVisitors').textContent = '0';
        loadVisitors();
        updateStats();
        await logActivity('🗑 Cleared ALL Visitors');
      } catch (e) { toast('Error: ' + e.message, 'error'); }
    });
    return;
  }

  if (id === 'btnClearAllActivity' || target.closest('#btnClearAllActivity')) {
    if (!firebaseReady) { toast('Not connected to server', 'error'); return; }
    showConfirm('Delete ALL Activity?', 'This will permanently delete ALL admin activity logs!', async () => {
      try {
        await window._remove(window._ref(window._db, 'adminActivity'));
        toast('✅ All activity deleted!', 'success');
        loadActivity();
      } catch (e) { toast('Error: ' + e.message, 'error'); }
    });
    return;
  }

  if (id === 'btnLogin' || target.closest('#btnLogin')) { doAdminLogin(); return; }
  if (id === 'btnLogout' || target.closest('#btnLogout')) { adminLogout(); return; }
  if (id === 'btnAddApp' || target.closest('#btnAddApp')) { addApp(); return; }
  if (id === 'btnUpdateAdmin' || target.closest('#btnUpdateAdmin')) { updateAdmin(); return; }
  if (id === 'btnSaveSettings' || target.closest('#btnSaveSettings')) { saveSettings(); return; }
  if (id === 'btnSaveApkLink' || target.closest('#btnSaveApkLink')) { saveApkLink(); return; }
  if (id === 'btnRemoveApkLink' || target.closest('#btnRemoveApkLink')) { removeApkLink(); return; }
  if (id === 'btnSaveEdit' || target.closest('#btnSaveEdit')) { saveEditApp(); return; }
  if (id === 'btnAddRemoteParam' || target.closest('#btnAddRemoteParam')) { showAddParamModal(); return; }
  if (id === 'btnSaveParam' || target.closest('#btnSaveParam')) { saveRemoteParam(); return; }

  if (id.startsWith('editAppBtn_')) { openEditApp(id.replace('editAppBtn_', '')); return; }
  if (id.startsWith('delAppBtn_')) {
    const key = id.replace('delAppBtn_', '');
    showConfirm('Delete App?', 'This cannot be undone.', () => deleteApp(key));
    return;
  }
  if (id.startsWith('delUserBtn_')) {
    const key = id.replace('delUserBtn_', '');
    showConfirm('Delete User?', 'This cannot be undone.', () => deleteUser(key));
    return;
  }
  if (id.startsWith('delReportBtn_')) {
    const key = id.replace('delReportBtn_', '');
    showConfirm('Delete Report?', 'This cannot be undone.', () => deleteReport(key));
    return;
  }
  
  // Edit param button (dynamically created)
  if (id.startsWith('editParamBtn_')) {
    const key = id.replace('editParamBtn_', '');
    editRemoteParam(key);
    return;
  }
  
  // Delete param button (dynamically created)
  if (id.startsWith('delParamBtn_')) {
    const key = id.replace('delParamBtn_', '');
    deleteRemoteParam(key);
    return;
  }
});

// ============ PANELS ============
function showPanel(id) {
  document.querySelectorAll('.admin-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.admin-tab').forEach(t => t.classList.remove('active'));
  const panel = document.getElementById(id);
  if (panel) panel.classList.add('active');
  const tab = document.querySelector(`.admin-tab[data-panel="${id}"]`);
  if (tab) tab.classList.add('active');

  if (id === 'dashboard') { loadVisitors(); loadActivity(); updateStats(); }
  if (id === 'appsList') loadApps();
  if (id === 'usersList') loadUsers();
  if (id === 'reportsPanel') loadReports();
  if (id === 'settings') {
    loadFirebaseConfig();
    loadRemoteConfig();
    loadApkLinkDisplay();
  }
}

// ============ VISITORS ============
async function loadVisitors() {
  const c = document.getElementById('visitorListContainer');
  if (!c) return;
  c.innerHTML = '<div class="spinner"></div>';
  try {
    const snap = await window._get(window._ref(window._db, 'visitors'));
    allVisitorsData = [];
    if (snap.exists()) {
      snap.forEach(ch => {
        const d = ch.val();
        d.key = ch.key;
        allVisitorsData.push(d);
      });
    }
    allVisitorsData.sort((a, b) => (b.lastVisit || 0) - (a.lastVisit || 0));
    const recent = allVisitorsData.slice(0, 25);
    let h = '';
    if (!recent.length) {
      h = '<div style="color:var(--text-dim);padding:20px;text-align:center;">No visitors yet</div>';
    } else {
      recent.forEach(v => {
        const lv = v.lastVisit ? new Date(v.lastVisit).toLocaleString('en-US', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }) : 'N/A';
        const dn = v.deviceName || 'Unknown';
        const hist = v.visitHistory;
        const hc = hist ? (Array.isArray(hist) ? hist.length : Object.keys(hist).length) : 0;
        h += `<div class="visitor-item" data-visitor-key="${esc(v.key)}">
          <div class="visitor-info">
            <span class="visitor-name">${esc(v.userName || dn)}</span>
            <span class="badge ${v.userName ? 'user' : 'guest'}">${v.userName ? 'user' : 'guest'}</span>
            <span class="visitor-detail">• ${esc(dn)}</span>
            <span class="visitor-detail">• ${esc(v.ram || 'N/A')}</span>
            <span class="visitor-detail">• ${hc} visits</span>
          </div>
          <div class="visitor-time">${lv}</div>
        </div>`;
      });
    }
    c.innerHTML = h;
    document.getElementById('totalVisitors').textContent = allVisitorsData.length;
  } catch (e) {
    c.innerHTML = '<div style="color:red;padding:10px;">Error loading visitors</div>';
  }
}

async function showVisitorDetail(vk) {
  const overlay = document.getElementById('visitorDetailOverlay');
  const content = document.getElementById('visitorDetailContent');
  if (!overlay || !content) return;

  overlay.classList.remove('hidden');
  content.innerHTML = '<div class="spinner"></div>';
  currentVisitorKey = vk;

  let v = null;
  try {
    const snap = await window._get(window._ref(window._db, `visitors/${vk}`));
    if (snap.exists()) { v = snap.val(); v.key = vk; }
  } catch (e) {
    content.innerHTML = '<div style="color:red;padding:40px;text-align:center;">❌ Error loading visitor data</div>';
    return;
  }

  if (!v) {
    content.innerHTML = '<div style="color:var(--text-dim);padding:40px;text-align:center;">❌ Visitor not found</div>';
    return;
  }

  const isU = !!v.userName;
  const dn = v.deviceName || 'Unknown Device';
  const fv = v.firstVisit ? new Date(v.firstVisit).toLocaleString() : 'N/A';
  const lv = v.lastVisit ? new Date(v.lastVisit).toLocaleString() : 'N/A';

  let h = `<div style="text-align:center;margin-bottom:20px;">
    <div style="width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,var(--orange),var(--orange-light));display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700;color:#000;margin:0 auto 10px;">${isU ? (v.userName || 'U')[0].toUpperCase() : '📱'}</div>
    <div style="font-size:18px;font-weight:700;">${esc(isU ? v.userName : dn)}</div>
    <div style="font-size:12px;color:var(--text-dim);">${isU ? 'Registered User' : 'Guest Device'} • ${v.visitCount || 0} total visits</div>
  </div>`;

  if (isU) {
    h += `
    <div class="detail-row"><span class="detail-label">👤 Name</span><span class="detail-value">${esc(v.userName)}</span></div>
    <div class="detail-row"><span class="detail-label">📧 Email</span><span class="detail-value">${esc(v.userEmail || 'N/A')}</span></div>
    <div class="detail-row"><span class="detail-label">📱 Phone</span><span class="detail-value">${esc(v.userPhone || 'N/A')}</span></div>
    <div class="detail-row"><span class="detail-label">⚧ Gender</span><span class="detail-value">${esc(v.userGender || 'N/A')}</span></div>`;
  }

  h += `
  <div class="detail-row"><span class="detail-label">📱 Device</span><span class="detail-value">${esc(dn)}</span></div>
  <div class="detail-row"><span class="detail-label">🧠 RAM</span><span class="detail-value">${esc(v.ram || 'N/A')}</span></div>
  <div class="detail-row"><span class="detail-label">⚙️ CPU</span><span class="detail-value">${esc(v.cpuCores || 'N/A')} cores</span></div>
  <div class="detail-row"><span class="detail-label">🖥 Platform</span><span class="detail-value">${esc(v.platform || 'N/A')}</span></div>
  <div class="detail-row"><span class="detail-label">📐 Screen</span><span class="detail-value">${esc(v.screenResolution || 'N/A')}</span></div>
  <div class="detail-row"><span class="detail-label">🌐 IP</span><span class="detail-value">${esc(v.ip || 'N/A')}</span></div>
  <div class="detail-row"><span class="detail-label">🔋 Battery</span><span class="detail-value">${esc(v.battery || 'N/A')} ${esc(v.batteryStatus || '')}</span></div>
  <div class="detail-row"><span class="detail-label">🌐 Browser</span><span class="detail-value">${esc(v.browser || 'N/A')}</span></div>
  <div class="detail-row"><span class="detail-label">🗣 Language</span><span class="detail-value">${esc(v.language || 'N/A')}</span></div>
  <div class="detail-row"><span class="detail-label">🕐 First Visit</span><span class="detail-value">${fv}</span></div>
  <div class="detail-row"><span class="detail-label">🕑 Last Visit</span><span class="detail-value">${lv}</span></div>
  <div class="detail-row"><span class="detail-label">🔢 Visit Count</span><span class="detail-value">${v.visitCount || 1} times</span></div>
  <div class="detail-row"><span class="detail-label">🔑 Device Token</span><span class="detail-value" style="font-size:10px;">${esc(v.deviceToken || v.key || 'N/A')}</span></div>`;

  // Visit History
  let hist = [];
  if (v.visitHistory) {
    hist = Array.isArray(v.visitHistory) ? v.visitHistory.filter(Boolean) : Object.values(v.visitHistory).filter(Boolean);
    hist.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
  }

  h += `<div style="margin-top:24px;border-top:1px solid var(--border);padding-top:16px;">
    <div style="font-weight:700;font-size:15px;color:var(--orange);margin-bottom:12px;">📜 Visit History (${hist.length} entries)</div>`;

  if (!hist.length) {
    h += '<div style="color:var(--text-dim);text-align:center;padding:20px;">No history recorded yet</div>';
  } else {
    h += '<div class="history-timeline">';
    hist.forEach((vh, i) => {
      const vt = new Date(vh.timestamp).toLocaleString('en-US', { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
      h += `<div class="history-item">
        <div class="history-time">#${i + 1} • ${vt}</div>
        <div class="history-details">
          <span class="history-badge">🌐 ${esc(vh.ip || 'N/A')}</span>
          <span class="history-badge">🌐 ${esc(vh.browser || 'N/A')}</span>
          <span class="history-badge">📐 ${esc(vh.screenResolution || 'N/A')}</span>
          <span class="history-badge">🧠 ${esc(vh.ram || 'N/A')}</span>
          <span class="history-badge">🔋 ${esc(vh.batteryLevel || 'N/A')}</span>
        </div>
      </div>`;
    });
    h += '</div>';
  }
  h += '</div>';
  content.innerHTML = h;
}

// ============ ACTIVITY ============
async function loadActivity() {
  const c = document.getElementById('activityLogContainer');
  if (!c) return;
  c.innerHTML = '<div class="spinner"></div>';
  try {
    const snap = await window._get(window._ref(window._db, 'adminActivity'));
    if (!snap.exists()) {
      c.innerHTML = '<div style="color:var(--text-dim);padding:10px;text-align:center;">No activity yet</div>';
      return;
    }
    let a = [];
    snap.forEach(ch => { a.push(ch.val()); });
    a.sort((x, y) => (y.timestamp || 0) - (x.timestamp || 0));
    let h = '';
    a.slice(0, 10).forEach(x => {
      const t = new Date(x.timestamp).toLocaleString('en-US', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
      h += `<div class="activity-item">
        <div class="activity-info">
          <span class="visitor-name">${esc(x.action)}</span>
          ${x.detail ? `<span class="visitor-detail">• ${esc(x.detail)}</span>` : ''}
        </div>
        <div class="visitor-time">${t}</div>
      </div>`;
    });
    c.innerHTML = h || '<div style="color:var(--text-dim);padding:10px;text-align:center;">No activity yet</div>';
  } catch (e) {
    c.innerHTML = '<div style="color:red;padding:10px;">Error loading activity</div>';
  }
}

// ============ AUTH ============
async function doAdminLogin() {
  const u = document.getElementById('adminUser').value.trim();
  const p = document.getElementById('adminPass').value;
  if (!u || !p) { toast('Fill all fields', 'error'); return; }
  if (!firebaseReady) { toast('Connecting to server...', 'info'); return; }
  try {
    const snap = await window._get(window._ref(window._db, 'admins'));
    if (snap.exists()) {
      let found = false, fk = null;
      snap.forEach(c => {
        const a = c.val();
        if ((a.username === u || a.email === u) && a.password === p) { found = true; fk = c.key; }
      });
      if (found) {
        currentAdminKey = fk;
        sessionStorage.setItem('admin_logged_in', 'true');
        sessionStorage.setItem('admin_key', fk);
        document.getElementById('loginPage').style.display = 'none';
        document.getElementById('adminDashboard').style.display = 'block';
        toast('Welcome Admin! 🎉', 'success');
        loadAll();
        await logActivity('🔐 Admin Login');
      } else { toast('Invalid credentials!', 'error'); }
    } else { toast('No admin accounts found!', 'error'); }
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

function adminLogout() {
  sessionStorage.clear();
  currentAdminKey = null;
  document.getElementById('loginPage').style.display = 'flex';
  document.getElementById('adminDashboard').style.display = 'none';
  toast('Logged out successfully', 'success');
}

function loadAll() { loadApps(); loadUsers(); loadReports(); updateStats(); loadVisitors(); loadActivity(); }

async function updateStats() {
  if (!firebaseReady) return;
  try {
    const [u, a, r, v] = await Promise.all([
      window._get(window._ref(window._db, 'users')),
      window._get(window._ref(window._db, 'apps')),
      window._get(window._ref(window._db, 'reports')),
      window._get(window._ref(window._db, 'visitors'))
    ]);
    document.getElementById('totalUsers').textContent = u.exists() ? u.size : 0;
    document.getElementById('totalApps').textContent = a.exists() ? a.size : 0;
    document.getElementById('totalReports').textContent = r.exists() ? r.size : 0;
    document.getElementById('totalVisitors').textContent = v.exists() ? v.size : 0;
  } catch (e) {}
}

// ============ APPS ============
async function addApp() {
  const n = document.getElementById('aName').value.trim();
  const c = document.getElementById('aCategory').value;
  const ic = document.getElementById('aIcon').value.trim() || '📱';
  const img = document.getElementById('aImageUrl').value.trim();
  const lk = document.getElementById('aLink').value.trim();
  const d = document.getElementById('aDesc').value.trim();
  const s1 = document.getElementById('aScreen1').value.trim();
  const s2 = document.getElementById('aScreen2').value.trim();
  const s3 = document.getElementById('aScreen3').value.trim();
  const s4 = document.getElementById('aScreen4').value.trim();
  const s5 = document.getElementById('aScreen5').value.trim();
  if (!n || !d) { toast('Name and Description are required', 'error'); return; }
  const appData = { name: n, icon: ic, imageUrl: img || null, category: c, description: d, link: lk || null, downloads: 0 };
  if (s1) appData.screenshot1 = s1;
  if (s2) appData.screenshot2 = s2;
  if (s3) appData.screenshot3 = s3;
  if (s4) appData.screenshot4 = s4;
  if (s5) appData.screenshot5 = s5;
  
  // Add linked Remote Config if available
  const remoteSnap = await window._get(window._ref(window._db, 'settings/firebaseConfig/remoteConfig'));
  if (remoteSnap.exists()) {
    appData.remoteConfig = remoteSnap.val();
  }
  
  try {
    await window._set(window._push(window._ref(window._db, 'apps')), appData);
    toast('✅ App added successfully!', 'success');
    await logActivity('➕ Added App', n);
    ['aName','aImageUrl','aDesc','aLink','aScreen1','aScreen2','aScreen3','aScreen4','aScreen5'].forEach(id => { const el = document.getElementById(id); if (el) el.value = ''; });
    document.getElementById('aIcon').value = '📱';
    loadApps(); updateStats();
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

function loadApps() {
  if (!firebaseReady) { setTimeout(loadApps, 600); return; }
  const l = document.getElementById('adminAppsList');
  if (!l) return;
  l.innerHTML = '<div class="spinner"></div>';
  window._get(window._ref(window._db, 'apps')).then(s => {
    if (!s.exists()) { l.innerHTML = '<div style="color:var(--text-dim);padding:20px;text-align:center;">No apps added yet</div>'; return; }
    let h = '';
    s.forEach(c => {
      const a = c.val();
      let rating = 0;
      if (a.reviews) {
        const vals = Object.values(a.reviews).map(r => r.rating || 0).filter(r => r > 0);
        if (vals.length > 0) rating = vals.reduce((t, r) => t + r, 0) / vals.length;
      }
      
      // Check if app has its own Remote Config
      const hasAppRemoteConfig = a.remoteConfig && Object.keys(a.remoteConfig).length > 0;
      
      h += `<div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:12px;display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <div>${a.imageUrl ? `<img src="${esc(a.imageUrl)}" style="width:40px;height:40px;border-radius:10px;object-fit:cover;" onerror="this.style.display='none'">` : ''}<span style="font-size:32px;">${esc(a.icon || '📱')}</span></div>
        <div style="flex:1;">
          <div style="font-weight:600;">${esc(a.name)}</div>
          <div style="font-size:11px;color:var(--text-dim);">
            ${esc(a.category)} • ⭐${rating.toFixed(1)} • ${formatNum(a.downloads || 0)} DL
            ${hasAppRemoteConfig ? '<span style="color:#4ade80;margin-left:6px;">• 🔧 Config</span>' : ''}
          </div>
        </div>
        <div style="display:flex;gap:6px;">
          <button class="btn btn-outline btn-sm" id="editAppBtn_${c.key}">✏️ Edit</button>
          <button class="btn btn-danger btn-sm" id="delAppBtn_${c.key}">🗑 Delete</button>
        </div>
      </div>`;
    });
    l.innerHTML = h;
  }).catch(e => { l.innerHTML = '<div style="color:red;padding:10px;">Error loading apps</div>'; });
}

async function deleteApp(k) {
  try {
    const snap = await window._get(window._ref(window._db, 'apps/' + k));
    const appName = snap.val()?.name || 'Unknown';
    await window._remove(window._ref(window._db, 'apps/' + k));
    toast('✅ App deleted!', 'success');
    await logActivity('🗑 Deleted App', appName);
    loadApps(); updateStats();
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

async function openEditApp(k) {
  const s = await window._get(window._ref(window._db, 'apps/' + k));
  const a = s.val();
  if (!a) { toast('App not found', 'error'); return; }
  
  // Load Remote Config for this app
  const appRemoteConfig = a.remoteConfig || {};
  const globalRemoteSnap = await window._get(window._ref(window._db, 'settings/firebaseConfig/remoteConfig'));
  const globalRemoteConfig = globalRemoteSnap.exists() ? globalRemoteSnap.val() : {};
  
  // Merge global config with app-specific (app-specific takes precedence)
  const mergedConfig = { ...globalRemoteConfig, ...appRemoteConfig };
  
  let remoteConfigHtml = '';
  if (Object.keys(mergedConfig).length > 0) {
    remoteConfigHtml = `
      <div class="app-remote-config-section">
        <div class="app-remote-config-title">🔧 Remote Config (Auto-loaded)</div>
        <div style="font-size:12px;color:var(--text-dim);margin-bottom:12px;">
          These parameters are automatically loaded from your saved Firebase Config.
          ${Object.keys(appRemoteConfig).length > 0 ? `<br><span style="color:var(--orange);">${Object.keys(appRemoteConfig).length} app-specific override(s) detected.</span>` : ''}
        </div>
        <div style="display:flex;flex-direction:column;gap:8px;">
    `;
    
    Object.keys(mergedConfig).sort().forEach(key => {
      const param = mergedConfig[key];
      const type = param.type || 'string';
      const isAppSpecific = appRemoteConfig.hasOwnProperty(key);
      let valueDisplay = param.value;
      
      if (type === 'boolean') {
        valueDisplay = param.value === true || param.value === 'true' ? '✅ true' : '❌ false';
      } else if (type === 'json') {
        try {
          valueDisplay = JSON.stringify(typeof param.value === 'string' ? JSON.parse(param.value) : param.value, null, 2);
        } catch {
          valueDisplay = param.value;
        }
      }
      
      remoteConfigHtml += `
        <div style="background:var(--card);border:1px solid ${isAppSpecific ? 'var(--orange)' : 'rgba(255,255,255,0.05)'};border-radius:8px;padding:10px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;flex-wrap:wrap;gap:6px;">
            <span style="font-weight:600;color:var(--orange);font-family:monospace;font-size:13px;">${esc(key)}</span>
            <div style="display:flex;gap:6px;align-items:center;">
              <span class="param-type-badge" style="${isAppSpecific ? 'background:rgba(255,140,66,0.3);' : ''}">${type}</span>
              ${isAppSpecific ? '<span style="font-size:10px;color:var(--orange);">App Override</span>' : '<span style="font-size:10px;color:var(--text-dim);">Global</span>'}
            </div>
          </div>
          <div class="param-value-display" style="font-size:12px;">${type === 'json' ? '<pre style="margin:0;white-space:pre-wrap;">' + esc(valueDisplay) + '</pre>' : esc(valueDisplay)}</div>
        </div>
      `;
    });
    
    remoteConfigHtml += '</div></div>';
  }
  
  document.getElementById('editAppContent').innerHTML = `
    <input type="hidden" id="editAppKey" value="${k}">
    <input type="hidden" id="editAppHasRemoteConfig" value="${Object.keys(appRemoteConfig).length > 0}">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="input-group" style="margin-bottom:10px;"><label>Name</label><input id="editName" value="${esc(a.name)}" placeholder="App name"></div>
      <div class="input-group" style="margin-bottom:10px;"><label>Category</label>
        <select id="editCategory">
          ${['Social', 'Games', 'Tools', 'Entertainment', 'Other'].map(c => `<option ${a.category === c ? 'selected' : ''}>${c}</option>`).join('')}
        </select>
      </div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="input-group" style="margin-bottom:10px;"><label>Icon</label><input id="editIcon" value="${esc(a.icon || '📱')}" placeholder="📱"></div>
      <div class="input-group" style="margin-bottom:10px;"><label>Image URL</label><input id="editImageUrl" value="${esc(a.imageUrl || '')}" placeholder="https://..."></div>
    </div>
    <div class="input-group" style="margin-bottom:10px;"><label>Link</label><input id="editLink" value="${esc(a.link || '')}" placeholder="https://..."></div>
    <div class="input-group" style="margin-bottom:10px;"><label>Description</label><textarea id="editDesc" rows="2" placeholder="App description...">${esc(a.description || '')}</textarea></div>
    <div style="font-size:12px;color:var(--text-dim);margin-bottom:8px;font-weight:600;">📸 App Screenshots</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="input-group" style="margin-bottom:8px;"><label>Screenshot 1</label><input id="editScreen1" value="${esc(a.screenshot1 || '')}" placeholder="https://..."></div>
      <div class="input-group" style="margin-bottom:8px;"><label>Screenshot 2</label><input id="editScreen2" value="${esc(a.screenshot2 || '')}" placeholder="https://..."></div>
      <div class="input-group" style="margin-bottom:8px;"><label>Screenshot 3</label><input id="editScreen3" value="${esc(a.screenshot3 || '')}" placeholder="https://..."></div>
      <div class="input-group" style="margin-bottom:8px;"><label>Screenshot 4</label><input id="editScreen4" value="${esc(a.screenshot4 || '')}" placeholder="https://..."></div>
      <div class="input-group" style="margin-bottom:8px;"><label>Screenshot 5</label><input id="editScreen5" value="${esc(a.screenshot5 || '')}" placeholder="https://..."></div>
    </div>
    
    ${remoteConfigHtml}
    
    <button class="btn btn-primary btn-sm" style="width:100%;margin-top:16px;" id="btnSaveEdit">💾 Save Changes</button>`;
  document.getElementById('editAppOverlay').classList.remove('hidden');
}

async function saveEditApp() {
  const k = document.getElementById('editAppKey')?.value;
  if (!k) return;
  const n = document.getElementById('editName')?.value.trim();
  const c = document.getElementById('editCategory')?.value;
  const ic = document.getElementById('editIcon')?.value.trim() || '📱';
  const img = document.getElementById('editImageUrl')?.value.trim();
  const lk = document.getElementById('editLink')?.value.trim();
  const d = document.getElementById('editDesc')?.value.trim();
  const s1 = document.getElementById('editScreen1')?.value.trim();
  const s2 = document.getElementById('editScreen2')?.value.trim();
  const s3 = document.getElementById('editScreen3')?.value.trim();
  const s4 = document.getElementById('editScreen4')?.value.trim();
  const s5 = document.getElementById('editScreen5')?.value.trim();
  const hasAppRemoteConfig = document.getElementById('editAppHasRemoteConfig')?.value === 'true';
  
  if (!n || !d) { toast('Name and Description are required', 'error'); return; }
  
  const updates = { 
    name: n, category: c, icon: ic, imageUrl: img || null, link: lk || null, description: d,
    screenshot1: s1 || null, screenshot2: s2 || null, screenshot3: s3 || null, screenshot4: s4 || null, screenshot5: s5 || null 
  };
  
  // If app had Remote Config, preserve it; otherwise don't touch it
  if (hasAppRemoteConfig) {
    const currentSnap = await window._get(window._ref(window._db, `apps/${k}/remoteConfig`));
    if (currentSnap.exists()) {
      updates.remoteConfig = currentSnap.val();
    }
  }
  
  try {
    await window._update(window._ref(window._db, 'apps/' + k), updates);
    toast('✅ App updated!', 'success');
    await logActivity('✏️ Edited App', n);
    closeModal('editAppOverlay');
    loadApps();
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

// ============ USERS ============
function loadUsers() {
  if (!firebaseReady) { setTimeout(loadUsers, 600); return; }
  const l = document.getElementById('adminUsersList');
  if (!l) return;
  l.innerHTML = '<div class="spinner"></div>';
  window._get(window._ref(window._db, 'users')).then(s => {
    if (!s.exists()) { l.innerHTML = '<div style="color:var(--text-dim);padding:20px;text-align:center;">No users registered yet</div>'; return; }
    let h = '';
    s.forEach(c => {
      const u = c.val();
      h += `<div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:12px;display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <div style="flex:1;">
          <div style="font-weight:600;">${esc(u.name)}</div>
          <div style="font-size:11px;color:var(--text-dim);">${esc(u.email || u.number)} • ${esc(u.gender || 'N/A')}</div>
        </div>
        <button class="btn btn-danger btn-sm" id="delUserBtn_${c.key}">🗑 Delete</button>
      </div>`;
    });
    l.innerHTML = h;
  }).catch(e => { l.innerHTML = '<div style="color:red;padding:10px;">Error loading users</div>'; });
}

async function deleteUser(k) {
  try {
    const snap = await window._get(window._ref(window._db, 'users/' + k));
    const userName = snap.val()?.name || 'Unknown';
    await window._remove(window._ref(window._db, 'users/' + k));
    toast('✅ User deleted!', 'success');
    await logActivity('🗑 Deleted User', userName);
    loadUsers(); updateStats();
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

// ============ REPORTS ============
function loadReports() {
  if (!firebaseReady) { setTimeout(loadReports, 600); return; }
  const l = document.getElementById('adminReportsList');
  if (!l) return;
  l.innerHTML = '<div class="spinner"></div>';
  window._get(window._ref(window._db, 'reports')).then(s => {
    if (!s.exists()) { l.innerHTML = '<div style="color:var(--text-dim);padding:20px;text-align:center;">No reports submitted yet</div>'; return; }
    let h = '';
    const now = Date.now();
    const THIRTY_DAYS = 30 * 24 * 60 * 60 * 1000;
    s.forEach(c => {
      const r = c.val();
      const t = r.timestamp ? new Date(r.timestamp).toLocaleString() : 'N/A';
      const isReview = r.type === 'auto_review' || r.source === 'review_section';
      const isReportUs = r.type === 'report_us' || r.source === 'report_us';
      const age = now - (r.timestamp || 0);
      const locked = isReview && age < THIRTY_DAYS;
      const daysLeft = Math.ceil((THIRTY_DAYS - age) / (24*60*60*1000));
      const sourceBadge = isReview
        ? '<span style="font-size:10px;background:var(--orange-dim);color:var(--orange);border:1px solid var(--border);padding:2px 7px;border-radius:99px;margin-left:6px;">Collected by review section</span>'
        : isReportUs
        ? '<span style="font-size:10px;background:rgba(255,100,100,0.12);color:#f87171;border:1px solid rgba(255,100,100,0.3);padding:2px 7px;border-radius:99px;margin-left:6px;">Collected by Report us</span>'
        : '';
      const deleteBtn = locked
        ? `<span style="font-size:10px;color:var(--text-dim);background:var(--card2);padding:4px 8px;border-radius:6px;">🔒 ${daysLeft}d left</span>`
        : `<button class="btn btn-danger btn-sm" id="delReportBtn_${c.key}">🗑</button>`;
      h += `<div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:12px;margin-bottom:8px;">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;">
          <span style="font-weight:600;display:flex;align-items:center;flex-wrap:wrap;">${esc(r.subject || 'No Subject')}${sourceBadge}</span>
          <div style="display:flex;gap:6px;align-items:center;">
            <span style="font-size:10px;color:var(--text-dim);">${t}</span>
            ${deleteBtn}
          </div>
        </div>
        <div style="font-size:11px;color:var(--text-dim);margin-top:4px;">From: ${esc(r.username || 'Anonymous')} | ${esc(r.email || '')}</div>
        <div style="font-size:12px;color:var(--text-dim);margin-top:6px;">${esc(r.message || '')}</div>
      </div>`;
    });
    l.innerHTML = h;
  }).catch(e => { l.innerHTML = '<div style="color:red;padding:10px;">Error loading reports</div>'; });
}

async function deleteReport(k) {
  try {
    await window._remove(window._ref(window._db, 'reports/' + k));
    toast('✅ Report deleted!', 'success');
    loadReports(); updateStats();
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

// ============ SETTINGS ============
async function updateAdmin() {
  const cp = document.getElementById('currentAdminPass').value.trim();
  const nu = document.getElementById('newAdminUser').value.trim();
  const np = document.getElementById('newAdminPass').value.trim();
  if (!cp) { toast('Enter current password', 'error'); return; }
  try {
    const s = await window._get(window._ref(window._db, `admins/${currentAdminKey}`));
    if (s.val()?.password === cp) {
      const u = {};
      if (nu) u.username = nu;
      if (np) u.password = np;
      if (Object.keys(u).length) {
        await window._update(window._ref(window._db, `admins/${currentAdminKey}`), u);
        toast('✅ Credentials updated!', 'success');
        await logActivity('🔐 Updated Admin Credentials');
        document.getElementById('currentAdminPass').value = '';
        document.getElementById('newAdminUser').value = '';
        document.getElementById('newAdminPass').value = '';
      } else { toast('Nothing to update', 'info'); }
    } else { toast('Wrong current password', 'error'); }
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

async function saveSettings() {
  const n = document.getElementById('websiteNameInput').value.trim() || 'SamWeb Store';
  const logo = document.getElementById('logoUrlInput')?.value.trim();
  localStorage.setItem('website_name', n);
  try {
    if (logo) {
      await window._set(window._ref(window._db, 'settings/logoUrl'), logo);
      const prev = document.getElementById('logoPreview');
      const prevWrap = document.getElementById('logoPreviewWrap');
      if (prev && logo) { prev.src = logo; prevWrap.style.display = 'block'; }
    } else {
      await window._remove(window._ref(window._db, 'settings/logoUrl'));
      const prevWrap = document.getElementById('logoPreviewWrap');
      if (prevWrap) prevWrap.style.display = 'none';
    }
  } catch(e) {}
  toast('✅ Settings saved!', 'success');
  logActivity('⚙️ Updated Website Settings', n);
}

// ============ APK LINK ============
async function loadApkLinkDisplay() {
  try {
    const [apkSnap, logoSnap] = await Promise.all([
      window._get(window._ref(window._db, 'settings/apkDownloadLink')),
      window._get(window._ref(window._db, 'settings/logoUrl'))
    ]);
    const input = document.getElementById('apkLinkInput');
    const display = document.getElementById('currentApkLinkDisplay');
    const text = document.getElementById('currentApkLinkText');
    if (apkSnap.exists() && apkSnap.val()) {
      if (input) input.value = apkSnap.val();
      if (display) display.style.display = 'block';
      if (text) text.textContent = apkSnap.val();
    } else {
      if (display) display.style.display = 'none';
    }
    const logoInput = document.getElementById('logoUrlInput');
    const prevWrap = document.getElementById('logoPreviewWrap');
    const prevImg = document.getElementById('logoPreview');
    if (logoSnap.exists() && logoSnap.val()) {
      if (logoInput) logoInput.value = logoSnap.val();
      if (prevImg) prevImg.src = logoSnap.val();
      if (prevWrap) prevWrap.style.display = 'block';
    }
  } catch (e) {}
}

async function saveApkLink() {
  const link = document.getElementById('apkLinkInput')?.value.trim();
  if (!link) { toast('Please enter a link', 'error'); return; }
  if (!link.startsWith('http')) { toast('Link must start with http/https', 'error'); return; }
  try {
    await window._set(window._ref(window._db, 'settings/apkDownloadLink'), link);
    toast('✅ APK Link saved! Users can now download APK.', 'success');
    await logActivity('📦 Set APK Download Link', link.substring(0, 40) + '...');
    loadApkLinkDisplay();
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

async function removeApkLink() {
  showConfirm('Remove APK Link?', 'The Download APK button will disappear from user website.', async () => {
    try {
      await window._remove(window._ref(window._db, 'settings/apkDownloadLink'));
      toast('✅ APK link removed!', 'success');
      await logActivity('📦 Removed APK Download Link');
      document.getElementById('apkLinkInput').value = '';
      loadApkLinkDisplay();
    } catch (e) { toast('Error: ' + e.message, 'error'); }
  });
}

// ============ INIT ============
window.addEventListener('firebaseReady', async () => {
  firebaseReady = true;
  console.log('✅ Firebase connected');
  const sk = sessionStorage.getItem('admin_key');
  if (sessionStorage.getItem('admin_logged_in') === 'true' && sk) {
    currentAdminKey = sk;
    document.getElementById('loginPage').style.display = 'none';
    document.getElementById('adminDashboard').style.display = 'block';
    loadAll();
  } else {
    document.getElementById('loginPage').style.display = 'flex';
  }
});
</script>
</body>
</html>
