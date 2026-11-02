"""
UI Theme and Modern Design System for AI VisionDesk Platform
Provides sleek enterprise glassmorphism styling, modern typography, responsive cards,
and visual status indicators while preserving Streamlit's native theme.
"""
import streamlit as st


def inject_custom_css():
    """Injects high-end, theme-adaptive CSS styles for enterprise visual aesthetics."""
    st.markdown("""
<style>
/* ─── Google Fonts Import ─── */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ─── Typography & Base Resets ─── */
html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    letter-spacing: -0.01em;
}

code, pre, [data-testid="stCodeBlock"] {
    font-family: 'JetBrains Mono', monospace !important;
}

/* ─── Top Main Layout Spacing ─── */
.main .block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3.5rem !important;
    max-width: 1320px !important;
}

/* ─── Modern Scrollbar ─── */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: transparent;
}
::-webkit-scrollbar-thumb {
    background: rgba(150, 150, 150, 0.25);
    border-radius: 999px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(150, 150, 150, 0.45);
}

/* ─── Sidebar Aesthetics ─── */
section[data-testid="stSidebar"] {
    border-right: 1px solid rgba(128, 128, 128, 0.15);
    background-color: var(--secondary-background-color);
}

/* Sidebar brand container */
.vd-sidebar-brand {
    padding: 1rem 0.5rem 1.25rem 0.5rem;
    margin-bottom: 0.75rem;
    border-bottom: 1px solid rgba(128, 128, 128, 0.15);
}

.vd-brand-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.15), rgba(217, 119, 6, 0.08));
    border: 1px solid rgba(245, 158, 11, 0.3);
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 700;
    color: #F59E0B;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.vd-brand-title {
    font-size: 1.15rem;
    font-weight: 800;
    line-height: 1.3;
    margin: 0 0 4px 0;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, var(--text-color) 0%, rgba(150, 150, 150, 0.9) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.vd-brand-sub {
    font-size: 0.78rem;
    opacity: 0.75;
    margin: 0;
}

/* Radio Navigation in Sidebar */
section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 6px;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: rgba(128, 128, 128, 0.05);
    border: 1px solid rgba(128, 128, 128, 0.12);
    border-radius: 10px;
    padding: 8px 14px;
    margin-bottom: 4px;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: pointer;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: rgba(245, 158, 11, 0.08);
    border-color: rgba(245, 158, 11, 0.35);
    transform: translateX(3px);
}

section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"],
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.18), rgba(217, 119, 6, 0.1)) !important;
    border-color: #F59E0B !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 12px rgba(245, 158, 11, 0.15);
}

/* Telemetry Card in Sidebar */
.vd-telemetry-card {
    background: rgba(128, 128, 128, 0.06);
    border: 1px solid rgba(128, 128, 128, 0.15);
    border-radius: 12px;
    padding: 12px 14px;
    margin-top: 1rem;
}

.vd-telemetry-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    opacity: 0.7;
    margin-bottom: 10px;
}

.vd-telemetry-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 6px 0;
    font-size: 0.8rem;
    border-bottom: 1px dashed rgba(128, 128, 128, 0.12);
}

.vd-telemetry-row:last-child {
    border-bottom: none;
    padding-bottom: 0;
}

.vd-pulse-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-right: 6px;
    animation: vdPulse 2s infinite ease-in-out;
}

.vd-pulse-green {
    background-color: #10B981;
    box-shadow: 0 0 8px #10B981;
}

.vd-pulse-amber {
    background-color: #F59E0B;
    box-shadow: 0 0 8px #F59E0B;
}

.vd-pulse-red {
    background-color: #EF4444;
    box-shadow: 0 0 8px #EF4444;
}

@keyframes vdPulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.55; transform: scale(1.15); }
}

/* ─── Hero / Header Banner ─── */
.vd-hero-banner {
    position: relative;
    overflow: hidden;
    background: linear-gradient(135deg, rgba(245, 158, 11, 0.08) 0%, rgba(128, 128, 128, 0.04) 50%, rgba(245, 158, 11, 0.03) 100%);
    border: 1px solid rgba(245, 158, 11, 0.22);
    border-radius: 16px;
    padding: 1.75rem 2rem;
    margin-bottom: 1.75rem;
    backdrop-filter: blur(8px);
    box-shadow: 0 8px 30px -10px rgba(0, 0, 0, 0.06);
}

.vd-hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(245, 158, 11, 0.12);
    border: 1px solid rgba(245, 158, 11, 0.28);
    color: #F59E0B;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 0.74rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 10px;
}

.vd-hero-title {
    font-size: 1.95rem;
    font-weight: 800;
    line-height: 1.25;
    margin: 0 0 8px 0;
    letter-spacing: -0.025em;
}

.vd-hero-subtitle {
    font-size: 0.98rem;
    opacity: 0.82;
    margin: 0 0 14px 0;
    max-width: 860px;
    line-height: 1.5;
}

.vd-tags-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.vd-tag-chip {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: rgba(128, 128, 128, 0.08);
    border: 1px solid rgba(128, 128, 128, 0.16);
    border-radius: 8px;
    padding: 3px 10px;
    font-size: 0.75rem;
    font-weight: 600;
    opacity: 0.85;
}

/* ─── Metric Cards Styling ─── */
div[data-testid="stMetric"] {
    background-color: var(--secondary-background-color) !important;
    border: 1px solid rgba(128, 128, 128, 0.16) !important;
    border-radius: 14px !important;
    padding: 16px 20px !important;
    box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.05) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease !important;
    position: relative;
    overflow: hidden;
}

div[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #F59E0B, #EF4444);
    opacity: 0.8;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px -4px rgba(0, 0, 0, 0.1) !important;
    border-color: rgba(245, 158, 11, 0.35) !important;
}

div[data-testid="stMetric"] [data-testid="stMetricLabel"] {
    font-size: 0.8rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
    opacity: 0.75 !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    font-size: 1.85rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.02em !important;
}

/* ─── Buttons Enhancement ─── */
.stButton > button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    letter-spacing: 0.01em !important;
    padding: 0.55rem 1.25rem !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    border: 1px solid rgba(128, 128, 128, 0.2) !important;
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
    color: #ffffff !important;
    border: none !important;
    box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35) !important;
}

.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #D97706 0%, #B45309 100%) !important;
    box-shadow: 0 6px 20px rgba(245, 158, 11, 0.45) !important;
    transform: translateY(-1.5px);
}

.stButton > button[kind="primary"]:active {
    transform: translateY(0);
}

/* Download Buttons */
.stDownloadButton > button {
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.55rem 1.25rem !important;
    transition: all 0.2s ease !important;
}

/* ─── File Uploader ─── */
div[data-testid="stFileUploader"] {
    border-radius: 14px !important;
}

div[data-testid="stFileUploader"] section {
    border: 2px dashed rgba(245, 158, 11, 0.35) !important;
    border-radius: 14px !important;
    background: rgba(128, 128, 128, 0.03) !important;
    padding: 1.5rem 1rem !important;
    transition: all 0.25s ease !important;
}

div[data-testid="stFileUploader"] section:hover {
    border-color: #F59E0B !important;
    background: rgba(245, 158, 11, 0.04) !important;
}

/* ─── Expanders ─── */
div[data-testid="stExpander"] {
    border: 1px solid rgba(128, 128, 128, 0.16) !important;
    border-radius: 12px !important;
    background: var(--secondary-background-color) !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03) !important;
    margin-top: 0.75rem !important;
    overflow: hidden !important;
}

div[data-testid="stExpander"] summary {
    font-weight: 600 !important;
    padding: 0.75rem 1rem !important;
}

/* ─── Inputs & Sliders ─── */
input[type="text"], textarea, div[data-baseweb="input"] {
    border-radius: 10px !important;
    transition: border-color 0.2s ease !important;
}

/* ─── Beautiful Card Containers ─── */
.vd-glass-card {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.16);
    border-radius: 14px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1.25rem;
    box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.04);
}

.vd-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.75rem;
    font-weight: 700;
    font-size: 1rem;
}

/* ─── Compliance / Violation Banners ─── */
.vd-banner-compliant {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.14) 0%, rgba(5, 150, 105, 0.06) 100%);
    border: 1.5px solid rgba(16, 185, 129, 0.4);
    border-radius: 14px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1.25rem;
    display: flex;
    align-items: flex-start;
    gap: 14px;
    box-shadow: 0 8px 24px -4px rgba(16, 185, 129, 0.12);
}

.vd-banner-violation {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.14) 0%, rgba(220, 38, 38, 0.06) 100%);
    border: 1.5px solid rgba(239, 68, 68, 0.4);
    border-radius: 14px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1.25rem;
    display: flex;
    align-items: flex-start;
    gap: 14px;
    box-shadow: 0 8px 24px -4px rgba(239, 68, 68, 0.12);
}

.vd-banner-icon {
    font-size: 1.75rem;
    line-height: 1;
}

.vd-banner-title {
    font-size: 1.05rem;
    font-weight: 800;
    margin: 0 0 4px 0;
    letter-spacing: -0.01em;
}

.vd-banner-text {
    font-size: 0.88rem;
    margin: 0;
    opacity: 0.88;
    line-height: 1.45;
}

.vd-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 0.78rem;
    font-weight: 700;
    margin: 3px 4px 3px 0;
}

.vd-chip-violation {
    background: rgba(239, 68, 68, 0.15);
    border: 1px solid rgba(239, 68, 68, 0.35);
    color: #EF4444;
}

.vd-chip-ok {
    background: rgba(16, 185, 129, 0.15);
    border: 1px solid rgba(16, 185, 129, 0.35);
    color: #10B981;
}

.vd-chip-neutral {
    background: rgba(128, 128, 128, 0.1);
    border: 1px solid rgba(128, 128, 128, 0.2);
    color: var(--text-color);
}

/* ─── Workflow Step Badges ─── */
.vd-workflow-flow {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    margin: 10px 0;
}

.vd-step-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(245, 158, 11, 0.12);
    border: 1px solid rgba(245, 158, 11, 0.3);
    color: #F59E0B;
    border-radius: 8px;
    padding: 4px 10px;
    font-size: 0.78rem;
    font-weight: 700;
}

.vd-step-arrow {
    opacity: 0.5;
    font-size: 0.85rem;
}

/* ─── Feature Card for Home ─── */
.vd-feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
    margin-bottom: 1.5rem;
}

.vd-feature-card {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.15);
    border-radius: 14px;
    padding: 1.25rem;
    transition: all 0.25s ease;
    display: flex;
    flex-direction: column;
}

.vd-feature-card:hover {
    border-color: rgba(245, 158, 11, 0.35);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.08);
}

.vd-feature-icon {
    font-size: 1.75rem;
    margin-bottom: 10px;
}

.vd-feature-title {
    font-size: 1rem;
    font-weight: 700;
    margin: 0 0 6px 0;
}

.vd-feature-desc {
    font-size: 0.84rem;
    opacity: 0.8;
    margin: 0;
    line-height: 1.45;
    flex-grow: 1;
}

/* ─── Search Result Card ─── */
.vd-search-card {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.15);
    border-left: 3px solid #F59E0B;
    border-radius: 10px;
    padding: 14px 18px;
    margin-bottom: 12px;
    transition: transform 0.15s ease;
}

.vd-search-card:hover {
    transform: translateX(2px);
    border-color: rgba(245, 158, 11, 0.4);
}

.vd-search-meta {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 6px;
    font-size: 0.78rem;
    font-weight: 700;
}

.vd-search-text {
    font-size: 0.88rem;
    line-height: 1.5;
    opacity: 0.9;
}
</style>
""", unsafe_allow_html=True)


def render_hero(badge: str, title: str, subtitle: str, tags: list = None):
    """Renders a sleek top hero banner for each page."""
    tags_html = ""
    if tags:
        tags_html = '<div class="vd-tags-row">' + "".join(
            f'<span class="vd-tag-chip">{tag}</span>' for tag in tags
        ) + '</div>'
    
    st.markdown(f"""
<div class="vd-hero-banner">
    <div class="vd-hero-badge">
        <span>⚡</span>
        <span>{badge}</span>
    </div>
    <div class="vd-hero-title">{title}</div>
    <div class="vd-hero-subtitle">{subtitle}</div>
    {tags_html}
</div>
""", unsafe_allow_html=True)


def render_sidebar_brand():
    """Renders the top branding widget in the sidebar."""
    st.sidebar.markdown("""
<div class="vd-sidebar-brand">
    <div class="vd-brand-badge">
        <span>🦺</span>
        <span>VisionDesk AI Pro</span>
    </div>
    <div class="vd-brand-title">Workplace Safety Intelligence</div>
    <p class="vd-brand-sub">Visual Analytics & BI Platform</p>
</div>
""", unsafe_allow_html=True)


def render_sidebar_telemetry(has_model: bool, has_gemini: bool, model_name: str, total_chunks: int):
    """Renders live system status telemetry in the sidebar."""
    model_dot = '<span class="vd-pulse-dot vd-pulse-green"></span> Ready' if has_model else '<span class="vd-pulse-dot vd-pulse-red"></span> Missing'
    gemini_dot = '<span class="vd-pulse-dot vd-pulse-green"></span> Online' if has_gemini else '<span class="vd-pulse-dot vd-pulse-amber"></span> No API Key'

    st.sidebar.markdown(f"""
<div class="vd-telemetry-card">
    <div class="vd-telemetry-header">
        <span>System Telemetry</span>
        <span>Live</span>
    </div>
    <div class="vd-telemetry-row">
        <span><b>YOLOv8 Model</b> (best.pt)</span>
        <span>{model_dot}</span>
    </div>
    <div class="vd-telemetry-row">
        <span><b>Gemini Engine</b> ({model_name})</span>
        <span>{gemini_dot}</span>
    </div>
    <div class="vd-telemetry-row">
        <span><b>Knowledge Base</b></span>
        <span><b>{total_chunks}</b> chunks</span>
    </div>
</div>
""", unsafe_allow_html=True)


def render_status_banner(compliant: bool, violations: list = None):
    """Renders modern compliance/violation status card for PPE detection."""
    violations = violations or []
    if compliant:
        st.markdown("""
<div class="vd-banner-compliant">
    <div class="vd-banner-icon">✅</div>
    <div>
        <div class="vd-banner-title" style="color: #10B981;">SITE FULLY COMPLIANT</div>
        <div class="vd-banner-text">All identified personnel satisfy mandated safety regulations. Zero PPE infractions recorded.</div>
    </div>
</div>
""", unsafe_allow_html=True)
    else:
        unique_violations = sorted(set(violations))
        chips = "".join(f'<span class="vd-chip vd-chip-violation">🚨 {v}</span>' for v in unique_violations)
        st.markdown(f"""
<div class="vd-banner-violation">
    <div class="vd-banner-icon">🚨</div>
    <div>
        <div class="vd-banner-title" style="color: #EF4444;">SAFETY VIOLATIONS DETECTED</div>
        <div class="vd-banner-text">The following required safety protections are missing from the inspected area:</div>
        <div style="margin-top: 8px;">{chips}</div>
    </div>
</div>
""", unsafe_allow_html=True)


def render_workflow_steps(steps: list):
    """Renders breadcrumb badges for LangGraph agent execution."""
    if not steps:
        return
    badges = []
    for i, s in enumerate(steps):
        badges.append(f'<span class="vd-step-badge">Step {i+1}: {s}</span>')
        if i < len(steps) - 1:
            badges.append('<span class="vd-step-arrow">➔</span>')
    st.markdown('<div class="vd-workflow-flow">' + "".join(badges) + '</div>', unsafe_allow_html=True)
