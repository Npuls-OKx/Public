#!/usr/bin/env python3
"""Navigatiecontrole van de requirementsboom.

Controleert de laagverwijzingen in Referentiemateriaal/requirementsboom/:
1. Ankerintegriteit en id-conventie: elke fragmentlink naar een boom-id
   resolvet naar een bestaand <a id>-anker; ankers zijn uniek; id's volgen
   de conventie (plat per soort, voluit, vier cijfers).
2. doel <-> epic: "Draagt bij aan" (epics.md) en "Van doel naar epic"
   (opdracht.md) beschrijven exact dezelfde relatie (set-gelijkheid).
3. epic <-> feature: elke sectiekop in features.md linkt naar precies een
   epic, elke epic heeft precies een sectie, en de Features-cel van de epic
   linkt naar de kop van die sectie.
4. feature <-> story: de Epic-cel van elke featurerij komt overeen met de
   sectie waarin de rij staat; de Stories-cel bevat exact de stories die
   met hun featurecel terugwijzen (of "geen").
5. story -> functionele eis: elke functionele-eis-link resolvet naar een
   rij-anker in de interactiepatronen van deze repository.
6. Terugleiding: de Story-kolom in de interactiepatronen is exact de
   inverse van de kolom Functionele eisen in stories.md (set-gelijkheid).

Bekende grenzen: alleen inline-links ([tekst](bestand#anker)) worden
gecontroleerd, referentiestijl-links niet (komen in de boom niet voor);
anker-achtige tekst in codeblokken telt mee als anker (faalt naar de
veilige kant); de featurecel vereist id en naam als linktekst.

Gebruik: python3 scripts/validate-requirementsboom-navigatie.py [boom-map]
Standaard: Referentiemateriaal/requirementsboom (interactiepatronen worden
twee mappen hoger onder Koppelvlakspecificaties/Interactiepatronen gezocht).
Exitcodes: 0 = schoon, 1 = problemen gevonden, 2 = pad niet gevonden.
Testgevallen: python3 -m unittest discover -s tests -v.
"""
import os
import re
import sys

KINDS = ("doel", "epic", "feature", "story")
ID_RE = re.compile(r"^(?:%s)-\d{4}$" % "|".join(KINDS))
ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')
EIS_LINK_RE = re.compile(
    r"\[functionele-eis-\d{4}\]\((\.\./\.\./Koppelvlakspecificaties/"
    r"Interactiepatronen/[\w\-]+\.md)#(functionele-eis-\d{4})\)")


def slug(text: str) -> str:
    """GitHub-kopslug van platte koptekst (linkmarkup al gestript)."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s, flags=re.UNICODE)
    return s.replace(" ", "-")


def cells(row: str) -> list[str]:
    return [c.strip() for c in row.strip().strip("|").split("|")]


def read_text(path: str) -> str:
    return open(path, encoding="utf-8").read()


def main() -> int:
    tree_dir = sys.argv[1] if len(sys.argv) > 1 else "Referentiemateriaal/requirementsboom"
    if not os.path.isdir(tree_dir):
        print(f"pad niet gevonden: {tree_dir}", file=sys.stderr)
        return 2
    problems: list[str] = []
    texts = {name: read_text(os.path.join(tree_dir, name))
             for name in os.listdir(tree_dir) if name.endswith(".md")}

    # 1. Ankers verzamelen: uniek en conform id-conventie
    anchors: dict[str, set[str]] = {}
    for name, content in texts.items():
        seen = anchors[name] = set()
        for anchor in ANCHOR_RE.findall(content):
            if anchor in seen:
                problems.append(f"{name}: dubbel anker {anchor}")
            seen.add(anchor)
            if not ID_RE.match(anchor):
                problems.append(f"{name}: anker {anchor} volgt de id-conventie niet")
    # 1b. Interne fragmentlinks naar boom-id's resolven
    for name, content in texts.items():
        for target_file, fragment in re.findall(r"\]\((?:([\w.-]+\.md))?#([\w\-]+)\)", content):
            if not ID_RE.match(fragment):
                continue  # kopsluglinks toetst punt 3
            target_name = target_file or name
            if fragment not in anchors.get(target_name, set()):
                problems.append(f"{name}: link #{fragment} zonder anker in {target_name}")

    # 2. doel <-> epic
    forward: dict[str, set[str]] = {}
    for row in texts["opdracht.md"].splitlines():
        m = re.match(r"\| \[(doel-\d{4})\]\(#\1\) \| (.*) \|$", row)
        if m:
            forward[m.group(1)] = set(re.findall(r"\[(epic-\d{4}) ", m.group(2)))
    backward: dict[str, set[str]] = {}
    epic_features_cell: dict[str, str] = {}
    for row in texts["epics.md"].splitlines():
        m = re.match(r'\| <a id="(epic-\d{4})"></a>\1 \|', row)
        if m:
            c = cells(row)
            goals = re.findall(r"\[(doel-\d{4})\]\(opdracht\.md#\1\)", c[3])
            if len(goals) != 1:
                problems.append(f"epics.md: {m.group(1)} zonder eenduidige Draagt-bij-aan-cel")
                continue
            backward.setdefault(goals[0], set()).add(m.group(1))
            epic_features_cell[m.group(1)] = c[5]
    for goal in sorted(set(forward) | set(backward)):
        if forward.get(goal, set()) != backward.get(goal, set()):
            problems.append(
                f"doel<->epic: {goal} vooruit {sorted(forward.get(goal, []))} "
                f"!= terug {sorted(backward.get(goal, []))}")

    # 3. epic <-> feature (secties) en 4. feature <-> story
    section_epic: dict[str, str] = {}
    feature_stories: dict[str, set[str]] = {}
    current_epic = None
    for row in texts["features.md"].splitlines():
        heading = re.match(r"## \[(.+)\]\(epics\.md#(epic-\d{4})\)\s*$", row)
        if heading:
            current_epic = heading.group(2)
            if current_epic in section_epic.values():
                problems.append(f"features.md: tweede sectie voor {current_epic}")
            section_epic[slug(heading.group(1))] = current_epic
            continue
        m = re.match(r'\| <a id="(feature-\d{4})"></a>\1 \|', row)
        if m:
            c = cells(row)
            epics_in_cell = re.findall(r"\[(epic-\d{4})\]\(epics\.md#\1\)", c[4])
            if epics_in_cell != ([current_epic] if current_epic else []):
                problems.append(
                    f"features.md: {m.group(1)} Epic-cel {epics_in_cell} "
                    f"!= sectie-epic {current_epic}")
            stories = re.findall(r"\[(story-\d{4})\]\(stories\.md#\1\)", c[5])
            if not stories and c[5] != "geen":
                problems.append(f"features.md: {m.group(1)} Stories-cel noch links noch \"geen\"")
            feature_stories[m.group(1)] = set(stories)
    for epic, cell in epic_features_cell.items():
        m = re.match(r"\[features\]\(features\.md#([\w\-]+)\)$", cell)
        if not m:
            problems.append(f"epics.md: {epic} Features-cel geen sectielink: {cell}")
        elif section_epic.get(m.group(1)) != epic:
            problems.append(f"epic<->feature: {epic} linkt #{m.group(1)}, "
                            f"maar die sectie hoort bij {section_epic.get(m.group(1))}")
    for section, epic in section_epic.items():
        if epic not in epic_features_cell:
            problems.append(f"epic<->feature: sectie #{section} wijst naar onbekende epic {epic}")

    story_feature: dict[str, str] = {}
    requirement_links: dict[tuple[str, str], set[str]] = {}
    for row in texts["stories.md"].splitlines():
        m = re.match(r'\| <a id="(story-\d{4})"></a>\1 \|', row)
        if m:
            c = cells(row)
            features = re.findall(r"\[(feature-\d{4}) [^\]]*\]\(features\.md#\1\)", c[2])
            if len(features) != 1:
                problems.append(f"stories.md: {m.group(1)} zonder eenduidige featurecel")
                continue
            story_feature[m.group(1)] = features[0]
            for rel_path, fragment in EIS_LINK_RE.findall(c[4]):
                requirement_links.setdefault(
                    (os.path.basename(rel_path), fragment), set()).add(m.group(1))
            if not re.search(r"functionele-eis-\d{4}", c[4]) and c[4] != "geen":
                problems.append(f"stories.md: {m.group(1)} Functionele-eisen-cel "
                                f"noch eis-link noch \"geen\"")
    stories_backward: dict[str, set[str]] = {}
    for story, feature in story_feature.items():
        stories_backward.setdefault(feature, set()).add(story)
        if feature not in feature_stories:
            problems.append(f"feature<->story: {story} wijst naar onbekende {feature}")
    for feature in sorted(set(feature_stories) | set(stories_backward)):
        if feature_stories.get(feature, set()) != stories_backward.get(feature, set()):
            problems.append(
                f"feature<->story: {feature} Stories-cel "
                f"{sorted(feature_stories.get(feature, []))} "
                f"!= terugwijzend {sorted(stories_backward.get(feature, []))}")

    # 5 en 6. story -> functionele eis en de terugleiding in de interactiepatronen
    ip_dir = os.path.normpath(os.path.join(tree_dir, "..", "..",
                                           "Koppelvlakspecificaties", "Interactiepatronen"))
    total_links = sum(len(v) for v in requirement_links.values())
    if os.path.isdir(ip_dir):
        ip_texts = {name: read_text(os.path.join(ip_dir, name))
                    for name in os.listdir(ip_dir) if name.endswith(".md")}
        reverse: dict[tuple[str, str], set[str]] = {}
        for name, content in ip_texts.items():
            for row in content.splitlines():
                m = re.match(r'\| <a id="(functionele-eis-\d{4})"></a>\1 \|', row)
                if not m:
                    continue
                c = cells(row)
                stories = set(re.findall(r"\[(story-\d{4})\]", c[3])) if len(c) > 3 else set()
                if not stories and (len(c) < 4 or c[3] != "geen"):
                    problems.append(f"{name}: {m.group(1)} Story-cel noch links noch \"geen\"")
                reverse[(name, m.group(1))] = stories
        for (name, eis), stories in requirement_links.items():
            if (name, eis) not in reverse:
                problems.append(f"stories.md: link naar {eis} zonder rij-anker in {name}")
            elif reverse[(name, eis)] != stories:
                problems.append(
                    f"terugleiding: {name} {eis} Story-cel {sorted(reverse[(name, eis)])} "
                    f"!= stories.md {sorted(stories)}")
        for (name, eis), stories in reverse.items():
            if stories and (name, eis) not in requirement_links:
                problems.append(
                    f"terugleiding: {name} {eis} noemt {sorted(stories)}, "
                    f"maar stories.md linkt die eis niet")
    else:
        problems.append(f"interactiepatronen-map niet gevonden: {ip_dir}")

    for problem in problems:
        print(problem)
    print(f"boomcontrole: {len(texts)} bestanden, {len(story_feature)} stories, "
          f"{len(feature_stories)} features, {len(epic_features_cell)} epics, "
          f"{len(forward)} doelen, {total_links} eis-links, "
          f"{len(problems)} problemen.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
