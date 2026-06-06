---
name: bible-video-workflow
description: >
  End-to-end content pipeline for the "Deep Made Simple" Bible YouTube channel. Five stages: topic
  ideation, scriptwriting, image prompts, video prompts, and thumbnail creation. Use whenever the user
  mentions Bible video scripts, YouTube Bible content, deep-dive Bible topics, watercolor image prompts,
  Bible thumbnails, narration scripts, or Bible video production. Trigger on "create a Bible video,"
  "generate Bible topics," "write a Bible script," "image prompts for my Bible video," "video prompts,"
  "Deep Made Simple," or any reference to this pipeline — even casually. If the user pastes a script
  and asks for image prompts, video prompts, or thumbnails, use this skill.
---

# Bible Video Workflow — Deep Made Simple

A five-stage content production pipeline for a Bible deep-dive YouTube channel. Each stage feeds into
the next, but users can enter at any stage if they already have the output from a previous one.

## The Five Stages

1. **Topic Ideation** → generates video title ideas with hooks and pattern labels (output: in conversation)
2. **Scriptwriting** → writes a full narration script from a chosen title (output: .md file)
3. **Image Prompts** → reads the script and generates one watercolor-style image prompt per visual beat (output: .md file)
4. **Video Prompts** → reads the image prompts and generates animation/motion prompts for each (output: .md file)
5. **Thumbnail Prompt** → generates a single YouTube thumbnail prompt for the video title (output: in conversation)

## How to Run the Workflow

### Default flow: sequential with pauses

When a user starts the pipeline (e.g., "create a Bible video" or "generate Bible topics"), begin at
Stage 1 and progress through each stage in order. After each stage, pause and confirm before moving on.

### Entering mid-pipeline

If the user already has output from an earlier stage, skip ahead:
- User provides a title → start at Stage 2 (Scriptwriting)
- User provides/pastes a script → start at Stage 3 (Image Prompts)
- User provides/pastes image prompts → start at Stage 4 (Video Prompts)
- User asks for a thumbnail with a title → start at Stage 5 (Thumbnail Prompt)

### Stage transitions

After each stage, briefly tell the user what the next stage is and ask if they want to proceed,
make changes, or skip ahead.

---

## Stage 1: Topic Ideation

Generate **10 video topic ideas** by default. After presenting them, offer to generate more
if the user wants a wider selection.

Before generating, read `references/topics.md` for the full title patterns, hook format, and guidelines.

**Output format:** For each topic, provide:
1. Title — exactly as it would appear on YouTube
2. Hook — 1–2 sentences describing the core insight or surprising angle
3. Pattern used — which of the 9 title patterns it follows

**After presenting topics:** Ask the user to pick one (or paste their own). Once they choose,
confirm the exact title wording before proceeding. The user may want to tweak phrasing —
accommodate edits until they're happy with the title.

---

## Stage 2: Scriptwriting

Write a complete narration script for the confirmed topic.

Before writing, read `references/script.md` for the full voice, structure, and style rules.

**Key parameters:**
- Word count: 3,500–5,000 words (7,000–9,000 for comprehensive catalog topics)
- Format: continuous prose paragraphs, no headings/bullets/labels/scene directions
- Every word is meant to be spoken aloud by a narrator
- Primary translation: New King James Version (NKJV)

**Output format:** Begin with `TOPIC:` followed by the topic title, then `SCRIPT:` followed by the
full script text. Save as a `.md` file to `/mnt/user-data/outputs/` with a filename derived from the
topic (e.g., `script-every-letter-paul-wrote.md`). Present it to the user with `present_files`.

**After delivering the script:** Pause and ask if the user wants revisions before moving to
image prompts.

---

## Stage 3: Image Prompt Generation

Read the completed script and generate one detailed image prompt for every distinct visual beat —
each new scene, person, location, concept, Bible verse, analogy, emotional shift, or timeline marker.

Before generating, read `references/images.md` for the full watercolor visual style, composition
types, and prompt structure.

**Key parameters:**
- Density: approximately one prompt per 35–75 words of script
- A 4,000-word script → roughly 55–115 image prompts
- A 5,000-word script → roughly 70–140 image prompts
- An 8,000-word script → roughly 115–230 image prompts
- Every prompt is fully self-contained (includes the complete style tag)
- 8 composition types: Scene Illustration, Character Portrait, Conceptual Diagram,
  Contrast/Transformation, Scripture/Text Feature, Timeline/Map, Symbolic/Metaphor, Flow/Process

**Output format:** Save all image prompts as a single `.md` file to `/mnt/user-data/outputs/`
(e.g., `image-prompts-every-letter-paul-wrote.md`). Present it to the user with `present_files`.

Each prompt formatted as:
```
Image [number]: [Brief description of the script moment]
[Full standalone prompt — scene description + style tag]
Script reference: "[1–2 sentences from the script this accompanies]"
```

**After delivering image prompts:** Pause and ask if the user wants to proceed to video prompts.

---

## Stage 4: Video Prompt Generation

Read the completed image prompts and generate one animation/motion prompt for each image,
turning static illustrations into 5–8 second animated clips.

Before generating, read `references/video.md` for the full motion philosophy, animation types
by composition, and prompt rules.

**Key parameters:**
- One video prompt per image prompt (matching numbering exactly)
- Each prompt specifies: visual content, camera motion, subject motion, art style, mood, duration
- Animation is subtle and cinematic — paintings breathing to life, not cartoons
- Every prompt includes the watercolor style line and negative prompt constraints

**Output format:** Save all video prompts as a single `.md` file to `/mnt/user-data/outputs/`
(e.g., `video-prompts-every-letter-paul-wrote.md`). Present it to the user with `present_files`.

Each prompt formatted as:
```
Video [number]: [Brief description matching the corresponding image]
[Full standalone video generation prompt]
Corresponding image: "Image [number]: [title from the image prompt list]"
```

**After delivering video prompts:** Pause and ask if the user wants to proceed to the thumbnail.

---

## Stage 5: Thumbnail Prompt Generation

Generate 1 thumbnail prompt for the video title.

Before generating, read `references/thumbnail.md` for the full thumbnail design system,
composition patterns, typography rules, and style specifications.

**Key parameters:**
- 1 thumbnail prompt per video title
- 6 composition patterns to choose from (Flanking Portraits, Character Grid, Symbol/Icon Grid,
  Timeline/Progression, Scroll Panorama, Central Character + Map)
- Two-tier text system: dark navy headline + warm brown/amber secondary line
- Fully self-contained prompt with style tag

**Output format:** Present in conversation with:
- Thumbnail concept (one sentence describing the composition pattern and visual strategy)
- Full prompt ready to paste into an image generation AI

**After delivering the thumbnail:** The pipeline is complete. Ask if the user wants to revise
anything or start a new video.

---

## General Rules Across All Stages

- The channel's voice is warm, authoritative, and unhurried — a deeply knowledgeable teacher
  walking the viewer through a discovery, not a preacher delivering a sermon.
- Protestant, evangelical perspective rooted in biblical authority. Scripture treated as divinely
  inspired and internally consistent.
- Original language work (Hebrew and Greek) is a signature element — use it frequently and accurately.
- Historical and archaeological details ground the content in real history (Josephus, Tacitus, etc.).
- Cross-referencing across the Bible is essential — always connect OT patterns to NT fulfillment.
- No emojis, no slang, no humor for humor's sake. Warm and human but always dignified.
- Never pad content. Every paragraph earns its place.
- The visual style across all image, video, and thumbnail prompts is a consistent biblical watercolor
  storybook aesthetic with soft sepia and earth tones.
