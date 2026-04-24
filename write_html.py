#!/usr/bin/env python3
# ECOTEC — Iron & Acid redesign (Brutalist Industrial)

HTML = """\
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>EcoTecnologias Honduras | Mantenimiento Industrial y Vehicular</title>
  <meta name="description" content="Soluciones profesionales de mantenimiento industrial y vehicular en Honduras. BG Products y CLR PRO MAX. 14 anos de experiencia, 40+ empresas." />
  <meta property="og:title" content="EcoTecnologias Honduras" />
  <meta property="og:description" content="Mas potencia. Menos riesgo. Resultados reales." />
  <meta property="og:image" content="https://images.leadconnectorhq.com/image/f_webp/q_80/r_1200/u_https://assets.cdn.filesafe.space/OaPWc8hFpKfG4cOlk5jf/media/686feaa29f20bf7bd184d5fe.png" />
  <meta property="og:type" content="website" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=IBM+Plex+Mono:wght@400;500;600;700&family=Barlow+Condensed:wght@400;600;700;900&display=swap" rel="stylesheet" />

  <style>
    /* =============================================
       IRON & ACID — ECOTEC BRUTALIST INDUSTRIAL
       ============================================= */

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }

    :root {
      --bg:       #0A0A08;
      --surface:  #121210;
      --surface2: #1A1A17;
      --acid:     #AAFF00;
      --acid-dim: #7ABF00;
      --orange:   #FF5500;
      --white:    #F0EDE6;
      --muted:    #888880;
      --border:   #2A2A26;
      --green:    #009A44;
      --blue:     #1F5FB0;
    }

    body {
      font-family: 'IBM Plex Mono', monospace;
      background: var(--bg);
      color: var(--white);
      line-height: 1.6;
      overflow-x: hidden;
      cursor: crosshair;
    }

    /* Grain overlay */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 9999;
      opacity: 0.035;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
      background-size: 128px 128px;
    }

    a { text-decoration: none; color: inherit; cursor: crosshair; }
    img { max-width: 100%; height: auto; display: block; }

    .container { max-width: 1200px; margin: 0 auto; padding: 0 32px; }

    /* ---- UTILITY ---- */
    .acid { color: var(--acid); }
    .orange { color: var(--orange); }

    /* ---- BUTTONS ---- */
    .btn {
      display: inline-block;
      font-family: 'Bebas Neue', sans-serif;
      font-size: 18px;
      letter-spacing: 3px;
      padding: 14px 36px;
      border: none;
      cursor: crosshair;
      transition: all 0.15s ease;
      position: relative;
      overflow: hidden;
    }
    .btn::after {
      content: '';
      position: absolute;
      inset: 0;
      background: rgba(255,255,255,0.06);
      transform: translateX(-100%);
      transition: transform 0.25s ease;
    }
    .btn:hover::after { transform: translateX(0); }

    .btn-acid {
      background: var(--acid);
      color: #000;
    }
    .btn-acid:hover { background: #CCFF33; transform: translate(-2px,-2px); box-shadow: 4px 4px 0 var(--acid-dim); }

    .btn-ghost {
      background: transparent;
      color: var(--white);
      border: 2px solid var(--white);
    }
    .btn-ghost:hover { border-color: var(--acid); color: var(--acid); transform: translate(-2px,-2px); box-shadow: 4px 4px 0 var(--acid); }

    .btn-orange {
      background: var(--orange);
      color: #fff;
    }
    .btn-orange:hover { background: #FF7722; transform: translate(-2px,-2px); box-shadow: 4px 4px 0 #CC3300; }

    /* ---- SECTION LABELS ---- */
    .label {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 4px;
      text-transform: uppercase;
      color: var(--acid);
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
    }
    .label::before {
      content: '';
      display: block;
      width: 32px;
      height: 2px;
      background: var(--acid);
      flex-shrink: 0;
    }

    .display-title {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(52px, 7vw, 96px);
      line-height: 0.92;
      letter-spacing: 2px;
      color: var(--white);
    }
    .display-title .hl { color: var(--acid); }
    .display-title .hl-o { color: var(--orange); }

    .body-text {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 14px;
      color: var(--muted);
      line-height: 1.8;
      max-width: 520px;
    }

    /* ============== NAVBAR ============== */
    .nav {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 100;
      border-bottom: 1px solid var(--border);
      background: rgba(10,10,8,0.92);
      backdrop-filter: blur(12px);
    }
    .nav-inner {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 64px;
    }
    .nav-logo img { height: 38px; width: auto; filter: brightness(1.1); }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 0;
      list-style: none;
    }
    .nav-links a {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--muted);
      padding: 8px 20px;
      border-left: 1px solid var(--border);
      transition: color 0.2s;
    }
    .nav-links a:hover { color: var(--acid); }
    .nav-links li:first-child a { border-left: none; }
    .nav-cta {
      border-left: 1px solid var(--border);
      padding-left: 24px;
    }
    .hamburger { display: none; background: none; border: 1px solid var(--border); padding: 8px; cursor: crosshair; }
    .hamburger span { display: block; width: 22px; height: 2px; background: var(--white); margin: 4px 0; }

    /* ============== HERO ============== */
    .hero {
      min-height: 100vh;
      display: flex;
      align-items: center;
      position: relative;
      overflow: hidden;
      padding-top: 64px;
    }

    /* Background image */
    .hero-bg {
      position: absolute;
      inset: 0;
      background-image: url(https://images.leadconnectorhq.com/image/f_webp/q_80/r_1200/u_https://assets.cdn.filesafe.space/OaPWc8hFpKfG4cOlk5jf/media/686ffd65ba56d5f5f515bb1a.jpeg);
      background-size: cover;
      background-position: center right;
      opacity: 0.12;
      filter: grayscale(1);
    }

    /* Giant text watermark */
    .hero-watermark {
      position: absolute;
      bottom: -40px;
      left: -20px;
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(180px, 22vw, 320px);
      color: transparent;
      -webkit-text-stroke: 1px rgba(170,255,0,0.07);
      pointer-events: none;
      user-select: none;
      white-space: nowrap;
      line-height: 1;
    }

    /* Diagonal grid lines */
    .hero-grid {
      position: absolute;
      inset: 0;
      pointer-events: none;
      opacity: 0.04;
      background-image:
        repeating-linear-gradient(0deg, var(--acid) 0, var(--acid) 1px, transparent 1px, transparent 80px),
        repeating-linear-gradient(90deg, var(--acid) 0, var(--acid) 1px, transparent 1px, transparent 80px);
    }

    .hero .container {
      position: relative;
      z-index: 2;
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 60px;
      align-items: center;
      padding-top: 80px;
      padding-bottom: 80px;
    }

    .hero-content {}

    .hero-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-family: 'IBM Plex Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 4px;
      text-transform: uppercase;
      color: #000;
      background: var(--acid);
      padding: 6px 14px;
      margin-bottom: 28px;
    }

    .hero-title {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(72px, 10vw, 140px);
      line-height: 0.88;
      letter-spacing: 3px;
      margin-bottom: 32px;
    }
    .hero-title .line { display: block; overflow: hidden; }
    .hero-title .hl { color: var(--acid); }
    .hero-title .hl-o { color: var(--orange); }
    .hero-title .stroke {
      color: transparent;
      -webkit-text-stroke: 2px var(--white);
    }

    .hero-desc {
      font-size: 13px;
      color: var(--muted);
      line-height: 1.9;
      max-width: 440px;
      margin-bottom: 40px;
      border-left: 3px solid var(--acid);
      padding-left: 20px;
    }
    .hero-desc strong { color: var(--white); font-weight: 600; }

    .hero-actions { display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }

    .hero-divider {
      width: 1px;
      height: 80px;
      background: var(--border);
      margin: 0 8px;
    }

    .hero-aside {
      display: flex;
      flex-direction: column;
      gap: 2px;
      align-self: flex-end;
      padding-bottom: 20px;
    }
    .hero-aside-item {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 11px;
      letter-spacing: 2px;
      color: var(--muted);
      text-transform: uppercase;
      writing-mode: vertical-rl;
      transform: rotate(180deg);
    }

    .hero-scroll {
      position: absolute;
      bottom: 40px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
      font-family: 'IBM Plex Mono', monospace;
      font-size: 10px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: var(--muted);
      animation: scrollBounce 2s ease-in-out infinite;
    }
    .hero-scroll::after {
      content: '';
      display: block;
      width: 1px;
      height: 40px;
      background: linear-gradient(to bottom, var(--acid), transparent);
    }

    @keyframes scrollBounce {
      0%, 100% { transform: translateX(-50%) translateY(0); }
      50% { transform: translateX(-50%) translateY(8px); }
    }

    /* ============== STATS ============== */
    .stats {
      position: relative;
      background: var(--surface);
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
      overflow: hidden;
    }
    .stats::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 2px;
      background: linear-gradient(to right, var(--acid), transparent);
    }
    .stats-inner {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
    }
    .stat-item {
      padding: 60px 40px;
      border-right: 1px solid var(--border);
      position: relative;
      overflow: hidden;
      transition: background 0.3s;
    }
    .stat-item:last-child { border-right: none; }
    .stat-item:hover { background: var(--surface2); }
    .stat-item::before {
      content: '';
      position: absolute;
      bottom: 0; left: 0;
      width: 0; height: 2px;
      background: var(--acid);
      transition: width 0.4s ease;
    }
    .stat-item:hover::before { width: 100%; }
    .stat-num {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(64px, 6vw, 96px);
      line-height: 1;
      color: var(--acid);
      display: block;
    }
    .stat-label {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 11px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: var(--muted);
      margin-top: 8px;
      display: block;
    }

    /* ============== BRANDS ============== */
    .brands {
      padding: 120px 0;
      position: relative;
      overflow: hidden;
    }

    /* Diagonal separator top */
    .slash-top {
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 60px;
      background: var(--surface);
      clip-path: polygon(0 0, 100% 0, 100% 0%, 0 100%);
    }

    .brands-header {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: end;
      margin-bottom: 80px;
    }
    .brands-header .body-text { margin-top: 20px; }

    .brands-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2px;
    }

    .bcard {
      background: var(--surface);
      border: 1px solid var(--border);
      position: relative;
      overflow: hidden;
      transition: border-color 0.3s;
    }
    .bcard:hover { border-color: var(--acid); }

    .bcard-top {
      position: relative;
      overflow: hidden;
    }
    .bcard-img {
      width: 100%;
      height: 280px;
      object-fit: cover;
      filter: grayscale(0.4) contrast(1.1);
      transition: filter 0.4s, transform 0.4s;
    }
    .bcard:hover .bcard-img {
      filter: grayscale(0) contrast(1.2);
      transform: scale(1.03);
    }

    /* Overlay diagonal on image */
    .bcard-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(160deg, transparent 40%, rgba(10,10,8,0.9) 100%);
      pointer-events: none;
    }

    .bcard-tag {
      position: absolute;
      top: 20px;
      left: 0;
      font-family: 'IBM Plex Mono', monospace;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 3px;
      text-transform: uppercase;
      padding: 6px 16px;
    }
    .bcard-tag-g { background: var(--acid); color: #000; }
    .bcard-tag-b { background: var(--blue); color: #fff; }

    .bcard-body { padding: 36px; }

    .bcard-title {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 52px;
      line-height: 1;
      letter-spacing: 2px;
      color: var(--white);
      margin-bottom: 16px;
    }
    .bcard-text {
      font-size: 13px;
      color: var(--muted);
      line-height: 1.8;
      margin-bottom: 28px;
    }

    .bcard-list {
      list-style: none;
      margin-bottom: 32px;
      border-top: 1px solid var(--border);
    }
    .bcard-list li {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 12px;
      color: var(--muted);
      padding: 10px 0;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 12px;
      transition: color 0.2s;
    }
    .bcard-list li:hover { color: var(--white); }
    .bcard-list li::before {
      content: '//';
      color: var(--acid);
      font-weight: 700;
      font-size: 10px;
      flex-shrink: 0;
    }

    /* ============== WHY US ============== */
    .why {
      padding: 120px 0;
      background: var(--surface);
      position: relative;
      clip-path: polygon(0 40px, 100% 0, 100% calc(100% - 40px), 0 100%);
      margin: -2px 0;
    }
    .why .container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 80px;
      align-items: center;
    }
    .why-img {
      position: relative;
    }
    .why-img img {
      width: 100%;
      height: 520px;
      object-fit: cover;
      filter: grayscale(0.3) contrast(1.1);
    }
    /* Acid frame on image */
    .why-img::before {
      content: '';
      position: absolute;
      top: -12px; left: -12px;
      right: 12px; bottom: 12px;
      border: 2px solid var(--acid);
      pointer-events: none;
      z-index: 1;
    }
    .why-img::after {
      content: 'ECOTEC';
      position: absolute;
      bottom: 28px;
      right: -8px;
      font-family: 'Bebas Neue', sans-serif;
      font-size: 72px;
      color: transparent;
      -webkit-text-stroke: 1px rgba(170,255,0,0.25);
      pointer-events: none;
    }

    .why-content .display-title { margin-bottom: 24px; }
    .why-content .body-text { margin-bottom: 48px; }

    .feats { display: grid; gap: 0; }
    .feat {
      display: flex;
      gap: 24px;
      padding: 24px 0;
      border-bottom: 1px solid var(--border);
      align-items: flex-start;
      transition: background 0.2s;
    }
    .feat:first-child { border-top: 1px solid var(--border); }
    .feat-num {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 36px;
      color: var(--acid);
      opacity: 0.5;
      line-height: 1;
      flex-shrink: 0;
      width: 48px;
      transition: opacity 0.2s;
    }
    .feat:hover .feat-num { opacity: 1; }
    .feat-title {
      font-family: 'Barlow Condensed', sans-serif;
      font-size: 18px;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--white);
      margin-bottom: 6px;
    }
    .feat-text {
      font-size: 12px;
      color: var(--muted);
      line-height: 1.8;
    }

    /* ============== CERTS ============== */
    .certs {
      padding: 80px 0;
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
      overflow: hidden;
    }
    .certs-inner {
      display: flex;
      align-items: center;
      gap: 0;
      overflow: hidden;
    }
    .certs-label {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 11px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: var(--muted);
      white-space: nowrap;
      padding-right: 48px;
      border-right: 1px solid var(--border);
      flex-shrink: 0;
    }
    .certs-track {
      display: flex;
      gap: 0;
      flex: 1;
      overflow: hidden;
    }
    .cert-badge {
      flex-shrink: 0;
      padding: 0 48px;
      border-right: 1px solid var(--border);
      text-align: center;
    }
    .cert-name {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 42px;
      letter-spacing: 2px;
      color: var(--white);
      transition: color 0.2s;
      display: block;
    }
    .cert-badge:hover .cert-name { color: var(--acid); }
    .cert-sub {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 10px;
      letter-spacing: 2px;
      color: var(--muted);
      text-transform: uppercase;
      display: block;
      margin-top: 4px;
    }

    /* ============== CONTACT ============== */
    .contact {
      padding: 120px 0;
      background: var(--bg);
    }
    .contact .container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 80px;
    }
    .contact-info .display-title { margin-bottom: 24px; }
    .contact-info .body-text { margin-bottom: 48px; }

    .contact-list { list-style: none; margin-bottom: 48px; }
    .contact-list li {
      display: flex;
      align-items: flex-start;
      gap: 20px;
      padding: 20px 0;
      border-bottom: 1px solid var(--border);
    }
    .c-code {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 10px;
      letter-spacing: 2px;
      color: var(--acid);
      text-transform: uppercase;
      flex-shrink: 0;
      width: 60px;
      padding-top: 2px;
    }
    .c-label {
      font-size: 11px;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--muted);
      display: block;
      margin-bottom: 4px;
    }
    .c-value {
      font-size: 14px;
      color: var(--white);
      font-weight: 500;
    }
    .c-value a { color: var(--white); transition: color 0.2s; }
    .c-value a:hover { color: var(--acid); }

    /* Contact Form */
    .cform {
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 48px;
      position: relative;
    }
    .cform::before {
      content: '';
      position: absolute;
      top: 0; left: 0;
      right: 0; height: 3px;
      background: linear-gradient(to right, var(--acid), var(--orange));
    }
    .cform-title {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 36px;
      letter-spacing: 2px;
      color: var(--white);
      margin-bottom: 6px;
    }
    .cform-sub {
      font-size: 12px;
      color: var(--muted);
      margin-bottom: 36px;
      letter-spacing: 1px;
    }

    .fg { margin-bottom: 20px; }
    .fg label {
      display: block;
      font-family: 'IBM Plex Mono', monospace;
      font-size: 10px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 8px;
    }
    .fg input, .fg select, .fg textarea {
      width: 100%;
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--white);
      font-family: 'IBM Plex Mono', monospace;
      font-size: 14px;
      padding: 14px 16px;
      outline: none;
      transition: border-color 0.2s;
    }
    .fg input:focus, .fg select:focus, .fg textarea:focus {
      border-color: var(--acid);
    }
    .fg input::placeholder, .fg textarea::placeholder { color: var(--muted); }
    .fg select { appearance: none; cursor: crosshair; }
    .fg select option { background: var(--bg); }
    .fg textarea { resize: vertical; min-height: 100px; }
    .frow { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    .fsub {
      width: 100%;
      padding: 16px;
      margin-top: 8px;
      font-size: 16px;
      letter-spacing: 4px;
    }

    /* ============== FOOTER ============== */
    .footer {
      background: var(--surface);
      border-top: 1px solid var(--border);
      padding: 80px 0 40px;
      position: relative;
    }
    .footer::before {
      content: '';
      position: absolute;
      top: 0; left: 0;
      right: 0; height: 2px;
      background: linear-gradient(to right, var(--acid), transparent);
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 60px;
      padding-bottom: 60px;
      border-bottom: 1px solid var(--border);
      margin-bottom: 40px;
    }
    .footer-logo img { height: 36px; margin-bottom: 20px; }
    .footer-desc {
      font-size: 12px;
      color: var(--muted);
      line-height: 1.9;
      max-width: 280px;
    }
    .fcol h4 {
      font-family: 'IBM Plex Mono', monospace;
      font-size: 10px;
      letter-spacing: 4px;
      text-transform: uppercase;
      color: var(--acid);
      margin-bottom: 24px;
    }
    .flinks { list-style: none; display: grid; gap: 12px; }
    .flinks a {
      font-size: 13px;
      color: var(--muted);
      transition: color 0.2s;
    }
    .flinks a:hover { color: var(--acid); }
    .fbot {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11px;
      color: var(--muted);
      letter-spacing: 1px;
      flex-wrap: wrap;
      gap: 12px;
    }

    /* Big watermark in footer */
    .footer-wm {
      font-family: 'Bebas Neue', sans-serif;
      font-size: clamp(80px, 12vw, 180px);
      color: transparent;
      -webkit-text-stroke: 1px rgba(170,255,0,0.06);
      pointer-events: none;
      user-select: none;
      text-align: center;
      line-height: 1;
      margin-bottom: -20px;
    }

    /* ============== WHATSAPP FLOAT ============== */
    .wa {
      position: fixed;
      bottom: 32px;
      right: 32px;
      z-index: 998;
      background: #25D366;
      width: 56px;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 2px solid rgba(255,255,255,0.2);
      box-shadow: 0 8px 32px rgba(37,211,102,0.4);
      transition: transform 0.2s, box-shadow 0.2s;
      cursor: crosshair;
    }
    .wa:hover {
      transform: scale(1.1) rotate(-5deg);
      box-shadow: 0 12px 40px rgba(37,211,102,0.6);
    }

    /* ============== ANIMATIONS ============== */
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(30px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .fade-up { opacity: 0; animation: fadeUp 0.7s ease forwards; }
    .fade-up:nth-child(1) { animation-delay: 0.1s; }
    .fade-up:nth-child(2) { animation-delay: 0.25s; }
    .fade-up:nth-child(3) { animation-delay: 0.4s; }
    .fade-up:nth-child(4) { animation-delay: 0.55s; }

    /* ============== TICKER BAND ============== */
    .ticker {
      background: var(--acid);
      overflow: hidden;
      white-space: nowrap;
      padding: 10px 0;
    }
    .ticker-inner {
      display: inline-flex;
      animation: ticker 18s linear infinite;
      gap: 0;
    }
    .ticker-item {
      font-family: 'Bebas Neue', sans-serif;
      font-size: 16px;
      letter-spacing: 4px;
      color: #000;
      padding: 0 40px;
      flex-shrink: 0;
    }
    .ticker-item::after {
      content: '//';
      margin-left: 40px;
      opacity: 0.4;
    }
    @keyframes ticker {
      from { transform: translateX(0); }
      to { transform: translateX(-50%); }
    }

    /* ============== RESPONSIVE ============== */
    @media (max-width: 1024px) {
      .hero .container { grid-template-columns: 1fr; }
      .hero-aside { display: none; }
      .stats-inner { grid-template-columns: repeat(2,1fr); }
      .brands-header { grid-template-columns: 1fr; }
      .brands-grid { grid-template-columns: 1fr; }
      .why .container { grid-template-columns: 1fr; }
      .contact .container { grid-template-columns: 1fr; }
      .footer-grid { grid-template-columns: 1fr 1fr; }
    }
    @media (max-width: 768px) {
      .nav-links, .nav-cta { display: none; }
      .hamburger { display: block; }
      .stats-inner { grid-template-columns: repeat(2,1fr); }
      .stat-item { padding: 40px 24px; }
      .certs-inner { flex-direction: column; align-items: flex-start; gap: 32px; }
      .certs-label { border-right: none; padding-right: 0; }
      .certs-track { flex-wrap: wrap; gap: 24px; }
      .cert-badge { border-right: none; padding: 0; }
      .footer-grid { grid-template-columns: 1fr; gap: 40px; }
      .cform { padding: 32px 24px; }
      .frow { grid-template-columns: 1fr; }
    }
    @media (max-width: 480px) {
      .stats-inner { grid-template-columns: 1fr 1fr; }
      .brands-header { gap: 32px; }
    }
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <nav class="nav">
    <div class="container nav-inner">
      <a href="#" class="nav-logo">
        <img src="https://images.leadconnectorhq.com/image/f_webp/q_80/r_1200/u_https://assets.cdn.filesafe.space/OaPWc8hFpKfG4cOlk5jf/media/686fe16b4e04f85d56a49abd.svg" alt="EcoTecnologias Honduras" />
      </a>
      <ul class="nav-links">
        <li><a href="#marcas">Marcas</a></li>
        <li><a href="#nosotros">Quienes somos</a></li>
        <li><a href="#bg-products">BG Products</a></li>
        <li><a href="#clr">CLR PRO MAX</a></li>
      </ul>
      <div class="nav-cta">
        <a href="https://wa.me/50494476370" target="_blank" rel="noopener" class="btn btn-acid">Escribenos</a>
      </div>
      <button class="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </nav>

  <!-- HERO -->
  <section class="hero">
    <div class="hero-bg"></div>
    <div class="hero-grid"></div>
    <div class="hero-watermark">ECOTEC</div>

    <div class="container">
      <div class="hero-content">
        <div class="hero-eyebrow fade-up">&#9646; 14 Anos en Honduras &#9646; +504 9447-6370</div>
        <h1 class="hero-title fade-up">
          <span class="line">MAS</span>
          <span class="line hl">POTENCIA.</span>
          <span class="line">MENOS</span>
          <span class="line hl-o">RIESGO.</span>
          <span class="line stroke">RESULTADOS</span>
          <span class="line hl">REALES.</span>
        </h1>
        <p class="hero-desc fade-up">
          Distribuidores oficiales de <strong>BG Products&reg;</strong> y <strong>CLR PRO MAX&reg;</strong> en Honduras.
          Mas de 14 anos entregando tecnologia internacional con soporte tecnico local a mas de <strong>40 empresas</strong>.
        </p>
        <div class="hero-actions fade-up">
          <a href="#contacto" class="btn btn-acid">Solicitar asesoria</a>
          <div class="hero-divider"></div>
          <a href="#marcas" class="btn btn-ghost">Ver marcas</a>
        </div>
      </div>
      <div class="hero-aside">
        <span class="hero-aside-item">BG Products&reg;</span>
        <span class="hero-aside-item">CLR PRO MAX&reg;</span>
        <span class="hero-aside-item">Honduras</span>
      </div>
    </div>

    <div class="hero-scroll">Scroll</div>
  </section>

  <!-- TICKER -->
  <div class="ticker">
    <div class="ticker-inner">
      <span class="ticker-item">BG Products</span>
      <span class="ticker-item">CLR PRO MAX</span>
      <span class="ticker-item">Mantenimiento vehicular</span>
      <span class="ticker-item">Limpieza industrial</span>
      <span class="ticker-item">Honduras</span>
      <span class="ticker-item">14 anos de experiencia</span>
      <span class="ticker-item">NSF Certificado</span>
      <span class="ticker-item">EPA Safer Choice</span>
      <span class="ticker-item">ISO Certificado</span>
      <span class="ticker-item">BG Products</span>
      <span class="ticker-item">CLR PRO MAX</span>
      <span class="ticker-item">Mantenimiento vehicular</span>
      <span class="ticker-item">Limpieza industrial</span>
      <span class="ticker-item">Honduras</span>
      <span class="ticker-item">14 anos de experiencia</span>
      <span class="ticker-item">NSF Certificado</span>
      <span class="ticker-item">EPA Safer Choice</span>
      <span class="ticker-item">ISO Certificado</span>
    </div>
  </div>

  <!-- STATS -->
  <div class="stats">
    <div class="stats-inner">
      <div class="stat-item">
        <span class="stat-num" data-count="14">0</span>
        <span class="stat-label">Anos de experiencia</span>
      </div>
      <div class="stat-item">
        <span class="stat-num" data-count="40">0</span>
        <span class="stat-label">Empresas atendidas</span>
      </div>
      <div class="stat-item">
        <span class="stat-num" data-count="2">0</span>
        <span class="stat-label">Lineas especializadas</span>
      </div>
      <div class="stat-item">
        <span class="stat-num" data-count="50">0</span>
        <span class="stat-label">Anos combinados de industria</span>
      </div>
    </div>
  </div>

  <!-- BRANDS -->
  <section class="brands" id="marcas">
    <div class="container">
      <div class="brands-header">
        <div>
          <div class="label">Nuestras marcas</div>
          <h2 class="display-title">
            TECNOLOGIA<br/>
            INTER<span class="hl">NACIONAL.</span><br/>
            <span class="hl-o">RESPALDO</span><br/>
            LOCAL.
          </h2>
        </div>
        <div>
          <p class="body-text">
            En ECOTEC no vendemos productos. Entregamos soluciones respaldadas
            por las marcas mas certificadas del mercado internacional, con soporte
            tecnico directo en Honduras.
          </p>
        </div>
      </div>

      <div class="brands-grid">

        <!-- BG Products -->
        <div class="bcard" id="bg-products">
          <div class="bcard-top">
            <img class="bcard-img"
              src="https://images.leadconnectorhq.com/image/f_webp/q_80/r_1200/u_https://assets.cdn.filesafe.space/OaPWc8hFpKfG4cOlk5jf/media/6870220c82ba630cff8aaa9f.png"
              alt="BG Products vehicular" />
            <div class="bcard-overlay"></div>
            <span class="bcard-tag bcard-tag-g">// Vehicular</span>
          </div>
          <div class="bcard-body">
            <h3 class="bcard-title">BG Products&reg;</h3>
            <p class="bcard-text">
              Soluciones profesionales para prolongar la vida util de motores,
              transmisiones, sistemas de combustible y direccion hidraulica.
            </p>
            <ul class="bcard-list">
              <li>Mantenimiento de motor y vida util</li>
              <li>Sistemas de transmision y diferencial</li>
              <li>Limpieza de sistema de combustible</li>
              <li>Direccion hidraulica y frenos</li>
              <li>Talleres, flotas y concesionarias</li>
            </ul>
            <a href="#contacto" class="btn btn-acid">Solicitar asesoria BG &rarr;</a>
          </div>
        </div>

        <!-- CLR PRO MAX -->
        <div class="bcard" id="clr">
          <div class="bcard-top">
            <img class="bcard-img"
              src="https://images.leadconnectorhq.com/image/f_webp/q_80/r_1200/u_https://assets.cdn.filesafe.space/OaPWc8hFpKfG4cOlk5jf/media/685053e3abc3e06ddb61a7a4.jpeg"
              alt="CLR PRO MAX industrial" />
            <div class="bcard-overlay"></div>
            <span class="bcard-tag bcard-tag-b">// Industrial</span>
          </div>
          <div class="bcard-body">
            <h3 class="bcard-title">CLR PRO MAX&reg;</h3>
            <p class="bcard-text">
              Desengrasantes y descalcificadores de alto impacto: biodegradables,
              sin solventes ni acidos. Para entornos industriales de alta exigencia.
            </p>
            <ul class="bcard-list">
              <li>Cocinas industriales y equipos</li>
              <li>Plantas de produccion y manufactura</li>
              <li>Calderas, hornos y sistemas hidraulicos</li>
              <li>Drenajes y sistemas sanitarios</li>
              <li>100% biodegradable, sin acidos</li>
            </ul>
            <a href="#contacto" class="btn btn-orange">Solicitar asesoria CLR &rarr;</a>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- WHY US -->
  <section class="why" id="nosotros">
    <div class="container">
      <div class="why-img">
        <img
          src="https://images.leadconnectorhq.com/image/f_webp/q_80/r_1200/u_https://assets.cdn.filesafe.space/OaPWc8hFpKfG4cOlk5jf/media/6872865a748b51aecc691802.png"
          alt="Por que elegirnos"
        />
      </div>
      <div class="why-content">
        <div class="label">Por que elegirnos</div>
        <h2 class="display-title">
          NO SOLO<br/>
          <span class="hl">VENDEMOS.</span><br/>
          ENTRE<span class="hl-o">GAMOS</span><br/>
          SOLUCIONES.
        </h2>
        <p class="body-text">
          Mas de 14 anos sirviendo a talleres, plantas industriales y
          profesionales en toda Honduras. Tecnologia de clase mundial
          con respaldo tecnico local.
        </p>
        <div class="feats">
          <div class="feat">
            <span class="feat-num">01</span>
            <div>
              <div class="feat-title">Certificaciones internacionales</div>
              <p class="feat-text">NSF, EPA Safer Choice e ISO. Los mas altos estandares globales de seguridad y medioambiente.</p>
            </div>
          </div>
          <div class="feat">
            <span class="feat-num">02</span>
            <div>
              <div class="feat-title">Soporte tecnico personalizado</div>
              <p class="feat-text">Asesoramos en seleccion, aplicacion y seguimiento garantizando resultados medibles.</p>
            </div>
          </div>
          <div class="feat">
            <span class="feat-num">03</span>
            <div>
              <div class="feat-title">Productos seguros y sostenibles</div>
              <p class="feat-text">Formulaciones biodegradables y ambientalmente responsables que cuidan tu operacion.</p>
            </div>
          </div>
          <div class="feat">
            <span class="feat-num">04</span>
            <div>
              <div class="feat-title">Respaldo local en Honduras</div>
              <p class="feat-text">Tecnologia de clase mundial con presencia y respuesta local cuando la necesitas.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CERTIFICATIONS -->
  <section class="certs">
    <div class="container">
      <div class="certs-inner">
        <div class="certs-label">Avalados por</div>
        <div class="certs-track">
          <div class="cert-badge"><span class="cert-name">NSF</span><span class="cert-sub">Food Safety</span></div>
          <div class="cert-badge"><span class="cert-name">EPA</span><span class="cert-sub">Safer Choice</span></div>
          <div class="cert-badge"><span class="cert-name">ISO</span><span class="cert-sub">International</span></div>
          <div class="cert-badge"><span class="cert-name">BG</span><span class="cert-sub">Products&reg;</span></div>
          <div class="cert-badge"><span class="cert-name">CLR</span><span class="cert-sub">PRO MAX&reg;</span></div>
        </div>
      </div>
    </div>
  </section>

  <!-- CONTACT -->
  <section class="contact" id="contacto">
    <div class="container">
      <div class="contact-info">
        <div class="label">Contactenos</div>
        <h2 class="display-title">
          LISTO PARA<br/>
          <span class="hl">MEJORAR</span><br/>
          TU OPERA<span class="hl-o">CION</span>?
        </h2>
        <p class="body-text">
          Cuentanos tu necesidad y un asesor especializado
          te contactara con la solucion mas adecuada.
        </p>
        <ul class="contact-list">
          <li>
            <span class="c-code">TEL</span>
            <div>
              <span class="c-label">Telefonos directos</span>
              <span class="c-value">
                <a href="tel:+50494476370">+504 9447-6370</a> &nbsp;/&nbsp;
                <a href="tel:+50488004403">+504 8800-4403</a>
              </span>
            </div>
          </li>
          <li>
            <span class="c-code">EMAIL</span>
            <div>
              <span class="c-label">Correo electronico</span>
              <span class="c-value">
                <a href="mailto:ventas@ecotecnologiashonduras.com">ventas@ecotecnologiashonduras.com</a>
              </span>
            </div>
          </li>
          <li>
            <span class="c-code">WA</span>
            <div>
              <span class="c-label">WhatsApp</span>
              <span class="c-value">
                <a href="https://wa.me/50494476370" target="_blank" rel="noopener">Escribenos aqui &rarr;</a>
              </span>
            </div>
          </li>
          <li>
            <span class="c-code">WEB</span>
            <div>
              <span class="c-label">Sitio web</span>
              <span class="c-value">
                <a href="https://ecotecnologiashonduras.com" target="_blank">www.ecotecnologiashonduras.com</a>
              </span>
            </div>
          </li>
        </ul>
        <a href="https://wa.me/50494476370" target="_blank" class="btn btn-acid">
          Contactar por WhatsApp &rarr;
        </a>
      </div>

      <div class="cform">
        <h3 class="cform-title">Solicitar asesoria</h3>
        <p class="cform-sub">// Respuesta en menos de 24 horas</p>
        <form action="#" method="POST">
          <div class="frow">
            <div class="fg">
              <label>Nombre *</label>
              <input type="text" name="nombre" placeholder="Tu nombre" required />
            </div>
            <div class="fg">
              <label>Empresa</label>
              <input type="text" name="empresa" placeholder="Tu empresa" />
            </div>
          </div>
          <div class="fg">
            <label>Telefono / WhatsApp *</label>
            <input type="tel" name="telefono" placeholder="+504 XXXX-XXXX" required />
          </div>
          <div class="fg">
            <label>Correo electronico</label>
            <input type="email" name="email" placeholder="tu@correo.com" />
          </div>
          <div class="fg">
            <label>Producto de interes</label>
            <select name="interes">
              <option value="">-- Selecciona --</option>
              <option value="bg">BG Products&reg; &mdash; Vehicular</option>
              <option value="clr">CLR PRO MAX&reg; &mdash; Industrial</option>
              <option value="ambos">Ambas lineas</option>
              <option value="otro">Otro</option>
            </select>
          </div>
          <div class="fg">
            <label>Mensaje</label>
            <textarea name="mensaje" placeholder="Describe tu necesidad..."></textarea>
          </div>
          <button type="submit" class="btn btn-acid fsub">
            Enviar solicitud &rarr;
          </button>
        </form>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="footer">
    <div class="footer-wm">ECOTEC</div>
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-logo">
            <img src="https://images.leadconnectorhq.com/image/f_webp/q_80/r_1200/u_https://assets.cdn.filesafe.space/OaPWc8hFpKfG4cOlk5jf/media/686fe16b4e04f85d56a49abd.svg" alt="EcoTecnologias Honduras" />
          </div>
          <p class="footer-desc">
            Soluciones de mantenimiento industrial y vehicular en Honduras.
            14 anos de experiencia con tecnologia internacional y respaldo local.
          </p>
        </div>
        <div class="fcol">
          <h4>Productos</h4>
          <ul class="flinks">
            <li><a href="#bg-products">BG Products Vehicular</a></li>
            <li><a href="#clr">CLR PRO MAX Industrial</a></li>
            <li><a href="#marcas">Ver todas las marcas</a></li>
          </ul>
        </div>
        <div class="fcol">
          <h4>Empresa</h4>
          <ul class="flinks">
            <li><a href="#nosotros">Quienes somos</a></li>
            <li><a href="#contacto">Contacto</a></li>
            <li><a href="https://wa.me/50494476370" target="_blank">WhatsApp</a></li>
            <li><a href="mailto:ventas@ecotecnologiashonduras.com">Correo</a></li>
          </ul>
        </div>
      </div>
      <div class="fbot">
        <span>&copy; 2025 EcoTecnologias Honduras. Todos los derechos reservados.</span>
        <span>
          <a href="tel:+50494476370">+504 9447-6370</a>
          &nbsp;&middot;&nbsp;
          <a href="mailto:ventas@ecotecnologiashonduras.com">ventas@ecotecnologiashonduras.com</a>
        </span>
      </div>
    </div>
  </footer>

  <!-- WhatsApp Float -->
  <a class="wa" href="https://wa.me/50494476370" target="_blank" rel="noopener" aria-label="WhatsApp">
    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="#fff">
      <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
    </svg>
  </a>

  <script>
    // Counter animation
    const counters = document.querySelectorAll('.stat-num[data-count]');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-count'));
          const suffix = target >= 40 ? '+' : (target === 2 ? '' : '+');
          let current = 0;
          const step = Math.ceil(target / 40);
          const timer = setInterval(() => {
            current = Math.min(current + step, target);
            el.textContent = current + suffix;
            if (current >= target) clearInterval(timer);
          }, 35);
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(c => observer.observe(c));

    // Hamburger (basic toggle)
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    hamburger && hamburger.addEventListener('click', () => {
      navLinks && navLinks.classList.toggle('open');
    });
  </script>
</body>
</html>
"""

with open("C:/Users/Usuario fixer/Downloads/ecotec-page/index.html", "w", encoding="utf-8") as f:
    f.write(HTML)
print("Written:", len(HTML), "bytes")
