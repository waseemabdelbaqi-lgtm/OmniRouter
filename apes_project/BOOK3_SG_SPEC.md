# Book 3 Part I — solutions for Book One classroom examples (one unit per agent)

Read /home/user/OmniRouter/apes_project/BUILD_SPEC.md (markup + rules) first. You are an expert AP Environmental Science teacher writing the answer key for the unsolved classroom examples in Book One, Unit N.

Input: /home/user/OmniRouter/apes_project/content/book1/UN.md — every `:::box example` block (first line `id: SG-UN-Ennn`). Examples may appear out of numeric order in the file; solve ALL of them. Figures a problem refers to are in content/book1/figs/ (view the PNG when a problem depends on one). Use the unit's own teaching (formulas, tables, simplified keys) so your method matches what the student learned.
Output: /home/user/OmniRouter/apes_project/content/book3/SG_UN_sol.md :
```
## Unit N — <unit title>
:::sol SG-UN-E001
...
:::
```
one `:::sol` block per example, in ascending ID order, no omissions, no duplicate IDs.
Solution style: lead with the final answer in bold (e.g. "**Answer: 4,800 kg.**" or "**Answer:** one sentence"), then the reasoning. Calculations: formula → substitution with units → result with units and sensible significant figures. Multi-part problems: label (a), (b), … each on its own paragraph. Conceptual items: the correct claim plus the reason in 2–5 sentences and, where useful, what a common wrong answer misses. Data/graph items: state the values read. Experimental design items: give a model answer listing each required element (question, hypothesis, independent/dependent/controlled variables, procedure, replication/control, data to collect, how to analyse) plus what else would be acceptable.
Accuracy is critical: re-derive every number twice; if a problem is ambiguous or inconsistent, solve it under the most reasonable reading, say so in one sentence, and ALSO record it in /home/user/OmniRouter/apes_project/content/audit/sg_issues_UN.md (and do NOT edit the Book One file). Do not copy anything from College Board materials.
Final reply: number of examples solved, any problem you flagged, ≤ 6 lines.
