<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ResuMind AI - Intelligent ATS Resume Analyzer</title>
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  <style>
    :root {
      --bg-dark: #090d16;
      --card-bg: rgba(22, 31, 49, 0.7);
      --card-border: rgba(255, 255, 255, 0.08);
      --primary: #6366f1;
      --primary-hover: #4f46e5;
      --primary-glow: rgba(99, 102, 241, 0.35);
      --accent: #06b6d4;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --success: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
      --sidebar-width: 260px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    body {
      background-color: var(--bg-dark);
      color: var(--text);
      min-height: 100vh;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 40%),
        radial-gradient(circle at 90% 80%, rgba(6, 182, 212, 0.12) 0%, transparent 40%);
    }

    /* Common Utilities */
    .btn {
      padding: 0.75rem 1.5rem;
      border-radius: 8px;
      font-weight: 600;
      border: none;
      cursor: pointer;
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      text-decoration: none;
      font-size: 0.95rem;
    }

    .btn-primary {
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: white;
      box-shadow: 0 4px 15px var(--primary-glow);
    }

    .btn-primary:hover {
      opacity: 0.95;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px var(--primary-glow);
    }

    .btn-secondary {
      background: rgba(255, 255, 255, 0.05);
      color: var(--text);
      border: 1px solid var(--card-border);
    }

    .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.1);
    }

    .btn-danger {
      background: var(--danger);
      color: white;
    }

    .card {
      background: var(--card-bg);
      backdrop-filter: blur(12px);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 1.75rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    .form-group {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      margin-bottom: 1.25rem;
    }

    .form-group label {
      font-size: 0.88rem;
      font-weight: 500;
      color: var(--text-muted);
    }

    .form-control {
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--card-border);
      padding: 0.85rem 1rem;
      border-radius: 8px;
      color: var(--text);
      font-size: 0.95rem;
      outline: none;
      transition: border-color 0.2s;
    }

    .form-control:focus {
      border-color: var(--primary);
    }

    /* Navigation Bar */
    .navbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.25rem 5%;
      border-bottom: 1px solid var(--card-border);
      background: rgba(9, 13, 22, 0.8);
      backdrop-filter: blur(10px);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .logo {
      font-size: 1.5rem;
      font-weight: 800;
      background: linear-gradient(135deg, #fff, var(--text-muted));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      cursor: pointer;
    }

    .logo i {
      color: var(--primary);
      -webkit-text-fill-color: initial;
    }

    .nav-links {
      display: flex;
      gap: 2rem;
      list-style: none;
      align-items: center;
    }

    .nav-links a {
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 500;
      transition: color 0.2s;
      cursor: pointer;
    }

    .nav-links a:hover, .nav-links a.active {
      color: var(--text);
    }

    /* Views Framework */
    .view-section {
      display: none;
      animation: fadeIn 0.35s ease-in-out forwards;
    }

    .view-section.active {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* 1. HERO & LANDING PAGE */
    .hero {
      text-align: center;
      padding: 5rem 1rem 3rem;
      max-width: 900px;
      margin: 0 auto;
    }

    .hero h1 {
      font-size: 3.5rem;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 1.5rem;
    }

    .hero h1 span {
      background: linear-gradient(135deg, var(--primary), var(--accent));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero p {
      font-size: 1.2rem;
      color: var(--text-muted);
      margin-bottom: 2.5rem;
    }

    .features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 2rem;
      padding: 4rem 5%;
      max-width: 1200px;
      margin: 0 auto;
    }

    .feature-card {
      text-align: left;
    }

    .feature-card i {
      font-size: 2rem;
      color: var(--primary);
      margin-bottom: 1rem;
    }

    .about-section {
      max-width: 900px;
      margin: 2rem auto 5rem;
      text-align: center;
      padding: 0 1rem;
    }

    footer {
      border-top: 1px solid var(--card-border);
      padding: 2.5rem 5%;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.9rem;
    }

    /* 2 & 3. AUTH PAGES (Login & Register) */
    .auth-container {
      max-width: 440px;
      margin: 4rem auto;
      padding: 0 1rem;
    }

    .auth-header {
      text-align: center;
      margin-bottom: 2rem;
    }

    .auth-header h2 {
      font-size: 1.8rem;
      margin-bottom: 0.5rem;
    }

    .google-btn {
      width: 100%;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--card-border);
      color: var(--text);
      padding: 0.75rem;
      border-radius: 8px;
      cursor: pointer;
      font-weight: 500;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.75rem;
      margin-bottom: 1.5rem;
      transition: background 0.2s;
    }

    .google-btn:hover {
      background: rgba(255, 255, 255, 0.12);
    }

    .divider {
      text-align: center;
      margin: 1.5rem 0;
      position: relative;
      color: var(--text-muted);
      font-size: 0.85rem;
    }

    .divider::before, .divider::after {
      content: '';
      position: absolute;
      top: 50%;
      width: 40%;
      height: 1px;
      background: var(--card-border);
    }

    .divider::before { left: 0; }
    .divider::after { right: 0; }

    .auth-options {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.85rem;
      margin-bottom: 1.5rem;
    }

    .auth-options a {
      color: var(--primary);
      text-decoration: none;
    }

    /* DASHBOARD LAYOUT (Dashboard, Upload, Result, History, Profile, Settings) */
    .app-layout {
      display: flex;
      min-height: calc(100vh - 73px);
    }

    .sidebar {
      width: var(--sidebar-width);
      border-right: 1px solid var(--card-border);
      background: rgba(15, 23, 42, 0.4);
      padding: 1.5rem 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      flex-shrink: 0;
    }

    .sidebar-link {
      display: flex;
      align-items: center;
      gap: 0.85rem;
      padding: 0.85rem 1rem;
      color: var(--text-muted);
      text-decoration: none;
      border-radius: 8px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s;
    }

    .sidebar-link:hover, .sidebar-link.active {
      background: rgba(99, 102, 241, 0.12);
      color: var(--primary);
    }

    .main-content {
      flex: 1;
      padding: 2.5rem;
      max-width: 1300px;
      overflow-y: auto;
    }

    /* 4. DASHBOARD VIEW */
    .dashboard-metrics {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1.5rem;
      margin-bottom: 2rem;
    }

    .metric-card {
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }

    .metric-icon {
      width: 52px;
      height: 52px;
      border-radius: 12px;
      background: rgba(99, 102, 241, 0.15);
      color: var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
    }

    .metric-data h4 {
      font-size: 1.6rem;
      font-weight: 700;
    }

    .metric-data p {
      font-size: 0.85rem;
      color: var(--text-muted);
    }

    .dashboard-grid {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 1.5rem;
    }

    /* CSS Custom Chart Simulation */
    .chart-container {
      height: 240px;
      display: flex;
      align-items: flex-end;
      gap: 1.5rem;
      padding-top: 2rem;
      border-bottom: 1px solid var(--card-border);
    }

    .chart-bar-wrap {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 0.5rem;
      height: 100%;
      justify-content: flex-end;
    }

    .chart-bar {
      width: 100%;
      max-width: 40px;
      background: linear-gradient(0deg, var(--primary), var(--accent));
      border-radius: 6px 6px 0 0;
      transition: height 1s ease;
    }

    .chart-label {
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    .activity-list {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin-top: 1rem;
    }

    .activity-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.75rem 0;
      border-bottom: 1px solid var(--card-border);
      font-size: 0.9rem;
    }

    /* 5. RESUME UPLOAD VIEW */
    .upload-zone {
      border: 2px dashed var(--card-border);
      border-radius: 16px;
      padding: 3.5rem 2rem;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s;
      background: rgba(15, 23, 42, 0.3);
      margin-bottom: 2rem;
    }

    .upload-zone:hover, .upload-zone.dragover {
      border-color: var(--primary);
      background: rgba(99, 102, 241, 0.05);
    }

    .upload-zone i {
      font-size: 3rem;
      color: var(--primary);
      margin-bottom: 1rem;
    }

    /* 6. ATS RESULT VIEW */
    .results-layout {
      display: grid;
      grid-template-columns: 1fr 2fr;
      gap: 1.5rem;
    }

    .score-box {
      text-align: center;
      padding: 2rem;
    }

    .gauge-wrapper {
      position: relative;
      width: 160px;
      height: 160px;
      margin: 0 auto 1.5rem;
    }

    .gauge-circle {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      background: conic-gradient(var(--primary) 87%, var(--card-border) 0);
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .gauge-inner {
      width: 125px;
      height: 125px;
      border-radius: 50%;
      background: var(--bg-dark);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2rem;
      font-weight: 800;
    }

    .section-checklist {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1rem;
      margin-bottom: 2rem;
    }

    .check-item {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.9rem;
      background: rgba(255, 255, 255, 0.03);
      padding: 0.75rem 1rem;
      border-radius: 8px;
    }

    .check-item i {
      color: var(--success);
    }

    .suggestions-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .suggestion-card {
      display: flex;
      align-items: flex-start;
      gap: 0.85rem;
      background: rgba(245, 158, 11, 0.08);
      border: 1px solid rgba(245, 158, 11, 0.2);
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.9rem;
    }

    .suggestion-card i {
      color: var(--warning);
      margin-top: 0.15rem;
    }

    /* 7. RESUME HISTORY VIEW */
    .history-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 1rem;
    }

    .history-table th, .history-table td {
      padding: 1rem;
      text-align: left;
      border-bottom: 1px solid var(--card-border);
      font-size: 0.9rem;
    }

    .history-table th {
      color: var(--text-muted);
      font-weight: 600;
    }

    .table-actions {
      display: flex;
      gap: 0.5rem;
    }

    /* 8 & 9. PROFILE & SETTINGS */
    .profile-header {
      display: flex;
      align-items: center;
      gap: 2rem;
      margin-bottom: 2rem;
    }

    .profile-avatar {
      width: 90px;
      height: 90px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2.2rem;
      color: white;
    }

    .settings-list {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .setting-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid var(--card-border);
    }

    /* Responsive Design */
    @media (max-width: 900px) {
      .app-layout { flex-direction: column; }
      .sidebar { width: 100%; border-right: none; border-bottom: 1px solid var(--card-border); }
      .dashboard-grid, .results-layout { grid-template-columns: 1fr; }
      .hero h1 { font-size: 2.5rem; }
    }
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <nav class="navbar">
    <div class="logo" onclick="navigateTo('home')">
      <i class="fa-solid fa-brain"></i> ResuMind AI
    </div>
    <ul class="nav-links" id="publicNav">
      <li><a onclick="navigateTo('home')">Home</a></li>
      <li><a onclick="navigateTo('home', 'features')">Features</a></li>
      <li><a onclick="navigateTo('home', 'about')">About</a></li>
      <li><a onclick="navigateTo('login')" class="btn btn-secondary" style="padding: 0.5rem 1rem;">Login</a></li>
      <li><a onclick="navigateTo('register')" class="btn btn-primary" style="padding: 0.5rem 1rem;">Get Started</a></li>
    </ul>
    <ul class="nav-links" id="privateNav" style="display: none;">
      <li><a onclick="navigateTo('dashboard')">Dashboard</a></li>
      <li><a onclick="navigateTo('profile')"><i class="fa-solid fa-circle-user"></i> Profile</a></li>
      <li><a onclick="logout()" class="btn btn-secondary" style="padding: 0.4rem 0.8rem;"><i class="fa-solid fa-right-from-bracket"></i></a></li>
    </ul>
  </nav>

  <!-- 1. HOME PAGE VIEW -->
  <div id="view-home" class="view-section active">
    <section class="hero">
      <h1>Optimize Your Resume for <span>ATS & AI Screening</span></h1>
      <p>Get instant feedback, match with target roles, and increase your interview callbacks by up to 3x with our intelligent analyzer.</p>
      <button class="btn btn-primary" onclick="navigateTo('register')" style="font-size: 1.1rem; padding: 0.9rem 2rem;">
        Get Started Free <i class="fa-solid fa-arrow-right"></i>
      </button>
    </section>

    <section id="features" class="features-grid">
      <div class="card feature-card">
        <i class="fa-solid fa-bolt"></i>
        <h3>Instant ATS Scoring</h3>
        <p style="color: var(--text-muted); margin-top: 0.5rem; font-size: 0.9rem;">Analyze formatting, structure, and readability metrics instantly against enterprise parser standards.</p>
      </div>
      <div class="card feature-card">
        <i class="fa-solid fa-crosshairs"></i>
        <h3>Role Keyword Match</h3>
        <p style="color: var(--text-muted); margin-top: 0.5rem; font-size: 0.9rem;">Identify missing technical and soft skills tailored specifically for your target job description.</p>
      </div>
      <div class="card feature-card">
        <i class="fa-solid fa-wand-magic-sparkles"></i>
        <h3>Actionable Feedback</h3>
        <p style="color: var(--text-muted); margin-top: 0.5rem; font-size: 0.9rem;">Receive step-by-step guidance on action verbs, bullet-point metrics, and section enhancements.</p>
      </div>
    </section>

    <section id="about" class="about-section card">
      <h2>About ResuMind AI</h2>
      <p style="color: var(--text-muted); margin-top: 1rem; line-height: 1.6;">
        ResuMind AI is built to bridge the gap between job seekers and Applicant Tracking Systems (ATS). Our algorithms scan your resume using modern HR parameters to give you a clear advantage in today's automated hiring process.
      </p>
    </section>

    <footer>
      <p>© 2026 ResuMind AI. All rights reserved. Empowering job seekers worldwide.</p>
    </footer>
  </div>

  <!-- 2. LOGIN VIEW -->
  <div id="view-login" class="view-section">
    <div class="auth-container">
      <div class="card">
        <div class="auth-header">
          <h2>Welcome Back</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">Login to access your analysis history</p>
        </div>

        <button class="google-btn" onclick="handleAuthSuccess()">
          <i class="fa-brands fa-google" style="color: #ea4335;"></i> Continue with Google
        </button>

        <div class="divider">OR</div>

        <form onsubmit="event.preventDefault(); handleAuthSuccess();">
          <div class="form-group">
            <label>Email Address</label>
            <input type="email" class="form-control" placeholder="alex@example.com" required value="demo@resumind.ai" />
          </div>
          <div class="form-group">
            <label>Password</label>
            <input type="password" class="form-control" placeholder="••••••••" required value="password123" />
          </div>
          <div class="auth-options">
            <label style="display: flex; align-items: center; gap: 0.4rem; cursor: pointer;">
              <input type="checkbox" checked /> Remember Me
            </label>
            <a href="#" onclick="alert('Password reset link sent to your email!')">Forgot Password?</a>
          </div>
          <button type="submit" class="btn btn-primary" style="width: 100%;">Sign In</button>
        </form>
        <p style="text-align: center; font-size: 0.85rem; color: var(--text-muted); margin-top: 1.5rem;">
          Don't have an account? <a href="#" onclick="navigateTo('register')" style="color: var(--primary);">Create Account</a>
        </p>
      </div>
    </div>
  </div>

  <!-- 3. REGISTER VIEW -->
  <div id="view-register" class="view-section">
    <div class="auth-container">
      <div class="card">
        <div class="auth-header">
          <h2>Create Your Account</h2>
          <p style="color: var(--text-muted); font-size: 0.9rem;">Start optimizing your resume for free</p>
        </div>

        <button class="google-btn" onclick="handleAuthSuccess()">
          <i class="fa-brands fa-google" style="color: #ea4335;"></i> Sign up with Google
        </button>

        <div class="divider">OR</div>

        <form onsubmit="event.preventDefault(); handleAuthSuccess();">
          <div class="form-group">
            <label>Full Name</label>
            <input type="text" class="form-control" placeholder="Alex Morgan" required />
          </div>
          <div class="form-group">
            <label>Email Address</label>
            <input type="email" class="form-control" placeholder="alex@example.com" required />
          </div>
          <div class="form-group">
            <label>Password</label>
            <input type="password" class="form-control" placeholder="••••••••" required />
          </div>
          <div class="form-group">
            <label>Confirm Password</label>
            <input type="password" class="form-control" placeholder="••••••••" required />
          </div>
          <button type="submit" class="btn btn-primary" style="width: 100%;">Create Account</button>
        </form>
        <p style="text-align: center; font-size: 0.85rem; color: var(--text-muted); margin-top: 1.5rem;">
          Already have an account? <a href="#" onclick="navigateTo('login')" style="color: var(--primary);">Sign In</a>
        </p>
      </div>
    </div>
  </div>

  <!-- MAIN APP WRAPPER (For Dashboard & Internal Tools) -->
  <div id="appLayout" class="app-layout" style="display: none;">
    
    <!-- 4. SIDEBAR -->
    <aside class="sidebar">
      <a class="sidebar-link active" id="s-dashboard" onclick="navigateTo('dashboard')"><i class="fa-solid fa-chart-pie"></i> Dashboard</a>
      <a class="sidebar-link" id="s-upload" onclick="navigateTo('upload')"><i class="fa-solid fa-cloud-arrow-up"></i> Upload Resume</a>
      <a class="sidebar-link" id="s-history" onclick="navigateTo('history')"><i class="fa-solid fa-clock-rotate-left"></i> Resume History</a>
      <a class="sidebar-link" id="s-profile" onclick="navigateTo('profile')"><i class="fa-solid fa-id-card"></i> Profile</a>
      <a class="sidebar-link" id="s-settings" onclick="navigateTo('settings')"><i class="fa-solid fa-gear"></i> Settings</a>
      <div style="margin-top: auto; padding-top: 1rem; border-top: 1px solid var(--card-border);">
        <a class="sidebar-link" onclick="logout()" style="color: var(--danger);"><i class="fa-solid fa-right-from-bracket"></i> Logout</a>
      </div>
    </aside>

    <!-- MAIN DASHBOARD CONTENT CONTAINER -->
    <main class="main-content">

      <!-- DASHBOARD VIEW -->
      <div id="view-dashboard" class="view-section">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
          <div>
            <h2>Welcome Back, Alex 👋</h2>
            <p style="color: var(--text-muted); font-size: 0.9rem;">Here is your resume optimization performance summary.</p>
          </div>
          <button class="btn btn-primary" onclick="navigateTo('upload')"><i class="fa-solid fa-plus"></i> Upload New</button>
        </div>

        <div class="dashboard-metrics">
          <div class="card metric-card">
            <div class="metric-icon"><i class="fa-solid fa-file-lines"></i></div>
            <div class="metric-data">
              <h4>12</h4>
              <p>Total Uploads</p>
            </div>
          </div>
          <div class="card metric-card">
            <div class="metric-icon" style="color: var(--accent); background: rgba(6, 182, 212, 0.15);"><i class="fa-solid fa-chart-line"></i></div>
            <div class="metric-data">
              <h4>81%</h4>
              <p>ATS Average</p>
            </div>
          </div>
          <div class="card metric-card">
            <div class="metric-icon" style="color: var(--success); background: rgba(16, 185, 129, 0.15);"><i class="fa-solid fa-trophy"></i></div>
            <div class="metric-data">
              <h4>94%</h4>
              <p>Highest Score</p>
            </div>
          </div>
        </div>

        <div class="dashboard-grid">
          <div class="card">
            <h3>Score Progression History</h3>
            <div class="chart-container">
              <div class="chart-bar-wrap"><div class="chart-bar" style="height: 60%;"></div><span class="chart-label">Upload 1</span></div>
              <div class="chart-bar-wrap"><div class="chart-bar" style="height: 72%;"></div><span class="chart-label">Upload 2</span></div>
              <div class="chart-bar-wrap"><div class="chart-bar" style="height: 68%;"></div><span class="chart-label">Upload 3</span></div>
              <div class="chart-bar-wrap"><div class="chart-bar" style="height: 84%;"></div><span class="chart-label">Upload 4</span></div>
              <div class="chart-bar-wrap"><div class="chart-bar" style="height: 94%;"></div><span class="chart-label">Upload 5</span></div>
            </div>
          </div>

          <div class="card">
            <h3>Recent Activity</h3>
            <div class="activity-list">
              <div class="activity-item">
                <div>
                  <strong>Software_Engineer_v2.pdf</strong>
                  <div style="font-size: 0.75rem; color: var(--text-muted);">2 hours ago</div>
                </div>
                <span style="color: var(--success); font-weight: 700;">87%</span>
              </div>
              <div class="activity-item">
                <div>
                  <strong>Frontend_Dev_Resume.pdf</strong>
                  <div style="font-size: 0.75rem; color: var(--text-muted);">Yesterday</div>
                </div>
                <span style="color: var(--warning); font-weight: 700;">74%</span>
              </div>
              <div class="activity-item">
                <div>
                  <strong>Fullstack_Resume_Draft.pdf</strong>
                  <div style="font-size: 0.75rem; color: var(--text-muted);">3 days ago</div>
                </div>
                <span style="color: var(--primary); font-weight: 700;">81%</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 5. RESUME UPLOAD VIEW -->
      <div id="view-upload" class="view-section">
        <h2 style="margin-bottom: 0.5rem;">Upload Resume for Analysis</h2>
        <p style="color: var(--text-muted); margin-bottom: 2rem;">Upload your file and select your targeted role to get tailored ATS insights.</p>

        <div class="card" style="max-width: 700px; margin: 0 auto;">
          <div class="upload-zone" id="dropzone" onclick="document.getElementById('fileInput').click()">
            <i class="fa-solid fa-cloud-arrow-up"></i>
            <h3>Drop Resume Here</h3>
            <p style="color: var(--text-muted); margin: 0.5rem 0;">OR</p>
            <span class="btn btn-secondary">Choose PDF/DOCX</span>
            <input type="file" id="fileInput" hidden accept=".pdf,.docx" onchange="handleFileSelect(this)" />
            <div id="selectedFileName" style="margin-top: 1rem; color: var(--primary); font-weight: 600;"></div>
          </div>

          <div class="form-group">
            <label>Target Role</label>
            <select class="form-control" id="targetRole">
              <option value="Web Developer">Web Developer</option>
              <option value="Java Developer">Java Developer</option>
              <option value="Python Developer">Python Developer</option>
              <option value="AI Engineer">AI Engineer</option>
              <option value="Data Analyst">Data Analyst</option>
            </select>
          </div>

          <button class="btn btn-primary" style="width: 100%; margin-top: 1rem;" onclick="processAnalysis()">
            <i class="fa-solid fa-microchip"></i> Analyze Resume Now
          </button>
        </div>
      </div>

      <!-- 6. ATS RESULT VIEW -->
      <div id="view-result" class="view-section">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
          <h2>ATS Scan Analysis Result</h2>
          <button class="btn btn-secondary" onclick="navigateTo('upload')"><i class="fa-solid fa-rotate-right"></i> Scan Another</button>
        </div>

        <div class="results-layout">
          <div class="card score-box">
            <h3>Overall Score</h3>
            <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 1.5rem;">Target Role: <strong id="resTargetRole" style="color: var(--text);">Web Developer</strong></p>
            
            <div class="gauge-wrapper">
              <div class="gauge-circle">
                <div class="gauge-inner">87%</div>
              </div>
            </div>
            
            <p style="color: var(--success); font-weight: 600;"><i class="fa-solid fa-circle-check"></i> High ATS Pass Chance</p>
          </div>

          <div style="display: flex; flex-direction: column; gap: 1.5rem;">
            <div class="card">
              <h3 style="margin-bottom: 1rem;">Detected Sections</h3>
              <div class="section-checklist">
                <div class="check-item"><i class="fa-solid fa-check"></i> Contact Details</div>
                <div class="check-item"><i class="fa-solid fa-check"></i> Skills</div>
                <div class="check-item"><i class="fa-solid fa-check"></i> Education</div>
                <div class="check-item"><i class="fa-solid fa-check"></i> Experience</div>
                <div class="check-item"><i class="fa-solid fa-check"></i> Projects</div>
                <div class="check-item"><i class="fa-solid fa-check"></i> Certifications</div>
                <div class="check-item"><i class="fa-solid fa-check"></i> Formatting</div>
                <div class="check-item"><i class="fa-solid fa-check"></i> Keywords</div>
              </div>
            </div>

            <div class="card">
              <h3 style="margin-bottom: 1rem;">Actionable Suggestions</h3>
              <div class="suggestions-list">
                <div class="suggestion-card"><i class="fa-solid fa-triangle-exclamation"></i> <div>Add more action verbs (e.g., Architected, Executed, Spearheaded).</div></div>
                <div class="suggestion-card"><i class="fa-solid fa-triangle-exclamation"></i> <div>Include missing framework keyword: <strong>JavaScript</strong>.</div></div>
                <div class="suggestion-card"><i class="fa-solid fa-triangle-exclamation"></i> <div>Improve Summary: Focus on quantifiable past impact.</div></div>
                <div class="suggestion-card"><i class="fa-solid fa-triangle-exclamation"></i> <div>Use standard ATS-friendly fonts like Arial, Calibri, or Helvetica.</div></div>
                <div class="suggestion-card"><i class="fa-solid fa-triangle-exclamation"></i> <div>Add measurable achievements (e.g., "Increased performance by 25%").</div></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 7. RESUME HISTORY VIEW -->
      <div id="view-history" class="view-section">
        <h2 style="margin-bottom: 0.5rem;">Resume Scan History</h2>
        <p style="color: var(--text-muted); margin-bottom: 2rem;">Manage and compare your previous ATS analysis logs.</p>

        <div class="card">
          <div style="display: flex; gap: 1rem; margin-bottom: 1.5rem;">
            <input type="text" class="form-control" placeholder="Search resumes..." style="flex: 1;" id="historySearch" onkeyup="filterHistory()" />
            <select class="form-control" style="width: 180px;" id="historyFilter" onchange="filterHistory()">
              <option value="all">All Scores</option>
              <option value="high">Above 80%</option>
              <option value="low">Below 80%</option>
            </select>
          </div>

          <table class="history-table">
            <thead>
              <tr>
                <th>Date</th>
                <th>Resume File</th>
                <th>ATS Score</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody id="historyTableBody">
              <tr>
                <td>2026-07-28</td>
                <td>Software_Engineer_v2.pdf</td>
                <td><span style="color: var(--success); font-weight: 700;">87%</span></td>
                <td class="table-actions">
                  <button class="btn btn-secondary" style="padding: 0.4rem 0.6rem;" onclick="navigateTo('result')"><i class="fa-solid fa-eye"></i></button>
                  <button class="btn btn-secondary" style="padding: 0.4rem 0.6rem;" onclick="alert('Downloading report...')"><i class="fa-solid fa-download"></i></button>
                  <button class="btn btn-danger" style="padding: 0.4rem 0.6rem;" onclick="this.closest('tr').remove()"><i class="fa-solid fa-trash"></i></button>
                </td>
              </tr>
              <tr>
                <td>2026-07-20</td>
                <td>Frontend_Dev_Resume.pdf</td>
                <td><span style="color: var(--warning); font-weight: 700;">74%</span></td>
                <td class="table-actions">
                  <button class="btn btn-secondary" style="padding: 0.4rem 0.6rem;" onclick="navigateTo('result')"><i class="fa-solid fa-eye"></i></button>
                  <button class="btn btn-secondary" style="padding: 0.4rem 0.6rem;" onclick="alert('Downloading report...')"><i class="fa-solid fa-download"></i></button>
                  <button class="btn btn-danger" style="padding: 0.4rem 0.6rem;" onclick="this.closest('tr').remove()"><i class="fa-solid fa-trash"></i></button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- 8. PROFILE VIEW -->
      <div id="view-profile" class="view-section">
        <h2 style="margin-bottom: 1.5rem;">User Profile</h2>
        <div class="card">
          <div class="profile-header">
            <div class="profile-avatar"><i class="fa-solid fa-user"></i></div>
            <div>
              <h3>Alex Morgan</h3>
              <p style="color: var(--text-muted);">Computer Science Student / Software Developer</p>
            </div>
          </div>

          <form onsubmit="event.preventDefault(); alert('Profile updated successfully!');">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
              <div class="form-group">
                <label>Full Name</label>
                <input type="text" class="form-control" value="Alex Morgan" />
              </div>
              <div class="form-group">
                <label>Email</label>
                <input type="email" class="form-control" value="alex@example.com" />
              </div>
              <div class="form-group">
                <label>Phone</label>
                <input type="text" class="form-control" value="+1 (555) 019-2834" />
              </div>
              <div class="form-group">
                <label>College / University</label>
                <input type="text" class="form-control" value="Stanford University" />
              </div>
            </div>
            <div class="form-group">
              <label>Key Skills (Comma separated)</label>
              <input type="text" class="form-control" value="JavaScript, React, Node.js, HTML5, CSS3, Git" />
            </div>
            <div class="form-group">
              <label>Experience Level</label>
              <input type="text" class="form-control" value="2 Years (Junior / Mid-level)" />
            </div>
            <div class="form-group">
              <label>Bio</label>
              <textarea class="form-control" rows="3">Passionate frontend developer focused on building interactive web applications and learning AI systems.</textarea>
            </div>
            <button type="submit" class="btn btn-primary"><i class="fa-solid fa-floppy-disk"></i> Update Profile</button>
          </form>
        </div>
      </div>

      <!-- 9. SETTINGS VIEW -->
      <div id="view-settings" class="view-section">
        <h2 style="margin-bottom: 1.5rem;">Account Settings</h2>
        <div class="card">
          <div class="settings-list">
            <div class="setting-item">
              <div>
                <strong>Appearance Theme</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted);">Select your preferred visual style</p>
              </div>
              <select class="form-control" style="width: 150px;">
                <option value="dark">Dark Glow</option>
                <option value="light">Light Mode</option>
              </select>
            </div>
            <div class="setting-item">
              <div>
                <strong>Email Notifications</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted);">Receive weekly ATS optimization tips</p>
              </div>
              <input type="checkbox" checked style="accent-color: var(--primary); transform: scale(1.3);" />
            </div>
            <div class="setting-item">
              <div>
                <strong>Language</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted);">Interface language</p>
              </div>
              <select class="form-control" style="width: 150px;">
                <option>English (US)</option>
                <option>Spanish</option>
                <option>French</option>
              </select>
            </div>
            <div class="setting-item">
              <div>
                <strong>Data Privacy</strong>
                <p style="font-size: 0.85rem; color: var(--text-muted);">Allow anonymous file parsing improvements</p>
              </div>
              <input type="checkbox" checked style="accent-color: var(--primary); transform: scale(1.3);" />
            </div>
            <div style="padding-top: 1rem; display: flex; justify-content: space-between;">
              <button class="btn btn-danger" onclick="if(confirm('Are you sure you want to delete your account?')) logout();">Delete Account</button>
              <button class="btn btn-secondary" onclick="logout()">Logout</button>
            </div>
          </div>
        </div>
      </div>

    </main>
  </div>

  <!-- JAVASCRIPT APP ARCHITECTURE -->
  <script>
    // App State Management
    let isAuthenticated = false;

    // View Navigation Engine
    function navigateTo(viewId, anchorId = null) {
      // Handle page view visibility
      document.querySelectorAll('.view-section').forEach(view => {
        view.classList.remove('active');
      });

      const appLayout = document.getElementById('appLayout');
      
      if (['dashboard', 'upload', 'result', 'history', 'profile', 'settings'].includes(viewId)) {
        if (!isAuthenticated) {
          navigateTo('login');
          return;
        }
        appLayout.style.display = 'flex';
        
        // Active state on Sidebar Links
        document.querySelectorAll('.sidebar-link').forEach(link => link.classList.remove('active'));
        const activeSidebar = document.getElementById(`s-${viewId}`);
        if(activeSidebar) activeSidebar.classList.add('active');
      } else {
        appLayout.style.display = 'none';
      }

      const targetView = document.getElementById(`view-${viewId}`);
      if (targetView) targetView.classList.add('active');

      // Scroll to specific section if specified (e.g. Features/About on home page)
      if (anchorId) {
        const anchorTarget = document.getElementById(anchorId);
        if (anchorTarget) anchorTarget.scrollIntoView({ behavior: 'smooth' });
      } else {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    // Auth Simulation
    function handleAuthSuccess() {
      isAuthenticated = true;
      document.getElementById('publicNav').style.display = 'none';
      document.getElementById('privateNav').style.display = 'flex';
      navigateTo('dashboard');
    }

    function logout() {
      isAuthenticated = false;
      document.getElementById('publicNav').style.display = 'flex';
      document.getElementById('privateNav').style.display = 'none';
      navigateTo('home');
    }

    // Drag and Drop Handling
    const dropzone = document.getElementById('dropzone');
    
    ['dragenter', 'dragover'].forEach(eventName => {
      dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropzone.classList.add('dragover');
      }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
      dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropzone.classList.remove('dragover');
      }, false);
    });

    dropzone.addEventListener('drop', (e) => {
      const dt = e.dataTransfer;
      const files = dt.files;
      if (files.length) {
        document.getElementById('fileInput').files = files;
        showFileName(files[0].name);
      }
    });

    function handleFileSelect(input) {
      if (input.files.length) {
        showFileName(input.files[0].name);
      }
    }

    function showFileName(name) {
      document.getElementById('selectedFileName').textContent = `Attached: ${name}`;
    }

    // Resume Processing Simulation
    function processAnalysis() {
      const fileInput = document.getElementById('fileInput');
      const targetRole = document.getElementById('targetRole').value;

      if (!fileInput.files.length && !document.getElementById('selectedFileName').textContent) {
        alert('Please attach a PDF or DOCX resume file first.');
        return;
      }

      // Update target role label in results view
      document.getElementById('resTargetRole').textContent = targetRole;

      // Navigate to results page
      navigateTo('result');
    }

    // Search and Filter History Table
    function filterHistory() {
      const searchVal = document.getElementById('historySearch').value.toLowerCase();
      const filterVal = document.getElementById('historyFilter').value;
      const rows = document.querySelectorAll('#historyTableBody tr');

      rows.forEach(row => {
        const fileName = row.cells[1].textContent.toLowerCase();
        const scoreText = row.cells[2].textContent;
        const score = parseInt(scoreText);

        let matchesSearch = fileName.includes(searchVal);
        let matchesFilter = true;

        if (filterVal === 'high') matchesFilter = score >= 80;
        if (filterVal === 'low') matchesFilter = score < 80;

        if (matchesSearch && matchesFilter) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
