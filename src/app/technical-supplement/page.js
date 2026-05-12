"use client";
import { useEffect, useRef, useState } from "react";
import styles from "./TechSupp.module.css";

const SLIDES = [
  { id: "s1", component: SlideTitle },
  { id: "s2", component: SlidePFD },
  { id: "s3", component: SlideSpecs },
  { id: "s4", component: SlideFootprint },
  { id: "s5", component: SlideOps },
];

function LogoMark() {
  return (
    <div className={styles.logoMark}>
      <svg className={styles.logoIcon} viewBox="0 0 28 28" fill="none">
        <circle cx="14" cy="14" r="12" stroke="#D4AF37" strokeWidth="1.5" fill="none" />
        <circle cx="14" cy="14" r="4" fill="#D4AF37" opacity="0.8" />
      </svg>
      <span className={styles.logoText}>BetulaR</span>
    </div>
  );
}

function SlideTitle() {
  return (
    <div className={`${styles.contentArea} ${styles.centered}`}>
      <div className={styles.tag} style={{ marginBottom: 12 }}>Technical Supplement</div>
      <div className={styles.slideTitle}>Industrial Cell Architecture</div>
      <div className={`${styles.goldLine} ${styles.goldLineCentered}`}></div>
      <p className={styles.subText}>
        Process flow diagram, equipment specifications, and scaling analysis for the BetulaR electrochemical platform.
      </p>
      <p className={styles.subTextDim} style={{ marginTop: 24 }}>
        For engineering and due diligence review · Not for general distribution
      </p>
      <p className={styles.patentTag}>PATENTS PENDING</p>
    </div>
  );
}

function SlidePFD() {
  return (
    <div className={styles.contentArea}>
      <div className={styles.tag}>Process Flow Diagram</div>
      <div className={styles.slideTitle}>Single Cell Module &amp; Leach Circuit</div>
      <div className={styles.goldLine}></div>

      <div className={styles.pfdBox}>
        <h3 className={styles.pfdBoxTitle}>Equipment Tags &amp; Streams</h3>
        <svg viewBox="0 0 1000 380" className={styles.pfdSvg}>
          <defs>
            <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
              <path d="M0,0 L8,3 L0,6Z" fill="rgba(255,255,255,0.5)" />
            </marker>
          </defs>
          {/* Feed Prep */}
          <rect x="20" y="140" width="100" height="50" rx="6" className={styles.pfdEquip} />
          <text x="70" y="170" textAnchor="middle" className={styles.pfdTag}>FEED PREP</text>
          {/* Leach Tank */}
          <rect x="180" y="100" width="100" height="90" rx="6" className={styles.pfdEquip} />
          <text x="230" y="148" textAnchor="middle" className={styles.pfdTag}>T-101</text>
          <text x="230" y="162" textAnchor="middle" className={styles.pfdLabel} fontSize="7">LEACH TANK</text>
          {/* Vacuum Filter */}
          <rect x="360" y="110" width="100" height="80" rx="6" className={styles.pfdEquip} />
          <text x="410" y="153" textAnchor="middle" className={styles.pfdTag}>F-101</text>
          <text x="410" y="167" textAnchor="middle" className={styles.pfdLabel} fontSize="7">VAC FILTER</text>
          {/* Electrochemical Cell */}
          <rect x="600" y="80" width="160" height="130" rx="6" className={styles.pfdEquip} />
          <text x="680" y="135" textAnchor="middle" className={styles.pfdTag}>C-101</text>
          <text x="680" y="148" textAnchor="middle" className={styles.pfdLabel} fontSize="7">DIVIDED CELL</text>
          <text x="645" y="165" textAnchor="middle" className={styles.pfdLabel} fontSize="7" fill="#D4AF37">ANODE</text>
          <text x="715" y="165" textAnchor="middle" className={styles.pfdLabel} fontSize="7" fill="#B87333">CATHODE</text>
          <line x1="680" y1="90" x2="680" y2="200" stroke="rgba(212,175,55,0.4)" strokeWidth="2" strokeDasharray="4 2" />
          <text x="680" y="215" textAnchor="middle" className={styles.pfdLabel} fontSize="7">MEMBRANE</text>
          {/* Collection Vessel */}
          <rect x="820" y="180" width="100" height="60" rx="6" className={styles.pfdEquip} />
          <text x="870" y="215" textAnchor="middle" className={styles.pfdTag}>V-101</text>
          {/* Neutralization */}
          <rect x="440" y="260" width="100" height="60" rx="6" className={styles.pfdEquip} />
          <text x="490" y="295" textAnchor="middle" className={styles.pfdTag}>N-101</text>

          {/* Streams */}
          <path d="M120,165 L180,165" className={styles.pfdStream} stroke="rgba(255,255,255,0.6)" />
          <text x="150" y="160" textAnchor="middle" className={styles.pfdLabel}>1 Slurry</text>
          <path d="M280,145 L360,145" className={styles.pfdStream} />
          <text x="320" y="140" textAnchor="middle" className={styles.pfdLabel}>3 Leached</text>
          <path d="M410,190 L410,260" className={styles.pfdStream} />
          <text x="418" y="225" textAnchor="start" className={styles.pfdLabel}>5 Solids</text>
          <path d="M460,145 L600,145" className={styles.pfdStream} />
          <text x="530" y="140" textAnchor="middle" className={styles.pfdLabel}>4 Pregnant</text>
          <path d="M600,125 L280,125" className={styles.pfdStream} />
          <text x="440" y="118" textAnchor="middle" className={styles.pfdLabel}>2 Regenerated Anolyte</text>
          <path d="M760,200 L820,200" className={styles.pfdStream} stroke="#B87333" />
          <text x="790" y="195" textAnchor="middle" className={styles.pfdLabel} fill="#B87333">7 Powder</text>
          <path d="M870,240 L870,280 Q870,310 600,310 L600,210" className={styles.pfdStream} stroke="rgba(255,255,255,0.3)" />
          <text x="735" y="305" textAnchor="middle" className={styles.pfdLabel} fontSize="7">8 Depleted Catholyte</text>
          <path d="M540,260 L540,190 L600,190" className={styles.pfdStream} stroke="rgba(255,255,255,0.3)" />
          <text x="555" y="220" textAnchor="start" className={styles.pfdLabel} fontSize="7">Wash water</text>
          <path d="M540,320 L540,340" className={styles.pfdStream} />
          <text x="548" y="335" textAnchor="start" className={styles.pfdLabel}>6 Dry Silt</text>
          <path d="M870,260 L870,280 Q870,340 600,340" className={styles.pfdStream} stroke="rgba(39,174,96,0.5)" />
          <text x="735" y="350" textAnchor="middle" className={styles.pfdLabel} fill="#27AE60" fontSize="7">9 Product</text>
        </svg>
      </div>

      <div className={styles.pfdFooter}>
        <div className={styles.pfdFooterCell}>
          <strong className={styles.goldText}>Key Control Points:</strong><br />
          ORP on Stream 2 → Anode current<br />
          pH on Stream 8 → Membrane &amp; bleed<br />
          Level/Pressure in C-101 → Back-pulse cleaning
        </div>
        <div className={styles.pfdFooterCellDim}>
          <strong>Single module throughput:</strong> 2,000–5,000 tpd solids<br />
          <strong>Modules for 500k tpa:</strong> 2–6 in parallel<br />
          <strong>Cycle:</strong> Regenerated lixiviant → Leach → Filter → Recover → Return
        </div>
      </div>
    </div>
  );
}

function SlideSpecs() {
  const specs = [
    { value: "10–20 m²", label: "Electrode Area", note: "Per cell (filter-press design)" },
    { value: "3,000–10,000 A", label: "Operating Current", note: "200–500 A/m² density" },
    { value: "3.5–5 V", label: "Cell Voltage", note: "Anode/cathode + ohmic drop" },
    { value: "2–5 ktpd", label: "Solid Throughput", note: "Per module (ore-dependent)" },
    { value: "10–50 kg/d", label: "Metal Recovery", note: "Valuable metals per module" },
    { value: "2–6 Modules", label: "For 500k tpa", note: "Parallel configuration" },
  ];
  const rows = [
    ["Cell type", "Divided filter-press", "Single cell, membrane-separated"],
    ["Anode", "Ti / MMO (IrO₂/Ta₂O₅)", "Chlorine evolution, pH 0–1"],
    ["Cathode", "Graphite / Ti with 3D coating", "High surface area; back-pulse harvest"],
    ["Membrane", "Low-cost CEM (proprietary)", "Solvent-cast, <$1/yd²"],
    ["Cell dimensions", "~4m × 2m × 3m (L×W×H)", "Skid-mounted"],
    ["Electrolyte volume", "2,000–5,000 L/cell", "Circulated to external leach tank"],
    ["Maintenance", "Swap electrodes/membrane in hours", "Bypass valves for isolation"],
  ];
  return (
    <div className={styles.contentArea}>
      <div className={styles.tag}>Cell Module</div>
      <div className={styles.slideTitle}>Specifications &amp; Throughput</div>
      <div className={styles.goldLine}></div>

      <div className={styles.specGrid}>
        {specs.map((s) => (
          <div key={s.label} className={styles.specCard}>
            <div className={styles.specValue}>{s.value}</div>
            <div className={styles.specLabel}>{s.label}</div>
            <div className={styles.specNote}>{s.note}</div>
          </div>
        ))}
      </div>

      <table className={`${styles.dataTable} ${styles.dataTableMt}`}>
        <tbody>
          <tr>
            <th className={styles.dataTableTh}>Parameter</th>
            <th className={styles.dataTableTh}>Specification</th>
            <th className={styles.dataTableTh}>Notes</th>
          </tr>
          {rows.map(([param, spec, note]) => (
            <tr key={param}>
              <td className={styles.dataTableTd}>{param}</td>
              <td className={styles.dataTableTd}>{spec}</td>
              <td className={styles.dataTableTd}>{note}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function SlideFootprint() {
  const rows = [
    ["Leach/Adsorption", "6–8 large tanks (~10m dia each)", "1–2 agitated leach tanks", true],
    ["Solid-Liquid Separation", "CCD circuit (multiple thickeners)", "1–2 vacuum drum filters", true],
    ["Refining Circuit", "Carbon stripping + electrowinning", "2–6 filter-press cells (SPR)", true],
    ["Tailings", "Wet dam (200+ hectares)", "None — dry stack", true, true],
    ["Cyanide handling", "Storage, mixing, detox", "None", true, true],
    ["Process building footprint", "~2,000–5,000 m²", "~500–1,000 m²", true],
    ["Capital Cost Estimate", "~A$100M", "A$15–25M", true, false, true],
  ];
  return (
    <div className={styles.contentArea}>
      <div className={styles.tag}>Footprint &amp; Capital</div>
      <div className={styles.slideTitle}>Plant Comparison (500,000 tpa)</div>
      <div className={styles.goldLine}></div>

      <table className={styles.dataTable}>
        <tbody>
          <tr>
            <th className={styles.dataTableTh}>Item</th>
            <th className={styles.dataTableTh}>Conventional CIL</th>
            <th className={styles.dataTableTh}>BetulaR Modular Plant</th>
          </tr>
          {rows.map(([item, conv, betr, isHighlight, isDim, isBold]) => (
            <tr key={item} style={isBold ? { borderTop: "1px solid rgba(212,175,55,0.4)" } : {}}>
              <td className={styles.dataTableTd}>{isBold ? <strong>{item}</strong> : item}</td>
              <td className={`${styles.dataTableTd} ${isDim ? styles.dim : ""}`}>
                {isBold ? <strong>{conv}</strong> : conv}
              </td>
              <td className={`${styles.dataTableTd} ${isHighlight ? styles.highlight : ""}`}>
                {isBold ? <strong>{betr}</strong> : betr}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className={styles.footprintDisclaimer}>
        BetulaR estimate includes crushing, grinding, leach tanks, cells, rectifiers, installation, and commissioning.
        Excludes site-specific earthworks and permitting.
      </div>
    </div>
  );
}

function SlideOps() {
  return (
    <div className={styles.contentArea}>
      <div className={styles.tag}>Operating Philosophy</div>
      <div className={styles.slideTitle}>Control, Maintenance &amp; Redundancy</div>
      <div className={styles.goldLine}></div>

      <div className={styles.opsGrid}>
        <div>
          <h4 className={styles.opsHeading}>Key Control Points</h4>
          <ul className={styles.opsList}>
            <li>→ ORP probe on regenerated anolyte → controls anode current to maintain &gt;1.5 V vs SHE</li>
            <li>→ pH sensor on catholyte return → detects acid build-up; triggers membrane current adjustment</li>
            <li>→ Pressure differential across membrane → initiates back-pulse cleaning cycle</li>
            <li>→ Inline XRF/ICP on pregnant solution → programs SPR voltage sequence</li>
            <li>→ Level sensors in collection vessel → triggers metal powder harvest cycle</li>
          </ul>
        </div>
        <div>
          <h4 className={styles.opsHeading}>Maintenance &amp; Redundancy</h4>
          <ul className={styles.opsList}>
            <li>→ Each cell module is isolated with bypass valves — one module offline, rest continue</li>
            <li>→ Electrode plates are segmented; swap individual plates, not the entire cell</li>
            <li>→ Membrane replacement: &lt;2 hours per cell (proprietary frame &amp; gasket design)</li>
            <li>→ Rectifiers are modular, off-the-shelf industrial DC units</li>
            <li>→ Pumps are magnetically driven, acid-resistant — standard chemical duty</li>
            <li>→ Full plant shutdown for membrane replacement not required</li>
          </ul>
        </div>
      </div>
      <div className={styles.opsBanner}>
        Designed for continuous operation · Hot-swappable components · Operator-friendly from day one
      </div>
    </div>
  );
}

export default function TechnicalSupplement() {
  const [current, setCurrent] = useState(0);
  const [animState, setAnimState] = useState("active"); // "active" | "exit"
  const total = SLIDES.length;
  const pendingRef = useRef(null);

  function navigate(dir) {
    setAnimState("exit");
    pendingRef.current = (current + dir + total) % total;
    setTimeout(() => {
      setCurrent(pendingRef.current);
      setAnimState("active");
    }, 450);
  }

  useEffect(() => {
    function onKey(e) {
      if (e.key === "ArrowRight" || e.key === "ArrowDown") navigate(1);
      if (e.key === "ArrowLeft" || e.key === "ArrowUp") navigate(-1);
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  });

  const touchX = useRef(0);

  const SlideComponent = SLIDES[current].component;

  return (
    <div className={styles.deck}>
      {/* Slide */}
      <div
        className={`${styles.slide} ${animState === "active" ? styles.slideActive : styles.slideExit}`}
        onTouchStart={(e) => { touchX.current = e.touches[0].clientX; }}
        onTouchEnd={(e) => {
          const dx = e.changedTouches[0].clientX - touchX.current;
          if (Math.abs(dx) > 50) navigate(dx < 0 ? 1 : -1);
        }}
      >
        <LogoMark />
        <SlideComponent />
      </div>

      {/* Nav */}
      <button className={`${styles.navBtn} ${styles.navPrev}`} onClick={() => navigate(-1)}>&#8249;</button>
      <button className={`${styles.navBtn} ${styles.navNext}`} onClick={() => navigate(1)}>&#8250;</button>
      <div className={styles.slideCounter}>{current + 1} / {total}</div>
      <div className={styles.progressBar} style={{ width: `${((current + 1) / total) * 100}%` }} />
    </div>
  );
}
