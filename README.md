<h1>🤖 AutoCrew: Autonomous Financial Modeling System</h1>

<h2>🌟 Project Overview</h2>
<p>
AutoCrew is an automated system designed to streamline and govern the end-to-end process of financial model development. 
Leveraging Large Language Models (LLMs) orchestrated by the CrewAI framework, AutoCrew takes a natural language task 
description (e.g., <i>"Build a credit risk model"</i>) and autonomously executes a multi-step workflow, culminating 
in a fully validated and audited model.
</p>

<p>
The system is built around two specialized, sequential Agent Crews to ensure regulatory compliance and robust 
Model Risk Management (MRM).
</p>

<h2>💡 Key Features</h2>
<ul>
  <li><b>Autonomous Workflow:</b> Executes the entire modeling pipeline from data preparation to final risk sign-off without human intervention.</li>
  <li><b>Dual-Crew Architecture:</b> Enforces separation of duties via a Modeling Crew (construction) and an MRM Crew (validation and audit).</li>
  <li><b>LLM Acceleration:</b> Utilizes high-performance LLMs (Meta Llama 3.1 8B via Groq LPU and Google Gemini 1.5 Flash).</li>
  <li><b>Built-in Simulator:</b> Includes a Stress Testing Engineer for economic shock simulations to validate model stability.</li>
  <li><b>Compliance Ready:</b> Generates an audit trail through the Compliance Officer.</li>
</ul>

<h2>🏗️ System Architecture</h2>
<p>AutoCrew employs a hierarchical agent system managed by CrewAI.</p>

<table>
  <tr>
    <th>Crew</th>
    <th>Agents Included</th>
    <th>Primary Responsibility</th>
  </tr>
  <tr>
    <td><b>Modeling Crew</b></td>
    <td>Data Analyst, ML Engineer, Technical Writer</td>
    <td>Data cleaning, feature engineering, model training, documentation</td>
  </tr>
  <tr>
    <td><b>MRM Crew</b></td>
    <td>Compliance Officer, Stress Testing Engineer, Chief Risk Officer</td>
    <td>Code audit, stress testing simulation, regulatory approval</td>
  </tr>
</table>

<h2>🚀 Getting Started</h2>

<h3>1. Prerequisites</h3>
<ul>
  <li>Python 3.10+</li>
  <li>Git</li>
</ul>

<h3>2. Clone the Repository</h3>
<pre><code>git clone https://github.com/YourUsername/AutoCrew-Financial-Agent-System.git
cd AutoCrew-Financial-Agent-System
</code></pre>

<h3>3. Setup Virtual Environment & Dependencies</h3>
<pre><code>python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
</code></pre>

<h3>4. Configure API Keys (Critical Security Step)</h3>
<p>Create a file named <b>.env</b> in the project root (never commit it to GitHub):</p>

<pre><code>GROQ_API_KEY=YOUR_GROQ_API_KEY_HERE
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY_HERE
</code></pre>

<h3>5. Run AutoCrew</h3>
<p>Execute the main script. You will be prompted to select an LLM (Groq recommended):</p>

<pre><code>python -m src.main
</code></pre>

<h2>🎯 Example Workflow</h2>
<p>
Upon running, AutoCrew processes the Credit Default Prediction dataset, producing a trained model and a 
detailed report approved by the Chief Risk Officer.
</p>

<h2>🛑 Security and Compliance</h2>
<ul>
  <li>API keys are protected by the <code>.gitignore</code>.</li>
  <li>All agent actions are logged for auditability, meeting Model Risk Management standards.</li>
</ul>

<h2>📜 License</h2>
<p>[Specify your license here: MIT, Apache 2.0, etc.]</p>

<h2>🤝 Contact</h2>
<p><b>Sarim Shah</b> — <a href="mailto:sarimoman@gmail.com">sarimoman@gmail.com</a></p>
