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
    .badge.config { background: rgba(34,197,94,0.2); color: #4ade80; }
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
    
    /* App Firebase Config Styles */
    .app-config-section { background: linear-gradient(135deg, rgba(34,197,94,0.08), rgba(34,197,94,0.03)); border: 1px solid rgba(34,197,94,0.25); border-radius: 12px; padding: 16px; margin-bottom: 16px; }
    .app-config-section.not-configured { background: linear-gradient(135deg, rgba(255,140,66,0.08), rgba(255,140,66,0.03)); border-color: var(--border); }
    .app-config-header { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 12px; }
    .app-config-title { display: flex; align-items: center; gap: 10px; font-weight: 700; font-size: 15px; color: var(--orange); }
    .app-config-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; margin-bottom: 12px; }
    .app-config-item { background: var(--card2); border-radius: 8px; padding: 10px; }
    .app-config-label { font-size: 10px; color: var(--text-dim); text-transform: uppercase; margin-bottom: 4px; }
    .app-config-value { font-weight: 600; font-size: 12px; word-break: break-all; }
    .upload-zone { border: 2px dashed var(--border); border-radius: 12px; padding: 24px; text-align: center; cursor: pointer; transition: all .3s; background: var(--card2); }
    .upload-zone:hover { border-color: var(--orange); background: var(--orange-dim); }
    .upload-zone.has-file { border-color: #4ade80; background: rgba(34,197,94,0.1); }
    .upload-zone-icon { font-size: 32px; margin-bottom: 8px; }
    .upload-zone-text { font-size: 13px; color: var(--text-dim); }
    .upload-zone-text strong { color: var(--orange); }
    .file-input { display: none; }
    
    /* Remote Config Styles */
    .remote-config-section { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 16px; margin-top: 16px; }
    .remote-config-header { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 14px; }
    .remote-config-title { font-weight: 700; font-size: 14px; color: var(--orange); }
    .param-list { display: flex; flex-direction: column; gap: 10px; max-height: 350px; overflow-y: auto; }
    .param-item { background: var(--card2); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 12px; display: flex; flex-direction: column; gap: 8px; transition: all .2s; }
    .param-item:hover { border-color: var(--orange); }
    .param-item-header { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; }
    .param-key { font-weight: 700; font-size: 13px; color: var(--orange); font-family: monospace; }
    .param-type-badge { font-size: 10px; padding: 2px 8px; border-radius: 10px; background: var(--orange-dim); color: var(--orange); font-weight: 600; text-transform: uppercase; }
    .param-value-display { background: var(--dark); border-radius: 6px; padding: 8px 12px; font-family: monospace; font-size: 12px; word-break: break-all; max-height: 80px; overflow-y: auto; }
    .param-actions { display: flex; gap: 6px; flex-wrap: wrap; }
    
    /* Empty state */
    .empty-state { text-align: center; padding: 30px 20px; color: var(--text-dim); }
    .empty-state-icon { font-size: 40px; margin-bottom: 10px; opacity: 0.5; }
    .empty-state-text { font-size: 13px; }
    
    /* Date badges */
    .date-badge { display: inline-flex; align-items: center; gap: 4px; font-size: 10px; color: var(--text-dim); background: var(--card2); padding: 3px 8px; border-radius: 6px; }
    
    /* Type selector */
    .type-selector { display: flex; gap: 8px; flex-wrap: wrap; }
    .type-option { padding: 6px 12px; border-radius: 6px; font-size: 11px; cursor: pointer; border: 1px solid var(--border); background: var(--card2); color: var(--text-dim); transition: all .2s; }
    .type-option:hover { border-color: var(--orange); }
    .type-option.selected { background: var(--orange); color: #000; border-color: var(--orange); font-weight: 600; }
    
    /* Add/Edit Parameter Modal */
    .param-form { display: flex; flex-direction: column; gap: 14px; }
    .param-form .input-group { margin-bottom: 0; }
    
    /* Tabs in modal */
    .modal-tabs { display: flex; gap: 6px; margin-bottom: 16px; background: var(--card2); padding: 4px; border-radius: 8px; }
    .modal-tab { padding: 8px 14px; background: transparent; border: none; color: var(--text-dim); border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: 500; transition: all .2s; font-family: 'Exo 2', sans-serif; flex: 1; text-align: center; }
    .modal-tab.active { background: var(--orange); color: #000; }
    .modal-tab-content { display: none; }
    .modal-tab-content.active { display: block; }
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
        
        <!-- Firebase Config Upload for New App -->
        <div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--border);">
          <div style="font-weight:700;font-size:14px;color:var(--orange);margin-bottom:12px;">🔥 Firebase Configuration (Optional)</div>
          <div class="upload-zone" id="newAppUploadZone">
            <div class="upload-zone-icon">📄</div>
            <div class="upload-zone-text">
              <strong>Upload google-services.json</strong><br>
              <span style="font-size:11px;">or skip for now</span>
            </div>
          </div>
          <input type="file" class="file-input" id="newAppGoogleJsonInput" accept=".json">
          <div id="newAppJsonPreview" class="hidden" style="margin-top:12px;"></div>
        </div>
        
        <button class="btn btn-primary btn-sm" id="btnAddApp" style="margin-top:16px;">➕ Add App</button>
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
  <div class="modal" style="max-width:800px;">
    <div class="modal-header">
      <span class="modal-title">✏️ Edit App</span>
      <button class="modal-close-btn" data-close="editAppOverlay">✕</button>
    </div>
    
    <!-- Tabs for App Edit -->
    <div class="modal-tabs">
      <button class="modal-tab active" data-modal-tab="appInfo">📱 App Info</button>
      <button class="modal-tab" data-modal-tab="firebaseConfig">🔥 Firebase Config</button>
      <button class="modal-tab" data-modal-tab="remoteParams">🔧 Parameters</button>
    </div>
    
    <!-- App Info Tab -->
    <div class="modal-tab-content active" id="tab_appInfo">
      <div id="editAppContent"></div>
    </div>
    
    <!-- Firebase Config Tab -->
    <div class="modal-tab-content" id="tab_firebaseConfig">
      <div id="editAppFirebaseContent">
        <div class="spinner"></div>
      </div>
    </div>
    
    <!-- Remote Params Tab -->
    <div class="modal-tab-content" id="tab_remoteParams">
      <div id="editAppRemoteParamsContent">
        <div class="spinner"></div>
      </div>
    </div>
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

<!-- ADD/EDIT PARAM MODAL -->
<div class="overlay hidden" id="paramModalOverlay">
  <div class="modal" style="max-width:500px;">
    <div class="modal-header">
      <span class="modal-title" id="paramModalTitle">➕ Add Parameter</span>
      <button class="modal-close-btn" data-close="paramModalOverlay">✕</button>
    </div>
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
        <button class="btn btn-primary" id="btnSaveParam" style="flex:1;">💾 Save</button>
        <button class="btn btn-outline" data-close="paramModalOverlay">Cancel</button>
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

// Current editing app
let currentEditingAppKey = null;
let currentEditingAppData = null;

// New app temp data
let newAppTempJson = null;
let newAppTempConfig = null;

// Param modal state
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

// ============ FIREBASE CONFIG EXTRACTION ============
function extractFirebaseConfig(json) {
  if (!json) return null;
  
  // Standard google-services.json structure
  if (json.project_info) {
    return {
      project_id: json.project_info.project_id,
      project_number: json.project_info.project_number,
      package_name: json.client?.[0]?.client_info?.android_client_info?.package_name || '',
      storage_bucket: json.project_info.storage_bucket,
      api_key: json.client?.[0]?.api_key?.[0]?.current_key || '',
      mobile_sdk_app_id: json.client?.[0]?.client_info?.mobilesdk_app_id || '',
      googleServicesJson: JSON.stringify(json)
    };
  }
  
  // Alternative structure
  if (json.projectId) {
    return {
      project_id: json.projectId,
      project_number: json.projectNumber || '',
      package_name: json.package_name || '',
      storage_bucket: json.storageBucket || '',
      api_key: json.apiKey || '',
      mobile_sdk_app_id: json.mobileSdkAppId || '',
      googleServicesJson: JSON.stringify(json)
    };
  }
  
  return null;
}

// ============ FIREBASE CONFIG UI (Per App) ============

function renderFirebaseConfigUI(appKey, appData, containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  
  const firebaseConfig = appData?.firebaseConfig;
  
  if (firebaseConfig?.googleServicesJson) {
    // Has config
    const uploadedAt = firebaseConfig.uploadedAt ? formatDate(firebaseConfig.uploadedAt) : 'N/A';
    const lastModified = firebaseConfig.lastModified ? formatDate(firebaseConfig.lastModified) : uploadedAt;
    
    container.innerHTML = `
      <div class="app-config-section">
        <div class="app-config-header">
          <div class="app-config-title">
            <span>🔥</span>
            <span>Firebase Connected</span>
            <span class="badge config">✔ Configured</span>
          </div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;">
            <button class="btn btn-warning btn-sm" onclick="replaceAppGoogleJson('${appKey}')">🔄 Replace</button>
            <button class="btn btn-outline btn-sm" onclick="viewAppGoogleJson('${appKey}')">👁 View JSON</button>
            <button class="btn btn-danger btn-sm" onclick="removeAppGoogleJson('${appKey}')">🗑 Remove</button>
          </div>
        </div>
        
        <div class="app-config-grid">
          <div class="app-config-item">
            <div class="app-config-label">Project ID</div>
            <div class="app-config-value">${esc(firebaseConfig.project_id || 'N/A')}</div>
          </div>
          <div class="app-config-item">
            <div class="app-config-label">Package Name</div>
            <div class="app-config-value">${esc(firebaseConfig.package_name || 'N/A')}</div>
          </div>
          <div class="app-config-item">
            <div class="app-config-label">Storage Bucket</div>
            <div class="app-config-value">${esc(firebaseConfig.storage_bucket || 'N/A')}</div>
          </div>
          <div class="app-config-item">
            <div class="app-config-label">API Key</div>
            <div class="app-config-value">${esc(firebaseConfig.api_key ? firebaseConfig.api_key.substring(0, 15) + '...' : 'N/A')}</div>
          </div>
        </div>
        
        <div style="display:flex;gap:12px;flex-wrap:wrap;">
          <div class="date-badge">📅 Uploaded: ${uploadedAt}</div>
          <div class="date-badge">✏️ Modified: ${lastModified}</div>
        </div>
        
        <div id="appJsonPreview_${appKey}" class="hidden" style="margin-top:12px;">
          <div style="background:var(--dark);border-radius:8px;padding:12px;font-family:monospace;font-size:11px;max-height:200px;overflow:auto;white-space:pre-wrap;word-break:break-all;">${esc(firebaseConfig.googleServicesJson)}</div>
        </div>
      </div>
    `;
  } else {
    // No config
    container.innerHTML = `
      <div class="app-config-section not-configured">
        <div class="app-config-header">
          <div class="app-config-title">
            <span>📄</span>
            <span>No Firebase Config</span>
          </div>
        </div>
        <div class="upload-zone" id="uploadZone_${appKey}">
          <div class="upload-zone-icon">📤</div>
          <div class="upload-zone-text">
            <strong>Click to upload</strong> google-services.json<br>
            <span style="font-size:11px;">or drag and drop JSON file</span>
          </div>
        </div>
        <input type="file" class="file-input" id="googleJsonInput_${appKey}" accept=".json">
        <div id="uploadPreview_${appKey}" class="hidden" style="margin-top:12px;"></div>
      </div>
    `;
    
    setTimeout(() => {
      const uploadZone = document.getElementById(`uploadZone_${appKey}`);
      const fileInput = document.getElementById(`googleJsonInput_${appKey}`);
      
      if (uploadZone) {
        uploadZone.addEventListener('click', () => fileInput?.click());
      }
      if (fileInput) {
        fileInput.addEventListener('change', (e) => handleAppGoogleJsonUpload(appKey, e));
      }
    }, 100);
  }
}

// Handle Google JSON Upload for App
async function handleAppGoogleJsonUpload(appKey, event) {
  const file = event.target.files?.[0];
  if (!file) return;
  
  try {
    const text = await file.text();
    const jsonData = JSON.parse(text);
    const configData = extractFirebaseConfig(jsonData);
    
    if (!configData) {
      toast('Invalid google-services.json structure', 'error');
      return;
    }
    
    // Update app with Firebase config
    await window._update(window._ref(window._db, `apps/${appKey}`), {
      firebaseConfig: {
        ...configData,
        uploadedAt: Date.now(),
        lastModified: Date.now()
      }
    });
    
    toast('✅ google-services.json uploaded!', 'success');
    await logActivity('📄 Uploaded google-services.json', configData.project_id);
    
    // Refresh the UI
    const snap = await window._get(window._ref(window._db, `apps/${appKey}`));
    if (snap.exists()) {
      renderFirebaseConfigUI(appKey, snap.val(), 'editAppFirebaseContent');
    }
    
  } catch (e) {
    toast('Error: ' + e.message, 'error');
  }
}

// Replace Google JSON
async function replaceAppGoogleJson(appKey) {
  const input = document.createElement('input');
  input.type = 'file';
  input.accept = '.json';
  
  input.addEventListener('change', async (e) => {
    const file = e.target.files?.[0];
    if (!file) return;
    
    try {
      const text = await file.text();
      const jsonData = JSON.parse(text);
      const configData = extractFirebaseConfig(jsonData);
      
      if (!configData) {
        toast('Invalid google-services.json structure', 'error');
        return;
      }
      
      // Preserve existing Remote Config
      const currentSnap = await window._get(window._ref(window._db, `apps/${appKey}`));
      const currentData = currentSnap.val() || {};
      const existingRemoteConfig = currentData.remoteConfig || {};
      
      await window._update(window._ref(window._db, `apps/${appKey}`), {
        firebaseConfig: {
          ...configData,
          uploadedAt: currentData.firebaseConfig?.uploadedAt || Date.now(),
          lastModified: Date.now(),
          remoteConfig: existingRemoteConfig
        }
      });
      
      toast('✅ google-services.json replaced!', 'success');
      await logActivity('🔄 Replaced google-services.json', configData.project_id);
      
      const snap = await window._get(window._ref(window._db, `apps/${appKey}`));
      if (snap.exists()) {
        renderFirebaseConfigUI(appKey, snap.val(), 'editAppFirebaseContent');
      }
      
    } catch (e) {
      toast('Error: ' + e.message, 'error');
    }
  });
  
  input.click();
}

// View JSON
function viewAppGoogleJson(appKey) {
  const preview = document.getElementById(`appJsonPreview_${appKey}`);
  if (preview) {
    preview.classList.toggle('hidden');
  }
}

// Remove JSON
async function removeAppGoogleJson(appKey) {
  showConfirm('🗑 Remove Firebase Config?', 'This will delete the google-services.json and all parameters for this app.', async () => {
    try {
      await window._update(window._ref(window._db, `apps/${appKey}`), {
        firebaseConfig: null,
        remoteConfig: null
      });
      
      toast('✅ Firebase config removed!', 'success');
      await logActivity('🗑 Removed Firebase Config', appKey);
      
      const snap = await window._get(window._ref(window._db, `apps/${appKey}`));
      if (snap.exists()) {
        renderFirebaseConfigUI(appKey, snap.val(), 'editAppFirebaseContent');
        renderRemoteParamsUI(appKey, null, 'editAppRemoteParamsContent');
      }
    } catch (e) {
      toast('Error: ' + e.message, 'error');
    }
  });
}

// ============ REMOTE CONFIG UI (Per App) ============

function renderRemoteParamsUI(appKey, appData, containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  
  const remoteConfig = appData?.firebaseConfig?.remoteConfig || appData?.remoteConfig || {};
  const params = Object.keys(remoteConfig);
  
  if (params.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <div class="empty-state-icon">🔧</div>
        <div class="empty-state-text">No parameters yet.<br>Click "Add Parameter" to create one.</div>
      </div>
      <button class="btn btn-primary btn-sm" onclick="showAddParamModal('${appKey}')" style="margin-top:12px;">➕ Add Parameter</button>
    `;
    return;
  }
  
  let html = '';
  params.sort().forEach(key => {
    const param = remoteConfig[key];
    const type = param.type || 'string';
    let valueDisplay = param.value;
    
    if (type === 'boolean') {
      valueDisplay = param.value === true || param.value === 'true' ? '✅ true' : '❌ false';
    } else if (type === 'json') {
      try {
        valueDisplay = JSON.stringify(typeof param.value === 'string' ? JSON.parse(param.value) : param.value, null, 2);
      } catch {}
    }
    
    html += `
      <div class="param-item">
        <div class="param-item-header">
          <span class="param-key">${esc(key)}</span>
          <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
            <span class="param-type-badge">${type}</span>
            <div class="param-actions">
              <button class="btn btn-outline btn-xs" onclick="editParam('${appKey}', '${esc(key)}')">✏️</button>
              <button class="btn btn-danger btn-xs" onclick="deleteParam('${appKey}', '${esc(key)}')">🗑</button>
            </div>
          </div>
        </div>
        <div class="param-value-display">${type === 'json' ? '<pre style="margin:0;white-space:pre-wrap;">' + esc(valueDisplay) + '</pre>' : esc(valueDisplay)}</div>
      </div>
    `;
  });
  
  container.innerHTML = `
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:10px;">
      <div style="font-weight:600;color:var(--orange);">🔧 Parameters (${params.length})</div>
      <button class="btn btn-primary btn-sm" onclick="showAddParamModal('${appKey}')">➕ Add</button>
    </div>
    <div class="param-list">${html}</div>
  `;
}

// ============ PARAM CRUD ============

function showAddParamModal(appKey) {
  currentEditingAppKey = appKey;
  editingParamKey = null;
  selectedParamType = 'string';
  
  document.getElementById('paramModalTitle').textContent = '➕ Add Parameter';
  document.getElementById('paramKeyInput').value = '';
  document.getElementById('paramKeyInput').readOnly = false;
  document.getElementById('paramKeyInput').style.opacity = '1';
  document.getElementById('paramValueInput').value = '';
  
  document.querySelectorAll('.type-option').forEach(opt => {
    opt.classList.toggle('selected', opt.dataset.type === 'string');
  });
  
  document.getElementById('paramModalOverlay').classList.remove('hidden');
}

function editParam(appKey, key) {
  currentEditingAppKey = appKey;
  editingParamKey = key;
  
  window._get(window._ref(window._db, `apps/${appKey}/firebaseConfig/remoteConfig/${key}`)).then(snap => {
    if (!snap.exists()) {
      // Try alternative path
      return window._get(window._ref(window._db, `apps/${appKey}/remoteConfig/${key}`));
    }
    return snap;
  }).then(snap => {
    if (!snap?.exists()) {
      toast('Parameter not found', 'error');
      return;
    }
    
    const param = snap.val();
    selectedParamType = param.type || 'string';
    
    document.getElementById('paramModalTitle').textContent = '✏️ Edit Parameter';
    document.getElementById('paramKeyInput').value = key;
    document.getElementById('paramKeyInput').readOnly = true;
    document.getElementById('paramKeyInput').style.opacity = '0.5';
    
    let displayValue = param.value;
    if (selectedParamType === 'boolean') {
      displayValue = param.value === true || param.value === 'true' ? 'true' : 'false';
    } else if (selectedParamType === 'json') {
      try {
        displayValue = typeof param.value === 'string' ? param.value : JSON.stringify(param.value, null, 2);
      } catch {}
    }
    
    document.getElementById('paramValueInput').value = displayValue;
    
    document.querySelectorAll('.type-option').forEach(opt => {
      opt.classList.toggle('selected', opt.dataset.type === selectedParamType);
    });
    
    document.getElementById('paramModalOverlay').classList.remove('hidden');
  });
}

async function saveParam() {
  if (!currentEditingAppKey) return;
  
  const keyInput = document.getElementById('paramKeyInput');
  const valueInput = document.getElementById('paramValueInput');
  
  let key = keyInput.value.trim();
  const value = valueInput.value.trim();
  
  if (!key) { toast('Key is required', 'error'); return; }
  if (!/^[a-zA-Z_][a-zA-Z0-9_]*$/.test(key)) {
    toast('Key must start with letter/underscore', 'error');
    return;
  }
  
  if (editingParamKey) {
    key = editingParamKey;
  } else {
    // Check exists
    const existing = await window._get(window._ref(window._db, `apps/${currentEditingAppKey}/firebaseConfig/remoteConfig/${key}`));
    if (existing?.exists()) {
      toast('Key already exists', 'error');
      return;
    }
  }
  
  // Parse value
  let parsedValue;
  switch (selectedParamType) {
    case 'number':
      parsedValue = Number(value);
      if (isNaN(parsedValue)) { toast('Invalid number', 'error'); return; }
      break;
    case 'boolean':
      parsedValue = value === 'true' || value === '1' || value.toLowerCase() === 'yes';
      break;
    case 'json':
      try { parsedValue = JSON.parse(value); }
      catch { toast('Invalid JSON', 'error'); return; }
      break;
    default:
      parsedValue = value;
  }
  
  const paramData = {
    value: parsedValue,
    type: selectedParamType,
    updatedAt: Date.now()
  };
  if (!editingParamKey) paramData.createdAt = Date.now();
  
  // Get existing params
  const snap = await window._get(window._ref(window._db, `apps/${currentEditingAppKey}/firebaseConfig`));
  const existing = snap.exists() ? (snap.val().remoteConfig || {}) : {};
  
  if (!editingParamKey) {
    existing[key] = paramData;
  } else {
    existing[key] = paramData;
  }
  
  await window._update(window._ref(window._db, `apps/${currentEditingAppKey}`), {
    'firebaseConfig/remoteConfig': existing,
    'firebaseConfig/lastModified': Date.now()
  });
  
  toast(editingParamKey ? '✅ Parameter updated!' : '✅ Parameter added!', 'success');
  await logActivity(editingParamKey ? '✏️ Updated Parameter' : '➕ Added Parameter', key);
  
  closeModal('paramModalOverlay');
  keyInput.readOnly = false;
  keyInput.style.opacity = '1';
  editingParamKey = null;
  
  // Refresh
  const appSnap = await window._get(window._ref(window._db, `apps/${currentEditingAppKey}`));
  if (appSnap.exists()) {
    renderRemoteParamsUI(currentEditingAppKey, appSnap.val(), 'editAppRemoteParamsContent');
  }
}

async function deleteParam(appKey, key) {
  showConfirm('🗑 Delete Parameter?', `Delete "${key}"?`, async () => {
    try {
      const snap = await window._get(window._ref(window._db, `apps/${appKey}/firebaseConfig/remoteConfig`));
      if (snap.exists()) {
        const params = { ...snap.val() };
        delete params[key];
        
        await window._update(window._ref(window._db, `apps/${appKey}`), {
          'firebaseConfig/remoteConfig': params,
          'firebaseConfig/lastModified': Date.now()
        });
      }
      
      toast('✅ Parameter deleted!', 'success');
      await logActivity('🗑 Deleted Parameter', key);
      
      const appSnap = await window._get(window._ref(window._db, `apps/${appKey}`));
      if (appSnap.exists()) {
        renderRemoteParamsUI(appKey, appSnap.val(), 'editAppRemoteParamsContent');
      }
    } catch (e) {
      toast('Error: ' + e.message, 'error');
    }
  });
}

// Type selector
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

  const closeBtn = target.closest('[data-close]');
  if (closeBtn) {
    closeModal(closeBtn.getAttribute('data-close'));
    if (closeBtn.getAttribute('data-close') === 'paramModalOverlay') {
      const keyInput = document.getElementById('paramKeyInput');
      if (keyInput) { keyInput.readOnly = false; keyInput.style.opacity = '1'; }
      editingParamKey = null;
    }
    return;
  }

  if (target.classList.contains('overlay')) { 
    const overlayId = target.id;
    if (overlayId === 'paramModalOverlay') {
      const keyInput = document.getElementById('paramKeyInput');
      if (keyInput) { keyInput.readOnly = false; keyInput.style.opacity = '1'; }
      editingParamKey = null;
    }
    closeModal(overlayId); 
    return; 
  }

  // Modal tabs
  const modalTab = target.closest('.modal-tab');
  if (modalTab) {
    const tabId = modalTab.dataset.modalTab;
    document.querySelectorAll('.modal-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.modal-tab-content').forEach(c => c.classList.remove('active'));
    modalTab.classList.add('active');
    document.getElementById(`tab_${tabId}`)?.classList.add('active');
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
    showConfirm('Clear History?', 'Delete all visit history?', async () => {
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
    showConfirm('Delete Visitor?', 'Permanently delete?', async () => {
      try {
        await window._remove(window._ref(window._db, `visitors/${currentVisitorKey}`));
        toast('✅ Visitor deleted!', 'success');
        currentVisitorKey = null;
        closeModal('visitorDetailOverlay');
        await logActivity('🗑 Deleted Visitor');
        loadVisitors();
        updateStats();
      } catch (e) { toast('Error: ' + e.message, 'error'); }
    });
    return;
  }

  if (id === 'btnClearAllVisitors' || target.closest('#btnClearAllVisitors')) {
    if (!firebaseReady) { toast('Not connected', 'error'); return; }
    showConfirm('Delete ALL Visitors?', 'This will delete ALL visitor data!', async () => {
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
    if (!firebaseReady) { toast('Not connected', 'error'); return; }
    showConfirm('Delete ALL Activity?', 'This will delete ALL activity logs!', async () => {
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
  if (id === 'btnSaveParam' || target.closest('#btnSaveParam')) { saveParam(); return; }

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
  if (id === 'settings') loadApkLinkDisplay();
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
    content.innerHTML = '<div style="color:red;padding:40px;text-align:center;">❌ Error</div>';
    return;
  }

  if (!v) {
    content.innerHTML = '<div style="color:var(--text-dim);padding:40px;text-align:center;">❌ Not found</div>';
    return;
  }

  const isU = !!v.userName;
  const dn = v.deviceName || 'Unknown Device';

  let h = `<div style="text-align:center;margin-bottom:20px;">
    <div style="width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,var(--orange),var(--orange-light));display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:700;color:#000;margin:0 auto 10px;">${isU ? (v.userName || 'U')[0].toUpperCase() : '📱'}</div>
    <div style="font-size:18px;font-weight:700;">${esc(isU ? v.userName : dn)}</div>
    <div style="font-size:12px;color:var(--text-dim);">${isU ? 'User' : 'Guest'} • ${v.visitCount || 0} visits</div>
  </div>`;

  h += `
  <div class="detail-row"><span class="detail-label">📱 Device</span><span class="detail-value">${esc(dn)}</span></div>
  <div class="detail-row"><span class="detail-label">🧠 RAM</span><span class="detail-value">${esc(v.ram || 'N/A')}</span></div>
  <div class="detail-row"><span class="detail-label">🖥 Platform</span><span class="detail-value">${esc(v.platform || 'N/A')}</span></div>
  <div class="detail-row"><span class="detail-label">🌐 IP</span><span class="detail-value">${esc(v.ip || 'N/A')}</span></div>`;

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
    c.innerHTML = h || '<div style="color:var(--text-dim);padding:10px;text-align:center;">No activity</div>';
  } catch (e) {
    c.innerHTML = '<div style="color:red;padding:10px;">Error</div>';
  }
}

// ============ AUTH ============
async function doAdminLogin() {
  const u = document.getElementById('adminUser').value.trim();
  const p = document.getElementById('adminPass').value;
  if (!u || !p) { toast('Fill all fields', 'error'); return; }
  if (!firebaseReady) { toast('Connecting...', 'info'); return; }
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
    } else { toast('No admin accounts!', 'error'); }
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

function adminLogout() {
  sessionStorage.clear();
  currentAdminKey = null;
  document.getElementById('loginPage').style.display = 'flex';
  document.getElementById('adminDashboard').style.display = 'none';
  toast('Logged out', 'success');
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
  
  if (!n || !d) { toast('Name and Description required', 'error'); return; }
  
  const appData = { name: n, icon: ic, imageUrl: img || null, category: c, description: d, link: lk || null, downloads: 0 };
  if (s1) appData.screenshot1 = s1;
  if (s2) appData.screenshot2 = s2;
  if (s3) appData.screenshot3 = s3;
  if (s4) appData.screenshot4 = s4;
  if (s5) appData.screenshot5 = s5;
  
  // Add Firebase config if uploaded for new app
  if (newAppTempConfig) {
    appData.firebaseConfig = newAppTempConfig;
  }
  
  try {
    await window._set(window._push(window._ref(window._db, 'apps')), appData);
    toast('✅ App added!', 'success');
    await logActivity('➕ Added App', n);
    
    // Clear form
    ['aName','aImageUrl','aDesc','aLink','aScreen1','aScreen2','aScreen3','aScreen4','aScreen5'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.value = '';
    });
    document.getElementById('aIcon').value = '📱';
    
    // Reset new app temp
    newAppTempJson = null;
    newAppTempConfig = null;
    const preview = document.getElementById('newAppJsonPreview');
    if (preview) { preview.classList.add('hidden'); preview.innerHTML = ''; }
    const uploadZone = document.getElementById('newAppUploadZone');
    if (uploadZone) uploadZone.classList.remove('has-file');
    
    loadApps();
    updateStats();
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

function loadApps() {
  if (!firebaseReady) { setTimeout(loadApps, 600); return; }
  const l = document.getElementById('adminAppsList');
  if (!l) return;
  l.innerHTML = '<div class="spinner"></div>';
  window._get(window._ref(window._db, 'apps')).then(s => {
    if (!s.exists()) { l.innerHTML = '<div style="color:var(--text-dim);padding:20px;text-align:center;">No apps yet</div>'; return; }
    let h = '';
    s.forEach(c => {
      const a = c.val();
      const hasConfig = a.firebaseConfig?.googleServicesJson;
      const hasParams = a.firebaseConfig?.remoteConfig && Object.keys(a.firebaseConfig.remoteConfig).length > 0;
      
      h += `<div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:12px;display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <div>${a.imageUrl ? `<img src="${esc(a.imageUrl)}" style="width:40px;height:40px;border-radius:10px;object-fit:cover;" onerror="this.style.display='none'">` : ''}<span style="font-size:32px;">${esc(a.icon || '📱')}</span></div>
        <div style="flex:1;">
          <div style="font-weight:600;">${esc(a.name)}</div>
          <div style="font-size:11px;color:var(--text-dim);">
            ${esc(a.category)} • ${formatNum(a.downloads || 0)} DL
            ${hasConfig ? '<span class="badge config" style="margin-left:6px;">🔥 Firebase</span>' : ''}
            ${hasParams ? '<span class="badge config" style="margin-left:2px;">🔧 ' + Object.keys(a.firebaseConfig.remoteConfig).length + '</span>' : ''}
          </div>
        </div>
        <div style="display:flex;gap:6px;">
          <button class="btn btn-outline btn-sm" id="editAppBtn_${c.key}">✏️ Edit</button>
          <button class="btn btn-danger btn-sm" id="delAppBtn_${c.key}">🗑</button>
        </div>
      </div>`;
    });
    l.innerHTML = h;
  }).catch(e => { l.innerHTML = '<div style="color:red;padding:10px;">Error</div>'; });
}

async function deleteApp(k) {
  try {
    const snap = await window._get(window._ref(window._db, 'apps/' + k));
    const appName = snap.val()?.name || 'Unknown';
    await window._remove(window._ref(window._db, 'apps/' + k));
    toast('✅ App deleted!', 'success');
    await logActivity('🗑 Deleted App', appName);
    loadApps();
    updateStats();
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

async function openEditApp(k) {
  currentEditingAppKey = k;
  
  const s = await window._get(window._ref(window._db, 'apps/' + k));
  const a = s.val();
  if (!a) { toast('App not found', 'error'); return; }
  currentEditingAppData = a;
  
  // Render App Info tab
  document.getElementById('editAppContent').innerHTML = `
    <input type="hidden" id="editAppKey" value="${k}">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="input-group" style="margin-bottom:10px;"><label>Name</label><input id="editName" value="${esc(a.name)}"></div>
      <div class="input-group" style="margin-bottom:10px;"><label>Category</label>
        <select id="editCategory">
          ${['Social', 'Games', 'Tools', 'Entertainment', 'Other'].map(c => `<option ${a.category === c ? 'selected' : ''}>${c}</option>`).join('')}
        </select>
      </div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="input-group" style="margin-bottom:10px;"><label>Icon</label><input id="editIcon" value="${esc(a.icon || '📱')}"></div>
      <div class="input-group" style="margin-bottom:10px;"><label>Image URL</label><input id="editImageUrl" value="${esc(a.imageUrl || '')}"></div>
    </div>
    <div class="input-group" style="margin-bottom:10px;"><label>Link</label><input id="editLink" value="${esc(a.link || '')}"></div>
    <div class="input-group" style="margin-bottom:10px;"><label>Description</label><textarea id="editDesc" rows="2">${esc(a.description || '')}</textarea></div>
    <div style="font-size:12px;color:var(--text-dim);margin-bottom:8px;font-weight:600;">📸 Screenshots</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="input-group" style="margin-bottom:8px;"><label>S1</label><input id="editScreen1" value="${esc(a.screenshot1 || '')}"></div>
      <div class="input-group" style="margin-bottom:8px;"><label>S2</label><input id="editScreen2" value="${esc(a.screenshot2 || '')}"></div>
      <div class="input-group" style="margin-bottom:8px;"><label>S3</label><input id="editScreen3" value="${esc(a.screenshot3 || '')}"></div>
      <div class="input-group" style="margin-bottom:8px;"><label>S4</label><input id="editScreen4" value="${esc(a.screenshot4 || '')}"></div>
      <div class="input-group" style="margin-bottom:8px;"><label>S5</label><input id="editScreen5" value="${esc(a.screenshot5 || '')}"></div>
    </div>
    <button class="btn btn-primary btn-sm" style="width:100%;margin-top:10px;" id="btnSaveEdit">💾 Save Info</button>
  `;
  
  // Render Firebase Config tab
  renderFirebaseConfigUI(k, a, 'editAppFirebaseContent');
  
  // Render Remote Params tab
  renderRemoteParamsUI(k, a, 'editAppRemoteParamsContent');
  
  // Switch to first tab
  document.querySelectorAll('.modal-tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.modal-tab-content').forEach(c => c.classList.remove('active'));
  document.querySelector('.modal-tab').classList.add('active');
  document.getElementById('tab_appInfo').classList.add('active');
  
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
  
  if (!n || !d) { toast('Name and Description required', 'error'); return; }
  
  const updates = { name: n, category: c, icon: ic, imageUrl: img || null, link: lk || null, description: d,
    screenshot1: s1 || null, screenshot2: s2 || null, screenshot3: s3 || null, screenshot4: s4 || null, screenshot5: s5 || null };
  
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
    if (!s.exists()) { l.innerHTML = '<div style="color:var(--text-dim);padding:20px;text-align:center;">No users</div>'; return; }
    let h = '';
    s.forEach(c => {
      const u = c.val();
      h += `<div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:12px;display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <div style="flex:1;">
          <div style="font-weight:600;">${esc(u.name)}</div>
          <div style="font-size:11px;color:var(--text-dim);">${esc(u.email || u.number)}</div>
        </div>
        <button class="btn btn-danger btn-sm" id="delUserBtn_${c.key}">🗑</button>
      </div>`;
    });
    l.innerHTML = h;
  }).catch(e => { l.innerHTML = '<div style="color:red;padding:10px;">Error</div>'; });
}

async function deleteUser(k) {
  try {
    await window._remove(window._ref(window._db, 'users/' + k));
    toast('✅ User deleted!', 'success');
    await logActivity('🗑 Deleted User');
    loadUsers();
    updateStats();
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

// ============ REPORTS ============
function loadReports() {
  if (!firebaseReady) { setTimeout(loadReports, 600); return; }
  const l = document.getElementById('adminReportsList');
  if (!l) return;
  l.innerHTML = '<div class="spinner"></div>';
  window._get(window._ref(window._db, 'reports')).then(s => {
    if (!s.exists()) { l.innerHTML = '<div style="color:var(--text-dim);padding:20px;text-align:center;">No reports</div>'; return; }
    let h = '';
    s.forEach(c => {
      const r = c.val();
      const t = r.timestamp ? new Date(r.timestamp).toLocaleString() : 'N/A';
      h += `<div style="background:var(--card);border:1px solid var(--border);border-radius:8px;padding:12px;margin-bottom:8px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
          <span style="font-weight:600;">${esc(r.subject || 'No Subject')}</span>
          <div style="display:flex;gap:6px;align-items:center;">
            <span style="font-size:10px;color:var(--text-dim);">${t}</span>
            <button class="btn btn-danger btn-sm" id="delReportBtn_${c.key}">🗑</button>
          </div>
        </div>
        <div style="font-size:11px;color:var(--text-dim);">${esc(r.message || '')}</div>
      </div>`;
    });
    l.innerHTML = h;
  }).catch(e => { l.innerHTML = '<div style="color:red;padding:10px;">Error</div>'; });
}

async function deleteReport(k) {
  try {
    await window._remove(window._ref(window._db, 'reports/' + k));
    toast('✅ Report deleted!', 'success');
    loadReports();
    updateStats();
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
        await logActivity('🔐 Updated Credentials');
        document.getElementById('currentAdminPass').value = '';
        document.getElementById('newAdminUser').value = '';
        document.getElementById('newAdminPass').value = '';
      } else { toast('Nothing to update', 'info'); }
    } else { toast('Wrong password', 'error'); }
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
  logActivity('⚙️ Updated Settings', n);
}

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
  if (!link) { toast('Enter a link', 'error'); return; }
  if (!link.startsWith('http')) { toast('Link must start with http', 'error'); return; }
  try {
    await window._set(window._ref(window._db, 'settings/apkDownloadLink'), link);
    toast('✅ APK Link saved!', 'success');
    await logActivity('📦 Set APK Link');
    loadApkLinkDisplay();
  } catch (e) { toast('Error: ' + e.message, 'error'); }
}

async function removeApkLink() {
  showConfirm('Remove APK Link?', 'Remove download button?', async () => {
    try {
      await window._remove(window._ref(window._db, 'settings/apkDownloadLink'));
      toast('✅ APK link removed!', 'success');
      await logActivity('📦 Removed APK Link');
      document.getElementById('apkLinkInput').value = '';
      loadApkLinkDisplay();
    } catch (e) { toast('Error: ' + e.message, 'error'); }
  });
}

// ============ NEW APP FILE UPLOAD ============
document.addEventListener('DOMContentLoaded', () => {
  const uploadZone = document.getElementById('newAppUploadZone');
  const fileInput = document.getElementById('newAppGoogleJsonInput');
  
  if (uploadZone && fileInput) {
    uploadZone.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', async (e) => {
      const file = e.target.files?.[0];
      if (!file) return;
      
      try {
        const text = await file.text();
        const jsonData = JSON.parse(text);
        const configData = extractFirebaseConfig(jsonData);
        
        if (!configData) {
          toast('Invalid google-services.json', 'error');
          return;
        }
        
        newAppTempJson = text;
        newAppTempConfig = {
          ...configData,
          uploadedAt: Date.now(),
          lastModified: Date.now()
        };
        
        const preview = document.getElementById('newAppJsonPreview');
        if (preview) {
          preview.classList.remove('hidden');
          preview.innerHTML = `
            <div style="background:rgba(34,197,94,0.15);border:1px solid rgba(34,197,94,0.3);border-radius:8px;padding:12px;">
              <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;">
                <span style="color:#4ade80;font-size:16px;">✅</span>
                <span style="font-weight:600;color:#4ade80;">JSON Ready</span>
              </div>
              <div style="font-size:12px;color:var(--text-dim);">
                <div>Project: ${esc(configData.project_id)}</div>
                <div>Package: ${esc(configData.package_name)}</div>
              </div>
            </div>
          `;
        }
        
        uploadZone.classList.add('has-file');
        toast('✅ JSON file ready!', 'success');
        
      } catch (e) {
        toast('Error reading file', 'error');
      }
    });
  }
});

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
