"""
AI-Powered Visual Data Analytics and Business Intelligence Platform - Streamlit dashboard (MILESTONE 4)
--------------------------------------------------
Run:  streamlit run app.py

Pages:
  🏠 Home          overview + status
  👷 PPE Detection image / video          (Milestone 1)
  📄 Documents     upload + search manuals (Milestone 2)
  🤖 Ask AI        LangGraph agent          (Milestone 3)
  📊 Dashboard     KPIs + charts            (Milestone 4)
  📋 Report        PDF download             (Milestone 4)
"""
import os
import tempfile

import cv2
import streamlit as st

import knowledge_base as kb
import storage
import vision
from agent import ask_agent
from documents import process_file
from llm import MODEL, has_key
from report import build_pdf, write_summary
from ui_theme import (
    inject_custom_css,
    render_hero,
    render_sidebar_brand,
    render_sidebar_telemetry,
    render_status_banner,
    render_workflow_steps,
)

# ── Page Configuration ──
st.set_page_config(
    page_title="AI-Powered Visual Data Analytics and Business Intelligence Platform",
    page_icon="🦺",
    layout="wide",
)

# Inject modern, theme-adaptive CSS design system
inject_custom_css()

# On Streamlit Cloud the API key comes from "Secrets"
try:
    if "GEMINI_API_KEY" in st.secrets:
        os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass


# ── load once ──────────────────────────────────────────────
@st.cache_resource
def get_model():
    return vision.load_model()


@st.cache_resource
def load_sample_manual():
    """If the knowledge base is empty (e.g. fresh cloud start), add a manual automatically."""
    if kb.total_chunks() == 0:
        for name in ["safety_manual.pdf", "sample_safety_manual.txt"]:
            path = os.path.join(vision.BASE_DIR, "data", name)
            if os.path.exists(path):
                kb.add_document(process_file(path), name)
                return name
    return None


def save_upload(uploaded):
    suffix = os.path.splitext(uploaded.name)[1]          # keep the real extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded.getbuffer())
        return tmp.name


model = get_model()
load_sample_manual()

# ── sidebar ────────────────────────────────────────────────
with st.sidebar:
    render_sidebar_brand()
    page = st.radio("Navigation", ["🏠 Home", "👷 PPE Detection", "📄 Documents",
                                  "🤖 Ask AI", "📊 Dashboard", "📋 Report"])
    st.divider()
    render_sidebar_telemetry(bool(model), has_key(), MODEL, kb.total_chunks())


# ══════════════════════════════════════════════════════════
# 🏠 HOME
# ══════════════════════════════════════════════════════════
if page == "🏠 Home":
    render_hero(
        badge="Executive Safety Operations",
        title="AI-Powered Visual Data Analytics and Business Intelligence Platform",
        subtitle="VisionDesk AI — Enterprise Multimodal Intelligence uniting YOLOv8 computer vision, ChromaDB vector knowledge retrieval, and LangGraph generative reasoning.",
        tags=["YOLOv8 PPE Vision", "ChromaDB Vector RAG", "LangGraph Multimodal Agent", "Executive BI & PDF Reporting"]
    )

    # System Status & Quick Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Detection Engine", "YOLOv8 Active" if model else "Model Offline")
    with m2:
        st.metric("Safety Knowledge", f"{kb.total_chunks()} Chunks")
    with m3:
        st.metric("Reasoning Model", MODEL if has_key() else "Key Pending")
    with m4:
        scans_count = len(storage.load_scans())
        st.metric("Audit History", f"{scans_count} Scans Logged")

    st.markdown("### 🌟 Platform Architecture & Capabilities")
    st.markdown("""
<div class="vd-feature-grid">
    <div class="vd-feature-card">
        <div class="vd-feature-icon">👷</div>
        <div class="vd-feature-title">1. PPE Computer Vision</div>
        <div class="vd-feature-desc">Upload site photography or video feeds to detect mandatory PPE compliance (helmets, vests, goggles, masks) with instant violation alerts.</div>
    </div>
    <div class="vd-feature-card">
        <div class="vd-feature-icon">📄</div>
        <div class="vd-feature-title">2. Document Knowledge Base</div>
        <div class="vd-feature-desc">Ingest site safety manuals, SOPs, and regulatory inspection reports into an indexed ChromaDB vector store with semantic similarity search.</div>
    </div>
    <div class="vd-feature-card">
        <div class="vd-feature-icon">🤖</div>
        <div class="vd-feature-title">3. Multimodal Ask AI</div>
        <div class="vd-feature-desc">Interactive LangGraph agent that reasons over camera observations and cites specific clauses in the safety manual to resolve complex questions.</div>
    </div>
    <div class="vd-feature-card">
        <div class="vd-feature-icon">📊</div>
        <div class="vd-feature-title">4. Business Intelligence</div>
        <div class="vd-feature-desc">Real-time KPI monitoring tracking overall compliance rates, violation frequency distributions, daily infraction trends, and user feedback.</div>
    </div>
    <div class="vd-feature-card">
        <div class="vd-feature-icon">📋</div>
        <div class="vd-feature-title">5. Executive Audit Reports</div>
        <div class="vd-feature-desc">One-click compliance reporting generating official downloadable PDF audit documents complete with AI-authored executive summaries.</div>
    </div>
</div>
""", unsafe_allow_html=True)

    # Workflow Architecture Banner
    st.markdown("### 🔄 End-to-End Multimodal Data Pipeline")
    st.markdown("""
<div class="vd-glass-card">
    <div style="font-size: 0.92rem; line-height: 1.6; opacity: 0.9;">
        <b>Data Journey:</b> 
        Site Imagery / Video ➔ <b>YOLOv8 Detection</b> (Classifies bounding boxes & violations) 
        ➔ <b>LangGraph Orchestrator</b> (Combines visual tags + query) 
        ➔ <b>ChromaDB Vector Retrieval</b> (Retrieves relevant safety clauses) 
        ➔ <b>Gemini LLM Synthesis</b> (Produces cited regulatory answer) 
        ➔ <b>BI Dashboard & PDF Reporting</b>
    </div>
</div>
""", unsafe_allow_html=True)

    if not model:
        st.warning("⚠️ Put your trained **best.pt** in the project folder to enable detection.")
    if not has_key():
        st.info("ℹ️ Add **GEMINI_API_KEY** to the `.env` file for AI answers.")


# ══════════════════════════════════════════════════════════
# 👷 PPE DETECTION  (Milestone 1)
# ══════════════════════════════════════════════════════════
elif page == "👷 PPE Detection":
    render_hero(
        badge="Milestone 1 • Computer Vision",
        title="👷 Real-time PPE Safety Detection",
        subtitle="Upload job-site photography or inspection video to automatically verify mandatory personal protective equipment and highlight safety violations.",
        tags=["YOLOv8 Deep Learning", "Automated Violation Flagging", "Multi-Frame Video Sampling"]
    )

    if not model:
        st.error("🚨 best.pt model weights not found in the project root folder. Please ensure the model file is present.")
        st.stop()

    # Controls Card
    with st.container():
        st.markdown('<div class="vd-glass-card">', unsafe_allow_html=True)
        col_ctrl1, col_ctrl2 = st.columns([1, 2])
        with col_ctrl1:
            kind = st.radio("Input Source", ["Image", "Video"], horizontal=True)
        with col_ctrl2:
            conf = st.slider("Detection Confidence Threshold", 0.1, 0.9, 0.4, 0.05,
                             help="Higher = fewer false alarms, but may miss some items")
        st.markdown('</div>', unsafe_allow_html=True)

    if kind == "Image":
        file = st.file_uploader("Upload job-site photo (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
        if file and st.button("⚡ Analyze Site Image", type="primary"):
            with st.spinner("Processing visual inference with YOLOv8..."):
                path = save_upload(file)
                dets = vision.detect(model, path, conf)
                result = vision.summarize(dets, file.name)
                storage.log_scan(file.name, result, "image")
                st.session_state["last"] = {
                    "name": file.name,
                    "result": result,
                    "dets": dets,
                    "image": vision.draw(cv2.imread(path), dets)
                }
    else:
        file = st.file_uploader("Upload inspection video feed (MP4, AVI, MOV)", type=["mp4", "avi", "mov"])
        every_n = st.slider("Frame Sampling Frequency (Check 1 of every N frames)", 1, 30, 5)
        if file and st.button("⚡ Analyze Video Stream", type="primary"):
            with st.spinner("Analyzing video frames & aggregating busiest timestamps..."):
                dets, preview, frames = vision.detect_video(model, save_upload(file), every_n, conf)
                result = vision.summarize(dets, file.name)
                storage.log_scan(file.name, result, "video")
                st.session_state["last"] = {
                    "name": f"{file.name} ({frames} frames)",
                    "result": result,
                    "dets": dets,
                    "image": preview
                }

    last = st.session_state.get("last")
    if last:
        st.markdown("---")
        r = last["result"]
        render_status_banner(r["compliant"], r["violations"])

        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("#### 📸 Annotated Visual Inspection")
            if last["image"] is not None:
                st.image(cv2.cvtColor(last["image"], cv2.COLOR_BGR2RGB),
                         caption=f"Visual Evidence: {last['name']}",
                         use_container_width=True)
        with col2:
            st.markdown("#### 📊 Detection Telemetry")
            m_col1, m_col2 = st.columns(2)
            with m_col1:
                st.metric("Total Objects", len(last["dets"]))
            with m_col2:
                st.metric("Safety Violations", len(r["violations"]))

            st.markdown("**Detected Class Inventory:**")
            if r["counts"]:
                chips_html = "".join(
                    f'<span class="vd-chip vd-chip-neutral">📦 <b>{cls}</b>: {cnt}</span>'
                    for cls, cnt in r["counts"].items()
                )
                st.markdown(f'<div style="margin-bottom: 12px;">{chips_html}</div>', unsafe_allow_html=True)
            else:
                st.caption("No individual objects classified.")

            st.markdown("""
<div class="vd-glass-card" style="margin-top: 15px; border-left: 3px solid #10B981;">
    <div style="font-size: 0.84rem;">
        💡 <b>AI Ready:</b> This detection result is automatically synchronized with the <b>🤖 Ask AI</b> module to cross-examine against safety regulations.
    </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════
# 📄 DOCUMENTS  (Milestone 2)
# ══════════════════════════════════════════════════════════
elif page == "📄 Documents":
    render_hero(
        badge="Milestone 2 • Vector Knowledge Base",
        title="📄 Safety Manuals & Documentation",
        subtitle="Ingest standard operating procedures, site guidelines, and safety manuals into the ChromaDB vector database for semantic intelligence.",
        tags=["ChromaDB Embeddings", "PDF / DOCX / TXT Ingestion", "Semantic Vector Search"]
    )

    # Document Upload Section
    st.markdown("### 📤 Upload New Safety Manuals or Inspection Reports")
    files = st.file_uploader("Upload safety policies / inspection protocols",
                             type=["pdf", "txt", "docx"], accept_multiple_files=True)
    if files and st.button("📥 Index into Knowledge Base", type="primary"):
        with st.spinner("Chunking, generating embeddings, and storing in ChromaDB..."):
            for f in files:
                chunks = process_file(save_upload(f))
                if chunks:
                    kb.add_document(chunks, f.name)
                    st.success(f"✅ **{f.name}**: successfully indexed {len(chunks)} chunks.")
                else:
                    st.warning(f"⚠️ **{f.name}**: no readable text found (scanned image PDF?).")

    # Document Inventory
    st.markdown("### 📚 Indexed Safety Documents")
    docs = kb.list_documents()
    if docs:
        col_stats1, col_stats2 = st.columns(2)
        with col_stats1:
            st.metric("Indexed Documents", len(docs))
        with col_stats2:
            st.metric("Total Vector Chunks", sum(docs.values()))

        st.table([{"Document Name": name, "Vector Chunks": n, "Status": "Active & Searchable"} for name, n in docs.items()])
    else:
        st.info("No documents indexed yet. Upload a manual above or place one in the data folder.")

    # Semantic Test Search
    st.markdown("### 🔍 Semantic Retrieval Studio")
    q = st.text_input("Test Query", placeholder="e.g. When must high-visibility vests or protective goggles be worn?")
    if q:
        with st.spinner("Querying vector space..."):
            results = kb.search(q, top_k=4)
        if results:
            st.markdown(f"**Top {len(results)} Semantic Matches:**")
            for r in results:
                dist = round(r['distance'], 4)
                st.markdown(f"""
<div class="vd-search-card">
    <div class="vd-search-meta">
        <span class="vd-chip vd-chip-ok">📄 {r['source']}</span>
        <span class="vd-chip vd-chip-neutral">Chunk #{r['chunk']}</span>
        <span class="vd-chip vd-chip-neutral">Distance: {dist}</span>
    </div>
    <div class="vd-search-text">{r['text']}</div>
</div>
""", unsafe_allow_html=True)
        else:
            st.caption("No matching passages found.")


# ══════════════════════════════════════════════════════════
# 🤖 ASK AI  (Milestone 3 - LangGraph agent)
# ══════════════════════════════════════════════════════════
elif page == "🤖 Ask AI":
    render_hero(
        badge="Milestone 3 • Multimodal LangGraph Agent",
        title="🤖 Workplace Safety Assistant",
        subtitle="Autonomous agent grounded in site safety documentation and live camera scan evidence, delivering cited regulatory answers.",
        tags=["LangGraph Stateful Agent", "Multimodal Grounding", "Gemini 1.5 Flash", "Human Feedback Alignment"]
    )

    last = st.session_state.get("last")
    use_image = False
    if last:
        st.markdown(f"""
<div class="vd-glass-card" style="border-left: 3px solid #F59E0B; padding: 12px 18px;">
    <b>📸 Active Visual Context Available:</b> <code>{last['name']}</code>
</div>
""", unsafe_allow_html=True)
        use_image = st.checkbox(f"Include camera detection evidence in agent context ({last['name']})", value=True)
        if use_image:
            st.caption(f"**Camera Findings:** {last['result']['text']}")

    question = st.text_input("Ask a safety or compliance question",
                             placeholder="e.g. Is this worker compliant? Which site rule specifies mandatory protective gear?")

    if st.button("🚀 Ask Safety AI", type="primary") and question:
        vis = last["result"] if (use_image and last) else None
        with st.spinner("LangGraph agent routing workflow and querying Gemini..."):
            out = ask_agent(question,
                            vision=vis["text"] if vis else "",
                            violations=vis["violations"] if vis else [])
        st.session_state["answer"] = {"question": question, **out}
        st.session_state["voted"] = False

    ans = st.session_state.get("answer")
    if ans:
        st.markdown("### 📋 Agent Assessment")
        st.markdown(f"""
<div class="vd-glass-card" style="border-left: 4px solid #10B981; font-size: 1.02rem; line-height: 1.6;">
    {ans["answer"]}
</div>
""", unsafe_allow_html=True)

        with st.expander("🔍 Agent Reasoning & Document Grounding Trace", expanded=True):
            st.markdown("**LangGraph Execution Pathway:**")
            render_workflow_steps(ans.get("steps", []))
            
            st.markdown("**Retrieved Regulatory Passages:**")
            for d in ans.get("docs", []):
                st.markdown(f"""
<div class="vd-search-card" style="margin-bottom: 8px;">
    <div class="vd-search-meta">
        <span class="vd-chip vd-chip-neutral">Source: {d['source']}</span>
        <span class="vd-chip vd-chip-neutral">Chunk #{d['chunk']}</span>
    </div>
    <div style="font-size: 0.85rem; opacity: 0.9;">{d['text']}</div>
</div>
""", unsafe_allow_html=True)

        # Human Feedback Section
        st.markdown("---")
        if not st.session_state.get("voted"):
            st.markdown("**Was this answer helpful and accurate?**")
            c1, c2, _ = st.columns([1, 1, 4])
            if c1.button("👍 Yes, Helpful"):
                storage.log_feedback(ans["question"], True)
                st.session_state["voted"] = True
                st.rerun()
            if c2.button("👎 No, Needs Improvement"):
                storage.log_feedback(ans["question"], False)
                st.session_state["voted"] = True
                st.rerun()
        else:
            st.success("✅ Thank you! Your feedback has been recorded in the BI Dashboard.")


# ══════════════════════════════════════════════════════════
# 📊 DASHBOARD  (Milestone 4)
# ══════════════════════════════════════════════════════════
elif page == "📊 Dashboard":
    render_hero(
        badge="Milestone 4 • Business Intelligence",
        title="📊 Workplace Safety & Compliance Dashboard",
        subtitle="Real-time KPI telemetry monitoring site compliance rate, violation categories, incident trends, and user satisfaction.",
        tags=["Real-time KPIs", "Trend Analytics", "Violation Distributions", "Target ≥85% Satisfaction"]
    )

    scans = storage.load_scans()
    k = storage.kpis(scans)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Scans Audited", k["scans"])
    with c2:
        comp_str = f"{k['compliance']}%" if k["compliance"] is not None else "-"
        st.metric("Site Compliance Rate", comp_str)
    with c3:
        st.metric("Total Violations", k["violations"])
    with c4:
        sat_str = f"{k['satisfaction']}%" if k["satisfaction"] is not None else "-"
        st.metric("AI Satisfaction", sat_str, help="Project target: ≥ 85% satisfaction")

    if scans.empty:
        st.info("ℹ️ No scan history recorded yet. Upload and analyze images in **👷 PPE Detection** to populate analytics.")
    else:
        st.markdown("---")
        left, right = st.columns(2)
        with left:
            st.markdown("#### 🚨 Violations by Category")
            counts = storage.violation_counts(scans)
            if len(counts):
                st.bar_chart(counts)
            else:
                st.success("🎉 Zero safety violations recorded to date!")
        with right:
            st.markdown("#### 📈 Daily Violation Trend")
            daily_series = scans.set_index("time")["violations"].resample("D").sum()
            st.line_chart(daily_series)

        st.markdown("---")
        st.markdown("#### 📋 Complete Inspection Audit Log")
        st.dataframe(scans.sort_values("time", ascending=False), hide_index=True, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🗑️ Clear Inspection History"):
        storage.clear_all()
        st.rerun()


# ══════════════════════════════════════════════════════════
# 📋 REPORT  (Milestone 4)
# ══════════════════════════════════════════════════════════
elif page == "📋 Report":
    render_hero(
        badge="Milestone 4 • Official Compliance Report",
        title="📋 Regulatory Compliance & Audit Report",
        subtitle="Generate formal safety documentation complete with Gemini-authored executive summaries, KPI tables, and downloadable PDF deliverables.",
        tags=["Official PDF Document", "Gemini Executive Brief", "Exportable CSV Audit Log"]
    )

    scans = storage.load_scans()

    st.markdown("""
<div class="vd-glass-card">
    <div style="font-size: 0.95rem; margin-bottom: 10px;">
        Generate an official compliance report summarizing recent site audits, violation distributions, and safety manual citations.
    </div>
</div>
""", unsafe_allow_html=True)

    if st.button("📑 Generate Official Compliance Report", type="primary"):
        k = storage.kpis(scans)
        counts = storage.violation_counts(scans)
        with st.spinner("Synthesizing executive summary with Gemini and assembling PDF..."):
            summary = write_summary(k, counts)
        st.session_state["report"] = {
            "summary": summary,
            "pdf": build_pdf(k, counts, scans, summary)
        }

    rep = st.session_state.get("report")
    if rep:
        st.markdown("---")
        st.markdown("### 📝 Executive Summary Brief")
        st.markdown(f"""
<div class="vd-glass-card" style="border-left: 4px solid #F59E0B; font-style: italic; font-size: 1.02rem; line-height: 1.6;">
    "{rep['summary']}"
</div>
""", unsafe_allow_html=True)

        st.markdown("### 📥 Download Deliverables")
        d_col1, d_col2 = st.columns(2)
        with d_col1:
            st.download_button(
                "⬇️ Download Official PDF Report",
                rep["pdf"],
                file_name="safety_compliance_report.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        with d_col2:
            st.download_button(
                "⬇️ Export Raw Telemetry (CSV)",
                scans.to_csv(index=False),
                file_name="scans.csv",
                mime="text/csv",
                use_container_width=True
            )
