/**
 * Cross-reference the SKILLS list against the `stack` of every role and
 * project, so the skills section can show where each tool was actually used.
 *
 * Matching is whole-token and case-insensitive, which is what keeps "SQL" from
 * claiming credit for "PostgreSQL" and "MySQL" while still letting "AWS" match
 * "AWS EC2".
 */

export interface StackEntry {
  /** Short display name: "fusionSpan", "ALTA". */
  name: string;
  stack: readonly string[];
}

const escape = (s: string) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

function matches(skill: string, stackItem: string): boolean {
  // "C/C++" and similar have no usable word boundary, so compare them whole.
  if (/[^\w\s.+#-]/.test(skill)) {
    return skill.toLowerCase() === stackItem.toLowerCase();
  }
  const re = new RegExp(`(?:^|[^\\w+#])${escape(skill)}(?:[^\\w+#]|$)`, 'i');
  return re.test(` ${stackItem} `);
}

export function buildSkillUsage(
  groups: { label: string; items: string[] }[],
  entries: StackEntry[],
): Record<string, string[]> {
  const usage: Record<string, string[]> = {};

  for (const group of groups) {
    for (const skill of group.items) {
      const where = entries
        .filter((e) => e.stack.some((s) => matches(skill, s)))
        .map((e) => e.name);
      usage[skill] = where;
    }
  }

  return usage;
}
