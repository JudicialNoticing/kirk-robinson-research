const fs = require('fs');
const path = require('path');
// `docx` is not a project dependency; resolve it from NODE_PATH first, then the Homebrew global.
let M = 'docx';
try { require.resolve(M); } catch (e) { M = '/opt/homebrew/lib/node_modules/docx'; }
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, LevelFormat, HeadingLevel, BorderStyle, WidthType,
        ShadingType, TableOfContents, Header, Footer, PageNumber } = require(M);

const SRC = process.argv[2], OUT = process.argv[3];
const CONTENT = 9360;

/* ---------- inline formatting ---------- */
function inline(text, base = {}) {
  const runs = [];
  (function walk(s, st) {
    const re = /(`[^`]+`)|(\*\*[\s\S]+?\*\*)|(\*[^*\n]+\*)/;
    let m;
    while ((m = re.exec(s)) !== null) {
      if (m.index > 0) runs.push(new TextRun({ text: s.slice(0, m.index), ...base, ...st }));
      if (m[1]) runs.push(new TextRun({ text: m[1].slice(1, -1), ...base, ...st, font: 'Consolas', size: 20 }));
      else if (m[2]) walk(m[2].slice(2, -2), { ...st, bold: true });
      else walk(m[3].slice(1, -1), { ...st, italics: true });
      s = s.slice(m.index + m[0].length);
    }
    if (s) runs.push(new TextRun({ text: s, ...base, ...st }));
  })(text, {});
  return runs.length ? runs : [new TextRun({ text: '', ...base })];
}

/* ---------- table ---------- */
const bd = { style: BorderStyle.SINGLE, size: 1, color: 'BFBFBF' };
const borders = { top: bd, bottom: bd, left: bd, right: bd };
function makeTable(rows) {
  const n = Math.max(...rows.map(r => r.length));
  const w = Math.floor(CONTENT / n);
  const widths = Array(n).fill(w);
  widths[n - 1] = CONTENT - w * (n - 1);
  return new Table({
    width: { size: CONTENT, type: WidthType.DXA },
    columnWidths: widths,
    rows: rows.map((cells, ri) => new TableRow({
      tableHeader: ri === 0,
      children: Array.from({ length: n }, (_, ci) => new TableCell({
        borders,
        width: { size: widths[ci], type: WidthType.DXA },
        shading: ri === 0 ? { fill: 'E7EEF5', type: ShadingType.CLEAR } : undefined,
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        children: [new Paragraph({
          spacing: { before: 20, after: 20 },
          children: inline(cells[ci] ?? '', ri === 0 ? { bold: true } : {})
        })]
      }))
    }))
  });
}

/* ---------- parse ---------- */
const lines = fs.readFileSync(SRC, 'utf8').split('\n');
const body = [];
let i = 0;
const isTable = s => /^\s*\|/.test(s);

while (i < lines.length) {
  let ln = lines[i];
  const t = ln.trim();

  if (t === '' ) { i++; continue; }

  if (t === '---') {
    body.push(new Paragraph({ text: '', spacing: { before: 60, after: 60 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: '2E75B6', space: 1 } } }));
    i++; continue;
  }

  // table block
  if (isTable(ln)) {
    const rows = [];
    while (i < lines.length && isTable(lines[i])) {
      const raw = lines[i].trim().replace(/^\|/, '').replace(/\|$/, '');
      const cells = raw.split('|').map(c => c.trim());
      if (!cells.every(c => /^:?-{2,}:?$/.test(c))) rows.push(cells);
      i++;
    }
    if (rows.length) { body.push(makeTable(rows)); body.push(new Paragraph({ text: '', spacing: { after: 120 } })); }
    continue;
  }

  // headings
  let h = t.match(/^(#{1,4})\s+(.*)$/);
  if (h) {
    const lvl = h[1].length;
    const map = { 1: HeadingLevel.HEADING_1, 2: HeadingLevel.HEADING_2, 3: HeadingLevel.HEADING_3, 4: HeadingLevel.HEADING_4 };
    body.push(new Paragraph({ heading: map[lvl], children: inline(h[2]), pageBreakBefore: false }));
    i++; continue;
  }

  // blockquote (may span lines, may contain its own headings/bullets)
  if (/^>/.test(t)) {
    const buf = [];
    while (i < lines.length && /^\s*>/.test(lines[i])) {
      buf.push(lines[i].trim().replace(/^>\s?/, ''));
      i++;
    }
    buf.forEach(q => {
      if (q.trim() === '') return;
      const qh = q.match(/^(#{1,4})\s+(.*)$/);
      const txt = qh ? qh[2] : q.replace(/^[-*]\s+/, '');
      body.push(new Paragraph({
        children: inline(txt, qh ? { bold: true, size: 24 } : {}),
        spacing: { before: 40, after: 40 },
        indent: { left: 360 },
        shading: { fill: 'F4F6F8', type: ShadingType.CLEAR },
        border: { left: { style: BorderStyle.SINGLE, size: 12, color: '2E75B6', space: 6 } }
      }));
    });
    body.push(new Paragraph({ text: '', spacing: { after: 80 } }));
    continue;
  }

  // bullets
  if (/^[-*]\s+/.test(t)) {
    body.push(new Paragraph({ numbering: { reference: 'bul', level: 0 },
      spacing: { before: 40, after: 40 }, children: inline(t.replace(/^[-*]\s+/, '')) }));
    i++; continue;
  }

  // numbered
  if (/^\d+\.\s+/.test(t)) {
    body.push(new Paragraph({ numbering: { reference: 'num', level: 0 },
      spacing: { before: 40, after: 40 }, children: inline(t.replace(/^\d+\.\s+/, '')) }));
    i++; continue;
  }

  body.push(new Paragraph({ spacing: { before: 60, after: 60 }, children: inline(t) }));
  i++;
}

/* ---------- document ---------- */
const doc = new Document({
  styles: {
    default: { document: { run: { font: 'Arial', size: 21 } } },
    paragraphStyles: [
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 34, bold: true, font: 'Arial', color: '1F3864' },
        paragraph: { spacing: { before: 300, after: 200 }, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 27, bold: true, font: 'Arial', color: '2E75B6' },
        paragraph: { spacing: { before: 260, after: 140 }, outlineLevel: 1 } },
      { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 23, bold: true, font: 'Arial', color: '333333' },
        paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 2 } },
      { id: 'Heading4', name: 'Heading 4', basedOn: 'Normal', next: 'Normal', quickFormat: true,
        run: { size: 21, bold: true, italics: true, font: 'Arial' },
        paragraph: { spacing: { before: 160, after: 80 }, outlineLevel: 3 } },
    ]
  },
  numbering: { config: [
    { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•',
      alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 640, hanging: 320 } } } }] },
    { reference: 'num', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.',
      alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 640, hanging: 320 } } } }] },
  ]},
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 },
      margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: 'TJR-P01 · State v. Robinson, No. 251403576 · PROVISIONAL · page ', size: 16, color: '666666' }),
                 new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '666666' })] })] }) },
    children: [
      new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: 'Contents', bold: true, size: 27, color: '2E75B6' })] }),
      new TableOfContents('Contents', { hyperlink: true, headingStyleRange: '1-3' }),
      new Paragraph({ pageBreakBefore: true, text: '' }),
      ...body
    ]
  }]
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(OUT, b); console.log('wrote', OUT, b.length, 'bytes'); });
