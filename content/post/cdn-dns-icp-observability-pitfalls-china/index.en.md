---
title: "Common CDN/DNS/ICP and Observability Pitfalls Before Entering China"
date: 2026-10-01T00:10:00+08:00
slug: cdn-dns-icp-observability-pitfalls-china
description: "Every pitfall in this collection comes from a real case, written as symptom → root cause → fix. The through-line is a complete availability and performance overhaul of my own blog in September 2026 — from 5.8% 5xx to nearly zero."
image: insight-icp.webp
categories:
    - SRE
---

This article collects the most common pitfalls on the road into China. Each one is written in three parts: **symptom → root cause → fix**. The through-line is a real case: my own blog (a Hugo static site on an edge CDN, hosted overseas, with real mainland traffic) went through a complete overhaul in September 2026 — taking 5xx from 5.79% of requests down to nearly zero.

## Pitfall 1: assuming a CDN means fast

**Symptom**: the CDN is fully on, overseas speed tests look great, the mainland stays slow.

**Root cause**: "the CDN is on" and "fast in the mainland" are different things. Three common sub-problems: no mainland nodes or no warm-up; by default only static file extensions are cached, so **HTML is never cached**; a high share of dynamic content punches through to origin.

**Case data**: in September my site served about 1.21 million requests with a direct HIT ratio of just 3%. Every HTML response carried `cf-cache-status: DYNAMIC` — each page view crossed the border back to origin.

**Fix**: add an edge cache rule covering HTML and extensionless paths — a 1-hour edge TTL with the browser respecting the origin. Warm-connection TTFB went from 0.7–0.9s to **0.26s**, and origin traffic fell off a cliff.

## Pitfall 2: 404s get cached too, and new pages can't go live

**Symptom**: after a deploy, a new page 404s for up to an hour even though the file clearly exists on the origin.

**Root cause**: once a cache rule makes extensionless paths cacheable, **old 404 responses get cached too**. If a new page URL was fetched once before deploy, that 404 sits at the edge for the full TTL.

**Case data**: this bit exactly when fixing a 404 on a listing page — the 404 persisted for six minutes after deploy until a manual cache purge.

**Fix**: add status-code TTLs to the cache rule — **404s cached for only 60 seconds, 5xx not cached at all**. New pages now become visible within a minute at the worst. A "purge after deploy" step was also added to the deployment pipeline, closing the window entirely.

## Pitfall 3: scanner traffic knocks origin over, and everything 504s together

**Symptom**: site-wide 504s with no pattern, dozens to hundreds per hour, constantly — not a one-off incident.

**Root cause**: floods of exploit-probe requests (`.php`, `.env`, `wp-*` and the like) all go back to origin when "HTML is never cached". The origin (or an intermediate layer) times out under probe pressure, and **every uncached request fails at once** — which looks like random flakiness.

**Case data**: September saw 69,000 504s, all GETs. By geography: 19k from mainland China, 13k from the US, 10k from France — the latter two classic scanner networks.

**Fix**: two layers — a WAF rule blocks exploit-probe paths right at the edge (paths ending `.php`, or containing `/wp-`, `.env`, `/.git`), zero origin cost; combined with HTML caching from Pitfall 1, the 504s lost their habitat. Note: audit your own real URLs before enabling blocks, to avoid false positives (this blog genuinely has old WordPress-era articles — their URLs use the /2009/07/…/ structure and are unaffected).

## Pitfall 4: testing only authoritative DNS, never recursive

**Symptom**: the authoritative side looks perfectly healthy, yet mainland users are still steered to distant nodes.

**Root cause**: mainland ISP recursive resolvers behave differently (caching, ECS support, zoning policy) from what you see at the authoritative side. Testing only authoritative DNS is testing half the path.

**Fix**: run `dig` directly from several mainland networks to verify where resolution actually lands; keep TTLs short enough to switch steering quickly during incidents.

## Pitfall 5: alerts for "down", but no data for "slow"

**Symptom**: all monitors are green, users keep complaining about slowness.

**Root cause**: traditional probes check availability (HTTP status codes) and ignore performance — yet in the mainland, "slow" is the dominant failure mode.

**Fix**: add real-user monitoring — at minimum, regional TTFB / Core Web Vitals. My site uses Cloudflare Web Analytics (free, cookieless, beacon auto-injected at the edge); it answers "how slow are mainland visitors, really" just fine.

---

Looking back, the five pitfalls form one causal chain: **no caching → heavy origin traffic → knocked over by scanners → shows up as instability; and monitoring that only watches availability → cannot see slowness → cannot diagnose**. The fix follows the same chain: cache first, then block, then observe. If you want to walk this chain on your own site, start with a systematic diagnostic:

{{< china-ready >}}
