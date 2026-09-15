# Team 3: ML and Remote Sensing Dataset Strategy

## 1.0 Dataset Strategy

SatQuery AI is designed to act as an interactive vision-language assistant capable of multimodal remote sensing image analysis through natural language text queries. To fulfill this complex scope, multiple specialized datasets are required. No single dataset currently provides sufficient high-quality annotations for all of the project's target capabilities, which include:

- Visual Question Answering (VQA)
- Image captioning
- Spatial grounding
- Change detection
- Optical-SAR / multimodal analysis

Consequently, the dataset strategy relies on a curated portfolio of datasets mapped to specific capabilities, ensuring robust training, validation, and evaluation across all required functions.

## 2.0 Mandatory Dataset Set

The following four datasets are confirmed as the mandatory project dataset set for initial implementation and evaluation:

1. **BigEarthNet.txt**
   - **Primary Role:** Foundation dataset for multimodal image-text representation.
   - **Relevant SatQuery Capability:** Image captioning and multimodal reasoning (Sentinel-1/Sentinel-2 paired imagery).
   - **Expected Use:** Training/adaptation, validation, and evaluation.
   - **Requirement Status:** Small representative subset required immediately; full dataset download deferred.
   - **Implementation Considerations:** Contains paired Sentinel-1 and Sentinel-2 imagery with multimodal text annotations. The manually verified benchmark split is critical for reliable evaluation.

2. **RSVQA**
   - **Primary Role:** Baseline question-answering dataset.
   - **Relevant SatQuery Capability:** Remote-sensing VQA.
   - **Expected Use:** Training/adaptation and evaluation.
   - **Requirement Status:** Small subset required immediately.
   - **Implementation Considerations:** Provides extensive question-answer pairs but lacks spatial grounding boxes. 

3. **VRSBench**
   - **Primary Role:** Grounded question-answering dataset.
   - **Relevant SatQuery Capability:** VQA and spatial grounding.
   - **Expected Use:** Training/adaptation and evaluation.
   - **Requirement Status:** Small subset required immediately.
   - **Implementation Considerations:** Critical for enabling the agent to point to specific spatial features in its responses.

4. **CDVQA**
   - **Primary Role:** Multitemporal question-answering dataset.
   - **Relevant SatQuery Capability:** Change-related VQA and change detection.
   - **Expected Use:** Training/adaptation and evaluation.
   - **Requirement Status:** Small subset required immediately.
   - **Implementation Considerations:** Bridges the gap between traditional change detection mapping and natural language querying.

## 3.0 Dataset-to-Capability Mapping

| Dataset | Capability | Primary Use |
|---------|------------|-------------|
| **BigEarthNet.txt** | Multimodal image-text / S1-S2 reasoning | Foundation training & benchmark evaluation |
| **RSVQA** | Remote-sensing VQA | Question-answering adaptation |
| **VRSBench** | VQA + grounding | Spatial reasoning and grounding adaptation |
| **CDVQA** | Change-related VQA | Multitemporal/change analysis adaptation |

## 4.0 Supplementary Dataset Catalogue

To ensure robustness and support experimental validation, the following datasets are included as supplementary resources:

- **SEN12-FLOOD**
  - **Relevance:** High-quality multimodal dataset for disaster response.
  - **Status:** Mandatory primary cross-modal fusion dataset.
  - **Capability Supported:** Optical-SAR fusion.

- **STURM-Flood**
  - **Relevance:** Secondary validation for flood-related multimodal analysis.
  - **Status:** Supplementary secondary dataset.
  - **Capability Supported:** Cross-modal/flood-related validation and maturity checking.

- **BigEarthNet-MM**
  - **Relevance:** Precursor to BigEarthNet.txt providing broad label spaces.
  - **Status:** Supplementary.
  - **Capability Supported:** Multimodal exploration and pre-training validation.

## 5.0 Multitemporal / Change-Analysis Decision

**Current Project Decision:** 
CDVQA / SECOND is the mandatory multitemporal path.

For the initial SatQuery implementation, the **CHANGE-VQA** path is selected as the primary change-analysis approach.

**Rationale:**
- It aligns directly with the natural-language query interface of SatQuery.
- It explicitly connects traditional change detection to the project's core VQA requirement.
- It enables the agent/controller to intelligently route temporal questions to a specialized sub-module.

**Secondary Path:**
Mask-based change-description is considered a possible secondary/extension path. It is explicitly not the mandatory first implementation.

*(Note: The multitemporal models and pipelines have not yet been implemented.)*

## 6.0 Optical-SAR Fusion Decision

**Current Project Decision:**
- **Primary:** SEN12-FLOOD
- **Secondary:** STURM-Flood
- **Supporting:** BigEarthNet-MM

**Implementation Timeline:**
- **September Scope:** Target a simple, reproducible optical-SAR fusion baseline.
- **January Stretch Goal:** Develop and evaluate a more sophisticated fusion architecture.

## 7.0 Compute-Aware Data Strategy

The available development environment is constrained:
- Hardware: MacBook Air M4
- Memory: 16 GB unified memory
- Storage: 1 TB external SSD
- Cloud Compute: No paid cloud GPU budget is currently assumed. Free environments (e.g., Kaggle) may be used for selected GPU-intensive experiments, but availability is not guaranteed.

**Data Management Rules:**
1. Do not require all datasets to be downloaded simultaneously.
2. Separate storage requirements from compute/training requirements.
3. Start development and exploration strictly with metadata, annotations, and small representative subsets.
4. Use small subsets for all pipeline development, dataloader testing, and initial model-selection experiments.
5. Download larger portions of datasets only when a specific, justified experiment requires them.
6. Avoid treating the full BigEarthNet.txt imagery archive as a prerequisite for initial development.
7. Where feasible, use LoRA/QLoRA as the planned adaptation strategy to accommodate compute limits.
8. The final model size must be verified against actual available compute before initiating October experiments.

## 8.0 September vs January Scope

### September Scope (Initial Phase)
- Dataset catalogue finalized.
- Mandatory datasets confirmed.
- Dataset roles mapped.
- Change-VQA path selected.
- SEN12-FLOOD selected as primary fusion dataset.
- STURM-Flood selected as secondary fusion dataset.
- Simple fusion baseline architecture identified.
- Small-sample exploration and pipeline validation initiated.

### January Stretch Goal
- More sophisticated optical-SAR fusion.
- Broader multimodal integration.
- Larger-scale experiments (if compute constraints permit).

*(Note: January work is planned future work and is not yet implemented.)*

## 9.0 Dataset Acquisition Plan

Dataset acquisition will follow a phased approach aligned with the compute-aware strategy:

- **Stage 1 — Development:** Acquire only metadata, text annotations, and small imagery samples to build and verify data pipelines.
- **Stage 2 — Experimental:** Acquire selected, specific subsets required to execute initial VQA, grounding, and change-detection experiments.
- **Stage 3 — Scale-up:** Download larger or full datasets only if explicitly justified by experimental requirements and validated against compute limits.

## 10.0 Current Status

### CONFIRMED:
- Mandatory dataset set (BigEarthNet.txt, RSVQA, VRSBench, CDVQA).
- SEN12-FLOOD as the primary fusion dataset.
- STURM-Flood as the secondary fusion dataset.
- CDVQA as the mandatory multitemporal dataset.
- Change-VQA as the primary mandatory path.
- BigEarthNet.txt as the multimodal S1/S2 foundation dataset.

### PENDING:
- Actual dataset sample exploration.
- BigEarthNet.txt dataloader implementation.
- Quantitative benchmark experiments.
- Final model selection after sample-level evaluation.
- Final compute-size confirmation.

## 11.0 References

- **BigEarthNet.txt:** Refer to the official BigEarthNet.txt paper and dataset documentation for S1/S2 imagery and text annotations.
- **RSVQA:** Refer to the official RSVQA paper and repository.
- **VRSBench:** Refer to the official VRSBench documentation.
- **CDVQA:** Refer to the CDVQA/SECOND paper and repository.
- **SEN12-FLOOD:** Refer to the official SEN12-FLOOD dataset publication.
- **STURM-Flood:** Refer to authoritative sources for STURM-Flood.
- **BigEarthNet-MM:** Refer to the original BigEarthNet multimodal paper and repository.
