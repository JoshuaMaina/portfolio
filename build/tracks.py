TRACKS = [
    # (side, title, metric, body, stack, short)
    ("A", "Clustered pricing cache", "10× faster",
     "I led the design and rollout of a clustered Hazelcast cache for cross-asset pricing, and it made pricing "
     "more than ten times faster. It handles product-specific pricing rules for more than ten instrument types. "
     "Operators can switch it on or off at runtime from a dashboard, and continuous monitoring and end-to-end "
     "validation tests check every result.",
     "Java, Hazelcast"),
    ("A", "Zero-downtime intra-day deployments", "0 downtime",
     "I built a custom Java load-balancing service for mission-critical pricing systems, from start to finish. "
     "It orchestrates rolling restarts automatically, so patches go out during the trading day without downtime, "
     "rather than waiting for a release window.",
     "Java"),
    ("A", "90% faster service start-up", "−90% start-up",
     "A critical library used to be downloaded at runtime when each service started. I changed its release model "
     "so it is pre-deployed to application hosts, which cut start-up time by 90% across every service the team "
     "owns. Its releases now follow the same rollout standards as production.",
     "Release engineering"),
    ("A", "Standard gRPC tooling", "−10% latency",
     "Shared tooling to standardise gRPC and Protocol Buffers across services, in Java and Python: client "
     "scaffolding, authentication middleware and distributed tracing. It helped cut client-server latency by "
     "more than 10% across several microservices.",
     "gRPC, Protocol Buffers, Java, Python"),
    ("A", "From OpenTracing to OpenTelemetry", "Zero rewrites",
     "OpenTracing was archived, so I led the move off it. I designed an internal tracing abstraction and "
     "refactored our repositories to use it. We swapped the backend to OpenTelemetry without touching "
     "application code, and the next migration will be just as easy.",
     "OpenTelemetry, Java"),
    ("A", "Monitoring the pricing flow", "Real-time",
     "I led the rollout of Prometheus monitoring across the core pricing flow, giving real-time visibility into "
     "latency and system health. I also extended our tracing, which cut support load and gave performance work "
     "real data to go on.",
     "Prometheus, distributed tracing"),
    ("A", "Shared worker pool framework", "Many → one",
     "I co-led the design and led the build of a scalable Python worker pool framework. It replaced several "
     "team-specific versions with one shared platform, which now runs internal and client-facing products.",
     "Python"),
    ("A", "Multi-region auto-scaling", "Scales both ways",
     "I helped build a configurable, multi-region auto-scaling framework for pricing systems. It adds capacity "
     "under heavy trading load and scales down when markets are quiet.",
     "Kubernetes"),
    ("B", "Multi-tenant agent platform", "1 runtime per user",
     "An internal platform where each user gets an isolated agent runtime, and traders can ship their own apps "
     "with no configuration. It grew out of moving five teams from bespoke dashboards onto one shared platform. "
     "It works by convention: one parameterised Dockerfile, the folder name as the app’s identity, per-app CI "
     "builds and automatic service discovery. I implemented the A2A protocol on top of our MCP-based "
     "orchestration, and rebuilt the task lifecycle as an explicit state machine backed by Redis.",
     "Python, MCP, A2A, Docker, GitHub Actions, Traefik, Redis"),
    ("B", "Grounded trading chat", "0 invented figures",
     "A chat assistant inside a trading dashboard, where one invented number is a financial risk. Answers are "
     "grounded in tool output and cite their sources. The interface renders figures straight from tool results "
     "rather than from model text, and an eval suite checks that this keeps holding.",
     "LLM tool use, Braintrust, Promptfoo"),
    ("B", "Bloomberg chat bots", "3 teams live",
     "I’m extending an internal Bloomberg API service so that teams can run interactive bots that listen and "
     "reply in chat rooms. Teams define a bot’s behaviour through a lightweight plug-in configuration. Three "
     "teams are already using it ahead of the production rollout.",
     "Bloomberg APIs, Python"),
    ("B", "Conditions written by agents", "In the studio",
     "In progress: letting an agent turn a request like “tell me if this stays above X for three hours” into a "
     "strict, auditable contract over live data, which triggers actions when it passes. Simple checks run "
     "deterministically and only fuzzy ones go to a smaller model, so costs stay flat as conditions multiply.",
     "System design"),
]
