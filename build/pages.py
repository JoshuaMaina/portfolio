"""Every page of the site. Years are listed oldest first here; the build shows them newest first.
Within a year, pages show in the order written below. Edit here, then run: python3 build/build.py"""

# Years shown on the timeline. Each one is a <section> holding that year's pages.
YEARS = [
    {
        "year": 2015,
        "pages": [
            {
                "id": "starehe",
                "where": "Starehe Boys’ Centre, Nairobi",
                "title": "Kenya Certificate of Secondary Education",
                "metric": "Grade A",
                "body": "Finished secondary school with an A. Along the way I led student groups including the "
                        "Research Club, earned Silver and Bronze in the President’s Award scheme, and trained "
                        "as a first aider with the St John Ambulance cadets.",
                "stack": "",
            },
        ],
    },
    {
        "year": 2016,
        "pages": [
            {
                "id": "archangel",
                "where": "Archangel Interactive, front-end intern",
                "title": "Where programming started",
                "metric": "First job",
                "body": "A summer building and testing websites. It was meant to be a side interest next to "
                        "actuarial science, but it’s where I learnt I wanted to build things.",
                "stack": "HTML, CSS, website testing",
            },
        ],
    },
    {
        "year": 2019,
        "pages": [
            {
                "id": "ibm",
                "where": "IBM student start-up programme, data analyst",
                "title": "A start-up inside a programme",
                "metric": "Team of students",
                "body": "IBM gave a small team of university students the chance to run a start-up. I was the "
                        "data analyst, working mostly in R and Watson Studio.",
                "stack": "R, IBM Watson Studio",
            },
            {
                "id": "liberty",
                "where": "Liberty Life Kenya, actuarial intern",
                "title": "Quotation tools and audit trails",
                "metric": "Excel to R",
                "body": "I audited actuarial models and wrote their audit trails. With another intern I built a "
                        "Group Life quotation tool, first in Excel and R Shiny, then automated it with macros. "
                        "I also investigated annuity payments and unit fund values, and helped value "
                        "unit-linked products.",
                "stack": "R, Shiny, Excel, VBA, Basys",
            },
        ],
    },
    {
        "year": 2020,
        "pages": [
            {
                "id": "nairobi",
                "where": "University of Nairobi",
                "title": "BSc Actuarial Science",
                "metric": "First class",
                "body": "Graduated with first-class honours, as the best student in second and final year. "
                        "Passed the Institute and Faculty of Actuaries papers CM1, CS1 and CB1, and was "
                        "vice-chair of the Nairobi Actuarial Students’ Association.",
                "stack": "Probability, statistics, quantitative modelling",
            },
            {
                "id": "summer-analyst",
                "where": "Goldman Sachs, summer analyst",
                "title": "Back-testing pricing models",
                "metric": "5 weeks, remote",
                "body": "A visualisation tool that compared new pricing models with the ones they would replace, "
                        "highlighting where their estimates differed across historical data.",
                "stack": "Highcharts, data analysis",
            },
        ],
    },
    {
        "year": 2021,
        "pages": [
            {
                "id": "load-balancer",
                "where": "Goldman Sachs, analyst",
                "title": "Zero-downtime intra-day deployments",
                "metric": "0 downtime",
                "body": "I built a custom Java load-balancing service for mission-critical pricing systems, "
                        "from start to finish. It orchestrates rolling restarts automatically, so patches go out "
                        "during the trading day without downtime, rather than waiting for a release window.",
                "stack": "Java",
            },
            {
                "id": "grpc",
                "where": "Goldman Sachs, analyst",
                "title": "Standard gRPC tooling",
                "metric": "−10% latency",
                "body": "Shared tooling to standardise gRPC and Protocol Buffers across services, in Java and "
                        "Python: client scaffolding, authentication middleware and distributed tracing. It "
                        "helped cut client-server latency by more than 10% across several microservices.",
                "stack": "gRPC, Protocol Buffers, Java, Python",
            },
            {
                "id": "monitoring",
                "where": "Goldman Sachs, analyst",
                "title": "Monitoring the pricing flow",
                "metric": "Real-time",
                "body": "I led the rollout of Prometheus monitoring across the core pricing flow, giving "
                        "real-time visibility into latency and system health. I also extended our tracing, "
                        "which cut support load and gave performance work real data to go on.",
                "stack": "Prometheus, distributed tracing",
            },
        ],
    },
    {
        "year": 2024,
        "pages": [
            {
                "id": "cache",
                "where": "Goldman Sachs, associate",
                "title": "Clustered pricing cache",
                "metric": "10× faster",
                "body": "I led the design and rollout of a clustered Hazelcast cache for cross-asset pricing, "
                        "and it made pricing more than ten times faster. It handles product-specific pricing "
                        "rules for more than ten instrument types. Operators can switch it on or off at runtime "
                        "from a dashboard, and continuous monitoring and end-to-end validation tests check "
                        "every result.",
                "stack": "Java, Hazelcast",
            },
            {
                "id": "start-up",
                "where": "Goldman Sachs, associate",
                "title": "90% faster service start-up",
                "metric": "−90% start-up",
                "body": "A critical library used to be downloaded at runtime when each service started. I changed "
                        "its release model so it is pre-deployed to application hosts, which cut start-up time "
                        "by 90% across every service the team owns. Its releases now follow the same rollout "
                        "standards as production.",
                "stack": "Release engineering",
            },
            {
                "id": "tracing",
                "where": "Goldman Sachs, associate",
                "title": "From OpenTracing to OpenTelemetry",
                "metric": "Zero rewrites",
                "body": "OpenTracing was archived, so I led the move off it. I designed an internal tracing "
                        "abstraction and refactored our repositories to use it. We swapped the backend to "
                        "OpenTelemetry without touching application code, and the next migration will be just "
                        "as easy.",
                "stack": "OpenTelemetry, Java",
            },
            {
                "id": "dashboards",
                "where": "Goldman Sachs, associate",
                "title": "Five teams, one dashboard platform",
                "metric": "5 teams moved",
                "body": "I helped move five teams from their own bespoke dashboards onto one shared internal "
                        "platform, extending it to cover what each team needed. I built Python utilities that "
                        "expose data sources dynamically, including Jupyter outputs, added per-user modals and "
                        "alerts, and helped teams set up end-to-end UI tests.",
                "stack": "Python, Jupyter, UI testing",
            },
            {
                "id": "workers",
                "where": "Goldman Sachs, associate",
                "title": "Shared worker pool framework",
                "metric": "Many → one",
                "body": "I co-led the design and led the build of a scalable Python worker pool framework. It "
                        "replaced several team-specific versions with one shared platform, which now runs "
                        "internal and client-facing products.",
                "stack": "Python",
            },
            {
                "id": "scaling",
                "where": "Goldman Sachs, associate",
                "title": "Multi-region auto-scaling",
                "metric": "Scales both ways",
                "body": "I helped build a configurable, multi-region auto-scaling framework for pricing "
                        "systems. It adds capacity under heavy trading load and scales down when markets are "
                        "quiet.",
                "stack": "Kubernetes",
            },
        ],
    },
    {
        "year": 2026,
        "pages": [
            {
                "id": "agent-platform",
                "where": "Goldman Sachs, vice president",
                "title": "Multi-tenant agent platform",
                "metric": "1 runtime per user",
                "body": "An internal platform where each user gets an isolated agent runtime, and traders can "
                        "ship their own apps with no configuration. It works by convention: one parameterised "
                        "Dockerfile, the folder name as the app’s identity, per-app CI builds and automatic "
                        "service discovery. I implemented the A2A protocol on top of our MCP-based "
                        "orchestration, and rebuilt the task lifecycle as an explicit state machine backed by "
                        "Redis.",
                "stack": "Python, MCP, A2A, Docker, GitHub Actions, Traefik, Redis",
            },
            {
                "id": "grounded-chat",
                "where": "Goldman Sachs, vice president",
                "title": "Grounded trading chat",
                "metric": "0 invented figures",
                "body": "A chat assistant inside a trading dashboard, where one invented number is a financial "
                        "risk. Answers are grounded in tool output and cite their sources. The interface "
                        "renders figures straight from tool results rather than from model text, and an eval "
                        "suite checks that this keeps holding.",
                "stack": "LLM tool use, Braintrust, Promptfoo",
            },
            {
                "id": "bloomberg",
                "where": "Goldman Sachs, vice president",
                "title": "Bloomberg chat bots",
                "metric": "3 teams live",
                "body": "I’m extending an internal Bloomberg API service so that teams can run interactive bots "
                        "that listen and reply in chat rooms. Teams define a bot’s behaviour through a "
                        "lightweight plug-in configuration. Three teams are already using it ahead of the "
                        "production rollout.",
                "stack": "Bloomberg APIs, Python",
            },
            {
                "id": "conditions",
                "where": "Goldman Sachs, vice president",
                "title": "Conditions written by agents",
                "metric": "In progress",
                "body": "Letting an agent turn a request like “tell me if this stays above X for three hours” "
                        "into a strict, auditable contract over live data, which triggers actions when it "
                        "passes. Simple checks run deterministically and only fuzzy ones go to a smaller "
                        "model, so costs stay flat as conditions multiply.",
                "stack": "System design",
            },
        ],
    },
]
