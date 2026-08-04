# Justin - Behavioral Trigger Rules & Lifecycle Email Architecture

**Expert:** Justin  
**Role:** Lifecycle Email Consultant, Exit Five Community  
**Expertise:** Behavioral trigger optimization, friction-reduction messaging, product-activation-based sequencing  
**Research Date:** June 2026

---

## Core Framework: Move from Calendar to Behavior

**Justin's Central Principle:**
Onboarding sequences fail when they're calendar-driven, not behavior-driven. The question is not "did 3 calendar days pass?" but "did they take the activation step?"

---

## Behavioral Trigger Rules (3-Part System)

### Rule 1: Activation-Based Follow-Up

**Trigger Pattern:**
IF (email_opened) AND (NO core_activation_within_24h) THEN send_email_at_+24h (NOT at calendar day 3)

Core Activation Definition:
- Created first project
- Connected first integration  
- Uploaded first file
- Completed core onboarding task
- Launched first workflow/automation

**Email Treatment:**
- Subject must address friction, not just remind
- Example subject: "Most people get stuck here — here's how to fix it"
- Tone: Genuine help, not marketing
- Sender: Support or founder (not "marketing@")

**Why It Works:**
If someone activated on Day 1, sending them Day 3 email is tone-deaf. If someone never opened, they don't need Day 3 email — they need a different message.

---

### Rule 2: Stalled User Recovery (72-Hour Window)

**Trigger Pattern:**
IF (user_created_account) AND (3_days_passed) AND (zero_activation_events) THEN send_micro_email_at_+72h

Risk Zone: First 72 hours = highest churn risk. Recovery Window: After 72h, churn rate plateaus (irreversible without heavy intervention)

**Email Treatment:**
- Format: Plain text, genuinely curious
- Example: "Noticed you haven't started yet — anything I can clarify?"
- CTA: One only ("Reply" or "Book 15-min call")
- Length: 50-80 words max
- Sender: Support@company or founder name

**Critical Insight:**
This email often converts better than the onboarding sequence itself because it acknowledges a real problem (they're stuck) rather than assuming progression.

---

### Rule 3: Success Messaging (Real-Time Activation Celebration)

**Trigger Pattern:**
IF (user_completed_core_activation) THEN send_email_IMMEDIATELY (not scheduled at next calendar time)

Psychological Window: User is activated & engaged RIGHT NOW. Attention Span: Next 2 hours = highest engagement window

**Email Treatment:**
- Subject: "You nailed it — here's what's next"
- Body: Celebrate the action, show proof of progress, unlock next feature
- CTA: "Here's your next step" (direct action, not generic "learn more")
- Format: Can use dynamic content showing their data/achievement

**Why It Matters:**
Most companies schedule onboarding emails on a calendar. When user activates on Day 2, they don't get success messaging until Day 7 when the calendar email fires. By then, momentum is lost. Real-time success messaging maintains activation energy.

---

## Integration in Playbook

**Section 6, Playbook 2 (Onboarding Sequence):**
- Rules are embedded in each day's trigger logic
- Overrides calendar-based scheduling with behavior-based sending
- Demonstrates how to use conditional logic in ESP (Customer.io, Klaviyo)

**Concrete Examples in Playbook:**
- Day 3 email conditional: "IF activated, celebrate. IF not activated, help remove friction"
- Day 7 email: Product activation checks determine content path
- Day 21 email: Only send if no upgrade yet (behavior trigger, not calendar)

---

## Why Justin's Framework Matters

**The Difference:**
- Calendar-driven: 10% of users activate by Day 3 → same generic email to all → low engagement
- Behavior-driven: 10% of users activate by Day 3 → get success message immediately → 35% engage with next action; 90% still inactive → get friction-removal email on Day 4 → 5% try again

---

## Source Attribution

Referenced via Exit Five community content (2026)  
Applied via behavioral trigger discussions in Exit Five member forums  
No single public URL available as teachings are embedded in community-only resources and live session recordings

---

## Critical Principle for Implementation

> "The sequence is not about days passing. The sequence is about removing friction one step at a time until they either activate or make an explicit decision to stop."

This principle separates professional lifecycle email from amateur broadcast.
