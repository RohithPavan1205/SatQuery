# SatQuery AI Architecture

This document outlines the planned architecture for SatQuery AI.

## Architecture Diagram

```text
User
   ↓
Frontend
   ↓ REST API
Backend API
   ├── Agent / Controller
   │       ↓
   │   Model Service Layer
   │
   ├── Storage
   │
   └── Evaluation Harness
           ↓
Result Aggregator + Confidence Estimator
   ├── Report Generator
   └── Frontend Output
```

## Components

- **User**: The end-user interacting with the system through natural language queries.
- **Frontend**: The user interface for submitting queries, uploading images, and viewing results.
- **Backend API**: Serves as the central router via REST API. It handles authentication, request validation, and orchestrates calls to the controller.
- **Agent / Controller**: The core orchestrator that interprets user queries, decides which models to invoke, and sequences the analysis pipeline.
- **Model Service Layer**: A suite of independent microservices hosting the various foundation models (vision-language models, specialized remote sensing models).
- **Storage**: Responsible for managing datasets, user sessions, image caching, and persistent records.
- **Evaluation Harness**: A dedicated subsystem for benchmarking model performance, testing prompts, and validating agent decisions against ground truth datasets.
- **Result Aggregator + Confidence Estimator**: Compiles the outputs from various models, resolves conflicting predictions, and assigns confidence scores.
- **Report Generator**: Formats the final analysis into comprehensive, exportable reports.
- **Frontend Output**: The structured response sent back to the frontend for visualization.

*Note: This diagram represents the planned architectural design. The functionality depicted here is not currently implemented in the codebase.*
