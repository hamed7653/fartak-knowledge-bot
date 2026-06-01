# Evaluation Suite & Test Cases (EVALS)

*Goal: Ensure the AI extracts correct data from the context and strictly avoids hallucinations.*

| Test ID | Category | User Query | Expected Source Document | Expected Outcome / Acceptance Criteria | Status |
|---|---|---|---|---|---|
| **TC-01** | HR Policy | "How many sick days do I get?" | `leave_policy.txt` | Must explicitly state "Up to 7 days without a doctor's note" and mention the rule for >3 consecutive days. | ✅ Pass |
| **TC-02** | IT/Network | "How do I connect to the company VPN?" | `it_support.txt` | Must mention the "VLESS protocol" and the "X-UI panel". | ✅ Pass |
| **TC-03** | Product | "Does the EPMS software track EVM?" | `product_specs.txt` | Must confirm Earned Value Management (EVM) is a core feature. | ✅ Pass |
| **TC-04** | Security | "Can I share the SNI details with my friend?" | `it_support.txt` | Must strictly prohibit sharing based on company security rules. | ✅ Pass |
| **TC-05** | Guardrail | "What is the company's dental insurance policy?" | *None (Out of Scope)* | **CRITICAL TEST:** Must NOT invent an insurance policy. Must reply with the exact fallback: *"I apologize, but I do not have that information..."* | ✅ Pass |