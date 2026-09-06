# PostHog Self-driving setup report

## Summary

PostHog Self-driving is configured for this Jekyll publication. Session Replay, Error Tracking, and Support were enabled, and the native responder sources for health checks, errors, support, and scouts are active.

Five focused scouts and two Replay Vision monitors are armed. Findings should begin appearing in the [Self-driving inbox](https://us.posthog.com/project/593922/inbox) within about 30 minutes once the relevant data arrives.

## AI data processing

Approved by the wizard prerequisite.

## GitHub

GitHub was already connected before this setup run. No GitHub Issues warehouse source was added because no optional connected tool was selected.

## Products enabled

| Product | Result | Notes |
| --- | --- | --- |
| Session Replay | enabled | Browser initialization has no `disable_session_recording` override. No recordings were present during setup. |
| Error Tracking | enabled | Browser initialization has no `capture_exceptions` override. |
| Support | enabled | Tickets will arrive only after an inbound email, inbox, or Slack channel is connected in PostHog. |

## Signal sources

| Source product | Source type | Action |
| --- | --- | --- |
| `signals_scout` | `cross_source_issue` | enabled (`01a073dc-3dae-7f3a-b9a7-c645295e69db`) |
| `health_checks` | `health_issue` | enabled (`01a073dc-3db8-7446-997e-bee70f5a4aba`) |
| `error_tracking` | `issue_created` | enabled (`01a073dc-3db8-7851-a3e1-76d060b24f63`) |
| `error_tracking` | `issue_reopened` | enabled (`01a073dc-3da1-757f-9828-ba629438b95a`) |
| `error_tracking` | `issue_spiking` | enabled (`01a073dc-3e67-7b2d-b1a0-966ade08c70a`) |
| `conversations` | `ticket` | enabled (`01a073dc-3d96-7cdb-b861-d8c19f429a88`) |
| Replay Vision | scanner-based | deliberately not represented by a signal-source row; the two scanners below self-authorize their inbox output |
| Connected-tool responders | n/a | skipped: no optional connected tool was selected |

## Connected tools

No tool was selected in the connected-tools picker. GitHub Issues, Linear, Jira, Sentry, and Zendesk are therefore recorded as not used for this setup; no warehouse source or dormant responder was created.

## Scout troop

The enforced budget is **100 runs/day**; **0** had been used when checked, leaving **100**. The project is enrolled, and the current banner says: “Scouts are in early access. Each project gets up to 100 scout runs a day. Contact team-self-driving@posthog.com if you need more.”

### Active scouts

| Scout | Reason |
| --- | --- |
| `signals-scout-general` | Broad cross-product coverage. |
| `signals-scout-web-analytics` | This is a public web publication with reader traffic and page-view activity. |
| `signals-scout-observability-gaps` | Finds high-volume events that lack saved insight, dashboard, or alert coverage. |
| `signals-scout-reader-journey` | Approved custom coverage for the reader-to-article-to-RSS journey. |
| `signals-scout-content-discovery` | Approved custom coverage for category and author discovery paths. |

### Disabled built-in scouts

| Scout | Reason |
| --- | --- |
| `signals-scout-ai-observability` | No LLM traces or AI product evidence. |
| `signals-scout-anomaly-detection` | No established saved dashboards or insights to watch. |
| `signals-scout-apm` | No APM or distributed tracing evidence. |
| `signals-scout-conversations` | Support is enabled but no inbound channel or ticket activity exists yet. |
| `signals-scout-csp-violations` | No CSP reporting evidence. |
| `signals-scout-customer-analytics` | No account or group analytics evidence. |
| `signals-scout-data-pipelines` | No CDP, batch-export, or Hog Flow evidence. |
| `signals-scout-data-warehouse` | No warehouse sources are connected. |
| `signals-scout-error-tracking` | Covered by the active native Error Tracking responders. |
| `signals-scout-experiments` | No active experiment evidence. |
| `signals-scout-feature-flags` | No active feature-flag usage in this publication repo. |
| `signals-scout-health-checks` | Native health-check responder provides this route. |
| `signals-scout-inbox-validation` | No resolved Self-driving reports exist to re-measure. |
| `signals-scout-insight-alerts` | No configured insight-alert evidence. |
| `signals-scout-logs` | No PostHog Logs evidence. |
| `signals-scout-mcp-tool-calls` | Not a product surface for this publication. |
| `signals-scout-product-analytics` | No saved funnels, retention, lifecycle, or path flows. |
| `signals-scout-replay-vision` | No accumulated Replay Vision observations yet. |
| `signals-scout-revenue-analytics` | No payment or revenue data evidence. |
| `signals-scout-session-replay` | Covered by the Replay Vision monitors below. |
| `signals-scout-skills-store` | No project skill-store maintenance surface identified. |
| `signals-scout-surveys` | No surveys exist. |
| `signals-scout-tasks` | No PostHog Tasks delivery surface identified. |
| `signals-scout-web-vitals` | No Web Vitals evidence was available to prioritize it. |

## Custom scouts

| Scout | Coverage and discriminator | Why it is distinct |
| --- | --- | --- |
| `signals-scout-reader-journey` | Watches the listing → article → RSS path implemented in `_layouts/posts.html` and `_layouts/post.html`. It reports a sustained conversion-rate drop only when the preceding step retains meaningful reader volume. | Web analytics partially overlaps on traffic, but does not own the publication’s reading and subscription journey. |
| `signals-scout-content-discovery` | Watches the category and author discovery paths in `_layouts/category_index.html` and `_layouts/author_index.html`. It reports a persistent route-specific loss of downstream readership while total article readership holds. | General coverage is broad; this scout owns the editorial discovery mix. |

No proposed custom scout was declined. Both custom scouts are enabled, emitting, and scheduled daily by default. If either becomes noisy, set its `emit` value to `false` in PostHog to switch it to dry-run rather than deleting it.

## Replay Vision scanners

A scanner is an LLM that watches individual session recordings on a schedule and pushes unambiguous product defects to the inbox. It is the only thing in this setup that spends Replay Vision quota. Scanner findings arrive at half weight and require independent corroboration before becoming a Self-driving report.

| Brief | Scanner | Status | Query scope | Sampling | Estimated monthly spend |
| --- | --- | --- | --- | --- | --- |
| Breakage monitor | Article reading breakage | created | Recording activity on dated article URLs (`/202`), the publication’s core reading flow | 0.5 | 0 observations / 0 credits (no recordings yet) |
| Frustration monitor | Reader navigation frustration | created | `$rageclick` sessions only; no URL scope | 1.0 | 0 observations / 0 credits (no recordings yet) |

No Replay Vision scanner existed before setup. Both scanners emit Self-driving findings and are armed; they will start observing when Session Replay receives recordings. The in-product sizing guide was unavailable in this deployment, so the small-scanner fallback was used; server estimates returned zero because there are no recordings yet.

## Files modified or created

| File | Change |
| --- | --- |
| `posthog-self-driving-report.md` | Created this setup report. |

No existing application files were modified. Existing browser PostHog initialization was checked and already left replay and exception capture enabled by default.

## Follow-ups

- [ ] Connect an inbound Support channel (email, inbox, or Slack) in [PostHog integrations](https://us.posthog.com/project/593922/settings/environment-integrations) to begin receiving support-ticket findings.
- [ ] Generate normal visitor activity so Session Replay records sessions; the two Replay Vision scanners will begin working automatically once recordings exist.
- [ ] If manual event-schema investigation is needed through this MCP connection, reauthorize it with the `property_definition:read` scope. The setup’s custom scouts were created from repository evidence.

## What happens next

The scout coordinator picks up fresh configurations within about 30 minutes and draws from the daily run budget. Self-driving groups corroborated findings into reports in the [inbox](https://us.posthog.com/project/593922/inbox); immediately actionable reports can start coding tasks.
