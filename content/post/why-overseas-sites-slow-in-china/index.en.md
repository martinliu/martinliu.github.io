---
title: "Why Is Your Overseas Site Slow and Unstable in Mainland China?"
date: 2026-10-01T00:10:00+08:00
slug: why-overseas-sites-slow-in-china
description: "Same site, two very different health reports — smooth overseas, slow and flaky in mainland China. This article breaks down where slowness and instability actually come from, layer by layer, with a checklist you can run yourself."
image: insight-aws-china.webp
categories:
    - DevOps
---

Same site, same code — yet two very different health reports: opening it from an overseas office takes a few hundred milliseconds, while customers in mainland China report that it is "slow" or "sometimes just doesn't load." This is probably the most common question asked by teams going global, and it is almost never the fault of a single component.

## First, separate two different problems: unavailable ≠ slow

Before troubleshooting, do one thing: sort the feedback into two buckets.

- **Unavailable**: users in some regions or on some ISPs get resolution or connection failures — an availability problem;
- **Slow**: everyone can open it, it is just slow — a performance problem.

The diagnostic paths are completely different. Treating "slow" as "down" (or the reverse) is the most common reason this class of issue stays unresolved.

## "Slow" is layered — peel it from outside in

When a page load becomes slow in mainland China, the cause is usually a stack of five layers:

1. **DNS steering**: resolution sends mainland users to distant nodes. Global Anycast is fine in itself, but if your DNS provider has no resolution points in the mainland, or the GeoDNS zoning policy is coarse, users are sent far away at the very first step.
2. **Cross-border links**: the quality of public transit between the mainland and overseas fluctuates on its own, especially at evening peak. You cannot change this layer, but you must know it exists — it sets the latency floor: the same architecture simply has a higher latency floor in the mainland.
3. **CDN coverage and warm-up**: turning on a CDN does not equal fast in the mainland. No mainland nodes, static assets never warmed, dynamic content (even HTML) never cached — every request goes back to origin, and the first two layers get amplified.
4. **Origin location**: an overseas origin means every origin fetch crosses the border; an origin in the mainland, or hosting that is mainland-friendly, changes the fetch path entirely.
5. **Front-end payload weight**: a high-latency link is an amplifier. A 3MB page that nobody notices at 200ms round trips is a disaster on a 300ms+ link.

## The mechanics of "sometimes fine, sometimes not": a real case

My own blog (hosted on an overseas edge network, with real mainland traffic) had this data in September 2026: about 1.21 million requests for the month, **with 5.79% ending in 5xx — almost all of them 504 gateway timeouts**. What makes it interesting is the distribution:

- Every single one was a GET, with a **sustained baseline of 60–240 per hour** — not an incident, a constant;
- The homepage alone accounted for nearly 30,000 504s;
- By geography, mainland China, the US, and France topped the list (the latter two clearly scanner traffic).

Root cause: HTML was never cached at the edge (`cf-cache-status: DYNAMIC`), so **every page view ran back to origin naked**. When the origin occasionally timed out under scanner pressure, every uncached request failed together — which looks exactly like "sometimes fine, sometimes not."

The fix was not complicated either: after adding an edge cache rule for HTML, warm-connection TTFB dropped from 0.7–0.9s to **0.26s**, origin fetches fell off a cliff, and the 504s lost their habitat. I will walk through the full story of this case in the pitfalls article.

## A self-service checklist you can run today

1. **Check where resolution lands**: `dig` your domain from a mainland machine or probe node; compare the returned IP/CNAME with overseas — are users being steered far away?
2. **Multi-region probing**: cover at least Beijing / Shanghai / Guangzhou directions across ISPs, and measure availability (can you connect at all), not just latency.
3. **TTFB by region**: use real-user Core Web Vitals data (or a RUM tool) for the TTFB distribution of mainland visitors — not just server-side monitoring.
4. **Resource waterfall**: open the page once in a mainland network and look at the waterfall — which segment is longest: DNS, connect, waiting for first byte, or asset download?
5. **Confirm caching behavior**: check the cache status in response headers (e.g. `cf-cache-status`) and verify whether HTML and static assets are actually being served from the edge.

If after these five steps you want a more systematic answer — based on real measurements, with prioritized improvements — take a look at the free diagnostic below.

{{< china-ready >}}
