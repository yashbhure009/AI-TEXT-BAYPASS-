# Zero-Width Character Injection Proof-of-Concept

A lightweight Python demonstration showcasing how invisible Unicode character injection (specifically `U+200B` Zero-Width Space) disrupts basic string-matching algorithms, tokenizers, and legacy AI text detectors.

Created by **Yash Bhure**.

---

## 📌 Overview

This project demonstrates a classic text obfuscation technique: inserting invisible non-printing Unicode characters between every visible character in a document. 

While the output appears completely unchanged to the human eye, the underlying byte array is fundamentally altered, causing simple pattern matchers and legacy NLP pipelines to misinterpret the text structure.

> **Note:** This repository is intended strictly for educational purposes to demonstrate how character tokenization works and how basic security/detection evasion mechanics operate.

---

## ⚙️ How It Works

The script reads a target text file and joins every character using `\u200b` (Zero-Width Space):

1. **Character Breakdown:** The file contents are read as a standard UTF-8 string.
2. **Invisible Injection:** `ZERO_WIDTH_SPACE.join(raw_text)` places `\u200b` between every single character and punctuation mark.
3. **Identical Visual Rendering:** Modern UI renderers ignore `U+200B` dimensions, making `"H\u200be\u200bl\u200bl\u200bo"` display visually as `"Hello"`.

```text
Visual Output:   H e l l o
Underlying Bytes: H\u200be\u200bl\u200bl\u200bo
```

🚀 Quick Start
Prerequisites
Python 3.x

Execution
Place your input text in assignment.txt.

Run the script:

### Execution

1. Place your input text in `assignment.txt`.
2. Run the script:

```bash
python bypass.py
```

3. View the generated obfuscated text in `clean_assignment.txt`.

🔍 Why Legacy Systems Get Bypassed
Tokenizer Disruption: Traditional NLP pipelines segment words by splitting on standard whitespace (\s). Injected characters cause words to register as massive, unrecognized strings.

Exact-Match Plagiarism Failure: Direct string hash comparisons fail because the byte sequence no longer matches the database source.

⚠️ Countermeasures & Why It Fails Modern Scanners
Modern academic integrity tools (e.g., Turnitin, GPTZero, CopyLeaks) easily counter this technique using multi-stage preprocessing pipelines:

Unicode Normalization (NFKC): Strips non-printable and zero-width characters prior to tokenization.

Obfuscation Detection Flags: Systems explicitly scan for high densities of non-standard Unicode characters (such as U+200B, U+200C, U+FEFF), flagging submissions for manual academic integrity review.

Semantic Analysis Unchanged: Once non-printable characters are stripped, the underlying text structure (perplexity, burstiness) remains intact for AI detection evaluation.
